from fastapi import APIRouter


router = APIRouter(prefix="/role", tags=["角色操作"])


@router.post("/addition")
async def addition():
    """
    角色增加
    """


@router.delete("/delete")
async def delete():
    """
    角色清除
    """


@router.put("/update")
async def update():
    """
    角色更新
    """


@router.get("/query")
async def query():
    """
    角色查询
    """
