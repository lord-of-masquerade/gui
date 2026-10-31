import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("My Application")
root.geometry("400x300")

heading=tk.Label(root,text="Login Form", font=("Arial",18,"bold"))
heading.grid(row=0,column=0,columnspan=2,pady=20)

#username
username_label=tk.Label(root,text="Username:")
username_label.grid(row=1,column=0,pady=10,padx=10)

username_entry=tk.Entry(root)
username_entry.grid(row=1,column=1,pady=10,padx=10)

#password
password_label=tk.Label(root,text="Password:")
password_label.grid(row=2,column=0,pady=10,padx=10)

password_entry=tk.Entry(root,show="*")
password_entry.grid(row=2,column=1,padx=10,pady=10)

def login():
    username=username_entry.get()
    password=password_entry.get()
    if username=="" or password=="":
        messagebox.showerror("Error","Please enter both Password and Username")
    else:
        messagebox.showinfo("Success",f"Welcome {username} !")
login_btn=tk.Button(root,text="Login",command=login)
login_btn.grid(row=4,column=1,pady=20)

root.mainloop()