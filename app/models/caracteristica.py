from sqlmodel import SQLModel, Field
from typing import Optional


class Base_Caracteristica(SQLModel):
    punto: int


class Caracteristica(Base_Caracteristica, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class Caracteristica_Create(Base_Caracteristica):
    pass


class Caracteristica_Read(Base_Caracteristica):
    id: int
