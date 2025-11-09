from fastapi import APIRouter, HTTPException
from typing import Optional

router = APIRouter()

# Dummy in-memory store for shares
shared_recipes = {}

@router.post("/share")
def share_recipe(user_id: int, recipe_id: int, platform: Optional[str] = None, privacy: Optional[str] = "private"):
    # Simulate OAuth verification
    if platform and platform.lower() not in ["facebook", "twitter", "instagram"]:
        raise HTTPException(status_code=400, detail="Unsupported social platform")
    key = (user_id, recipe_id)
    shared_recipes[key] = {"platform": platform, "privacy": privacy}
    return {"status": "shared", "platform": platform, "privacy": privacy}
