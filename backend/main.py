from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import time

app = FastAPI(title="Mood-based Recipe Recommender")

# Mock database
recipes_db = [
    {"id": 1, "name": "Spaghetti Carbonara", "tags": ["happy", "energetic"]},
    {"id": 2, "name": "Chicken Soup", "tags": ["sad", "comfort"]},
    {"id": 3, "name": "Avocado Toast", "tags": ["relaxed", "happy"]}
]

class MoodInput(BaseModel):
    mood: str

class Recipe(BaseModel):
    id: int
    name: str

@app.post("/mood-to-recipes", response_model=List[Recipe])
def mood_to_recipes(mood_input: MoodInput):
    start_time = time.time()
    mood = mood_input.mood.lower()
    # Simple rule-based matching for demonstration
    matched_recipes = [r for r in recipes_db if mood in r["tags"]]
    # Return up to 5 recipes
    result = matched_recipes[:5]
    elapsed = time.time() - start_time
    if elapsed > 2.0:
        raise HTTPException(status_code=503, detail="Response time exceeded 2 seconds")
    return result
