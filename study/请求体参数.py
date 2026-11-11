from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"message": "Hello World"}


# 注册：用户名和密码 -> str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名，长度要求2-10个字")
    password: str = Field(min_length=3, max_length=20)


class Book(BaseModel):
    title: str = Field(...,min_length=2, max_length=20)
    author: str = Field(...,min_length=2, max_length=10)
    publisher: str = Field("中国人民出版社")
    price: float=Field(...,gt=0)


@app.post("/register")
async def register(user: User):
    return user


@app.post("/book")
async def book(book: Book):
    return book
