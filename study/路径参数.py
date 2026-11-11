from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/book/{id}")
async def get_book(id: int = Path(...,gt=0,lt=101,description="书籍的id，取值范围1~100")):
    return {"id": id, "title": f"这是第{id}本书"}

@app.get("/user/{id}")
async def get_user(id: int):
    return {"id": id, "title": f"普通用户{id}"}

# 需求：查找书籍的作者，路径参数 name，长度范围 2-10
@app.get("/author/{name}")
async def get_author(name: str=Path(...,min_length=2,max_length=10)):
    return {"msg": f"这是{name}的信息"}

@app.get("/news/{id}")
async def get_news(id: int=Path(...)):
    return