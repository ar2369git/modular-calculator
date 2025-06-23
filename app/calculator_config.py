import os
from dotenv import load_dotenv
from .exceptions import ConfigError

load_dotenv()

class Config:
    # Only AUTO_SAVE is read at import time
    AUTO_SAVE = os.getenv("AUTO_SAVE", "true").lower() in ("1", "true", "yes")

    @classmethod
    def validate(cls):
        path = os.getenv("HISTORY_PATH")
        if not path:
            raise ConfigError("HISTORY_PATH not set in environment")
        # set it once a valid value is present
        cls.HISTORY_PATH = path
