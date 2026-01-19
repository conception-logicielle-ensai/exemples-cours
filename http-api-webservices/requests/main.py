from fastapi import FastAPI
from controllers.pokemon_controller import router as pokemon_router

app = FastAPI(title="Pokémon API")

# Inclure le router Pokémon
app.include_router(pokemon_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
