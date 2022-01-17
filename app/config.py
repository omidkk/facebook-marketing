"""Flask configuration variables."""
import logging
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Facebook Marketing
    ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
    AD_ACCOUNT_ID = environ.get("AD_ACCOUNT_ID")
    APP_SECRET = environ.get("APP_SECRET")
    APP_ID = environ.get("APP_ID")
    PAGE_ID = environ.get("PAGE_ID")
