import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to initialize the database
def init_db():
    connection = sqlite3.connect('asiel.db')  # Connects to the database
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cat_table (
            UID INTEGER PRIMARY KEY,
            Naam TEXT,
            Dier TEXT
        )
    """)
    connection.commit()
    connection.close()

# Function to add a record to the database
def add_function():
    uid = enterUID.get()
    naam = enternaam.get()
    dier = enterDier.get()
    
    if not (uid and naam and dier):
        messagebox.showerror("Error", "All fields must be filled")
        return

    try:
        uid = int(uid)
    except ValueError:
        messagebox.showerror("Error", "UID must be an integer")
        return

    connection = sqlite3.connect('asiel.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO cat_table (UID, Naam, Dier) VALUES (?, ?, ?)", (uid, naam, dier))
    connection.commit()
    connection.close()
    messagebox.showinfo("Success", "Record added successfully")

    enterUID.delete(0, tk.END)
    enternaam.delete(0, tk.END)
    enterDier.delete(0, tk.END)

# Function to delete a record from the database
def delete_function():
    uid = enterUID.get()

    if not uid:
        messagebox.showerror("Error", "UID must be filled")
        return

    try:
        uid = int(uid)
    except ValueError:
        messagebox.showerror("Error", "UID must be an integer")
        return

    connection = sqlite3.connect('asiel.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cat_table WHERE UID = ?", (uid,))
    connection.commit()
    connection.close()
    messagebox.showinfo("Success", "Record deleted successfully")

    enterUID.delete(0, tk.END)
    enternaam.delete(0, tk.END)
    enterDier.delete(0, tk.END)

# Function to display records from the database
def display_function():
    connection = sqlite3.connect('asiel.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cat_table")
    records = cursor.fetchall()
    connection.close()

    display_window = tk.Toplevel(root)
    display_window.title("Cat Entries")

    for i, (uid, naam, dier) in enumerate(records):
        tk.Label(display_window, text=f"UID: {uid}, Naam: {naam}, Dier: {dier}").grid(row=i, column=0, padx=10, pady=5)

# Function to set up the UI
def setup_ui():
    global enterUID, enternaam, enterDier, root
    
    root = tk.Tk()
    root.title("Asiel.Pyform")
    root.geometry("300x300")

    tk.Label(root, text="UID").grid(column=0, row=0, pady=5, padx=5)
    enterUID = tk.Entry(root)
    enterUID.grid(column=0, row=1, pady=5, padx=5)

    tk.Label(root, text="Naam").grid(column=0, row=2, pady=5, padx=5)
    enternaam = tk.Entry(root)
    enternaam.grid(column=0, row=3, pady=5, padx=5)

    tk.Label(root, text="Dier").grid(column=0, row=4, pady=5, padx=5)
    enterDier = tk.Entry(root)
    enterDier.grid(column=0, row=5, pady=5, padx=5)

    button_add = tk.Button(root, text="Add", command=add_function)
    button_add.grid(column=1, row=0)

    button_delete = tk.Button(root, text="Delete", command=delete_function)
    button_delete.grid(column=1, row=1)

    button_display = tk.Button(root, text="Display", command=display_function)
    button_display.grid(column=1, row=2)

    root.mainloop()

# Initialize the database
init_db()

# Set up the UI
setup_ui()
