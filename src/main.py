from fastapi import FastAPI
from routes import Auth
import uvicorn

app = FastAPI()

app.include_router(Auth.auth, tags=["Autenticacion y Gestion JWT"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
