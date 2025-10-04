from fastapi import FastAPI

from routers import crud_router

app = FastAPI()

app.include_router(crud_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
