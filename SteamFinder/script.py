import random
import os

def generate_random_app_id():
    return str(random.randint(1, 7))

def check_duplicate_app_id(file_path, app_id):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            existing_app_ids = file.read().splitlines()
            if app_id in existing_app_ids:
                return True
    return False

def save_app_id(file_path, app_id):
    with open(file_path, 'a') as file:
        file.write(app_id + '\n')

def main():
    steam_url = "https://store.steampowered.com/app/"
    found_app_file = "FoundSteamApp.txt"
    blacklisted_app_file = "BlacklistedSteamApp.txt"
    
    random_app_id = generate_random_app_id()
    
    if not check_duplicate_app_id(blacklisted_app_file, random_app_id):
        if not check_duplicate_app_id(found_app_file, random_app_id):
            app_url = steam_url + random_app_id
            print("Generated app URL:", app_url)
            
            with open(found_app_file, 'a') as file:
                file.write(app_url + '\n')
        else:
            print("App URL already exists in the found app file.")
    else:
        print("App URL blacklisted.")
    
    save_app_id(blacklisted_app_file, random_app_id)

if __name__ == '__main__':
    main()
