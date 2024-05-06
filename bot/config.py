from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "24339011"))
    API_HASH = env.get("TELEGRAM_API_HASH", "a85d1d917af0d4d02811a9a007b8dcda")
    OWNER_ID = int(env.get("OWNER_ID", "5475357007"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Itachixfiletolink_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7063658748:AAGBBU0mAkCBmfkqEDa8-Ab_1mOa0nTrRU8")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002079492072"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("https://filestreamzz-e29bb1d94044.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
