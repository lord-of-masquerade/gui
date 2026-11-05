import tkinter as tk
from tkinter import messagebox
""
root=tk.Tk()
root.title("A Little Happiness")
root.geometry("400x350")
root.config(bg="pink")

#Welcome function for you Ipshita
def welcome():
    name=entry.get()
    if name=='':
        messagebox.showwarning("Oops!", "Please enter your name!")
    else:
        messagebox.showinfo(
            " Hello!",
            "Hey " + name + "! You are amazing! ❤️"
            )
