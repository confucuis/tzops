import asyncio
import logging
import uvicorn

from fastapi import FastAPI
from taoist.router import user


app = FastAPI(debug=True)

app.include_router(user.router)

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
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info(TAOIST)

    try:
        uvicorn.run("taoist.main:app", host="0.0.0.0", port=7000)
    except Exception:
        pass


if __name__ == "__main__":
    asyncio.run(main())
