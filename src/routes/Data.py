from fastapi import APIRouter, Depends, Security, status, UploadFile, File
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from utils.Security import SecurityToken
from utils.log import logger
from models.Users import User
from services.AuthService import AuthService
from datetime import datetime
import os

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

                file_name, file_ext = os.path.splitext(file.filename)
                file_name = f"{file_name}_{datetime.now().strftime('%d-%m-%Y_%H_%M_%S')}{file_ext}"
                file_path = os.path.join(incoming_path, file_name)
                with open(file_path, "wb") as f:
                    f.write(contents)

                logger.info(
                    f"archivo {file.filename} recibido enviado por {payload['id']} {payload['username']}")
                logger.info(
                    f"archivo generado {file_path} enviado por {payload['id']} {payload['username']}")
                message = [{"message": f"archivo {file.filename} recibido"}]
                message.append({"archivo generado":f"{file_path}"})
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
