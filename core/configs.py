import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
# from typing import ClassVar

load_dotenv(find_dotenv())

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
user = os.environ["POSTGRES_USER"]
pw = os.environ["POSTGRES_PASSWORD"]
db_name = os.environ["POSTGRES_DB"]

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação

    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str 
    # DBBaseModel: ClassVar = DBBaseModel 

    class Config:
        case_sensitive = True 

settings = Settings(
    DB_URL = f"postgresql+asyncpg://{user}:{pw}@{host}:{port}/{db_name}"
)