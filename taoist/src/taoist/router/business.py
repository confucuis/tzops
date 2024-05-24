from fastapi import APIRouter


router = APIRouter(prefix="/business", tags=["业务操作"])


@router.post("/")
async def test():
    pass
