import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("My Application")
root.geometry("400x300")

heading=tk.Label(root,text="Login Form", font=("Arial",18,"bold"))
heading.grid(row=0,column=0,columnspan=2,pady=20)

username_label=tk.Label(root,text="Username:")
username_label.grid(row=1,column=0,pady=10,padx=10)

username_entry=tk.Entry(root)
username_entry.grid(row=1,column=1,pady=10,padx=10)

