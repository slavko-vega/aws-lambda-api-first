from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/good-bye")
def read_root():
    # return {"Hello": "World"}
    return "Good Bye"

handler = Mangum(app)