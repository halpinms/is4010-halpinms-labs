import argparse
import sys
import config
from weather_api import WeatherAPI, format_current_weather, format_forecast
from favorites import FavoritesManager

def main():
    """
    Main entry point for the Weather CLI application.

    This function parses command-line arguments and dispatches to the 
    appropriate weather or favorites functionality.
    """
    parser = argparse.ArgumentParser(description="Weather CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Weather commands")

    # Current subcommand
    current_parser = subparsers.add_parser("current", help="Get current weather")
    current_parser.add_argument("location", help="City name or favorite name")

    # Forecast subcommand
    forecast_parser = subparsers.add_parser("forecast", help="Get weather forecast")
    forecast_parser.add_argument("location", help="City name or favorite name")
    forecast_parser.add_argument("--days", type=int, default=3, choices=range(1, 4), help="Number of days (1-3)")

    # Favorites subcommand
    favorites_parser = subparsers.add_parser("favorites", help="Manage favorite locations")
    fav_subparsers = favorites_parser.add_subparsers(dest="fav_command", help="Favorites commands")

    # Favorites add
    fav_add_parser = fav_subparsers.add_parser("add", help="Add a favorite location")
    fav_add_parser.add_argument("name", help="Favorite name (e.g., home)")
    fav_add_parser.add_argument("location", help="Location string (e.g., London)")

    # Favorites list
    fav_subparsers.add_parser("list", help="List all favorites")

    # Favorites remove
    fav_remove_parser = fav_subparsers.add_parser("remove", help="Remove a favorite location")
    fav_remove_parser.add_argument("name", help="Favorite name to remove")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    fav_manager = FavoritesManager()
    api = WeatherAPI(config.WEATHER_API_KEY)

    if args.command == "current":
        # Resolve location from favorites if it exists
        location = fav_manager.get_location(args.location) or args.location
        data = api.get_current_weather(location)
        if data:
            print(format_current_weather(data))
        else:
            print(f"Error: Could not fetch weather for '{location}'")
            sys.exit(1)

    elif args.command == "forecast":
        location = fav_manager.get_location(args.location) or args.location
        data = api.get_forecast(location, args.days)
        if data:
            print(format_forecast(data))
        else:
            print(f"Error: Could not fetch forecast for '{location}'")
            sys.exit(1)

    elif args.command == "favorites":
        if args.fav_command == "add":
            if fav_manager.add(args.name, args.location):
                print(f"Added favorite: {args.name} -> {args.location}")
            else:
                print(f"Error: Favorite '{args.name}' already exists.")
                sys.exit(1)
        elif args.fav_command == "list":
            favorites = fav_manager.list_all()
            if favorites:
                print("Your favorite locations:")
                for name, location in favorites.items():
                    print(f"- {name}: {location}")
            else:
                print("No favorites found.")
        elif args.fav_command == "remove":
            if fav_manager.remove(args.name):
                print(f"Removed favorite: {args.name}")
            else:
                print(f"Error: Favorite '{args.name}' not found.")
                sys.exit(1)
        else:
            favorites_parser.print_help()

if __name__ == "__main__":
    main()
