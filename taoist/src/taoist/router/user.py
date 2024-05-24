import time
from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["用户操作"])


@router.post("/login")
async def login():
    """
    用户登陆
    """
    time.sleep(10)
    return "login success !"


@router.post("/signout")
async def signout():
    """
    用户登出
    """


@router.post("/register")
async def register():
    """
    用户注册
    """


@router.delete("/delete")
async def delete():
    """
    用户清除
    """


@router.put("/update")
async def update():
    """
    用户更新
    """


@router.get("/query")
async def query():
    """
    用户查询
    """
