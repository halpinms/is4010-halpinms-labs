# test_lab07.py
import json
from lab07_contact_book import save_contacts_to_json, load_contacts_from_json


# Test the round trip of saving and loading
def test_save_and_load_round_trip(tmp_path):
    # tmp_path is a pytest fixture that provides a temporary directory
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "contacts.json"

    contacts = [
        {"name": "Ada Lovelace", "email": "ada@example.com"},
        {"name": "Grace Hopper", "email": "grace@example.com"},
    ]

    # Save the contacts
    save_contacts_to_json(contacts, p)

    # Load them back
    loaded_contacts = load_contacts_from_json(p)

    assert loaded_contacts == contacts


# Test loading from a non-existent file
def test_load_from_non_existent_file(tmp_path):
    p = tmp_path / "non_existent.json"
    # Should handle FileNotFoundError and return an empty list
    assert load_contacts_from_json(p) == []


# Test saving an empty list
def test_save_empty_list(tmp_path):
    p = tmp_path / "empty.json"

    save_contacts_to_json([], p)

    with open(p, "r") as f:
        data = json.load(f)
        assert data == []
