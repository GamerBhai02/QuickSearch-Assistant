import tkinter as tk
from tkinter import Label, Button, messagebox
import webbrowser

root = tk.Tk()
root.title("QuickSearch Assistant")
root.geometry("500x400")
root.configure(bg='skyblue')

selected_platform = None
instruction_label = None

def search_youtube():
    query = entry.get()
    if query:
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a search query.")

def search_google():
    query = entry.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a search query.")

def search_instagram():
    username = entry.get().replace('@', "")
    if username:
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a username.")

def search_twitter():
    username = entry.get().replace('@', "")
    if username:
        url = f"https://twitter.com/{username}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a Twitter username.")

def search_facebook():
    query = entry.get()
    if query:
        url = f"https://www.facebook.com/{query}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a Facebook username or page name.")

def search_linkedin():
    username = entry.get()
    if username:
        url = f"https://www.linkedin.com/in/{username}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a LinkedIn username.")

def update_instruction(platform):
    global selected_platform, instruction_label
    selected_platform = platform
    
    if instruction_label:
        instruction_label.destroy()
    
    if platform == "YouTube":
        instruction_label = Label(root, text="Enter search query to find videos on YouTube", bg='skyblue', font=("Arial", 12))
    elif platform == "Google":
        instruction_label = Label(root, text="Enter search query to search the web on Google", bg='skyblue', font=("Arial", 12))
    elif platform == "Instagram":
        instruction_label = Label(root, text="Enter Instagram username (e.g., @username)", bg='skyblue', font=("Arial", 12))
    elif platform == "Twitter":
        instruction_label = Label(root, text="Enter Twitter username (e.g., @username)", bg='skyblue', font=("Arial", 12))
    elif platform == "Facebook":
        instruction_label = Label(root, text="Enter Facebook username or page name", bg='skyblue', font=("Arial", 12))
    elif platform == "LinkedIn":
        instruction_label = Label(root, text="Enter LinkedIn username (e.g., username)", bg='skyblue', font=("Arial", 12))
    
    instruction_label.pack(pady=10)
    
    entry.delete(0, tk.END)

def perform_search():
    if selected_platform == "YouTube":
        search_youtube()
    elif selected_platform == "Google":
        search_google()
    elif selected_platform == "Instagram":
        search_instagram()
    elif selected_platform == "Twitter":
        search_twitter()
    elif selected_platform == "Facebook":
        search_facebook()
    elif selected_platform == "LinkedIn":
        search_linkedin()

def ask_platform():
    platform_label = Label(root, text="Please select a platform to search:", bg='skyblue', font=("Arial", 12))
    platform_label.pack(pady=10)

    platform_options = ["Select a platform", "YouTube", "Google", "Instagram", "Twitter", "Facebook", "LinkedIn"]
    platform_var = tk.StringVar(root)
    platform_var.set(platform_options[0])

    platform_menu = tk.OptionMenu(root, platform_var, *platform_options, command=update_instruction)
    platform_menu.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

search_button = Button(root, text="Search", command=perform_search, width=20)
search_button.pack(pady=10)

ask_platform()

root.mainloop()
