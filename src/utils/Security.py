import datetime
import pytz
import jwt

from config.setting import sk


class SecurityToken():
    jwt_key = sk
    tz = pytz.timezone("America/Caracas")

    @classmethod
    def generate_token(cls, user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz)+datetime.timedelta(days=180),
            'id': user.id,
            'username': user.username,
            'fullname': user.fullname,
            'rol': user.rol
        }
        # jwt.encode(payload, cls.jwt_key, algorithm="HS256")

        return jwt.encode(payload, cls.jwt_key, algorithm="HS256")

    @classmethod
    def verify_token(cls, token):
        if (len(token) > 0):
            # para validar el Bearer Token con postman
            # token_validated = str(validar_bearer(token))

            try:
                payload = jwt.decode(token, cls.jwt_key, algorithms=["HS256"])

                return payload
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, jwt.InvalidTokenError) as ex:
                return ex

    @classmethod
    def verify_token_admin(cls, token):
        if (len(token) > 0):
            try:
                payload = jwt.decode(token, cls.jwt_key, algorithms=["HS256"])
                if payload['rol'] == "admin":
                    return True
                else:
                    return False
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, jwt.InvalidTokenError) as ex:
                return ex

        # para validar cuando en postman el tipo de autenticacion es Bearer Token
        # def validar_bearer(token):

        #     if token[0:6] == "Bearer":
        #         token_validated = str(token).split(' ')[1]
        #         return token_validated
        #     else:
        #         return token
