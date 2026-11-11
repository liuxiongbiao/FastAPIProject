from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 需求 查询新闻 --> 分页，skip：跳过的记录数， limit：返回的记录数 10

@app.get("/news/news_list")
async def get_news_list(
        skip: int = Query(0, description="跳过的记录数", lt=100),
        limit: int = Query(10, description="返回的记录数")
):
    return {"skip": skip, "limit": limit}

# 练习
@app.get("/book")
async def get_book(category : str = Query("Python开发",min_length=5,max_length=255,description="图书分类")):
    return {"category": category}
