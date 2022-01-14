"""Flask configuration variables."""
import logging
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    logging.basicConfig(
        filename=environ.get("LOG_FILE"),
        level=logging._nameToLevel.get(environ.get("LOG_LEVEL")),
    )
