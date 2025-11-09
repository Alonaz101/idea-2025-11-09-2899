from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# In-memory store for demo
community_recipes = {}
recipe_ratings = {}

class CommunityRecipe(BaseModel):
    id: int
    user_id: int
    title: str
    content: str

class RecipeRating(BaseModel):
    recipe_id: int
    rating: int

@router.post("/community/submit")
def submit_recipe(recipe: CommunityRecipe):
    if recipe.id in community_recipes:
        raise HTTPException(status_code=400, detail="Recipe already submitted")
    community_recipes[recipe.id] = recipe
    recipe_ratings[recipe.id] = []
    return {"status": "submitted", "recipe_id": recipe.id}

@router.post("/community/rate")
def rate_recipe(rating: RecipeRating):
    if rating.recipe_id not in recipe_ratings:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if rating.rating < 1 or rating.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    recipe_ratings[rating.recipe_id].append(rating.rating)
    avg_rating = sum(recipe_ratings[rating.recipe_id]) / len(recipe_ratings[rating.recipe_id])
    return {"avg_rating": avg_rating}
