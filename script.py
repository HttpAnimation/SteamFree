import webbrowser
import time
import sys

file_path = "game.txt"

# Read URLs from the file
with open(file_path, "r") as file:
    urls = file.readlines()

# Remove any leading/trailing whitespace and newline characters
urls = [url.strip() for url in urls]

# Determine if running in auto mode
auto_mode = "--auto" in sys.argv

# Open each URL
for url in urls:
    webbrowser.open(url)
    print(f"Opened URL: {url}")

    if auto_mode:
        time.sleep(0.3)
    else:
        # Wait for user input to continue
        user_input = input("Click 'Add to Library' and press Enter to continue ('q' to quit): ")
        if user_input.lower() == "q":
            break

print("Done.")

