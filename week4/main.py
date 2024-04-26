from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
# 模板套用工具
templates = Jinja2Templates(directory="templates")
# 存取資料工具
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

# 根路徑，套用 "index.html" 
@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# signin路徑，判斷是否有缺少輸入值，定義對應的錯誤訊息
# 若輸入正確會導向member，紀錄SIGNED-IN為ture
# 錯誤導向error並挾帶對應的錯誤訊息
@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if username == "test" and password == "test":
        session = request.session
        session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=302)
    elif not username or not password:
        if not username and not password:
            error_message = "請輸入帳號、密碼"
        elif not username:
            error_message = "請輸入帳號"
        elif not password:
                error_message = "請輸入密碼"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=302)
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=302)

# member路徑，會先確認SIGNED-IN是否為ture(已登入)，如果是才套用"member.html"，否則回到首頁
@app.get("/member")
async def member_page(request: Request):
    signed = request.session.get("SIGNED-IN")
    if signed is True:
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/")

# error路徑，套用 "error.html" 
@app.get("/error")
async def error_page(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

# signout路徑，紀錄SIGNED-IN為false(已登出)，重新導向首頁
@app.get("/signout")
async def signout(request:Request):
    session = request.session
    session["SIGNED-IN"] = False
    return RedirectResponse(url="/")