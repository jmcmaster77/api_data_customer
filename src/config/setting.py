from dotenv import load_dotenv
import os

load_dotenv()

host = os.environ["host"]
database = os.environ["database"]
db_user = os.environ["db_user"]
db_password = os.environ["db_password"]
port = os.environ["port"]
sk = os.environ["sk"]

URIDB = f"mariadb+pymysql://{db_user}:{db_password}@{host}:{port}/{database}?charset=utf8mb4"
