from ..utils.db import get_session
from ..models.caracteristica import Caracteristica
from sqlmodel import select


def post(input):
    with get_session() as session:
        c = Caracteristica(punto=input.punto)
        session.add(c)
        session.commit()
        session.refresh(c)
        return c


def get(id: int):
    with get_session() as session:
        c = session.query(Caracteristica).get(id)
        return c


def get_all():
    with get_session() as session:
        c = session.exec(select(Caracteristica)).all()
        return c
