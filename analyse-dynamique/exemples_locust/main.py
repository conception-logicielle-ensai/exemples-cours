from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
import time
import random

app = FastAPI(
    title="🚀 API de Démonstration High-Performance",
    version="2.0.0",
    description="API vitrine avec endpoints optimisés pour tests de charge",
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modèles de données
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    category: str = "general"
    in_stock: bool = True


class User(BaseModel):
    username: str
    email: str
    created_at: float | None = None


class Stats(BaseModel):
    total_items: int
    total_users: int
    avg_price: float
    uptime: float


# Base de données simulée avec plus de données
items_db = [
    Item(
        id=i,
        name=f"Produit {i}",
        description=f"Description du produit {i}",
        price=round(random.uniform(10, 1000), 2),
        category=random.choice(["electronics", "books", "clothing", "food"]),
        in_stock=random.choice([True, True, True, False]),
    )
    for i in range(1, 101)
]

users_db = []
start_time = time.time()


@app.get("/")
async def root():
    """Endpoint racine avec informations vitrine"""
    return {
        "message": "🚀 Bienvenue sur l'API High-Performance",
        "version": "2.0.0",
        "endpoints": {
            "docs": "/docs",
            "stats": "/stats",
            "items": "/items",
            "users": "/users",
        },
        "status": "🟢 Operational",
    }


@app.get("/health")
async def health_check():
    """Vérification de santé détaillée"""
    return {
        "status": "healthy",
        "uptime": round(time.time() - start_time, 2),
        "timestamp": time.time(),
    }


@app.get("/stats", response_model=Stats)
async def get_stats():
    """Statistiques en temps réel"""
    avg_price = sum(item.price for item in items_db) / len(items_db) if items_db else 0
    return Stats(
        total_items=len(items_db),
        total_users=len(users_db),
        avg_price=round(avg_price, 2),
        uptime=round(time.time() - start_time, 2),
    )


@app.get("/items", response_model=List[Item])
async def get_items(
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    in_stock: bool | None = None,
    limit: int = 100,
):
    """Récupère les items avec filtres avancés"""
    filtered = items_db

    if category:
        filtered = [i for i in filtered if i.category == category]
    if min_price is not None:
        filtered = [i for i in filtered if i.price >= min_price]
    if max_price is not None:
        filtered = [i for i in filtered if i.price <= max_price]
    if in_stock is not None:
        filtered = [i for i in filtered if i.in_stock == in_stock]

    return filtered[:limit]


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Récupère un item spécifique"""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Crée un nouvel item"""
    items_db.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Met à jour un item"""
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            items_db[i] = item
            return item
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Supprime un item"""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[i]
            return {"message": "Item supprimé", "id": item_id}
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.post("/users", response_model=User, status_code=201)
async def create_user(user: User):
    """Crée un nouvel utilisateur"""
    user.created_at = time.time()
    users_db.append(user)
    return user


@app.get("/users", response_model=List[User])
async def get_users():
    """Récupère tous les utilisateurs"""
    return users_db


if __name__ == "__main__":
    import asyncio

    uvicorn.run(app, host="0.0.0.0", port=8000)
