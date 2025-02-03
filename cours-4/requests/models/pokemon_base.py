from pydantic import BaseModel

class PokemonBase(BaseModel):
    id: int
    name: str
    weight: int
    height: int
