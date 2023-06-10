import random
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def generate_random_app_id():
    return str(random.randint(1, 9999999))


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


def generate_app_url():
    random_app_id = generate_random_app_id()
    app_url = f"https://store.steampowered.com/app/{random_app_id}"
    return app_url


def generate_app_button_click():
    app_url = generate_app_url()
    if not check_duplicate_app_id(blacklisted_app_file, app_url):
        found_app_list.insert(tk.END, app_url)
    else:
        messagebox.showinfo("Blacklisted App URL", "App URL is blacklisted.")


def save_app_url():
    app_url = found_app_list.get(tk.ACTIVE)
    save_app_id(found_app_file, app_url)
    found_app_list.delete(tk.ACTIVE)
    messagebox.showinfo("App URL Saved", "App URL has been saved successfully.")


def set_dark_mode():
    style.theme_use("clam")
    style.configure(".", background="black", foreground="white")
    style.configure("TEntry", fieldbackground="gray")
    style.configure("TButton", relief=tk.RAISED)


def create_main_window():
    window = tk.Tk()
    window.title("Steam App URL Generator")
    window.geometry("400x400")
    window.configure(bg="black")

    # Style and dark mode
    global style
    style = ttk.Style()
    set_dark_mode()

    # Generate App URL Button
    generate_app_button = ttk.Button(window, text="Generate App URL", command=generate_app_button_click)
    generate_app_button.pack(pady=10)

    # Found App List
    global found_app_list
    found_app_list = tk.Listbox(window, selectbackground="gray")
    found_app_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Save Button
    save_button = ttk.Button(window, text="Save App URL", command=save_app_url)
    save_button.pack(pady=10)

    return window


if __name__ == '__main__':
    found_app_file = "FoundSteamApp.txt"
    blacklisted_app_file = "BlacklistedSteamApp.txt"

    if not os.path.isfile(found_app_file):
        with open(found_app_file, 'w'):
            pass

    if not os.path.isfile(blacklisted_app_file):
        with open(blacklisted_app_file, 'w'):
            pass

    main_window = create_main_window()
    main_window.mainloop()
