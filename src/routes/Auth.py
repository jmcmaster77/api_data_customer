from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from models.ModelUsersdb import Usuarios
from utils.db import db
from passlib.hash import sha256_crypt

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
        rc = db.query(Usuarios).filter_by(username=user_data.username).first()

        if rc is None:
            fecha = datetime.now()
            # la base de datos acepta el datetime en ese formato
            fecha = fecha.strftime("%Y/%m/%d %H:%M:%S")
            password_encrypted = sha256_crypt.encrypt(user_data.password)
            newuser = Usuarios(user_data.username, password_encrypted,
                               user_data.fullname, user_data.rol, fecha, False)
            db.add(newuser)
            db.commit()
            return {"message": f"usuario registrado con el id: {newuser.id}"}
        else:
            return {"message": f"usuario: {user_data.username} ya se encuentra registrado"}

    except Exception as e:
        print("Error: ", e)
        return {"message": f"recibido pero hay un error: {e}"}


class UserGet(BaseModel):
    id: int
    username: str
    password: str
