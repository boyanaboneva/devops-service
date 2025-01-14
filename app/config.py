from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    LOG_LEVEL: str


settings = Settings()

# https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': settings.LOG_LEVEL,
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': settings.LOG_LEVEL,
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': settings.LOG_LEVEL,
            'propagate': True
        },
        "uvicorn": {
            "handlers": ["console"],
            "propagate": False,
        },
    }
}
