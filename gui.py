import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk


# ====================================
# GLOBAL VARIABLES
# ====================================

selected_image_path = ""


# ====================================
# VALIDATION
# ====================================

def validate_rating(rating):

    if not rating.isdigit():
        raise ValueError("Rating must be a number.")

    rating = int(rating)

    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5.")

    return rating


# ====================================
# SAVE USER LOG
# ====================================

def save_log(location, theme, rating, description, image_path):

    with open("user_logs.txt", "a") as file:

        file.write(
            f"{location},{theme},{rating},{description},{image_path}\n"
        )


# ====================================
# LOAD USER LOGS
# ====================================

def load_logs():

    logs = []

    try:

        with open("user_logs.txt", "r") as file:

            for line in file:

                logs.append(line.strip())

    except FileNotFoundError:

        return []

    return logs


# ====================================
# SAVE SHARED LOG
# ====================================

def save_shared_log(location, theme, rating, description, image_path):

    with open("shared_logs.txt", "a") as file:

        file.write(
            f"{location},{theme},{rating},{description},{image_path}\n"
        )


# ====================================
# SAVE COMMENT
# ====================================

def save_comment(location, comment):

    with open("comments.txt", "a") as file:

        file.write(f"{location}:{comment}\n")


# ====================================
# GUI WINDOW
# ====================================

window = tk.Tk()

window.title("PhotoJourney")

window.geometry("1250x900")

window.configure(bg="#f4f1ea")


# ====================================
# TITLE
# ====================================

title = tk.Label(
    window,
    text="PhotoJourney",
    font=("Helvetica", 38, "bold"),
    bg="#f4f1ea",
    fg="#1d3557"
)

title.pack(pady=10)

subtitle = tk.Label(
    window,
    text="Capturing Places, Understanding Perspectives",
    font=("Helvetica", 15, "italic"),
    bg="#f4f1ea",
    fg="#555555"
)

subtitle.pack(pady=5)


# ====================================
# INPUT FRAME
# ====================================

input_frame = tk.Frame(
    window,
    bg="#f4f1ea"
)

input_frame.pack(pady=15)


# ====================================
# LOCATION
# ====================================

location_label = tk.Label(
    input_frame,
    text="Location:",
    font=("Helvetica", 12, "bold"),
    bg="#f4f1ea",
    fg="#333333"
)

location_label.grid(row=0, column=0, padx=10, pady=10)

location_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Helvetica", 11),
    relief="flat",
    bd=4
)

location_entry.grid(row=0, column=1)


# ====================================
# THEME
# ====================================

theme_label = tk.Label(
    input_frame,
    text="Photography Theme:",
    font=("Helvetica", 12, "bold"),
    bg="#f4f1ea",
    fg="#333333"
)

theme_label.grid(row=1, column=0, padx=10, pady=10)

theme_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Helvetica", 11),
    relief="flat",
    bd=4
)

theme_entry.grid(row=1, column=1)


# ====================================
# RATING
# ====================================

rating_label = tk.Label(
    input_frame,
    text="Rating (1-5):",
    font=("Helvetica", 12, "bold"),
    bg="#f4f1ea",
    fg="#333333"
)

rating_label.grid(row=2, column=0, padx=10, pady=10)

rating_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Helvetica", 11),
    relief="flat",
    bd=4
)

rating_entry.grid(row=2, column=1)


# ====================================
# DESCRIPTION
# ====================================

description_label = tk.Label(
    input_frame,
    text="Description:",
    font=("Helvetica", 12, "bold"),
    bg="#f4f1ea",
    fg="#333333"
)

description_label.grid(row=3, column=0, padx=10, pady=10)

description_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Helvetica", 11),
    relief="flat",
    bd=4
)

description_entry.grid(row=3, column=1)


# ====================================
# IMAGE PREVIEW
# ====================================

image_label = tk.Label(
    window,
    bg="#f4f1ea"
)

image_label.pack(pady=10)


# ====================================
# OUTPUT AREA
# ====================================

output_text = tk.Text(
    window,
    width=100,
    height=16,
    font=("Helvetica", 11),
    bg="white",
    fg="#333333",
    relief="flat",
    bd=4,
    padx=15,
    pady=15
)

