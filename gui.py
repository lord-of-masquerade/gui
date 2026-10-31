import tkinter as tk

root=tk.Tk()
root.title("my application")
root.geometry("500x300")

def greet():
    label.config(text="welcome")
label=tk.Label(root,text="hello")
label.pack()

btn=tk.Button(root,text="Click here!",command=greet)
btn.pack()

root.mainloop()
