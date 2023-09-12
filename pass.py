import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length=int(length_entry.get())
    character_sets=[]
    if include_uppercase.get():
        character_sets.append(string.ascii_uppercase)
    if include_lowercase.get():
        character_sets.append(string.ascii_lowercase)
    if include_special_chars.get():
       character_sets.append(string.punctuation)
    if not character_sets:
        messagebox.showerror("Error!Please select proper character code for the password")
        return
    password=""
    for _ in range(length):
        character_set=random.choice(character_sets)
        password+=random.choice(character_set)
    password_entry.delete(0,tk.END)
    password_entry.insert(tk.END,password)
    
def my_reset(): 
     length_entry.delete(0,tk.END)
     password_entry.delete(0,tk.END)
     if isinstance(uppercase_checkbox,tk.Checkbutton):
            uppercase_checkbox.deselect()
     if isinstance(lowercase_checkbox,tk.Checkbutton):
            lowercase_checkbox.deselect()     
     if isinstance(digits_checkbox ,tk.Checkbutton):
            digits_checkbox .deselect()
     if isinstance(special_chars_checkbox,tk.Checkbutton):
            special_chars_checkbox.deselect()
     if isinstance():
            password_entry.delete()
    


root=tk.Tk()
root.title("Password Generator")
root.geometry("400x275")
root.resizable(False, False)

include_uppercase= tk.BooleanVar()
include_lowercase = tk.BooleanVar()
include_digits = tk.BooleanVar()
include_special_chars = tk.BooleanVar()

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()
uppercase_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=include_uppercase)
uppercase_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=include_lowercase)
lowercase_checkbox.pack()

digits_checkbox = tk.Checkbutton(root, text="Digits", variable=include_digits)
digits_checkbox.pack()

special_chars_checkbox = tk.Checkbutton(root, text="Special Characters", variable=include_special_chars)
special_chars_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10) 
reset_button = tk.Button(root, text="Reset", command=my_reset)
reset_button.pack(pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.pack()

root.mainloop()
    
    