import os 
os.system("pip install requests")
import requests


file_urls = [
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/install.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/script.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/uninstall.py"
]

# Download each file
for url in file_urls:
    file_name = url.split("/")[-1]  # Extract the file name from the URL

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Downloaded file: {file_name}")
    else:
        print(f"Failed to download file: {file_name}. Error code: {response.status_code}")

