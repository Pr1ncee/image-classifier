import os

from dotenv import load_dotenv

load_dotenv()


class PostgresConfig:
    HOST = os.getenv("POSTGRES_HOST", "localhost")
    PWD = os.getenv("POSTGRES_PASSWORD", "postgres")
    USER = os.getenv("POSTGRES_USER", "postgres")
    NAME = os.getenv("POSTGRES_NAME", "del_corso")
    PORT = os.getenv("POSTGRES_PORT", "5432")


class GeneralConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    DEBUG = os.getenv("DEBUG", True)
    LANGUAGE_CODE = "en"
    TIME_ZONE = "Europe/Moscow"
    TARGET_IMAGE_DIR = "images/"


class AdminConfig:
    USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    EMAIL = os.getenv("ADMIN_EMAIL", "admin@admin.com")
    PWD = os.getenv("ADMIN_PWD", "admin")


general_config = GeneralConfig()
postgres_config = PostgresConfig()
admin_config = AdminConfig()
