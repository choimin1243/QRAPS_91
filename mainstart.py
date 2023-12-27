from fastapi import FastAPI
from main import appends
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from package import pack
from rcpackage import rcpack
import models
from database import engine
from fastapi import FastAPI, Form, Request, Depends
from Lpackage import Lpack

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

templates = Jinja2Templates(directory="templates")
templates.env.globals.update(enumerate=enumerate)

app.include_router(appends, prefix="/api")
app.include_router(pack, prefix="/package")
app.include_router(rcpack, prefix="/rcpackage")
app.include_router(Lpack,prefix="/Lpackage")
models.Base.metadata.create_all(bind=engine)
















@app.get("/")
async def render_upload_form(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
