# 在 PyCharm Terminal 中启动 FastAPI 项目

## 常用命令格式

在 PyCharm 底部的 Terminal 中，进入项目根目录后运行：

```powershell
uvicorn 模块路径:FastAPI实例名 --reload
```

- `uvicorn`：运行 FastAPI 应用的服务器。正确拼写是 `uvicorn`，不是 `unvicorn`。
- 模块路径：从当前终端所在的项目目录开始写。目录和 `.py` 文件名用点号连接，文件名不写 `.py`。
- `:`：分隔模块路径和 FastAPI 应用实例名。
- `app`：通常是代码里的 `app = FastAPI()`。
- `--reload`：开发时修改代码后自动重启服务器。

## 示例一：文件在项目根目录

目录结构：

```text
项目/
└── main.py
```

`main.py` 中定义了 `app = FastAPI()`，在项目根目录的 PyCharm Terminal 中运行：

```powershell
uvicorn main:app --reload
```

## 示例二：文件在一个子目录中

目录结构：

```text
项目/
└── study/
    └── luyou.py
```

在项目根目录的 PyCharm Terminal 中运行：

```powershell
uvicorn study.luyou:app --reload
```

## 示例三：文件在两层子目录中

目录结构：

```text
项目/
└── study/
    └── api/
        └── luyou.py
```

在项目根目录的 PyCharm Terminal 中运行：

```powershell
uvicorn study.api.luyou:app --reload
```

## FastAPI 实例使用其他变量名

如果文件中定义的是 `api = FastAPI()`，冒号后就写 `api`：

```powershell
uvicorn study.luyou:api --reload
```

## `python -m` 是什么？

也可以用下面的形式启动：

```powershell
python -m uvicorn study.luyou:app --reload
```

这里的 `python -m` 是 Python 的一种启动模块方式，不是 PyCharm 命令。它会通过当前 Python 解释器运行 Uvicorn。两种形式都可以；如果 PyCharm Terminal 已激活项目的 `.venv`，直接运行 `uvicorn ...` 通常就可以。

## 记忆方法

- 点号 `.` 表示进入子目录，最后一段是 Python 文件名（不带 `.py`）。
- 冒号 `:` 后面是 FastAPI 实例的变量名。
- 命令中的模块路径取决于终端当前所在目录。