output_text.pack(pady=20)

output_text.insert(
    tk.END,
    "🌍 Welcome to PhotoJourney!\n\n"
    "Capture your travels and discover your photography perspective."
)


# ====================================
# CLEAR INPUTS
# ====================================

def clear_inputs():

    location_entry.delete(0, tk.END)

    theme_entry.delete(0, tk.END)

    rating_entry.delete(0, tk.END)

    description_entry.delete(0, tk.END)


# ====================================
# CHOOSE IMAGE
# ====================================

def choose_image():

    global selected_image_path
    global preview_image

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if file_path:

        selected_image_path = file_path

        image = Image.open(file_path)

        image = image.resize((400, 250))

        preview_image = ImageTk.PhotoImage(image)

        image_label.config(image=preview_image)

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            f"📸 Image Selected:\n\n{file_path}"
        )


# ====================================
# ADD LOG
# ====================================

def add_log_gui():

    location = location_entry.get()

    theme = theme_entry.get()

    rating = rating_entry.get()

    description = description_entry.get()

    try:

        rating = validate_rating(rating)

        save_log(
            location,
            theme,
            rating,
            description,
            selected_image_path
        )

        share = messagebox.askyesno(
            "Share Log",
            "Would you like to share this log with other users?"
        )

        if share:

            save_shared_log(
                location,
                theme,
                rating,
                description,
                selected_image_path
            )

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            "✅ Travel log saved successfully!"
        )

        clear_inputs()

    except ValueError as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


# ====================================
# VIEW LOGS
# ====================================

def view_logs_gui():

    output_text.delete("1.0", tk.END)

    logs = load_logs()

    if len(logs) == 0:

        output_text.insert(
            tk.END,
            "No logs found."
        )

        return

    for log in logs:

        parts = log.split(",")

        if len(parts) < 5:
            continue

        location, theme, rating, description, image = parts

        output_text.insert(
            tk.END,
            f"""
📍 Location: {location}

📸 Theme: {theme}

⭐ Rating: {rating}

📝 Description: {description}

🖼️ Image: {image}

----------------------------------------
"""
        )


# ====================================
# ANALYZE LOGS
# ====================================

def analyze_logs_gui():

    output_text.delete("1.0", tk.END)

    logs = load_logs()

    if len(logs) == 0:

        output_text.insert(
            tk.END,
            "No logs available."
        )

        return

    total_rating = 0

    theme_count = {}

    location_count = {}

    for log in logs:

        parts = log.split(",")

        if len(parts) < 5:
            continue

        location, theme, rating, description, image = parts

        rating = int(rating)

        total_rating += rating

        if theme in theme_count:

            theme_count[theme] += 1

        else:

            theme_count[theme] = 1

        if location in location_count:

            location_count[location] += 1

        else:

            location_count[location] = 1

    average_rating = total_rating / len(logs)

    favorite_theme = max(
        theme_count,
        key=theme_count.get
    )

    favorite_location = max(
        location_count,
        key=location_count.get
    )

    output_text.insert(
        tk.END,
        f"""
📊 Photography Analysis

----------------------------------------

📁 Total Logs: {len(logs)}

⭐ Average Rating: {average_rating:.2f}

📸 Favorite Theme: {favorite_theme}

🌍 Most Visited Location: {favorite_location}

----------------------------------------
"""
    )

    # ====================================
    # PHOTOGRAPHY PERSONALITY SYSTEM
    # ====================================

    if favorite_theme.lower() == "street":

        personality = "🎭 Street Storyteller"

        personality_description = (
            "You enjoy capturing human emotion, movement,\n"
            "and cinematic urban moments."
        )

        recommendation = (
            "Try exploring night street photography\n"
            "or documentary-style storytelling."
        )

    elif favorite_theme.lower() == "nature":

        personality = "🎭 Quiet Landscape Observer"

        personality_description = (
            "You are drawn to calm scenery, atmosphere,\n"
            "and reflective visual storytelling."
        )

        recommendation = (
            "Try sunrise landscape photography\n"
            "or environmental compositions."
        )

    elif favorite_theme.lower() == "food":

        personality = "🎭 Visual Experience Curator"

        personality_description = (
            "You appreciate detail, texture, colour,\n"
            "and aesthetic presentation."
        )

        recommendation = (
            "Experiment with café photography\n"
            "and cinematic food compositions."
        )

    elif favorite_theme.lower() == "architecture":

        personality = "🎭 Geometry Explorer"

        personality_description = (
            "You are fascinated by structure, symmetry,\n"
            "and spatial storytelling."
        )

        recommendation = (
            "Try minimalist architectural photography\n"
            "and leading-line compositions."
        )

    else:

        personality = "🎭 Creative Explorer"

        personality_description = (
            "You enjoy experimenting with different\n"
            "perspectives and visual styles."
        )

        recommendation = (
            "Continue exploring new themes and locations."
        )

    output_text.insert(
        tk.END,
        f"""

🎭 Photography Personality

{personality}

{personality_description}

📸 Recommendation

{recommendation}

----------------------------------------
"""
    )


