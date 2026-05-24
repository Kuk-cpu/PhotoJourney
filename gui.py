import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ====================================
# PHOTOLOG CLASS
# ====================================

class PhotoLog:

    def __init__(
        self,
        location,
        theme,
        rating,
        description,
        image_path
    ):

        self.location = location
        self.theme = theme
        self.rating = rating
        self.description = description
        self.image_path = image_path


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

    with open(os.path.join(BASE_DIR, "user_logs.txt"), "a") as file:

        file.write(
            f"{location},{theme},{rating},{description},{image_path}\n"
        )


# ====================================
# LOAD USER LOGS
# ====================================

def load_logs():

    logs = []

    try:

        with open(os.path.join(BASE_DIR, "user_logs.txt"), "r") as file:

            for line in file:

                logs.append(line.strip())

    except FileNotFoundError:

        return []

    return logs


# ====================================
# SAVE SHARED LOG
# ====================================

def save_shared_log(location, theme, rating, description, image_path):

    with open(os.path.join(BASE_DIR, "shared_logs.txt"), "a") as file:

        file.write(
            f"{location},{theme},{rating},{description},{image_path}\n"
        )


# ====================================
# SAVE COMMENT
# ====================================

def save_comment(location, comment):

    with open(os.path.join(BASE_DIR, "comments.txt"), "a") as file:

        file.write(f"{location}:{comment}\n")


# ====================================
# MAIN WINDOW
# ====================================

window = tk.Tk()

window.title("PhotoJourney")

window.geometry("1536x1024")

window.resizable(True, True)


# ====================================
# CANVAS
# ====================================

canvas = tk.Canvas(
    window,
    highlightthickness=0,
    bd=0
)

canvas.pack(
    fill="both",
    expand=True
)


# ====================================
# BACKGROUND IMAGE
# ====================================

bg_path = os.path.join(BASE_DIR, "santorini.jpg")

original_bg = Image.open(bg_path)


def resize_background(event=None):

    width = max(window.winfo_width(), 1536)

    height = max(window.winfo_height(), 1024)

    resized = original_bg.resize((width, height))

    bg_photo = ImageTk.PhotoImage(resized)

    canvas.bg_photo = bg_photo

    canvas.delete("bg")

    canvas.create_image(
        0,
        0,
        image=bg_photo,
        anchor="nw",
        tags="bg"
    )

    canvas.tag_lower("bg")


window.bind("<Configure>", resize_background)


# ====================================
# COLORS
# ====================================

TRANSPARENT_BG = "#2d4059"

CARD_BG = "#f4ede4"

TEXT_COLOR = "#1d3557"


# ====================================
# TITLE
# ====================================

title = tk.Label(
    canvas,
    text="PhotoJourney",
    font=("Snell Roundhand", 60, "bold"),
    bg=TRANSPARENT_BG,
    fg="white",
    padx=20,
    pady=8
)

canvas.create_window(
    770,
    75,
    window=title
)


# ====================================
# SUBTITLE
# ====================================

subtitle = tk.Label(
    canvas,
    text="Every Place Has a Story.",
    font=("Times New Roman", 22, "italic"),
    bg=TRANSPARENT_BG,
    fg="white",
    padx=15,
    pady=5
)

canvas.create_window(
    770,
    140,
    window=subtitle
)


# ====================================
# WELCOME BOX
# ====================================

welcome_box = tk.Label(
    canvas,
    text=(
        "☀️ Welcome to PhotoJourney!\n\n"
        "Capture moments.\n"
        "Explore perspectives.\n"
        "Remember forever.\n\n"
        "❤️"
    ),
    font=("Helvetica", 11),
    bg=CARD_BG,
    fg=TEXT_COLOR,
    justify="left",
    padx=18,
    pady=18
)

canvas.create_window(
    230,
    175,
    window=welcome_box
)


# ====================================
# INPUT CARD
# ====================================

input_frame = tk.Frame(
    canvas,
    bg=CARD_BG,
    padx=28,
    pady=24
)

canvas.create_window(
    560,
    420,
    window=input_frame
)


