## Final project recommendation tool for students in EE 021
# Author: Ayush Pandey
# Oct 27, 2024

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("EE 021 Final Project Recommendation Tool")
root.geometry("700x550")

# Define the options
majors = [
    "EE with emphasis in electric vehicles",
    "EE with emphasis in sustainable energy",
    "EE with emphasis in computer engineering",
    "EE with emphasis in machine learning",
    "EE with emphasis in ground and aerial robotics",
    "Other: Non-electrical engineering major."
]

careers = [
    "Hardware engineer (chips, embedded circuits, power electronics)",
    "Software engineer",
    "Data analyst / AI technology",
    "Research (PhD in Electrical Engineering areas)",
    "Research (PhD in Computer Engineering areas)",
    "RF and communications engineer",
    "Solar and photovoltaics engineer",
    "Electric vehicle engineer",
    "Management of electrical engineering systems",
    "Consultancy",
    "Teaching",
    "Educational technology / lab designer",
    "Roboticist",
    "Government and/or policy related to engineering",
    "Automobile industry",
    "Control systems engineer"
]

confidence_levels = [
    "Highly confident",
    "Fairly confident",
    "Confident (with some help from resources)",
    "Not confident, but getting there",
    "Not confident at all"
]

major_frame = tk.LabelFrame(root, text="Select your preferred major of study")
major_frame.pack(padx=10, pady=5, fill="x")

major_label = tk.Label(major_frame, text="Major:")
major_label.pack(side="left", padx=5, pady=5)

major_var = tk.StringVar()
major_combobox = ttk.Combobox(major_frame, textvariable=major_var, values=majors, state='readonly', width=50)
major_combobox.pack(side="left", padx=5, pady=5)

career_frame = tk.LabelFrame(root, text="Select your preferred career choice")
career_frame.pack(padx=10, pady=5, fill="x")

career_label = tk.Label(career_frame, text="Career Option:")
career_label.pack(side="left", padx=5, pady=5)

career_var = tk.StringVar()
career_combobox = ttk.Combobox(career_frame, textvariable=career_var, values=careers, state='readonly', width=70)
career_combobox.pack(side="left", padx=5, pady=5)

confidence_frame = tk.LabelFrame(root, text="Select your confidence level in Python programming")
confidence_frame.pack(padx=10, pady=5, fill="x")

confidence_label = tk.Label(confidence_frame, text="Confidence Level in Python:")
confidence_label.pack(anchor="w", padx=5, pady=5)

confidence_var = tk.IntVar()

for idx, level in enumerate(confidence_levels, start=1):
    rb = tk.Radiobutton(confidence_frame, text=level, variable=confidence_var, value=idx)
    rb.pack(anchor="w")

def get_recommendation():
    major = major_var.get()
    if major not in majors:
        messagebox.showerror("Error", "Please select your Major.")
        return
    major_index = majors.index(major) + 1  # indices start from 1

    career = career_var.get()
    if career not in careers:
        messagebox.showerror("Error", "Please select your career choice.")
        return
    career_index = careers.index(career) + 1

    confidence = confidence_var.get()
    if confidence == 0:
        messagebox.showerror("Error", "Please select your confidence level in Python programming.")
        return

    # weights
    weights = {
        'Advanced Python programming': 0,
        'MATLAB': 0,
        'C++': 0,
        'Assembly language': 0
    }

    # weights based on major
    if major_index in [1, 2]:
        # EV and sustainable energy
        weights['MATLAB'] += 3
        weights['Advanced Python programming'] += 3
    elif major_index in [3, 4]:
        # CE and ML
        weights['C++'] += 4
        weights['Assembly language'] += 2
    elif major_index == 5:
        # Robotics
        weights['C++'] += 2
        weights['MATLAB'] += 2
        weights['Advanced Python programming'] += 3
    elif major_index == 6:
        # Other
        weights['Advanced Python programming'] += 3
        weights['MATLAB'] += 4

    # weights based on career
    if career_index == 1:
        # hardware
        weights['MATLAB'] += 2
        weights['Assembly language'] += 4
    if career_index == 2:
        # Software engineer
        weights['C++'] += 4
    if career_index == 3:
        # Data analyst / AI technology
        weights['Advanced Python programming'] += 3
        weights['C++'] += 2
    if career_index == 4:
        # PhD in EE
        weights['Advanced Python programming'] += 1
        weights['MATLAB'] += 2
    if career_index == 5:
        # PhD in ECE/EECS
        weights["C++"] += 2
        weights["Advanced Python programming"] += 2
    if career_index == 6:
        # RF and communications engineer
        weights['MATLAB'] += 3
    if career_index in [7, 8]:
        # solar, PV, EV
        weights['MATLAB'] += 2
        weights["Advanced Python programming"] += 1
    if career_index in [9, 10]:
        # management and consultancy
        weights['Advanced Python programming'] += 2
    if career_index in [11, 12]:
        # teaching, educational technology
        weights['Advanced Python programming'] += 2
        weights['MATLAB'] += 2
    if career_index == 13:
        # roboticist
        weights['C++'] += 2
        weights['MATLAB'] += 2
    if career_index == 14:
        # government and policy
        weights['MATLAB'] += 1
        weights['Advanced Python programming'] += 1
    if career_index in [15, 16]:
        # automobile and control systems
        weights['MATLAB'] += 2
        weights["Advanced Python programming"] += 2

    # weights based on confidence level
    if confidence == 1:
        weights['Advanced Python programming'] += 1
        weights['C++'] += 3
        weights['Assembly language'] += 2
    elif confidence == 2:
        weights['Advanced Python programming'] += 1
        weights['C++'] += 2
        weights['Assembly language'] += 1
    elif confidence == 3:
        weights['Advanced Python programming'] += 1
        weights['MATLAB'] += 2
    elif confidence == 4:
        weights["MATLAB"] += 3
    elif confidence == 5:
        weights['MATLAB'] += 4

    # Determine the highest weight(s)
    # max_weight = max(weights.values())
    # recommended_languages = [lang for lang, weight in weights.items() if weight == max_weight]
    recommended_languages = sorted(weights.items(), key=lambda item: item[1], reverse=True)
    display_recommendation(recommended_languages)

def display_recommendation(sorted_languages):
    # # Clear previous recommendation
    for widget in recommendation_frame.winfo_children():
        widget.destroy()

    recommendation_label = tk.Label(
        recommendation_frame,
        text="Top 2 recommended choices:",
        font=("Helvetica", 14)
    )
    recommendation_label.pack(pady=10)

    # Get the top 2 choices
    top_choices = sorted_languages[:2]

    for lang, weight in top_choices:
        lang_label = tk.Label(
            recommendation_frame,
            text=lang + " with score: " + str(weight),
            font=("Helvetica", 16, 'bold'),
            fg="white",
            bg="#4CAF50",  # Green background
            padx=10,
            pady=10
        )
        lang_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10, padx=10, fill="x", expand=False)
recommendation_frame = tk.LabelFrame(root, text="Recommended Programming Languages", padx=10, pady=5)
recommendation_frame.pack(padx=10, pady=5, fill="both", expand=True)  # ensures it fills the space left

# Button to trigger recommendation
recommend_button = tk.Button(button_frame, text="Get Recommendation", command=get_recommendation)
recommend_button.pack()

root.mainloop()
