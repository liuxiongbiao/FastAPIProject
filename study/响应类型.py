from fastapi import FastAPI
from fastapi.responses import HTMLResponse,FileResponse

app = FastAPI()

@app.get("/")
async def say_hello():
    return {"message": "Hello World"}

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"

# 接口：返回一张图片内容
@app.get("/file", response_class=FileResponse)
async def get_file():
    path= "./files/1.jpg"
    return FileResponse(path)