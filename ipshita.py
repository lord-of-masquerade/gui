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

#clear function to clear the entry and reset the checkbox
def clear():
    entry.delete(0, tk.End)
    happy.set(0)

#label for the welcome message
label=tk.Label(root,text="What's your name,little purr ball?",bg="pink")
label.pack()

#button to show the welcome message
btn=tk.Button(
    root, text="Send me a smile! ❤️",
    command=welcome, bg="purple",
    fg="white"
)
btn.pack()


# Clear button
clear_btn = Button(
    root,
    text="Clear",
    command=clear
)
clear_btn.pack(pady=5)