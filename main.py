def display_menu():
    print("\n=== PhotoJourney ===")
    print("1. Add Travel Log")
    print("2. View My Logs")
    print("3. Analyze My Photography")
    print("4. Explore Shared Locations")
    print("5. Add Comment")
    print("6. Exit")


# -------------------------
# VALIDATION
# -------------------------

def validate_rating(rating):
    if not rating.isdigit():
        raise ValueError("Rating must be a number.")

    rating = int(rating)

    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5.")

    return rating


# -------------------------
# SAVE USER LOG
# -------------------------

def save_log(location, theme, rating, description):
    with open("user_logs.txt", "a") as file:
        file.write(f"{location},{theme},{rating},{description}\n")


# -------------------------
# ADD TRAVEL LOG
# -------------------------

def add_log():
    print("\n=== Add Travel Log ===")

    location = input("Enter location: ")
    theme = input("Enter photography theme: ")
    rating = input("Enter rating (1-5): ")
    description = input("Enter short description: ")

    try:
        rating = validate_rating(rating)

        save_log(location, theme, rating, description)

        print("Travel log saved successfully!")

        share = input("Would you like to share this log? (y/n): ")

        if share.lower() == "y":
            save_shared_log(location, theme, rating, description)
            print("Log shared successfully!")

    except ValueError as error:
        print("Error:", error)


# -------------------------
# LOAD USER LOGS
# -------------------------

def load_logs():
    logs = []

    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                logs.append(line.strip())

    except FileNotFoundError:
        print("No log file found.")

    return logs


# -------------------------
# VIEW USER LOGS
# -------------------------

def view_logs():
    print("\n=== My Travel Logs ===")

    logs = load_logs()

    if len(logs) == 0:
        print("No logs found.")
        return

    for log in logs:
        location, theme, rating, description = log.split(",")

        print(f"""
Location: {location}
Theme: {theme}
Rating: {rating}
Description: {description}
------------------------
""")


# -------------------------
# ANALYZE PHOTOGRAPHY
# -------------------------

def analyze_logs():
    print("\n=== Photography Analysis ===")

    logs = load_logs()

    if len(logs) == 0:
        print("No logs available for analysis.")
        return

    total_rating = 0
    theme_count = {}

    for log in logs:
        location, theme, rating, description = log.split(",")

        rating = int(rating)

        total_rating += rating

        if theme in theme_count:
            theme_count[theme] += 1
        else:
            theme_count[theme] = 1

    average_rating = total_rating / len(logs)

    favorite_theme = max(theme_count, key=theme_count.get)

    print(f"Average Rating: {average_rating:.2f}")
    print(f"Most Common Photography Theme: {favorite_theme}")

    # Recommendation system
    if favorite_theme == "street":
        print("Recommendation: Try more night street photography!")

    elif favorite_theme == "nature":
        print("Recommendation: Explore landscape photography!")

    elif favorite_theme == "food":
        print("Recommendation: Try cafe photography and close-up shots!")

    else:
        print("Recommendation: Continue exploring different styles!")


# -------------------------
# SHARED LOCATION SYSTEM
# -------------------------

def save_shared_log(location, theme, rating, description):
    with open("shared_logs.txt", "a") as file:
        file.write(f"{location},{theme},{rating},{description}\n")


def explore_locations():
    print("\n=== Explore Shared Locations ===")

    location_search = input("Enter a location: ")

    found = False

    try:
        with open("shared_logs.txt", "r") as file:

            for line in file:
                location, theme, rating, description = line.strip().split(",")

                if location.lower() == location_search.lower():

                    found = True

                    print(f"""
Location: {location}
Theme: {theme}
Rating: {rating}
Description: {description}
------------------------
""")

        if not found:
            print("No shared logs found for this location.")

    except FileNotFoundError:
        print("Shared log file not found.")


# -------------------------
# COMMENTS SYSTEM
# -------------------------

def add_comment():
    print("\n=== Add Comment ===")

    location = input("Enter location: ")
    comment = input("Enter your comment: ")

    with open("comments.txt", "a") as file:
        file.write(f"{location}:{comment}\n")

    print("Comment added successfully!")


def view_comments():
    print("\n=== View Comments ===")

    location_search = input("Enter location: ")

    found = False

    try:
        with open("comments.txt", "r") as file:

            for line in file:
                location, comment = line.strip().split(":")

                if location.lower() == location_search.lower():

                    found = True
                    print(f"- {comment}")

        if not found:
            print("No comments found.")

    except FileNotFoundError:
        print("Comment file not found.")


# -------------------------
# TESTING FUNCTION
# -------------------------

def test_validate_rating():

    assert validate_rating("5") == 5

    try:
        validate_rating("abc")
    except ValueError:
        print("Test Passed!")

    try:
        validate_rating("10")
    except ValueError:
        print("Test Passed!")


# -------------------------
# MAIN PROGRAM
# -------------------------

test_validate_rating()

while True:

    display_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_log()

    elif choice == "2":
        view_logs()

    elif choice == "3":
        analyze_logs()

    elif choice == "4":
        explore_locations()

    elif choice == "5":
        add_comment()
        view_comments()

    elif choice == "6":
        print("Thank you for using PhotoJourney!")
        break

    else:
        print("Invalid choice.")
        continue