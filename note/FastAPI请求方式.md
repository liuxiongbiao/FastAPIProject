# FastAPI 中 GET、POST 与其他请求方式

## 1. HTTP 请求方式是什么

HTTP 请求方式（HTTP method）表示客户端希望服务器对某个资源执行什么操作。常见的有 `GET`、`POST`、`PUT`、`PATCH` 和 `DELETE`。

## 2. GET 和 POST 的区别

| 对比项 | GET | POST |
|---|---|---|
| 常见用途 | 查询、读取数据 | 提交数据、新增资源或执行操作 |
| 参数通常放置位置 | URL 路径或查询参数 | 请求体（常见为 JSON） |
| 是否适合直接在浏览器地址栏测试 | 适合 | 通常需要 Swagger、HTTP 客户端或前端程序发送请求 |
| 典型例子 | 按分类查询书籍 | 新增一本书 |

### GET 示例

请求地址：

```text
http://127.0.0.1:8000/books?category=小说
```

`category=小说` 是查询参数。FastAPI 会把它传给函数中的 `category` 参数。

### POST 示例

POST 通常把要提交的数据放在 JSON 请求体里：

```json
{
  "title": "示例书名",
  "category": "小说",
  "price": 29.9
}
```

数据不在 URL 中，但这不代表它自动加密；传输敏感数据仍应使用 HTTPS。

## 3. FastAPI 代码示例

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    category: str
    price: float


@app.get("/books")
async def get_books(category: str | None = None):
    return {"action": "查询书籍", "category": category}


@app.post("/books")
async def create_book(book: Book):
    return {"action": "新增书籍", "book": book.model_dump()}
```

- `@app.get("/books")` 定义 GET 接口。
- `category: str | None = None` 是可选查询参数；例如 `/books?category=小说`。
- `Book` 继承 `BaseModel`，描述 POST 请求体需要包含哪些字段及其类型。
- `book: Book` 表示 FastAPI 从请求体读取 JSON，并按 `Book` 的规则校验。
- 本例只返回接收到的数据，没有将其保存到数据库。

### 用 PyCharm HTTP Client 测试

```http
GET http://127.0.0.1:8000/books?category=小说
Accept: application/json

###

POST http://127.0.0.1:8000/books
Content-Type: application/json

{
  "title": "示例书名",
  "category": "小说",
  "price": 29.9
}
```

也可以打开 `http://127.0.0.1:8000/docs`，在 FastAPI 自动生成的交互式文档中测试接口。

## 4. FastAPI 还支持哪些请求方式

| 方法 | 常见用途 | FastAPI 装饰器示例 |
|---|---|---|
| `PUT` | 整体替换或更新资源 | `@app.put("/books/{book_id}")` |
| `PATCH` | 只更新资源的一部分 | `@app.patch("/books/{book_id}")` |
| `DELETE` | 删除资源 | `@app.delete("/books/{book_id}")` |
| `HEAD` | 类似 GET，但不返回响应正文 | `@app.head("/books")` |
| `OPTIONS` | 查询接口支持的通信选项；浏览器跨域时也常用于预检 | `@app.options("/books")` |
| `TRACE` | 诊断请求经过的路径，普通业务接口很少使用 | `@app.trace("/books")` |

FastAPI 也支持用 `@app.post(...)`、`@app.get(...)` 等装饰器定义接口。HTTP 标准还定义了 `CONNECT`，但它主要用于建立网络隧道，通常不会用于普通业务 API。

## 5. 初学时怎么选

- 查数据：通常用 `GET`。
- 新增数据或提交操作：通常用 `POST`。
- 整体更新：通常用 `PUT`。
- 部分更新：通常用 `PATCH`。
- 删除数据：通常用 `DELETE`。

HTTP 方法表达的是接口语义；最终接口具体做什么仍由服务器端代码决定。按惯例，GET 应用于读取，不应让 GET 请求悄悄修改数据。

## 参考

- [FastAPI：First Steps（路径操作与请求方法）](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI：Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI：Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [RFC 9110：HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
