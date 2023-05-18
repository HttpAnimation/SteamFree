import os
import requests

url = "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/game.txt"
output_file = "game.txt"

# Delete the existing file, if it exists
if os.path.exists(output_file):
    os.remove(output_file)
    print(f"{output_file} deleted successfully.")

# Download the new file
response = requests.get(url)
if response.status_code == 200:
    with open(output_file, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Error code: {response.status_code}")

