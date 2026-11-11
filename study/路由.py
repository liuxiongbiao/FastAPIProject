from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 访问 /hello 响应结果 msg：你好 FastAPI
@app.get("/hello")
async def say_hello():
    return {"message": "你好 FastAPI"}
# 练习
@app.get("/user/hello")
async def say_hello_user():
    return {"message": "我正在学习Fast API"}


