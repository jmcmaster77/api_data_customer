from fastapi import APIRouter, Depends, Security, status
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from datetime import datetime
from schemas.ModelUsersdb import Usuarios
from services.AuthService import AuthService
from models.Users import User
from utils.db import db
from utils.log import logger
from utils.Security import SecurityToken
from passlib.hash import sha256_crypt
from datetime import datetime
import pytz
auth = APIRouter()


@auth.get("/")
def test_server():
    logger.info("server request status send ok")
    return {"status": "Server Up"}


# configuracion del la key para el token
token_key = APIKeyHeader(name="Authorization")


def get_current_token(auth_key: str = Security(token_key)):
    return auth_key


class Token(BaseModel):
    token: str


class Duser(BaseModel):
    username: str
    password: str
    fullname: str
    rol: str


@auth.post("/create_user")
def new_user(user_data: Duser, received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:
            rc = db.query(Usuarios).filter_by(
                username=user_data.username).first()

            if rc is None:
                fecha = datetime.now()
                # la base de datos acepta el datetime en ese formato
                fecha = fecha.strftime("%Y/%m/%d %H:%M:%S")
                password_encrypted = sha256_crypt.encrypt(user_data.password)
                newuser = Usuarios(user_data.username, password_encrypted,
                                   user_data.fullname, user_data.rol, fecha, False)
                db.add(newuser)
                db.commit()
                logger.info(
                    f"Usuario id: {newuser.id} - {newuser.username} registrado  por {payload['id']} - {payload['username']}")
                return {"message": f"usuario {newuser.username } registrado con el id: {newuser.id}"}
            else:
                logger.error(
                    f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado")
                return {"message": f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado"}

        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}

    elif has_access is not True and has_access is not False:
        logger.error(
            f"se intento registrar un usuario error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"se intento registrar un usuario por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


@auth.post("/create_users")
def new_users(user_list: list[Duser], received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:
            mensajes = {"Resgistros": []}
            registro = 0
            for user_data in user_list:
                rc = db.query(Usuarios).filter_by(
                    username=user_data.username).first()
                if rc is None:
                    registro += 1
                    fecha = datetime.now()
                    # la base de datos acepta el datetime en ese formato
                    fecha = fecha.strftime("%Y/%m/%d %H:%M:%S")
                    password_encrypted = sha256_crypt.encrypt(
                        user_data.password)
                    newuser = Usuarios(user_data.username, password_encrypted,
                                       user_data.fullname, user_data.rol, fecha, False)
                    db.add(newuser)
                    db.commit()
                    logger.info(
                        f"Usuario id: {newuser.id} - {newuser.username} registrado  por {payload['id']} - {payload['username']}")
                    mensajes["Resgistros"].append(
                        {registro: f"usuario {newuser.username } registrado con el id: {newuser.id}"})
                else:
                    registro += 1
                    logger.error(
                        f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado")
                    mensajes["Resgistros"].append(
                        {registro: f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado"})
            return {"result": mensajes}
        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}
    elif has_access is not True and has_access is not False:
        logger.error(
            f"se intento registrar un usuario error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"se intento registrar un usuario por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


@auth.get("/users")
def get_users(received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:

            # metodo donde me traigo solo los campos y le doy formato a la fecha y empaqueto el json como requiero

            registros = db.query(Usuarios).with_entities(
                Usuarios.id, Usuarios.username, Usuarios.fullname, Usuarios.rol, Usuarios.fecha, Usuarios.deleted).all()

            if registros is not None:
                resultado = [

                    {
                        "id": row[0],
                        "username": row[1],
                        "fullname": row[2],
                        "rol": row[3],
                        "fecha": row[4].strftime("%d/%m/%y %H:%M")
                    }

                    for row in registros
                    if row[5] is not True
                ]
                logger.info(
                    f"Lista de usuarios solicitada por {payload['id']} - {payload['username']}")
                return resultado

            # metodo donde consulto todos los datos obteniendo una lista de objetos pasando
            # los resultados a una variable para aplicar un filtro y dar formato a la fecha y solo los datos que desel enviar

            # registros = db.query(Usuarios).all()

            # if registros is not None:
            #     resultados = []
            #     for registro in registros:
            #         if registro.deleted is not True:
            #             resultado = {
            #                 "id": registro.id,
            #                 "username": registro.username,
            #                 "fullname": registro.fullname,
            #                 "rol": registro.rol,
            #                 "fecha" : registro.fecha.strftime("%d/%m/%y %H:%M"),
            #             }
            #             resultados.append(resultado)

            #     return resultados
            else:
                logger.info(
                    f"Lista de usuarios solicitada por {payload['id']} - {payload['username']}")
                logger.error(
                    "No hay usuarios registrados en la base de datos o.O")
                return {"message": "No hay usuarios registrados en la base de datos o.O"}

        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}
    elif has_access is not True and has_access is not False:
        logger.error(
            f"Se intento solicitar una lista de usuario error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"Se intento solicitar una lista de usuario por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


class Dparam(BaseModel):
    type: str
    param: str


@auth.post("/user_info")
def send_user_data(doption: Dparam, received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:
            if doption.type == "id":
                rc = db.query(Usuarios).filter_by(
                    id=int(doption.param)).first()
            elif doption.type == "username":
                rc = db.query(Usuarios).filter_by(
                    username=doption.param).first()

            if rc is not None:
                data_user = {
                    "id": rc.id,
                    "username": rc.username,
                    "fullname": rc.fullname,
                    "rol": rc.rol,
                    "registrado": rc.fecha.strftime("%d/%m/%y %H:%M"),
                    "deleted": rc.deleted
                }
                logger.info(
                    f"Se consulta usuario con el tipo de busqueda {doption.type} y el parametro {doption.param} solicitada por {payload['id']} - {payload['username']}")
                logger.info(
                    f"Se consulto informacion del usuario {rc.id} - {rc.username} solicitada por {payload['id']} - {payload['username']}")
                return data_user

            else:
                logger.info(
                    f"Se consulta usuario con el tipo de busqueda {doption.type} y el parametro {doption.param} solicitada por {payload['id']} - {payload['username']}")
                logger.error("la busqueda del usuario no arrojo resultados")
                return {"message": f"la busqueda del usuario con el tipo de busqueda {doption.type} y el parametro {doption.param} no arrojo resultados"}

        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}
    elif has_access is not True and has_access is not False:
        logger.error(
            f"Se intento consultar informacion del usuario {doption.type} - {doption.param} error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"Se intento consultar informacion del usuario {doption.type} - {doption.param} por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


class Dparam_to_update(BaseModel):
    id: str
    username: str
    fullname: str
    rol: str


@auth.post("/update_data_user")
def update_data_user(doption: Dparam_to_update, received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:
            rc = db.query(Usuarios).filter_by(id=int(doption.id)).first()

            if rc is not None:

                # validar que el username no este siendo utlizado por otro usuario

                valrc = db.query(Usuarios).filter_by(
                    username=doption.username).first()

                if valrc is None:

                    data_user = {
                        "datos": "encontrados",
                        "id": rc.id,
                        "username": rc.username,
                        "fullname": rc.fullname,
                        "rol": rc.rol,
                    }

                    rc.username = doption.username
                    rc.fullname = doption.fullname
                    rc.rol = doption.rol
                    db.commit()
                    data_user_updated = {
                        "datos": "actualizados",
                        "id": rc.id,
                        "username": rc.username,
                        "fullname": rc.fullname,
                        "rol": rc.rol,
                    }

                    mensaje = []
                    mensaje.append(data_user)
                    mensaje.append(data_user_updated)
                    logger.info(
                        f"Se modifico informacion del usuario {doption.id} - {doption.username} solicitada por {payload['id']} - {payload['username']}")
                    return mensaje

                elif valrc.id == rc.id:

                    data_user = {
                        "datos": "encontrados",
                        "id": rc.id,
                        "username": rc.username,
                        "fullname": rc.fullname,
                        "rol": rc.rol,
                    }

                    rc.username = doption.username
                    rc.fullname = doption.fullname
                    rc.rol = doption.rol
                    db.commit()
                    data_user_updated = {
                        "datos": "actualizados",
                        "id": rc.id,
                        "username": rc.username,
                        "fullname": rc.fullname,
                        "rol": rc.rol,
                    }

                    mensaje = []
                    mensaje.append(data_user)
                    mensaje.append(data_user_updated)
                    logger.info(
                        f"Se modifico informacion del usuario {doption.id} - {doption.username} solicitada por {payload['id']} - {payload['username']}")
                    return mensaje

                else:

                    mensaje = []
                    error = {
                        "mensaje": f"el username {doption.username} esta siendo utilizado por el id {valrc.id} ",
                        "username": valrc.username,
                        "fullname": valrc.fullname
                    }
                    mensaje.append(error)
                    logger.error(
                        f"Se intento modificar informacion del usuario {doption.id} - {doption.username} solicitada por {payload['id']} - {payload['username']}")
                    return mensaje

            else:

                return {"message": f"la busqueda del id {doption.id} no arrojo resultados"}

        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}
    elif has_access is not True and has_access is not False:
        logger.error(
            f"Se intento modificar informacion del usuario {doption.id} - {doption.username} error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        logger.warning(
            f"Se intento modificar informacion del usuario {doption.id} - {doption.username} por {payload['id']} - {payload['username']} sin autorizacion")
        message = {"message": "Usuario no tiene autorizacion"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


class Dparam_to_mark_deleted(BaseModel):
    id: str
    deleted: bool


@auth.post("/mark_user_deleted")
def mark_user_as_deleted(doption: Dparam_to_mark_deleted, received_token: Token = Depends(get_current_token)):
    has_access = SecurityToken.verify_token_admin(received_token)
    payload = SecurityToken.verify_token(received_token)
    if has_access is True:

        try:
            rc = db.query(Usuarios).filter_by(id=int(doption.id)).first()
    #       print("doption", f"id: {doption.id} deleted: {doption.deleted}")
            if rc is not None:

                data_user = {
                    "datos": "Usuario",
                    "id": rc.id,
                    "username": rc.username,
                    "fullname": rc.fullname,
                    "rol": rc.rol,
                    "deleted": rc.deleted,
                }

                rc.deleted = doption.deleted
                db.commit()
                message_info = {
                    "operation": "successfully",
                    "message": f"usuario fue marcado con la condicion borrado {doption.deleted}",
                }

                message = []
                message.append(data_user)
                message.append(message_info)
                logger.info(
                    f"El usuario id {doption.id} fue marcado con la condicion borrado en - {doption.deleted} solicitada por {payload['id']} - {payload['username']}")
                return message
            else:
                logger.error(f"Al marcar como borrado id {doption.id} la busqueda no arrojo resultados solicitada por {payload['id']} - {payload['username']}")
                return {"message": f"la busqueda del id {doption.id} no arrojo resultados"}

        except Exception as e:
            logger.error(f"Excepción: {e}")
            return {"Error": f"recibido pero hay un error: {e}"}
    elif has_access is not True and has_access is not False:
        logger.error(
            f"Se intento marcar el usuario id {doption.id} con la condicion borrada en - {doption.deleted} error: {has_access}")
        message = {"message": f"Error: {has_access}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    elif has_access is False:
        message = {"message": "Usuario no tiene autorizacion"}
        logger.warning(
            f"Se intento marcar el usuario id {doption.id} con la condicion borrada en - {doption.deleted} por {payload['id']} - {payload['username']} sin autorizacion")
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)


class User_x_gen_token(BaseModel):
    id: int
    username: str
    password: str


# generado un token por user by id
@auth.post("/gen_token")
def generacion_token_fou_user(user: User_x_gen_token):

    _user = User(user.id, user.username, user.password, None, None)
    authenticate_user = AuthService.login_user(_user)

    if authenticate_user != None:
        if authenticate_user == "User has been mark as Deleted":
            logger.error(
                f"Error al generar token para el usuario id {user.id} {user.username} error usuario marcado como borrado")
            message = {"message": f"Token no generated: {authenticate_user}"}
            return JSONResponse(status_code=status.HTTP_412_PRECONDITION_FAILED, content=message)

        else:
            encode_token = SecurityToken.generate_token(authenticate_user)
            logger.info(
                f"Se genera token para el usuario id {user.id} {user.username} satisfactoriamente")
            return {"success": True, "token": encode_token}
    else:
        logger.error(
            f"Error al generar token para el usuario id {user.id} {user.username} error autenticacion")
        return {"success": False, "message": "token no generado validar datos enviados"}


@auth.post("/verify_token", status_code=status.HTTP_200_OK)
def verify_token(token: Token = Depends(get_current_token)):
    # print("token", token)
    tz = pytz.timezone("America/Caracas")
    payload = SecurityToken.verify_token(token)

    # print("payload", type(payload))
    # print("payload", payload["id"])

    if isinstance(payload, dict):
        # print("payload", payload)
        _user = User(payload['id'], payload['username'], None, None, None)
        isdeleted = AuthService.user_mark_as_deleted(_user)

        if isdeleted is False:
            message = []
            message.append({"message": "Token Valido"})
            payload['iat'] = datetime.fromtimestamp(
                payload['iat'], tz).strftime('%d de %B de %Y, %H:%M:%S UTC')
            payload['exp'] = datetime.fromtimestamp(
                payload['exp'], tz).strftime('%d de %B de %Y, %H:%M:%S UTC')
            message.append(payload)
            logger.info(
                f"Se valida un token para el usuario id {payload['id']} {payload['username']} satisfactoriamente")
            return message
        elif isdeleted is True:
            message = []
            message.append({"Warning": "User marcado como borrado"})
            message.append({"message": "Token Valido"})
            payload['iat'] = datetime.fromtimestamp(
                payload['iat'], tz).strftime('%d de %B de %Y, %H:%M:%S UTC')
            payload['exp'] = datetime.fromtimestamp(
                payload['exp'], tz).strftime('%d de %B de %Y, %H:%M:%S UTC')
            message.append(payload)
            logger.warning(
                f"Se valida un token para el usuario id {payload['id']} {payload['username']} usuario con condicion borrado")
            return message
        elif isdeleted is None:
            logger.error(
                f"Error al validar el token para el usuario id {payload['id']} no esta registrado")
            message = {"message": f"User id: {payload['id']} no registrado"}
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
    else:
        # print("Error", payload)
        logger.error(
            f"Se intenta validar un token {payload}")
        message = {"message": f"Token error: {payload}"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=message)
