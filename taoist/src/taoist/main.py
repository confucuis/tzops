from fastapi import FastAPI

from taoist.router import user


app = FastAPI(debug=True)

app.include_router(user.router)


def main():
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7000)
