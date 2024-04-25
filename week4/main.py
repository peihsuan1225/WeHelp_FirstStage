from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
# 模板套用工具
templates = Jinja2Templates(directory="templates")
# 存取資料工具
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

# 根路徑，渲染 "index.html" 
@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 定義帳號密碼的輸入值
class SigninData(BaseModel):
    username: str
    password: str

# signin路徑，判斷是否有缺少輸入的值，並顯示對應的錯誤訊息
# 若輸入正確會回傳signed:Ture，錯誤會回傳signed:False並顯示對應的錯誤訊息
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

# member路徑，會先確認是否已經有user數據(已登入)，如果有才渲染"member.html"，否則回到首頁
@app.get("/member")
async def member_page(request: Request):
    user = request.session.get("user")
    if user:
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/")

# error路徑，渲染 "error.html" 模板
@app.get("/error")
async def error_page(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

# signout路徑，移除用戶數據(已登出)，重新導向首頁
@app.get("/signout")
async def signout(request:Request):
    request.session.pop("user", None)
    return RedirectResponse(url="http://127.0.0.1:8000/")