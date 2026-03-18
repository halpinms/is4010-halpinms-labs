import pytest
import json
import os
from lab07_contact_book import save_contacts_to_json, load_contacts_from_json

def test_save_contacts_creates_file():
    """Test that save_contacts_to_json creates a JSON file."""
    test_file = 'test_contacts.json'
    test_contacts = [{"name": "Alice", "email": "alice@test.com"}]

    # Clean up if file exists
    if os.path.exists(test_file):
        os.remove(test_file)

    save_contacts_to_json(test_contacts, test_file)
    assert os.path.exists(test_file), "File was not created"

    # Clean up
    os.remove(test_file)

def test_save_and_load_contacts():
    """Test saving and loading contacts returns the same data."""
    test_file = 'test_contacts.json'
    test_contacts = [
        {"name": "Bob", "email": "bob@test.com"},
        {"name": "Charlie", "email": "charlie@test.com"}
    ]

    save_contacts_to_json(test_contacts, test_file)
    loaded_contacts = load_contacts_from_json(test_file)

    assert loaded_contacts == test_contacts

    # Clean up
    os.remove(test_file)

def test_load_nonexistent_file_returns_empty_list():
    """Test that loading a non-existent file returns an empty list."""
    result = load_contacts_from_json('nonexistent_file.json')
    assert result == [], "Should return empty list for non-existent file"

def test_save_empty_list():
    """Test saving an empty contact list."""
    test_file = 'test_empty.json'
    save_contacts_to_json([], test_file)

    with open(test_file, 'r') as f:
        data = json.load(f)

    assert data == []
    os.remove(test_file)

def test_save_contact_with_multiple_fields():
    """Test saving contacts with various fields."""
    test_file = 'test_complex.json'
    contacts = [
        {
            "name": "Eve",
            "email": "eve@test.com",
            "phone": "555-1234",
            "company": "TechCorp"
        }
    ]

    save_contacts_to_json(contacts, test_file)
    loaded = load_contacts_from_json(test_file)

    assert loaded == contacts
    assert loaded[0]["phone"] == "555-1234"

    os.remove(test_file)

def test_json_file_is_formatted():
    """Test that saved JSON file has proper formatting (indentation)."""
    test_file = 'test_format.json'
    contacts = [{"name": "Test", "email": "test@test.com"}]

    save_contacts_to_json(contacts, test_file)

    with open(test_file, 'r') as f:
        content = f.read()

    # Check for indentation (should have newlines and spaces)
    assert '\n' in content, "JSON should be formatted with newlines"
    assert '    ' in content, "JSON should have indentation"

    os.remove(test_file)
