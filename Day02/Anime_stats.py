anime_names = []
anime_genres = []
episodes_watched = []
total_episodes = []
anime_ratings = []
anime_status = []


# ---------- FUNCTIONS ----------

def add_anime():
    name = input("Enter anime name: ")
    genre = input("Enter genre: ")
    total = int(input("Enter total episodes: "))

    if total <= 0:
        print("Total episodes must be greater than 0.")
        return

    anime_names.append(name)
    anime_genres.append(genre)
    episodes_watched.append(0)
    total_episodes.append(total)
    anime_ratings.append(0)
    anime_status.append("Plan to Watch")

    print("Anime added successfully!")


def update_progress():
    if len(anime_names) == 0:
        print("No anime available.")
        return

    display_all_anime(short=True)
    index = int(input("Select anime number to update progress: ")) - 1

    if index < 0 or index >= len(anime_names):
        print("Invalid selection.")
        return

    watched = int(input("Enter episodes watched: "))

    if watched < 0 or watched > total_episodes[index]:
        print("Invalid episode count.")
        return

    episodes_watched[index] = watched

    if watched == total_episodes[index]:
        anime_status[index] = "Completed"
    elif watched > 0:
        anime_status[index] = "Watching"

    print("Progress updated successfully!")


def rate_anime():
    if len(anime_names) == 0:
        print("No anime available.")
        return

    display_all_anime(short=True)
    index = int(input("Select anime number to rate: ")) - 1

    if index < 0 or index >= len(anime_names):
        print("Invalid selection.")
        return

    rating = float(input("Enter rating (1 to 10): "))

    if rating < 1 or rating > 10:
        print("Rating must be between 1 and 10.")
        return

    anime_ratings[index] = rating
    print("Rating added successfully!")


def drop_anime():
    if len(anime_names) == 0:
        print("No anime available.")
        return

    display_all_anime(short=True)
    index = int(input("Select anime number to drop: ")) - 1

    if index < 0 or index >= len(anime_names):
        print("Invalid selection.")
        return

    anime_status[index] = "Dropped"
    print("Anime marked as dropped.")


def display_all_anime(short=False):
    if len(anime_names) == 0:
        print("Watchlist is empty.")
        return

    print("\n--- ANIME WATCHLIST ---")
    for i in range(len(anime_names)):
        if short:
            print(f"{i+1}. {anime_names[i]} ({anime_status[i]})")
        else:
            print(f"""
Anime Name       : {anime_names[i]}
Genre            : {anime_genres[i]}
Episodes Watched : {episodes_watched[i]} / {total_episodes[i]}
Rating           : {anime_ratings[i]}
Status           : {anime_status[i]}
------------------------------
            """)


def filter_by_status():
    status = input("Enter status (Watching / Completed / Dropped / Plan to Watch): ")

    found = False
    for i in range(len(anime_names)):
        if anime_status[i].lower() == status.lower():
            print(f"{anime_names[i]} - {anime_status[i]}")
            found = True

    if not found:
        print("No anime found with this status.")


def show_statistics():
    if len(anime_names) == 0:
        print("No data available.")
        return

    completed = 0
    watching = 0
    dropped = 0

    for status in anime_status:
        if status == "Completed":
            completed += 1
        elif status == "Watching":
            watching += 1
        elif status == "Dropped":
            dropped += 1

    avg_rating = 0
    rated_count = 0
    for rating in anime_ratings:
        if rating > 0:
            avg_rating += rating
            rated_count += 1

    if rated_count > 0:
        avg_rating /= rated_count

    print("\n--- WATCHLIST STATISTICS ---")
    print("Total Anime     :", len(anime_names))
    print("Completed       :", completed)
    print("Watching        :", watching)
    print("Dropped         :", dropped)
    print("Average Rating  :", round(avg_rating, 2))


def show_menu():
    print("""
========= ANIME WATCHLIST MENU =========
1. Add Anime
2. Update Watching Progress
3. Rate Anime
4. Drop Anime
5. View All Anime
6. Filter Anime by Status
7. Show Statistics
8. Exit
=======================================
    """)


# ---------- MAIN LOOP ----------

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_anime()
    elif choice == "2":
        update_progress()
    elif choice == "3":
        rate_anime()
    elif choice == "4":
        drop_anime()
    elif choice == "5":
        display_all_anime()
    elif choice == "6":
        filter_by_status()
    elif choice == "7":
        show_statistics()
    elif choice == "8":
        print("Exiting Anime Watchlist. Bye Otaku 👋")
        break
    else:
        print("Invalid choice. Try again.")
