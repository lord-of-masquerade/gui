import tkinter as tk

root=tk.Tk()
root.title("my application")
root.geometry("500x300")

def greet():
    name=entry.get()

    if name=="":
        label.config(text="Please enter your name")
    else:
        label.config(text=f"Welcome {name} !")
entry=tk.Entry(root)
entry.pack(pady=10) 

def clear():
    entry.delete(0,tk.END)
    label.config(text="")

label=tk.Label(root,text="hello")
label.pack()

btn=tk.Button(root,text="Click here!",command=greet)
btn.pack()
clr_btn=tk.Button(root,text="Clear",command=clear)
clr_btn.pack()

root.mainloop()
