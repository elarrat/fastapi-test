from fastapi import FastAPI
from app.container import Container
from app.server.controllers.StudentController import router

container = Container()

app = FastAPI()
app.include_router(router, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}