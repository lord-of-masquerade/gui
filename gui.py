import tkinter as tk

root=tk.Tk()
root.title("my application")
root.geometry("500x300")

def greet():
    label.config(text="welcome")
    name=entry.get()

    if name=="":
        label.config(text="Please enter your name")
    else:
        label.config(text=f"Welcome {name} !")
entry=tk.Entry(root)
entry.pack(pady=10) 

label=tk.Label(root,text="hello")
label.pack()

btn=tk.Button(root,text="Click here!",command=greet)
btn.pack()

root.mainloop()
