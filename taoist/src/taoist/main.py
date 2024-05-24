import asyncio

from fastapi import FastAPI
from taoist.router import user, role
from taoist.log import UVICORN_CONFIG, logger, Color


app = FastAPI(debug=True)

app.include_router(user.router)
app.include_router(role.router)

TAOIST = r"""
@@@@@@@@@@@@       @@@@@       @@@@@@@@@@@    @@@@@    @@@@@@@@@@@ @@@@@@@@@@@@         _____
@@@@@@@@@@@@      @@@ @@@      @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@@        | ? ? |
    @@@@         @@@   @@@     @@@@   @@@@ @@@@@@@@@@@ @@@@@           @@@@            \__-__/
    @@@@        @@@@@@@@@@@    @@@@   @@@@    @@@@@    @@@@@@@@@@@     @@@@             _| |_
    @@@@       @@@@@@@@@@@@@   @@@@   @@@@    @@@@@          @@@@@     @@@@            /-----\
    @@@@      @@@         @@@  @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@     @@@@            + |.| +
    @@@@     @@@@@       @@@@@ @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@     @@@@            +=====+
"""


def main():
    import uvicorn

    logger.info(Color.YELLOW + TAOIST + Color.RESET)

    setting = uvicorn.Config(
        "taoist.main:app",
        host="0.0.0.0",
        port=7000,
        reload=True,
        log_level="info",
        workers=1,  # 配置多个进程运行
        log_config=UVICORN_CONFIG,
    )

    try:
        logger.info("Server Start On http://0.0.0.0:7000")
        server = uvicorn.Server(setting)
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("Server is shutting down gracefully.")
    except Exception:
        pass


if __name__ == "__main__":
    main()
