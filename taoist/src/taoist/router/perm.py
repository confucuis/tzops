from fastapi import APIRouter


router = APIRouter(prefix="/perm", tags=["权限操作"])


@router.post("/addition")
async def addition():
    """
    权限增加
    """


@router.delete("/delete")
async def delete():
    """
    权限清除
    """


@router.put("/update")
async def update():
    """
    权限更新
    """


@router.get("/query")
async def query():
    """
    权限查询
    """
