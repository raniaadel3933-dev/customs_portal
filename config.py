import os
import secrets


class Config:
    SECRET_KEY = os.environ.get("APP_SECRET_KEY") or secrets.token_hex(32)

    DB_CONFIG = {
        "host": os.environ.get("DB_HOST") or os.environ.get("MYSQLHOST") or "",
        "user": os.environ.get("DB_USER") or os.environ.get("MYSQLUSER") or "",
        "password": os.environ.get("DB_PASSWORD") or os.environ.get("MYSQLPASSWORD") or "",
        "database": os.environ.get("DB_NAME") or os.environ.get("MYSQLDATABASE") or "",
        "port": int((os.environ.get("DB_PORT") or os.environ.get("MYSQLPORT") or "3306").strip() or "3306"),
        "connection_timeout": int((os.environ.get("DB_CONNECTION_TIMEOUT") or "5").strip() or "5"),
        "autocommit": False,
    }