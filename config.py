import os
import secrets


class Config:
    SECRET_KEY = os.environ.get("APP_SECRET_KEY") or secrets.token_hex(32)

    DB_CONFIG = {
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": os.environ.get("DB_USER", "root"),
        "password": os.environ.get("DB_PASSWORD", ""),
        "database": os.environ.get("DB_NAME", "customs_portal"),
        "port": int(os.environ.get("DB_PORT", "3306")),
        "connection_timeout": int(os.environ.get("DB_CONNECTION_TIMEOUT", "5")),
        "autocommit": False,
    }