import webbrowser
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Read the game URLs from the file
with open('game.txt', 'r') as file:
    game_urls = [line.strip() for line in file.readlines()]

# Extract the app names from the URLs
game_names = []
for url in game_urls:
    parts = url.split('/')
    if len(parts) >= 6:
        game_names.append(parts[-2])
    else:
        game_names.append("Invalid URL")

# Open URL in browser
def open_url(url):
    webbrowser.open_new(url)

# Create GUI window
window = tk.Tk()
window.title("Steam Free")
window.geometry("600x600")

# Apply dark theme
style = ThemedStyle(window)
style.set_theme("black")
style.configure("TFrame", background="dark grey")

# Create a frame with a vertical scrollbar
frame = ttk.Frame(window)
frame.pack(fill='both', expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Create buttons for each game
for name, url in zip(game_names, game_urls):
    name = name.replace("_", " ")  # Replace underscores with spaces
    button = ttk.Button(inner_frame, text=name, command=lambda u=url: open_url(u))
    button.pack(pady=5)

# Add the inner frame to the canvas
inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the GUI loop
window.mainloop()
