import os

file_path = "game.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted games successfully.")
else:
    print(f"{file_path} does not exist.")

