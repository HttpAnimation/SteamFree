import os
import platform
import subprocess
import requests
import sys

# Install requests library if not already installed
def install_requests():
    try:
        import requests
    except ImportError:
        if platform.system() == "Windows":
            subprocess.call(["pip", "install", "requests"])
        elif platform.system() == "Darwin":
            subprocess.call(["pip3", "install", "requests"])
            subprocess.call(["pip", "install", "ttkthemes"])
            subprocess.call(["sudo", "apt-get", "install", "python3-tk"])

# Check if requests library is installed
try:
    import requests
except ImportError:
    install_requests()

file_urls = [
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/InstallAndUpdate.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/Games.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/game.txt",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/uninstall.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/Mods.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/Build.py",
    "https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/gui.py"   
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
