from fastapi import FastAPI
from routes import Auth, Data
# para la base personas 
from utils.db import engine
from schemas import ModelUsersdb, ModelVentasdb
from utils.log import logger
from config.setting import app_run_port
import uvicorn

app = FastAPI()

app.include_router(Auth.auth, tags=["Autenticacion y Gestion JWT"])
app.include_router(Data.data, tags=["gestion de datos"])

# Creando todas las tablas definidas en los modelos

ModelUsersdb.Base.metadata.create_all(bind=engine)
ModelVentasdb.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    logger.info("API running on port: " + str(app_run_port))
    uvicorn.run(app, host="0.0.0.0", port=app_run_port)
