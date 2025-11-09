from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Dummy in-memory store
user_favorites = {}

class FavoriteRecipe(BaseModel):
    user_id: int
    recipe_id: int

@router.post("/favorites/add")
def add_favorite(fav: FavoriteRecipe):
    if fav.user_id not in user_favorites:
        user_favorites[fav.user_id] = set()
    user_favorites[fav.user_id].add(fav.recipe_id)
    return {"status": "added"}

@router.get("/favorites/{user_id}", response_model=List[int])
def get_favorites(user_id: int):
    return list(user_favorites.get(user_id, []))
