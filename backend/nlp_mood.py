from fastapi import APIRouter
from pydantic import BaseModel
import re

router = APIRouter()

class TextMoodInput(BaseModel):
    text: str

@router.post("/nlp-mood")
def analyze_mood(input: TextMoodInput):
    # Dummy NLP analysis: map keywords to moods
    text = input.text.lower()
    mood_map = {
        "happy": ["glad", "joy", "happy", "excited"],
        "sad": ["sad", "down", "unhappy"],
        "relaxed": ["calm", "relaxed", "peaceful"],
        "energetic": ["energetic", "active", "lively"]
    }
    for mood, keywords in mood_map.items():
        for kw in keywords:
            if re.search(r"\b" + kw + r"\b", text):
                return {"detected_mood": mood}
    return {"detected_mood": "neutral"}
