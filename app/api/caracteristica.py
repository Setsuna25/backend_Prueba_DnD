from ..utils.db import get_session
from ..models.caracteristica import Caracteristica


def post_caracteristica(input):
    with get_session() as session:
        c = Caracteristica(punto=input.punto)
        session.add(c)
        session.commit()
        session.refresh(c)
        return c
