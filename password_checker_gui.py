import tkinter as tk
from tkinter import StringVar
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength = 0
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    if strength == 5:
        feedback = "Strong"
        color = "#32CD32"
    elif strength >= 3:
        feedback = "Moderate"
        color = "#FFA500"
    else:
        feedback = "Weak"
        color = "#FF4500"

    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        suggestions.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        suggestions.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        suggestions.append("Password should include at least one number.")
    if not special_char_criteria:
        suggestions.append("Password should include at least one special character (e.g., !, @, #, etc.).")

    return feedback, color, suggestions, strength

def update_strength_feedback(*args):
    password = password_var.get()
    feedback, color, suggestions, strength = assess_password_strength(password)
    strength_label.config(text=f"Strength: {feedback}", fg=color)

    if strength == 5:
        canvas.itemconfig(strength_bar, fill="#32CD32")
    elif strength >= 3:
        canvas.itemconfig(strength_bar, fill="#FFA500")
    else:
        canvas.itemconfig(strength_bar, fill="#FF4500")
    canvas.coords(strength_bar, (0, 0, strength * 60, 25))

    suggestion_text.delete(1.0, tk.END)
    if suggestions:
        suggestion_text.insert(tk.END, "Suggestions to improve your password:\n")
        for suggestion in suggestions:
            suggestion_text.insert(tk.END, f"- {suggestion}\n")

def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

window = tk.Tk()
window.title("Password Complexity Checker")
window.geometry("450x500")
window.config(bg="#ADD8E6")

heading = tk.Label(window, text="Password Complexity Checker", font=("Arial", 16, "bold"), bg="#ADD8E6", fg="#4B0082")
heading.pack(pady=15)

password_var = StringVar()
password_var.trace("w", update_strength_feedback)
password_label = tk.Label(window, text="Enter Password:", bg="#ADD8E6", font=("Arial", 12), fg="#000080")
password_label.pack(pady=5)
password_entry = tk.Entry(window, textvariable=password_var, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(window, text="Show Password", variable=show_password_var, onvalue=True, offvalue=False, command=toggle_password, bg="#ADD8E6", fg="#000080")
show_password_checkbox.pack()

strength_label = tk.Label(window, text="Strength: ", font=("Arial", 12, "bold"), bg="#ADD8E6")
strength_label.pack(pady=10)

canvas = tk.Canvas(window, width=300, height=25, bg="#D3D3D3")
canvas.pack(pady=10)
strength_bar = canvas.create_rectangle(0, 0, 0, 25, fill="#FF4500")

suggestion_label = tk.Label(window, text="Suggestions:", font=("Arial", 12, "bold"), bg="#ADD8E6", fg="#000080")
suggestion_label.pack(pady=5)
suggestion_text = tk.Text(window, height=5, width=40, wrap="word", font=("Arial", 10), bg="white", fg="black", bd=1, relief="solid")
suggestion_text.pack(pady=10)

window.mainloop()

