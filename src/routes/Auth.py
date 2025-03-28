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
            return {"message": f"usuario {new_user.username } registrado con el id: {newuser.id}"}
        else:

            return {"message": f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado"}

    except Exception as e:
        return {"Error": f"recibido pero hay un error: {e}"}


@auth.post("/create_users")
def new_users(user_list: list[Duser]):
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
                password_encrypted = sha256_crypt.encrypt(user_data.password)
                newuser = Usuarios(user_data.username, password_encrypted,
                                   user_data.fullname, user_data.rol, fecha, False)
                db.add(newuser)
                db.commit()
                mensajes["Resgistros"].append(
                    {registro: f"usuario {new_user.username } registrado con el id: {newuser.id}"})
            else:
                registro += 1
                mensajes["Resgistros"].append(
                    {registro: f"usuario: {rc.username} con el id:{rc.id} ya se encuentra registrado"})
        return {"result": mensajes}
    except Exception as e:
        return {"Error": f"recibido pero hay un error: {e}"}


@auth.get("/users")
def get_users():
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

            return {"message": "No hay usuarios registrados en la base de datos o.O"}

    except Exception as e:
        return {"Error": f"recibido pero hay un error: {e}"}


class Dparam(BaseModel):
    type: str
    param: str


@auth.post("/user_info")
def send_user_data(doption: Dparam):

    try:
        if doption.type == "id":
            rc = db.query(Usuarios).filter_by(id=int(doption.param)).first()
        elif doption.type == "username":
            rc = db.query(Usuarios).filter_by(username=doption.param).first()

        if rc is not None:
            data_user = {
                "id": rc.id,
                "username": rc.username,
                "fullname": rc.fullname,
                "rol": rc.rol,
                "registrado": rc.fecha.strftime("%d/%m/%y %H:%M"),
                "deleted": rc.deleted
            }

            return data_user

        else:

            return {"message": f"la busqueda del usuario con el tipo de busqueda {doption.type} y el parametro {doption.param} no arrojo resultados"}

    except Exception as e:
        return {"Error": f"recibido pero hay un error: {e}"}
