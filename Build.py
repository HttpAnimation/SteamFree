import os

def create_file(file_name):
    if os.path.isfile(file_name):
        print(f"File '{file_name}' already exists. Skipping creation.")
    else:
        try:
            with open(file_name, 'w') as file:
                print(f"File '{file_name}' created successfully.")
        except IOError:
            print(f"An error occurred while creating the file '{file_name}'.")

exclude_games_file = "ExcludeGames.txt"
exclude_mods_file = "ExcludeMods.txt"

create_file(exclude_games_file)
create_file(exclude_mods_file)
