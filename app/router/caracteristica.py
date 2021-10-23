from typing import List

from app.api.caracteristica import get, get_all, post
from app.models.caracteristica import Caracteristica_Create, Caracteristica_Read
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/", response_model=Caracteristica_Read, status_code=201)
def post_one(payload: Caracteristica_Create):
    return post(payload)


@router.get("/", response_model=List[Caracteristica_Read], status_code=201)
def get():
    return get_all()


@router.get("/{id}", response_model=Caracteristica_Read, status_code=201)
def get_one(id: int):
    return get(id=id)
