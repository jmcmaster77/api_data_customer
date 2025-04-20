from fastapi import FastAPI
from routes import Auth
from sqlalchemy.orm import Session
from utils.log import logger
from config.setting import app_run_port
import uvicorn

app = FastAPI()

app.include_router(Auth.auth, tags=["Autenticacion y Gestion JWT"])

if __name__ == "__main__":
    logger.info("API running on port: " + str(app_run_port))
    uvicorn.run(app, host="0.0.0.0", port=app_run_port)
