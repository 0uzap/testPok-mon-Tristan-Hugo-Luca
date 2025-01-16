# app/routers/pokemons.py

"""
Endpoint pour les routes pokemons
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import battle_pokemon

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/battle}")
def battle_pokemon(first_api_id: int, second_api_id: int):
  """
    renvoie le gagnant entre deux pokémons
  """
  return battle_pokemon(first_api_id, second_api_id)
  """  try:
        gagnant = battle_pokemon(first_api_id, second_api_id)
        return {"gagnant": gagnant}
    except Exception as e:
        return {"error": f"Une erreur est survenue : {str(e)}"}"""
