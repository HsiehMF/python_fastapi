from typing import List, Optional
from pydantic import BaseModel

class role(BaseModel):
    number: int = None
    name: str = ''
    types: List[str] = None

class BasePokemon(role, BaseModel):
    evolutions: List[role] = None
