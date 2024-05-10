import mysql.connector
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
# 模板套用工具
templates = Jinja2Templates(directory="templates")
# 存取資料工具
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

# 連線到資料庫的資訊
def connect_to_database():
    return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "jessica1225",
    database = "website"
)


# 根路徑，套用 "index.html" 
@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# signup路徑，由前端獲取姓名、帳號、密碼
# 連線到資料庫確認是否已有存在的username，若有導向到error路徑，若無則新增資料到member table 並導向到根路徑
@app.post("/signup")
async def signup(request:Request, signup_name: str = Form(None), signup_username: str = Form(None), signup_password: str = Form(None)):
    mydb = connect_to_database()
    cursor = mydb.cursor()
    signup_query = "SELECT * FROM member WHERE username = %s COLLATE utf8mb4_bin"
    cursor.execute(signup_query, (signup_username,))
    result = cursor.fetchall()
    if result:
        cursor.close()
        mydb.close()
        return RedirectResponse(url="/error?message=Repeated username", status_code=302)    
    insert_query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (signup_name, signup_username, signup_password))
    mydb.commit()
    cursor.close()
    mydb.close()
    return RedirectResponse(url="/", status_code=302)

# signin路徑，由前端獲取帳號、密碼
# 連線到資料庫確認是否有對應的帳號、密碼，若有則儲存登入狀態、會員ID、會員姓名、會員帳號 並導向member路徑，若無則導向到error路徑
@app.post("/signin")
async def signin(request: Request, signin_username: str = Form(None), signin_password: str = Form(None)):
    mydb = connect_to_database()
    cursor = mydb.cursor()
    signin_query = "SELECT * FROM member WHERE username = %s COLLATE utf8mb4_bin AND password = %s COLLATE utf8mb4_bin"
    cursor.execute(signin_query, (signin_username, signin_password))
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    if result:
        session = request.session
        session["SIGNED-IN"] = True
        session["ID"] = result[0][0]
        session["NAME"] = result[0][1]
        session["USERNAME"] = result[0][2]
        return RedirectResponse(url="/member", status_code=302)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=302)

# member路徑，會先確認SIGNED-IN是否為ture(已登入)，如果是才套用"member.html"，否則回到根路徑
# 連線到資料庫抓取所有message的data(時間倒序)，欄位包括 message.id, message.content, message.member_id, member.name 
@app.get("/member")
async def member_page(request: Request):
    signed = request.session.get("SIGNED-IN")
    if signed is True:
        mydb = connect_to_database()
        cursor = mydb.cursor()
        name_message_query = """
        SELECT message.id, message.content, message.member_id, member.name 
        FROM message
        JOIN member ON message.member_id = member.id
        ORDER BY message.time DESC 
        """
        cursor.execute(name_message_query)
        result = cursor.fetchall()
        cursor.close()
        mydb.close()
        return templates.TemplateResponse("member.html", {"request": request,"result": result})
    else:
        return RedirectResponse(url="/")

# CreateMessage路徑，將 當前紀錄的會員id 和 前端獲取的留言內容 加入message table，並導向member路徑
@app.post("/CreateMessage")
async def createMessage(request: Request, messgae_content:str = Form(None)):
    mydb = connect_to_database()
    cursor = mydb.cursor()
    insert_query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    cursor.execute(insert_query, (request.session["ID"], messgae_content))
    mydb.commit()
    cursor.close()
    mydb.close()
    return RedirectResponse(url="/member", status_code=302)

# deleteMessage路徑，先確認 將被刪除的留言的使用者id 是否等於 當前登入的使用者id
# 上方條件成立才連線到資料庫，透過message_id刪除對應留言，並導向member路徑
@app.post("/deleteMessage")
async def deleteMessage(request: Request):
    data = await request.json()
    message_id = data.get("message_id")
    mydb = connect_to_database()
    cursor = mydb.cursor()
    select_query = """
    SELECT * FROM message
    WHERE id = %s
    """
    cursor.execute(select_query,(message_id,))
    result = cursor.fetchall()
    
    if result[0][1] == request.session["ID"]:
        delete_query = """
        DELETE FROM message
        WHERE id = %s
        """
        cursor.execute(delete_query, (message_id,))
        mydb.commit()
        cursor.close()
        mydb.close()
        return RedirectResponse(url="/member", status_code=302)
    
    cursor.close()
    mydb.close()

    
# error路徑，套用 "error.html" 
@app.get("/error")
async def error_page(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

# signout路徑，紀錄SIGNED-IN為false(已登出)、清除會員ID、會員姓名、會員帳號的值，重新導向根路徑
@app.get("/signout")
async def signout(request:Request):
    session = request.session
    session["SIGNED-IN"] = False
    session["ID"] = None
    session["NAME"] = None
    session["USERNAME"] = None
    return RedirectResponse(url="/")