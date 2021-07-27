from pydantic import BaseModel
from .role import role, BasePokemon
from typing import List

class PokemonParameter(BasePokemon):
    pass

class PokemonResponse(BaseModel):
    result: List[BasePokemon]
