import tkinter as tk
from tkinter import *
from tkinter import Label
import string
import random

def accept_password():
    global username_label
    username = username_label.get()
    print(f"Accepted username: {username}")
    global password_entry
    password = password_entry.get()
    print(f"Accepted password: {password}")

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for i in range(length))

def generate_password():
    global password_entry
    length = int(length_entry.get())
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root=tk.Tk()
num=[3,5,7,9,11]
Variable =IntVar(root)
root.geometry("550x350")
root.title("Password Generator")
root.config(bg="#000000")

username_label = tk.Label(root, text="User Name:",fg="#FFFFFF",bg="#000000",font="Arial")
username_label.grid(row=0, column=0,ipadx=20,padx=5, pady=15)
username_label=tk.Entry(root)
username_label.grid(row=0, column=1,ipadx=50,padx=50,pady=15)

length_label = tk.Label(root, text="Password Length:",fg="#FFFFFF",bg="#000000",font="Arial")
length_label.grid(row=1, column=0, padx=5, pady=5,)
length_entry = OptionMenu(root,Variable, *num,)
length_entry.grid(row=1, column=1,ipadx=50, padx=5, pady=5)

password_label = tk.Label(root, text="Generated Password:",font="Arial",fg="#FFFFFF",bg="#000000")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=5, pady=5)

accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.place(x=20,y=200)
root.mainloop()