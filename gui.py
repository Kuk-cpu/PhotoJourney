import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import os


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

    def summary(self):

        return (
            f"{self.location} | "
            f"{self.theme} | "
            f"{self.rating}"
        )


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
# RECURSIVE IMAGE COUNTER
# ====================================

def count_images_recursively(folder):

    total = 0

    try:

        items = os.listdir(folder)

        for item in items:

            path = os.path.join(folder, item)

            if os.path.isdir(path):

                total += count_images_recursively(path)

            elif item.endswith((".jpg", ".png", ".jpeg")):

                total += 1

    except:

        return 0

    return total


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
# MAIN WINDOW
# ====================================

window = tk.Tk()

window.title("PhotoJourney")

window.geometry("1400x1000")

window.configure(bg="#f4f1ea")

window.resizable(True, True)


# ====================================
# SCROLLABLE CANVAS
# ====================================

main_canvas = tk.Canvas(
    window,
    bg="#f4f1ea",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    window,
    orient="vertical",
    command=main_canvas.yview
)

scrollable_frame = tk.Frame(
    main_canvas,
    bg="#f4f1ea"
)

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(
        scrollregion=main_canvas.bbox("all")
    )
)

main_canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

main_canvas.configure(
    yscrollcommand=scrollbar.set
)

main_canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# ====================================
# TITLE
# ====================================

title = tk.Label(
    scrollable_frame,
    text="PhotoJourney",
    font=("Helvetica", 38, "bold"),
    bg="#f4f1ea",
    fg="#1d3557"
)

title.pack(pady=10)

subtitle = tk.Label(
    scrollable_frame,
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
    scrollable_frame,
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
    scrollable_frame,
    bg="#f4f1ea"
)

image_label.pack(pady=15)


# ====================================
# OUTPUT AREA
# ====================================

output_text = tk.Text(
    scrollable_frame,
    width=110,
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

        image = image.resize((600, 400))

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

    for widget in scrollable_frame.winfo_children():

        if isinstance(widget, tk.Frame) and widget != input_frame and widget != button_frame:
            widget.destroy()

    logs = load_logs()

    if len(logs) == 0:

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            "No logs found."
        )

        return

    for log in logs:

        parts = log.split(",")

        if len(parts) < 5:
            continue

        location, theme, rating, description, image_path = parts

        card = tk.Frame(
            scrollable_frame,
            bg="white",
            bd=2,
            relief="solid"
        )

        card.pack(
            pady=15,
            padx=20,
            fill="x"
        )

        if os.path.exists(image_path):

            try:

                image = Image.open(image_path)

                image = image.resize((300, 200))

                photo = ImageTk.PhotoImage(image)

                image_label_card = tk.Label(
                    card,
                    image=photo,
                    bg="white"
                )

                image_label_card.image = photo

                image_label_card.pack(pady=10)

            except:

                pass

        info = tk.Label(
            card,
            text=
            f"""
📍 Location: {location}

📸 Theme: {theme}

⭐ Rating: {rating}

📝 Description: {description}
""",
            font=("Helvetica", 11),
            bg="white",
            justify="left"
        )

        info.pack(
            padx=20,
            pady=10,
            anchor="w"
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

🖼️ Total Images Uploaded: {total_images}

⭐ Average Rating: {average_rating:.2f}

📸 Favorite Theme: {favorite_theme}

🌍 Most Visited Location: {favorite_location}

----------------------------------------
"""
    )

    if favorite_theme.lower() == "street":

        personality = "🎭 Street Storyteller"

    elif favorite_theme.lower() == "nature":

        personality = "🎭 Quiet Landscape Observer"

    elif favorite_theme.lower() == "food":

        personality = "🎭 Visual Experience Curator"

    elif favorite_theme.lower() == "architecture":

        personality = "🎭 Geometry Explorer"

    else:

        personality = "🎭 Creative Explorer"

    output_text.insert(
        tk.END,
        f"""

🎭 Photography Personality

{personality}

----------------------------------------
"""
    )


# ====================================
# EXPLORE SHARED LOCATIONS
# ====================================

def explore_locations_gui():

    output_text.delete("1.0", tk.END)

    location_search = location_entry.get().lower()

    theme_search = theme_entry.get().lower()

    rating_search = rating_entry.get().lower()

    description_search = description_entry.get().lower()

    found = False

    try:

        with open("shared_logs.txt", "r") as file:

            for line in file:

                parts = line.strip().split(",")

                if len(parts) < 5:
                    continue

                location, theme, rating, description, image = parts

                location_lower = location.lower()

                theme_lower = theme.lower()

                rating_lower = str(rating).lower()

                description_lower = description.lower()

                match = True

                if location_search != "":

                    if location_search not in location_lower:

                        match = False

                if theme_search != "":

                    if theme_search not in theme_lower:

                        match = False

                if rating_search != "":

                    if rating_search not in rating_lower:

                        match = False

                if description_search != "":

                    if description_search not in description_lower:

                        match = False

                if match:

                    found = True

                    output_text.insert(
                        tk.END,
                        f"""
🌍 Shared Community Log

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
                "No matching shared logs found."
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
        "💬 Comment Added Successfully!\n\n"
    )

    try:

        with open("comments.txt", "r") as file:

            for line in file:

                output_text.insert(
                    tk.END,
                    f"{line}\n"
                )

    except FileNotFoundError:

        output_text.insert(
            tk.END,
            "No comments found."
        )


# ====================================
# BUTTON FRAME
# ====================================

button_frame = tk.Frame(
    scrollable_frame,
    bg="#f4f1ea"
)

button_frame.pack(pady=20)


# ====================================
# BUTTON STYLE
# ====================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Custom.TButton",
    background="#457b9d",
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
    style="Custom.TButton",
    command=add_log_gui
)

add_button.grid(row=0, column=0, padx=10)

view_button = ttk.Button(
    button_frame,
    text="View Logs",
    style="Custom.TButton",
    command=view_logs_gui
)

view_button.grid(row=0, column=1, padx=10)

analyze_button = ttk.Button(
    button_frame,
    text="Analyze",
    style="Custom.TButton",
    command=analyze_logs_gui
)

analyze_button.grid(row=0, column=2, padx=10)

explore_button = ttk.Button(
    button_frame,
    text="Explore",
    style="Custom.TButton",
    command=explore_locations_gui
)

explore_button.grid(row=0, column=3, padx=10)

comment_button = ttk.Button(
    button_frame,
    text="Add Comment",
    style="Custom.TButton",
    command=add_comment_gui
)

comment_button.grid(row=0, column=4, padx=10)

image_button = ttk.Button(
    button_frame,
    text="Choose Photo",
    style="Custom.TButton",
    command=choose_image
)

image_button.grid(row=0, column=5, padx=10)


# ====================================
# MOUSE WHEEL SCROLL
# ====================================

def _on_mousewheel(event):

    main_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

main_canvas.bind_all(
    "<MouseWheel>",
    _on_mousewheel
)


# ====================================
# RUN APP
# ====================================

window.mainloop()