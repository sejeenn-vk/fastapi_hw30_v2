from dotenv import dotenv_values, load_dotenv

load_dotenv()
config = dotenv_values("../.env")

DB_NAME = config.get("DB_NAME")
DB_URL = f"sqlite+aiosqlite:///./{DB_NAME}"


class Settings:
    DB_NAME = DB_NAME
    DB_URL = DB_URL
