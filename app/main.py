from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Campus Help Assistant")

app.include_router(router)