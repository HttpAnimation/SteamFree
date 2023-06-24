import webbrowser
import time
import sys
import os
import requests

exclude_file_path = "ExcludeDLCS.api"
game_file_path = "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/dlcs.api"

# Check if the exclude file exists, and create it if it doesn't
if not os.path.isfile(exclude_file_path):
    with open(exclude_file_path, "w") as exclude_file:
        pass  # Empty pass statement to create an empty file

# Read excluded URLs from the file
with open(exclude_file_path, "r") as exclude_file:
    excluded_urls = exclude_file.read().splitlines()

# Read game URLs from the file
response = requests.get(game_file_path)
game_urls = response.text.splitlines()

# Determine if running in auto mode
auto_mode = "--auto" in sys.argv

# Open each URL
for url in game_urls:
    if url not in excluded_urls:
        webbrowser.open(url)
        print(f"Opened URL: {url}")

        if auto_mode:
            time.sleep(0.3)
        else:
            # Wait for user input to continue
            user_input = input("Click 'Add to Library' and press Enter to continue ('q' to quit): ")
            if user_input.lower() == "q":
                break

        # Add the opened URL to the exclude list
        excluded_urls.append(url)

        # Write the updated excluded URLs to the file
        with open(exclude_file_path, "a") as exclude_file:
            exclude_file.write(url + '\n')

print("Done.")
