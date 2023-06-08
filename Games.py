import webbrowser
import time
import sys

exclude_file_path = "ExcludeGames.txt"
game_file_path = "game.txt"

# Read excluded URLs from the file
with open(exclude_file_path, "r") as exclude_file:
    excluded_urls = exclude_file.read().splitlines()

# Read game URLs from the file
with open(game_file_path, "r") as game_file:
    game_urls = game_file.read().splitlines()

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

