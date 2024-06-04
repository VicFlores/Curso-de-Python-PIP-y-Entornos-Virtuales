from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_list():
    return ["item1", "item2", "item3"]


@app.get("/contact")
def get_contact():
    return {"name": "Vic", "email": "vicflores@gmail.com"}
