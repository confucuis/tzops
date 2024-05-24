import asyncio

from fastapi import FastAPI
from taoist.router import router
from taoist.core.log import UVICORN_CONFIG, logger, Color
from taoist.core.config import settings


app = FastAPI(
    title=settings.app_name,
    debug=settings.app_debug,
    summary=settings.app_summary,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(router, prefix=settings.app_prefix)

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
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
        log_level=settings.app_loglevel,
        workers=settings.app_works,  # 配置多个进程运行
        log_config=UVICORN_CONFIG,
    )

    try:
        logger.info(f"Server Start On: http://{settings.app_host}:{settings.app_port}")
        server = uvicorn.Server(setting)
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("Server is shutting down gracefully.")
    except Exception:
        pass


if __name__ == "__main__":
    main()
