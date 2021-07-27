from fastapi import APIRouter, HTTPException
from ..schema.base import PokemonResponse, PokemonParameter
from ..pokomon_repo.repo import Pocket

router = APIRouter()

# CREATE
@router.post('/pokemon/{pokemon_name}', response_model=PokemonResponse)
async def create_pokemon(pokemon_name:str, pokemon: PokemonParameter):
    try:
        pocket = Pocket()
        output = pocket.insert(pokemon_name, pokemon)
        return PokemonResponse(result=[output])
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

# READ_ALL
@router.get('/pokemon', response_model=PokemonResponse)
async def read_all_pokemon():
    try:
        pocket = Pocket()
        output = pocket.read()
        return PokemonResponse(result=output)
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

# READ_BY_ID
@router.get('/pokemon/{pokemon_number}', response_model=PokemonResponse)
async def read_by_id_pokemon(pokemon_number: int):
    try:
        pocket = Pocket()
        ouput = pocket.read_by_id(pokemon_number)
        return PokemonResponse(result=[ouput])
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

# UPDATE
@router.put('/pokemon/{pokemon_number}', response_model=PokemonResponse)
async def update_pokemon(pokemon_number: int, pokemon: PokemonParameter):
    try:
        pocket = Pocket()
        output= pocket.update(pokemon_number, pokemon)
        return PokemonResponse(result=[output])
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

# DELETE
@router.delete('/pokemon/{pokemon_number}')
async def delete_pokemon(pokemon_number: int):
    try:
        pocket = Pocket()
        output = pocket.delete(pokemon_number)
        return {'delete': output}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

# FILTER_BY_TYPES
@router.get('/pokemon/filter/{type}', response_model=PokemonResponse)
async def filter_pokemon_by_type(type: str):
    try:
        pocket = Pocket()
        output = pocket.filter(type)
        return PokemonResponse(result=output)
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))
