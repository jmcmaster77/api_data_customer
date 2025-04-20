from fastapi import APIRouter, Depends, Security, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from utils.Security import SecurityToken
from utils.log import logger

# log


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
