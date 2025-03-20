from fastapi import FastAPI, APIRouter


auth = APIRouter()


@auth.get("/")
def test_server():
    return {"status": "Server Up"}
