import requests
import os
import random
import time

def generate_steam_url(app_id):
    return f"https://store.steampowered.com/app/{app_id}"

def check_game_price(app_id):
    url = generate_steam_url(app_id)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "Free to Play" in response.text:
                return "free"
            else:
                return "paid"
    except requests.exceptions.RequestException:
        return "error"
    return None

def save_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

def generate_and_save_urls():
    while True:
        app_id = random.randint(1, 1000000)
        game_price = check_game_price(app_id)
        if game_price is not None:
            url = generate_steam_url(app_id)
            print("Checking URL:", url)
            if game_price == "free":
                save_to_file("Freegamefound.txt", url)
            elif game_price == "paid":
                save_to_file("Paidgamefound.txt", url)
            elif game_price == "error":
                save_to_file("Error.txt", url)

        time.sleep(1)  # Add a delay to avoid overwhelming the server

# Create files if they don't exist
if not os.path.exists("Freegamefound.txt"):
    open("Freegamefound.txt", "w").close()
if not os.path.exists("Paidgamefound.txt"):
    open("Paidgamefound.txt", "w").close()
if not os.path.exists("Error.txt"):
    open("Error.txt", "w").close()

generate_and_save_urls()
