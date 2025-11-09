from fastapi import APIRouter

router = APIRouter()

supported_languages = ["en", "es", "fr", "de"]

@router.get("/lang/{lang_code}")
def get_language_content(lang_code: str):
    if lang_code not in supported_languages:
        return {"error": "Language not supported"}
    # Dummy content for demo
    content = {
        "en": "Welcome to Mood Recipe App",
        "es": "Bienvenido a la aplicación Mood Recipe",
        "fr": "Bienvenue dans l'application Mood Recipe",
        "de": "Willkommen bei der Mood Recipe App"
    }
    return {"message": content[lang_code]}
