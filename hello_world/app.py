from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def read_root():
    # return {"Hello": "World"}
    return "Hello World"

@app.get("/hello/{name}")
def read_root(name: str = None):
    return "Hello World, " + name.capitalize()

@app.get("/api/{tenant_id}/hello/{name}")
def read_root(tenant_id: str = None, name: str = None):
    return "Hello World, " + name.capitalize() + " from " + tenant_id

handler = Mangum(app)