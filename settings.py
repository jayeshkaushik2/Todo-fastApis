from decouple import config

class Settings:
    DEBUG = config("DEBUG", default=False, cast=bool)
    DATABASE_URL = config("DATABASE_URL", default="")

conf = Settings()