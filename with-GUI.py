import tkinter as tk
from tkinter import messagebox

def blocker(path1, redirect1, site1):
    try:
        with open(path1, 'r+') as f:
            contain = f.read()
            if site1 not in contain:  # Ensure the site is not already blocked
                f.write(redirect1 + " " + site1 + "\n")
                messagebox.showinfo("Success", f"{site1} has been blocked.")
            else:
                messagebox.showwarning("Warning", f"{site1} is already blocked.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    entry_block.delete(0, tk.END)
def unblock(path1, site1):
    try:
        with open(path1, 'r') as f:
            lines = f.readlines()
        with open(path1, 'w') as f:
            for line in lines:
                if site1 not in line:
                    f.write(line)
        messagebox.showinfo("Success", f"{site1} has been unblocked.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    entry_unblock.delete(0, tk.END)

def block_website():
    site = entry_block.get()
    if site:
        blocker(path, redirect, site)
    else:
        messagebox.showwarning("Input Error", "Please enter a website URL to block.")

def unblock_website():
    site = entry_unblock.get()
    if site:
        unblock(path, site)
    else:
        messagebox.showwarning("Input Error", "Please enter a website URL to unblock.")

# File path and redirect IP
path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

# Tkinter GUI setup
st = tk.Tk()
st.title("Website Blocker")
st.geometry("680x600")
st.configure(bg="#f0f8ff")  # Light blue background

label1 = tk.Label(st, text="Website Blocker", font=("Arial", 27, "bold"), bg="#f0f8ff", fg="#000080")  # Dark blue text
label1.pack(pady=30)

label2 = tk.Label(st, text="For Blocking", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="green")  # Orange-red text
label2.place(x=88, y=180)

entry_block = tk.Entry(st, font=("Arial", 15), bg="white", fg="#000000")  # Light dark blue background, black text
entry_block.place(x=30, y=250, width=280)

block_btn = tk.Button(st, text="Block", font=("Arial", 20, "bold"), command=block_website, bg="red", fg="#ffffff")  # Red background, white text
block_btn.place(x=103, y=333)

label3 = tk.Label(st, text="For Unblocking", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="green")  # Orange-red text
label3.place(x=410, y=180)

entry_unblock = tk.Entry(st, font=("Arial", 15), bg="white", fg="#000000")  # Light dark blue background, black text
entry_unblock.place(x=380, y=250, width=280)

unblock_btn = tk.Button(st, text="Unblock", font=("Arial", 20, "bold"), command=unblock_website, bg="#ff6347", fg="#ffffff")  # Tomato background, white text
unblock_btn.place(x=445, y=333)

st.mainloop()
