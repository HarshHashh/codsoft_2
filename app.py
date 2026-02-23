import tkinter as tk
from tkinter import ttk

BG = "#f8fafc"
CARD = "#ffffff"
TEXT = "#020617"
MUTED = "#64748b"
GREEN = "#16a34a"
GREEN_DARK = "#15803d"
BORDER = "#e5e7eb"

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear()
        display.insert(0, str(result))
    except: 
        clear()
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x480")
root.configure(bg=BG)
root.resizable(True, True)

# Card container
card = tk.Frame(root, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
card.pack(padx=15, pady=15, fill="both", expand=True)

# Display
display = tk.Entry(
    card,
    font=("Segoe UI", 20),
    justify="right",
    relief="flat",
    bg=BG,
    fg=TEXT
)
display.pack(fill="x", padx=12, pady=(15, 10), ipady=10)

# Buttons container
buttons = tk.Frame(card, bg=CARD)
buttons.pack(padx=10, pady=10)

# Button layout
btns = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for text, r, c in btns:
    action = calculate if text == "=" else lambda x=text: press(x)
    tk.Button(
        buttons,
        text=text,
        command=action,
        font=("Segoe UI", 12, "bold"),
        bg=GREEN if text == "=" else BG,
        fg="white" if text == "=" else TEXT,
        relief="flat",
        width=5,
        height=2,
        activebackground=GREEN_DARK if text == "=" else "#e5e7eb"
    ).grid(row=r, column=c, padx=5, pady=5)

# Clear button
tk.Button(
    card,
    text="Clear",
    command=clear,
    font=("Segoe UI", 11, "bold"),
    bg="#ef4444",
    fg="white",
    relief="flat",
    activebackground="#dc2626"
).pack(fill="x", padx=12, pady=(5, 15))

root.mainloop()
