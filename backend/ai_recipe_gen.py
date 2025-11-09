from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class RecipeRequest(BaseModel):
    user_id: int
    mood: str
    preferences: List[str] = []
    history: List[int] = []

class GeneratedRecipe(BaseModel):
    id: int
    name: str
    description: str

@router.post("/generate-recipes", response_model=List[GeneratedRecipe])
def generate_recipes(request: RecipeRequest):
    # Mock AI: generate 2 personalized recipes
    recipes = [
        {"id": 101, "name": "AI Special Salad", "description": "A personalized healthy salad based on your mood."},
        {"id": 102, "name": "AI Mood Smoothie", "description": "A refreshing smoothie tailored to your energetic mood."}
    ]
    return recipes
