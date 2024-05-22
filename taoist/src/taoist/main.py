import asyncio
import uvicorn

import uvicorn.config
import uvicorn.server
from fastapi import FastAPI
from taoist.router import user, role
from taoist.log import UVICORN_CONFIG, logger, Color


app = FastAPI(debug=True)

app.include_router(user.router)
app.include_router(role.router)

TAOIST = """
@@@@@@@@@@@@       @@@@@       @@@@@@@@@@@      @@@     @@@@@@@@@@@ @@@@@@@@@@@@ 
@@@@@@@@@@@@      @@@ @@@      @@@@@@@@@@@  @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@@
    @@@@         @@@   @@@     @@@@   @@@@    @@@@@@@   @@@@@           @@@@    
    @@@@        @@@@@@@@@@@    @@@     @@@     @@@@@    @@@@@@@@@@@     @@@@
    @@@@       @@@@@@@@@@@@@   @@@@   @@@@     @@@@@          @@@@@     @@@@
    @@@@      @@@         @@@  @@@@@@@@@@@    @@@@@@@   @@@@@@@@@@@     @@@@
    @@@@     @@@@@       @@@@@ @@@@@@@@@@@  @@@@@@@@@@@ @@@@@@@@@@@     @@@@
"""


def main():
    logger.info(Color.YELLOW + TAOIST + Color.RESET)

    setting = uvicorn.Config(
        "taoist.main:app",
        host="0.0.0.0",
        port=7000,
        reload=True,
        log_level="error",
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
