from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse


app = FastAPI()

@app.get("/")
async def load_home(request: Request):
    return FileResponse("homepage.html")

@app.post("/submit-item")
async def handle_form(my_name:str = Form(...),my_age:str = Form(...)):
    print(f"The user typed: {my_name}")
    print(f"The user's age is {my_age}")
    return f"The message was successfully recieved: {my_name,my_age}"

@app.get("/secondary_page")
async def load_secondary():
    return FileResponse("secondary.html")