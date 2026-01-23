from pydantic import BaseModel

class Item(BaseModel):
    """
    Représente un article avec ses détails.
    
    - **name**: Le nom de l'article.
    - **description**: Une description optionnelle de l'article.
    - **price**: Le prix de l'article.
    - **tax**: Une taxe optionnelle associée à l'article.
    - **tags**: Une liste de tags associés à l'article.
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
