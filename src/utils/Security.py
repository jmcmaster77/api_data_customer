import datetime
import pytz
import jwt

from config.setting import sk


class Security():
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
