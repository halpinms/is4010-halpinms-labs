import os
import json
import pytest
from favorites import FavoritesManager

@pytest.fixture
def temp_favorites_file(tmp_path):
    """
    Fixture for creating a temporary favorites JSON file.
    """
    f = tmp_path / "test_favorites.json"
    return str(f)

def test_add_favorite(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    assert manager.add("home", "Cincinnati, OH") is True
    assert manager.get_location("home") == "Cincinnati, OH"

def test_add_duplicate_favorite(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    manager.add("home", "Cincinnati, OH")
    # Duplicate with same case
    assert manager.add("home", "Columbus, OH") is False
    # Duplicate with different case
    assert manager.add("HOME", "Columbus, OH") is False

def test_remove_favorite(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    manager.add("home", "Cincinnati, OH")
    assert manager.remove("home") is True
    assert manager.get_location("home") is None

def test_remove_non_existent_favorite(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    assert manager.remove("ghost") is False

def test_list_all_favorites(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    manager.add("home", "Cincinnati, OH")
    manager.add("work", "Columbus, OH")
    favorites = manager.list_all()
    assert len(favorites) == 2
    assert favorites["home"] == "Cincinnati, OH"
    assert favorites["work"] == "Columbus, OH"

def test_get_location_case_insensitive(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    manager.add("HoMe", "Cincinnati, OH")
    assert manager.get_location("home") == "Cincinnati, OH"
    assert manager.get_location("HOME") == "Cincinnati, OH"
    assert manager.get_location("HoMe") == "Cincinnati, OH"

def test_persistence(temp_favorites_file):
    manager1 = FavoritesManager(temp_favorites_file)
    manager1.add("home", "Cincinnati, OH")
    
    manager2 = FavoritesManager(temp_favorites_file)
    assert manager2.get_location("home") == "Cincinnati, OH"

def test_load_non_existent_file(tmp_path):
    # Pass a path that doesn't exist
    non_existent = str(tmp_path / "non_existent.json")
    manager = FavoritesManager(non_existent)
    assert manager.list_all() == {}

def test_load_corrupted_json(temp_favorites_file):
    with open(temp_favorites_file, 'w') as f:
        f.write("{ invalid json")
    
    manager = FavoritesManager(temp_favorites_file)
    assert manager.list_all() == {}

def test_remove_case_insensitive(temp_favorites_file):
    manager = FavoritesManager(temp_favorites_file)
    manager.add("HoMe", "Cincinnati, OH")
    assert manager.remove("HOME") is True
    assert manager.get_location("home") is None
