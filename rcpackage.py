from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Request, Depends
from fastapi import APIRouter,Request
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todos2


rcpack = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals.update(enumerate=enumerate)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@rcpack.get("/")
async def render_upload_form(request: Request):
    return templates.TemplateResponse("rcpackage.html", {"request": request})


def hello2(db: Session = Depends(get_db)):
    todos2 = db.query(Todos2).all()
    package=[package.title for package in todos2]
    return package


@rcpack.post("/send-text/")
async def send_list(request: Request, db: Session = Depends(get_db), text: str = Form(...)):
    new_todo = Todos2(title=text)
    db.add(new_todo)
    db.commit()
    new_packages = db.query(Todos2).all()
    new_package = [package.title for package in new_packages]

    return templates.TemplateResponse("rcpackage.html", {"request": request})


def get_all_todos_from_db(db: Session):
    todos = db.query(Todos2).all()
    return todos
