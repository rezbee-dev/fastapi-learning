from fastapi import FastAPI

from app.item import ItemRouter

app = FastAPI()
app.include_router(ItemRouter)

@app.get("/hello")
async def root():
    return {"message":"Hello World"}

# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def startup(app: FastAPI):
#     print("Starting FastAPI backend...")
#     db = init_db()
#     print("Database loaded")
#     yield
#     print("...stopping FastAPI backend")