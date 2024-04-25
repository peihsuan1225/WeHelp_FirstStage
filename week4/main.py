from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="super-secret-key")


@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class SigninData(BaseModel):
    username: str
    password: str
    
@app.post("/signin")
async def signin(signin_data: SigninData, request: Request):
    username = signin_data.username
    password = signin_data.password
    if not username or not password:
        if not username and not password:
            error_message = "請輸入帳號、密碼"
        elif not username:
            error_message = "請輸入帳號"
        elif not password:
                error_message = "請輸入密碼"
        
        return JSONResponse(status_code=400, content={"signed": False,  "message": error_message})

    if username == "test" and password == "test":
        request.session["user"] = {"username":"password"}
        return{"signed":True}
    else:
        return JSONResponse(status_code=400,content={"signed":False,"message":"帳號、或密碼輸入錯誤"})

@app.get("/member")
async def member_page(request: Request):
    user = request.session.get("user")
    if user:
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/")

@app.get("/error")
async def error_page(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

@app.get("/signout")
async def signout(request:Request):
    request.session.pop("user", None)
    return RedirectResponse(url="http://127.0.0.1:8000/")