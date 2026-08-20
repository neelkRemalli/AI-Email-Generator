import os

from dotenv import load_dotenv

from src.exceptions import ConfigurationError


load_dotenv()


class Settings:
    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "openai/gpt-oss-20b:free"
    REQUEST_TIMEOUT = 30
    MAX_RETRIES = 3


if not Settings.API_KEY:
    raise ConfigurationError(
        "OPENAI_API_KEY is missing in .env"
    )


   




