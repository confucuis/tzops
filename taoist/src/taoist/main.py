import asyncio
import logging
import uvicorn

from fastapi import FastAPI
import uvicorn.config
import uvicorn.server
from taoist.router import user
from taoist.config import UVICORN_CONFIG


app = FastAPI(debug=True)

app.include_router(user.router)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


TAOIST = """
@@@@@@@@@@@@       @@@@@       @@@@@@@@@@@      @@@     @@@@@@@@@@@ @@@@@@@@@@@@ 
@@@@@@@@@@@@      @@@ @@@      @@@@@@@@@@@              @@@@@@@@@@@ @@@@@@@@@@@@
    @@@@         @@@   @@@     @@@     @@@  @@@@@@@@@@@ @@@@            @@@@    
    @@@@        @@@@@@@@@@@    @@@     @@@    @@@@@@@   @@@@@@@@@@@     @@@@
    @@@@       @@@@@@@@@@@@@   @@@     @@@     @@@@@           @@@@     @@@@
    @@@@      @@@         @@@  @@@@@@@@@@@    @@@@@@@   @@@@@@@@@@@     @@@@
    @@@@     @@@@@       @@@@@ @@@@@@@@@@@  @@@@@@@@@@@ @@@@@@@@@@@     @@@@
"""


def main():
    logger.info(TAOIST)

    setting = uvicorn.Config(
        "taoist.main:app",
        host="0.0.0.0",
        port=7000,
        reload=True,
        log_config=UVICORN_CONFIG,
    )

    try:
        server = uvicorn.Server(setting)
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("Server is shutting down gracefully.")
    except Exception:
        pass


if __name__ == "__main__":
    main()
