from uvicorn.config import LOGGING_CONFIG

# 复制默认配置
UVICORN_CONFIG = LOGGING_CONFIG.copy()

# 修改格式
UVICORN_CONFIG["formatters"]["default"]["fmt"] = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
UVICORN_CONFIG["formatters"]["default"]["datefmt"] = "%Y-%m-%d %H:%M:%S"

# 应用到access日志记录器
UVICORN_CONFIG["loggers"]["uvicorn.access"]["propagate"] = False
UVICORN_CONFIG["loggers"]["uvicorn.access"]["handlers"] = ["default"]
UVICORN_CONFIG["loggers"]["uvicorn.access"]["level"] = "INFO"

# 应用到error日志记录器
UVICORN_CONFIG["loggers"]["uvicorn.error"]["propagate"] = False
UVICORN_CONFIG["loggers"]["uvicorn.error"]["handlers"] = ["default"]
UVICORN_CONFIG["loggers"]["uvicorn.error"]["level"] = "INFO"
