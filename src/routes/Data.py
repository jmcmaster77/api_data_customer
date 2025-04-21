from fastapi import APIRouter, Depends, Security, status, UploadFile, File
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from utils.Security import SecurityToken
from utils.log import logger
from models.Users import User
from models.Pedidos import Pedido
from services.AuthService import AuthService
from datetime import datetime
from utils.db import db
from schemas.ModelVentasdb import Ventas
import os
import csv

data = APIRouter()

# configuracion del la key para el token
token_key = APIKeyHeader(name="Authorization")


def get_current_token(auth_key: str = Security(token_key)):
    return auth_key


class Token(BaseModel):
    token: str


@data.post("/log", response_class=PlainTextResponse)
def new_user(received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:
        try:
            with open("api_data_customer.log", "r") as file:
                content = file.read()
                logger.info(
                    f"Solicitud del log por {payload['id']} - {payload['username']}")
            return PlainTextResponse(content=content, status_code=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Se intento solicitar el log error: {e}")
            message = {"message": f"Error: {e}"}
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=message)
    elif has_access is not True and has_access is not False:
        logger.error(
            f"Se intento solicitar el log error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"Se intento solicitar el log por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


route_path = os.path.abspath(os.path.dirname(__file__))
base_path = os.path.join(os.path.dirname(route_path), "")
incoming_path = os.path.join(os.path.dirname(base_path), "incoming")


def remplazar_coma_x_punto(valor):
    valor = valor.replace(',', '.')
    return float(valor)

def format_fecha(fecha):
    return datetime.strptime(fecha, "%m/%d/%Y")

def validar_lote(lote):
    rc = db.query(Ventas).filter_by(
        lote=lote).first()
    if rc is None:
        return False
    else:
        return True


@data.post("/incoming")
async def upload_file(file: UploadFile = File(...), received_token: Token = Depends(get_current_token)):
    payload = SecurityToken.verify_token(received_token)
    if isinstance(payload, dict):
        _user = User(payload['id'], payload['username'], None, None, None)
        isdeleted = AuthService.user_mark_as_deleted(_user)

        if isdeleted is False:
            try:
                contents = await file.read()
                # print("data recibida", contents)
                # parametros para generar el archivo en incoming
                file_name, file_ext = os.path.splitext(file.filename)
                file_name = f"{file_name}_{datetime.now().strftime('%d-%m-%Y_%H_%M_%S')}{file_ext}"
                file_path = os.path.join(incoming_path, file_name)
                # parametros para validar los pedidos a cargar en la db
                decoded_contens = contents.decode("utf-8")
                reader = csv.reader(
                    decoded_contens.splitlines(), delimiter="|")

                pedidos = []

                for row in reader:
                    pedido = Pedido(None, format_fecha(row[0]), row[1], row[2], row[3], row[4], row[5], remplazar_coma_x_punto(
                        row[6]), int(row[7]), int(row[8]), (row[9]))
                    # print("pedido", vars(pedido)) # la funcion vars te muestra todos los atributos de los objetos muy cuchi

                    pedidos.append({
                        "fecha": pedido.fecha,
                        "cedula": pedido.cedula,
                        "cliente_name": pedido.cliente_name,
                        "direccion": pedido.direccion,
                        "telefono": pedido.telefono,
                        "correo": pedido.correo,
                        "costo": pedido.costo,
                        "metodo_pago": pedido.metodo_pago,
                        "estado_pedido": pedido.estado_pedido,
                        "lote": pedido.lote
                    })
                # valido que el lote en todos los registros sea el mismo
                lotes = {pedido["lote"] for pedido in pedidos}
                # print("lotes:", list(lotes)[0])
                if len(lotes) == 1:
                    # print("val_lotes OK, todos los registros tienen el mismo lote.")
                    # valido que el lote no este registrado en la db
                    lote_existe = validar_lote(list(lotes)[0])
                    if lote_existe is False:
                        # genero el archivo
                        with open(file_path, "wb") as f:
                            f.write(contents)
                        # cargo los pedidos en la db
                        db.add_all([Ventas(**pedido) for pedido in pedidos])
                        db.commit()
                        db.close()
                        logger.info(
                            f"Se cargo en las ventas el lote {list(lotes)[0]} de pedidos por {payload['id']} {payload['username']}")
                        mensaje2 = {
                            "Cantidad registros": f"{len(pedidos)}"}

                        # porque soy bipolar y estoy intentando si el metodo de arriba funciona -_-
                        # new_pedido = Ventas(
                        #     pedido.fecha, pedido.cedula, pedido.cliente_name, pedido.direccion, pedido.telefono,
                        #     pedido.correo, pedido.costo, pedido.metodo_pago, pedido.estado_pedido, pedido.lote)
                    else:
                        # error en caso de que el lote ya este registrado en la base de datos
                        logger.error(
                            f"Se intento cargar un archivo {file.filename} pero el {list(lotes)[0]} ya existe en la BD por {payload['id']} {payload['username']}")
                        message = {
                            "message": f"Se intento cargar un archivo {file.filename} pero el {list(lotes)[0]} ya existe en la BD"}
                        return JSONResponse(status_code=status.HTTP_412_PRECONDITION_FAILED, content=message)
                else:

                    # print("val_lotes ERROR todos los registros NO tienen el mismo lote.")
                    logger.error(
                        f"Se intento cargar un archivo {file.filename} con lotes diferentes en los registros {lotes} por {payload['id']} {payload['username']}")
                    message = {
                        "message": f"Se intento cargar un archivo {file.filename} con lotes diferentes en los registros {lotes}"}
                    return JSONResponse(status_code=status.HTTP_412_PRECONDITION_FAILED, content=message)

                logger.info(
                    f"archivo {file.filename} recibido enviado por {payload['id']} {payload['username']}")
                logger.info(
                    f"archivo generado {file_path} enviado por {payload['id']} {payload['username']}")
                message = [{"message": f"archivo {file.filename} recibido"}]
                message.append({"archivo generado": f"{file_path}"})
                message.append(mensaje2)
                return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=message)

            except Exception as e:
                logger.error(f"Se intento cargar un archivo error: {e}")
                message = {"message": f"Error: {e}"}
                return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=message)

        elif isdeleted is True:
            logger.error(
                f"Al cargar el archivo usuario {payload['id']} {payload['username']} marcado como borrado")
            message = {
                "mensaje": f"Usuario {payload['id']} {payload['username']} marcado como borrado"}
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=message)
        elif isdeleted is None:
            logger.error(
                f"Error al cargar el archivo el usuario id {payload['id']} no esta registrado")
            message = {"message": f"User id: {payload['id']} no registrado"}
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    else:
        logger.error(
            f"Error cargando archivo {payload}")
        message = {"message": f"Error cargando archivo: {payload}"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=message)
