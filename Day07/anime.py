# =====================================================
# DAY 07: FILE-BASED ANIME TRACKING SYSTEM
# =====================================================

FILENAME = "anime_data.txt"


# ------------------ FILE UTILITIES ------------------

def load_anime_data():
    anime_list = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, genre, rating = line.strip().split("|")
                anime_list.append({
                    "name": name,
                    "genre": genre,
                    "rating": float(rating)
                })
    except FileNotFoundError:
        pass  # File will be created later
    return anime_list


def save_anime_data(anime_list):
    with open(FILENAME, "w") as file:
        for anime in anime_list:
            file.write(f"{anime['name']}|{anime['genre']}|{anime['rating']}\n")


# ------------------ CORE FUNCTIONS ------------------

def add_anime(anime_list):
    try:
        name = input("Enter anime name: ")
        genre = input("Enter genre: ")
        rating = float(input("Enter rating (1-10): "))

        if rating < 1 or rating > 10:
            print("Rating must be between 1 and 10.")
            return

        anime_list.append({
            "name": name,
            "genre": genre,
            "rating": rating
        })

        save_anime_data(anime_list)
        print("Anime added successfully!")

    except ValueError:
        print("Invalid input. Please enter correct values.")


def show_anime(anime_list):
    if not anime_list:
        print("No anime records found.")
        return

    print("\n--- Anime List ---")
    for anime in anime_list:
        print(f"Name: {anime['name']}, Genre: {anime['genre']}, Rating: {anime['rating']}")


def recommend_by_genre(anime_list):
    genre = input("Enter genre to search: ")
    found = False

    for anime in anime_list:
        if anime["genre"].lower() == genre.lower():
            print(f"Recommended: {anime['name']} ({anime['rating']})")
            found = True

    if not found:
        print("No anime found for this genre.")


def delete_anime(anime_list):
    name = input("Enter anime name to delete: ")
    for anime in anime_list:
        if anime["name"].lower() == name.lower():
            anime_list.remove(anime)
            save_anime_data(anime_list)
            print("Anime deleted successfully.")
            return
    print("Anime not found.")


# ------------------ MENU ------------------

def show_menu():
    print("""
========= ANIME TRACKER =========
1. Add Anime
2. View Anime List
3. Recommend by Genre
4. Delete Anime
5. Exit
================================
    """)


# ------------------ MAIN LOOP ------------------

def main():
    anime_list = load_anime_data()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_anime(anime_list)
        elif choice == "2":
            show_anime(anime_list)
        elif choice == "3":
            recommend_by_genre(anime_list)
        elif choice == "4":
            delete_anime(anime_list)
        elif choice == "5":
            print("Exiting Anime Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
