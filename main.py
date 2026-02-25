from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import FileResponse, RedirectResponse


app = FastAPI()

@app.get("/")
async def load_home(request: Request):
    return FileResponse("homepage.html")

@app.post("/submit-item")
async def handle_form(my_name:str = Form(...),my_age:str = Form(...)):
    if my_name.strip() and my_age.strip():
        print(f"The user typed: {my_name}")
        print(f"The user's age is {my_age}")
        return RedirectResponse(url=f"/secondary_page?name={my_name}&age={my_age}", status_code=303)
    else:
        return HTTPException(status_code=400, detail="Invalid input: Both name and age are required.")

@app.get("/secondary_page")
async def load_secondary():
    return FileResponse("secondary.html")