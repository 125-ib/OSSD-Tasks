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
    if not u or not p:
        messagebox.showwarning("Oops!", "Please fill in all fields.")
        return
    users = read_file()
    if u in users and users[u] == p:
        messagebox.showinfo("Welcome!", f"Good to see you, {u}! 👋")
    else:
        messagebox.showerror("Failed", "Incorrect username or password.")

def signup():
    u = entry_user.get()
    p = entry_pass.get()
    if not u or not p:
        messagebox.showwarning("Oops!", "Please fill in all fields.")
        return
    users = read_file()
    if u in users:
        messagebox.showerror("Taken!", "This username is already registered.")
    else:
        write_file(u, p)
        messagebox.showinfo("Success!", f"Account created for {u}! 🎉")

def main():
    global entry_user, entry_pass

    root.configure(bg="#f0f4f8")
    root.geometry("350x450")
    root.resizable(False, False)

    tk.Label(root, text="🔐 Login System", font=("Helvetica", 18, "bold"),
             bg="#f0f4f8", fg="#2d3748").pack(pady=(30, 5))

    tk.Label(root, text="Your personal account portal",
             font=("Helvetica", 9), bg="#f0f4f8", fg="#a0aec0").pack()

    frame = tk.Frame(root, bg="white", padx=25, pady=25)
    frame.pack(padx=30, pady=20, fill="x")

    tk.Label(frame, text="Username", font=("Helvetica", 10, "bold"),
             bg="white", fg="#4a5568").pack(anchor="w")
    entry_user = tk.Entry(frame, font=("Helvetica", 11), relief="solid", bd=1)
    entry_user.pack(fill="x", pady=(3, 12), ipady=5)

    tk.Label(frame, text="Password", font=("Helvetica", 10, "bold"),
             bg="white", fg="#4a5568").pack(anchor="w")
    entry_pass = tk.Entry(frame, font=("Helvetica", 11), show="*", relief="solid", bd=1)
    entry_pass.pack(fill="x", pady=(3, 0), ipady=5)

    btn_frame = tk.Frame(root, bg="#f0f4f8")
    btn_frame.pack(fill="x", padx=30)

    tk.Button(btn_frame, text="Login", font=("Helvetica", 11, "bold"),
              bg="#4299e1", fg="white", relief="flat",
              cursor="hand2", pady=8, command=login).pack(fill="x", pady=(0, 8))

    tk.Button(btn_frame, text="Sign Up", font=("Helvetica", 11, "bold"),
              bg="#48bb78", fg="white", relief="flat",
              cursor="hand2", pady=8, command=signup).pack(fill="x")

root = tk.Tk()
root.title("Login System")
main()
root.mainloop()