import json
import os
from typing import Dict, Optional

class FavoritesManager:
    """
    Manager for storing and retrieving favorite weather locations.

    Parameters
    ----------
    filepath : str, optional
        Path to the JSON file where favorites are stored. Defaults to "favorites.json".
    """
    def __init__(self, filepath: str = "favorites.json"):
        self.filepath = filepath
        self.favorites: Dict[str, str] = self._load()

    def _load(self) -> Dict[str, str]:
        """
        Load favorites from the JSON file.

        Returns
        -------
        Dict[str, str]
            Dictionary of name: location.
        """
        if not os.path.exists(self.filepath):
            return {}
        
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def _save(self) -> bool:
        """
        Save current favorites to the JSON file.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.favorites, f, indent=4)
            return True
        except IOError:
            return False

    def add(self, name: str, location: str) -> bool:
        """
        Add a new favorite location.

        Parameters
        ----------
        name : str
            The name to give the favorite (e.g., 'home').
        location : str
            The location string (e.g., 'Cincinnati, OH').

        Returns
        -------
        bool
            True if added, False if name already exists.
        """
        name_lower = name.lower()
        if name_lower in (k.lower() for k in self.favorites.keys()):
            return False
        
        self.favorites[name] = location
        return self._save()

    def remove(self, name: str) -> bool:
        """
        Remove a favorite location by name.

        Parameters
        ----------
        name : str
            The name of the favorite to remove.

        Returns
        -------
        bool
            True if removed, False if not found.
        """
        name_lower = name.lower()
        # Find the actual key (case-insensitive)
        actual_key = next((k for k in self.favorites.keys() if k.lower() == name_lower), None)
        
        if actual_key:
            del self.favorites[actual_key]
            return self._save()
        return False

    def list_all(self) -> Dict[str, str]:
        """
        Return all favorites.

        Returns
        -------
        Dict[str, str]
            Dictionary of all favorites.
        """
        return self.favorites

    def get_location(self, name: str) -> Optional[str]:
        """
        Get the location string for a favorite name.

        Parameters
        ----------
        name : str
            The name of the favorite.

        Returns
        -------
        Optional[str]
            The location string if found, else None.
        """
        name_lower = name.lower()
        actual_key = next((k for k in self.favorites.keys() if k.lower() == name_lower), None)
        return self.favorites.get(actual_key) if actual_key else None
