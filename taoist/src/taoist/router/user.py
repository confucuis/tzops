import time
from fastapi import APIRouter


router = APIRouter(prefix="/user")


@router.get("/login")
async def login():
    time.sleep(10)
    return "login success !"
