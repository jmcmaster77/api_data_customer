from models.Users import User
from utils.db import db
from schemas.ModelUsersdb import Usuarios
from passlib.hash import sha256_crypt


class AuthService():

    @classmethod
    def login_user(cls, user):
        try:
            authenticate_user = None

            rc = db.query(Usuarios).filter_by(id=user.id).first()

            if rc is not None:
                # Devs Notes Si el Usuario esta marcado como borrado no generar token
                if rc.deleted:
                    return "User has been mark as Deleted"
                else:
                    if user.username == rc.username and sha256_crypt.verify(user.password, rc.password):
                        authenticate_user = User(
                            rc.id, rc.username, None, rc.fullname, rc.rol)

                    return authenticate_user

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def user_mark_as_deleted(cls, user):
        try:
            rc = db.query(Usuarios).filter_by(id=user.id).first()
            if rc is not None:
                return rc.deleted
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
