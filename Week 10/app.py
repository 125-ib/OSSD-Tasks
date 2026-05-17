import tkinter as tk
from tkinter import messagebox

def read_file():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                users[u] = p
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login():
    u = entry_user.get()
    p = entry_pass.get()
    users = read_file()
    if u in users and users[u] == p:
        messagebox.showinfo("Login", f"Welcome {u}!")
    else:
        messagebox.showerror("Login", "Wrong username or password!")

def signup():
    u = entry_user.get()
    p = entry_pass.get()
    users = read_file()
    if u in users:
        messagebox.showerror("Signup", "User already exists!")
    else:
        write_file(u, p)
        messagebox.showinfo("Signup", "Account created successfully!")

def main():
    global entry_user, entry_pass

    tk.Label(root, text="Username").pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    tk.Button(root, text="Login",  command=login).pack(pady=5)
    tk.Button(root, text="Signup", command=signup).pack()

root = tk.Tk()
root.title("Login System")
main()
root.mainloop()