from ..models import *
from sqlmodel import Session, SQLModel, create_engine

from ..config import get_settings


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)

def get_session():
    return Session(engine)


engine = create_engine(get_settings().database_url, echo=True)