# ====================================
# EXPLORE SHARED LOCATIONS
# ====================================

def explore_locations_gui():

    output_text.delete("1.0", tk.END)

    search_location = location_entry.get()

    found = False

    try:

        with open("shared_logs.txt", "r") as file:

            for line in file:

                parts = line.strip().split(",")

                if len(parts) < 5:
                    continue

                location, theme, rating, description, image = parts

                if location.lower() == search_location.lower():

                    found = True

                    output_text.insert(
                        tk.END,
                        f"""
🌍 Shared Log

📍 Location: {location}

📸 Theme: {theme}

⭐ Rating: {rating}

📝 Description: {description}

🖼️ Image: {image}

----------------------------------------
"""
                    )

        if not found:

            output_text.insert(
                tk.END,
                "No shared logs found for this location."
            )

    except FileNotFoundError:

        output_text.insert(
            tk.END,
            "No shared logs file found."
        )


# ====================================
# ADD COMMENT
# ====================================

def add_comment_gui():

    location = location_entry.get()

    comment = description_entry.get()

    if location == "" or comment == "":

        messagebox.showerror(
            "Error",
            "Location and comment cannot be empty."
        )

        return

    save_comment(location, comment)

    output_text.delete("1.0", tk.END)

    output_text.insert(
        tk.END,
        "💬 Comment added successfully!"
    )


# ====================================
# BUTTON FRAME
# ====================================

button_frame = tk.Frame(
    window,
    bg="#f4f1ea"
)

button_frame.pack(pady=20)


# ====================================
# BUTTON STYLES
# ====================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Blue.TButton",
    background="#457b9d",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)

style.configure(
    "Green.TButton",
    background="#588157",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)

style.configure(
    "Orange.TButton",
    background="#e76f51",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)

style.configure(
    "Purple.TButton",
    background="#6d597a",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)

style.configure(
    "Pink.TButton",
    background="#b56576",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)

style.configure(
    "Dark.TButton",
    background="#264653",
    foreground="white",
    font=("Helvetica", 11, "bold"),
    padding=10
)


# ====================================
# BUTTONS
# ====================================

add_button = ttk.Button(
    button_frame,
    text="Add Log",
    style="Blue.TButton",
    command=add_log_gui
)

add_button.grid(row=0, column=0, padx=10)


view_button = ttk.Button(
    button_frame,
    text="View Logs",
    style="Green.TButton",
    command=view_logs_gui
)

view_button.grid(row=0, column=1, padx=10)


analyze_button = ttk.Button(
    button_frame,
    text="Analyze",
    style="Orange.TButton",
    command=analyze_logs_gui
)

analyze_button.grid(row=0, column=2, padx=10)


explore_button = ttk.Button(
    button_frame,
    text="Explore",
    style="Purple.TButton",
    command=explore_locations_gui
)

explore_button.grid(row=0, column=3, padx=10)


comment_button = ttk.Button(
    button_frame,
    text="Add Comment",
    style="Pink.TButton",
    command=add_comment_gui
)

comment_button.grid(row=0, column=4, padx=10)


image_button = ttk.Button(
    button_frame,
    text="Choose Photo",
    style="Dark.TButton",
    command=choose_image
)

image_button.grid(row=0, column=5, padx=10)


# ====================================
# RUN WINDOW
# ====================================

window.mainloop()