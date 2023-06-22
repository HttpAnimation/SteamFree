import requests
import os

def generate_steam_url(app_id):
    return f"https://store.steampowered.com/app/{app_id}"

def check_game_price(app_id):
    url = generate_steam_url(app_id)
    response = requests.get(url)
    if response.status_code == 200:
        if "Free to Play" in response.text:
            return "free"
        else:
            return "paid"
    return None

def save_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

def generate_and_save_urls(app_ids):
    for app_id in app_ids:
        game_price = check_game_price(app_id)
        if game_price is not None:
            if game_price == "free":
                save_to_file("Freegamefound.txt", generate_steam_url(app_id))
            else:
                save_to_file("Paidgamefound.txt", generate_steam_url(app_id))

# Example usage
app_ids = [730, 570, 440]  # Replace with your desired Steam app IDs

# Create files if they don't exist
if not os.path.exists("Freegamefound.txt"):
    open("Freegamefound.txt", "w").close()
if not os.path.exists("Paidgamefound.txt"):
    open("Paidgamefound.txt", "w").close()

generate_and_save_urls(app_ids)