# ====================================
# ENTRY STYLE
# ====================================

def create_entry():

    entry = tk.Entry(
        input_frame,
        width=26,
        font=("Helvetica", 11),
        bg="white",
        fg=TEXT_COLOR,
        relief="flat",
        bd=0,
        insertbackground=TEXT_COLOR,
        highlightthickness=1,
        highlightbackground="#d9c5ae",
        highlightcolor="#d9c5ae"
    )

    return entry


# ====================================
# LABEL STYLE
# ====================================

def create_label(text):

    return tk.Label(
        input_frame,
        text=text,
        font=("Helvetica", 11, "bold"),
        bg=CARD_BG,
        fg=TEXT_COLOR
    )


# ====================================
# LOCATION
# ====================================

location_label = create_label("Location:")

location_label.grid(
    row=0,
    column=0,
    padx=8,
    pady=10,
    sticky="e"
)

location_entry = create_entry()

location_entry.grid(
    row=0,
    column=1,
    ipady=5
)


# ====================================
# THEME
# ====================================

theme_label = create_label("Photography Theme:")

theme_label.grid(
    row=1,
    column=0,
    padx=8,
    pady=10,
    sticky="e"
)

theme_entry = create_entry()

theme_entry.grid(
    row=1,
    column=1,
    ipady=5
)


# ====================================
# RATING
# ====================================

rating_label = create_label("Rating (1-5):")

rating_label.grid(
    row=2,
    column=0,
    padx=8,
    pady=10,
    sticky="e"
)

rating_entry = create_entry()

rating_entry.grid(
    row=2,
    column=1,
    ipady=5
)


# ====================================
# DESCRIPTION
# ====================================

description_label = create_label("Description:")

description_label.grid(
    row=3,
    column=0,
    padx=8,
    pady=10,
    sticky="e"
)

description_entry = create_entry()

description_entry.grid(
    row=3,
    column=1,
    ipady=5
)


# ====================================
# BUTTON STYLE
# ====================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Custom.TButton",
    background="#d8c3a5",
    foreground=TEXT_COLOR,
    font=("Helvetica", 10, "bold"),
    padding=10,
    borderwidth=0
)

style.map(
    "Custom.TButton",
    background=[("active", "#c8ae8d")]
)


# ====================================
# BUTTONS
# ====================================

add_button = ttk.Button(
    canvas,
    text="Add Log",
    style="Custom.TButton",
    command=lambda: add_log_gui()
)

canvas.create_window(
    480,
    560,
    window=add_button
)

view_button = ttk.Button(
    canvas,
    text="View Logs",
    style="Custom.TButton",
    command=lambda: view_logs_gui()
)

canvas.create_window(
    620,
    560,
    window=view_button
)

analyze_button = ttk.Button(
    canvas,
    text="Analyze",
    style="Custom.TButton",
    command=lambda: analyze_logs_gui()
)

canvas.create_window(
    480,
    620,
    window=analyze_button
)

explore_button = ttk.Button(
    canvas,
    text="Explore",
    style="Custom.TButton",
    command=lambda: explore_locations_gui()
)

canvas.create_window(
    620,
    620,
    window=explore_button
)

comment_button = ttk.Button(
    canvas,
    text="Add Comment",
    style="Custom.TButton",
    command=lambda: add_comment_gui()
)

canvas.create_window(
    480,
    680,
    window=comment_button
)

image_button = ttk.Button(
    canvas,
    text="Choose Photo",
    style="Custom.TButton",
    command=lambda: choose_image()
)

canvas.create_window(
    620,
    680,
    window=image_button
)


# ====================================
# OUTPUT AREA
# ====================================

output_text = tk.Text(
    canvas,
    width=60,
    height=24,
    font=("Helvetica", 11),
    bg=CARD_BG,
    fg=TEXT_COLOR,
    relief="flat",
    bd=0,
    padx=22,
    pady=22
)

canvas.create_window(
    1000,
    500,
    window=output_text
)

