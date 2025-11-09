import pytest
from pydantic import ValidationError
from backend.models import User, Recipe

def test_user_creation_valid():
    user = User(id=1, username="validuser", email="user@example.com")
    assert user.id == 1
    assert user.username == "validuser"
    assert user.email == "user@example.com"
    assert user.is_active is True  # default

def test_user_creation_optional_email():
    user = User(id=1, username="validuser")
    assert user.email is None

def test_user_username_min_length():
    with pytest.raises(ValidationError):
        User(id=1, username="ab")  # less than 3 chars

def test_user_username_max_length():
    valid_username = "u" * 50
    user = User(id=1, username=valid_username)
    assert user.username == valid_username

    too_long_username = "u" * 51
    with pytest.raises(ValidationError):
        User(id=1, username=too_long_username)

def test_user_activate_deactivate():
    user = User(id=1, username="user1")
    user.deactivate()
    assert user.is_active is False
    user.activate()
    assert user.is_active is True

def test_recipe_creation_defaults():
    recipe = Recipe(id=1, title="Recipe Title")
    assert recipe.id == 1
    assert recipe.title == "Recipe Title"
    assert recipe.description is None
    assert recipe.is_published is False

def test_recipe_publish_unpublish():
    recipe = Recipe(id=1, title="Recipe Title")
    recipe.publish()
    assert recipe.is_published is True
    recipe.unpublish()
    assert recipe.is_published is False
