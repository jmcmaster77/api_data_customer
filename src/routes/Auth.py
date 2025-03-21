from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel

from models.Users import User
from models.ModelUsersdb import Usuarios
from utils.db import db

auth = APIRouter()


@auth.get("/")
def test_server():
    return {"status": "Server Up"}


class Duser(BaseModel):
    username: str
    password: str
    fullname: str
    rol: str


@auth.post("/create_user")
def new_user(user_data: Duser):
    try:
        print("data user incoming", user_data)

        rc = db.query(Usuarios).filter_by(username=user_data.username).first()
        # rc = Usuarios. query.filter_by(user_data.username).first()
        print("request", rc)

        return {"message": "recibido"}
    except Exception as e:
        print("Error en la conexion ", e)
        return {"message": "recibido pero hay un error con la db conexion"}


class UserGet(BaseModel):
    id: int
    username: str
    password: str
