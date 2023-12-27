from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Request, Depends
from fastapi import APIRouter,Request
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Lpackage
import re

Lpack = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.globals.update(enumerate=enumerate)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@Lpack.get("/")
async def render_upload_form(request: Request):
    return templates.TemplateResponse("Lpackage.html", {"request": request})


def call_Lpackage(db: Session = Depends(get_db)):
    Lpacks = db.query(Lpackage).all()
    package=[package.title for package in Lpacks]
    return package


@Lpack.post("/send-text/")
async def send_list(request: Request, db: Session = Depends(get_db), package: str = Form(...),partnumber: str = Form(...)):
    new_todo = Lpackage(package=package,partnumber=partnumber)
    db.add(new_todo)
    db.commit()
    L_something = db.query(Lpackage).all()
    package_list = [L_one.package for L_one in L_something]
    partnumber_list=[L_one.partnumber for L_one in L_something]
    print(package_list)
    print(partnumber_list)





    return templates.TemplateResponse("Lpackage.html", {"request": request})


def get_all_Lpackage_package_from_db(db: Session):
    Lpackages = db.query(Lpackage.package).all()
    package_list = [L_one.package for L_one in Lpackages]
    return package_list


def get_all_Lpackage_partnumber_from_db(db: Session):
    Lpartnmuber=db.query(Lpackage.partnumber).all()
    partnumber_list = [L_one.partnumber for L_one in Lpartnmuber]

    return partnumber_list




