from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def hello():
    # return {"Hello": "World"}
    return "Hello World"

@app.get("/hello/{name}")
def hello_by_name(name: str = None):
    return "Hello World, " + name.capitalize()

@app.get("/api/{tenant_id}/hello/{name}")
def hello_by_name_from_tenant(tenant_id: str = None, name: str = None):
    return "Hello World, " + name.capitalize() + " from " + tenant_id

handler = Mangum(app)