output_text.insert(
    tk.END,
    "🌍 Welcome to PhotoJourney!\n\n"
    "Capture your travels and discover your photography perspective."
)


# ====================================
# IMAGE PREVIEW
# ====================================

image_label = tk.Label(
    canvas,
    bg=CARD_BG,
    bd=0
)

canvas.create_window(
    320,
    850,
    window=image_label
)


# ====================================
# QUOTE
# ====================================

quote_label = tk.Label(
    canvas,
    text="“We travel not to escape life, but for life not to escape us. ❤️”",
    font=("Times New Roman", 18, "italic"),
    bg=TRANSPARENT_BG,
    fg="white",
    padx=20,
    pady=6
)

canvas.create_window(
    770,
    770,
    window=quote_label
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

        image = image.resize((320, 220))

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

        log = PhotoLog(
            location,
            theme,
            rating,
            description,
            selected_image_path
        )

        save_log(
            log.location,
            log.theme,
            log.rating,
            log.description,
            log.image_path
        )

        share = messagebox.askyesno(
            "Share Log",
            "Would you like to share this log with other users?"
        )

        if share:

            save_shared_log(
                log.location,
                log.theme,
                log.rating,
                log.description,
                log.image_path
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

    output_text.image_list = []

    for log in logs:

        parts = log.split(",")

        if len(parts) < 5:
            continue

        location, theme, rating, description, image_path = parts

        output_text.insert(
            tk.END,
            f"\n📍 Location: {location}\n"
        )

        output_text.insert(
            tk.END,
            f"📸 Theme: {theme}\n"
        )

        output_text.insert(
            tk.END,
            f"⭐ Rating: {rating}\n"
        )

        output_text.insert(
            tk.END,
            f"📝 Description: {description}\n\n"
        )

        if os.path.exists(image_path):

            try:

                img = Image.open(image_path)

                img = img.resize((350, 220))

                photo = ImageTk.PhotoImage(img)

                output_text.image_create(
                    tk.END,
                    image=photo
                )

                output_text.image_list.append(photo)

                output_text.insert(
                    tk.END,
                    "\n\n"
                )

            except:

                pass

        output_text.insert(
            tk.END,
            "────────────────────────────\n\n"
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

    total_images = 0

    for log in logs:

        parts = log.split(",")

        if len(parts) < 5:
            continue

        location, theme, rating, description, image = parts

        rating = int(rating)

        total_rating += rating

        if image.strip() != "":

            total_images += 1

        theme_count[theme] = theme_count.get(theme, 0) + 1

        location_count[location] = location_count.get(location, 0) + 1

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

────────────────────────────

📁 Total Logs: {len(logs)}

🖼️ Total Images Uploaded: {total_images}

⭐ Average Rating: {average_rating:.2f}

📸 Favorite Theme: {favorite_theme}

🌍 Most Visited Location: {favorite_location}

────────────────────────────
"""
    )


# ====================================
# EXPLORE
# ====================================

def explore_locations_gui():

    output_text.delete("1.0", tk.END)

    try:

        with open(os.path.join(BASE_DIR, "shared_logs.txt"), "r") as file:

            for line in file:

                output_text.insert(
                    tk.END,
                    f"{line}\n"
                )

    except FileNotFoundError:

        output_text.insert(
            tk.END,
            "No shared logs file found."
        )


# ====================================
# COMMENTS
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
        "💬 Community Comments\n\n"
    )

    try:

        with open(os.path.join(BASE_DIR, "comments.txt"), "r") as file:

            comments = file.readlines()

            if len(comments) == 0:

                output_text.insert(
                    tk.END,
                    "No comments yet."
                )

            else:

                for line in comments:

                    if ":" in line:

                        location_name, user_comment = line.strip().split(":", 1)

                        output_text.insert(
                            tk.END,
                            f"""
📍 {location_name}

💭 "{user_comment}"

────────────────────────────

"""
                        )

    except FileNotFoundError:

        output_text.insert(
            tk.END,
            "No comments found."
        )
# ====================================
# START APP
# ====================================

window.after(
    100,
    resize_background
)

window.mainloop()