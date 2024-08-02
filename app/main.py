from fastapi import FastAPI
from app.routes import astro_event, astro_position

app = FastAPI()

app.include_router(astro_event.router, prefix="/api")
app.include_router(astro_position.router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}