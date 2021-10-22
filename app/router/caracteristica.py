from fastapi import APIRouter, HTTPException

from app.api.caracteristica import post_caracteristica
from app.models.caracteristica import Caracteristica_Create, Caracteristica_Read


router = APIRouter()


@router.post("/", response_model=Caracteristica_Read, status_code=201)
def create_caracteristica(payload: Caracteristica_Create) -> Caracteristica_Read:
    return post_caracteristica(payload)
