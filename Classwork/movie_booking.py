# ------------------------------------------------------------------ #

# Favourite movie:
# 1. Inception
# 2. The Matrix
# 3. interstellar
# 4. The Dark Knight

# showtime:
# M, A, E

# Features:
# 1. Available movies and timings
# 2. seats - number of tickets, Regular/ vip
# 3. ticket prices - 12 EUR, 24 EUR
# 4. Show them the booking conformation

# ------------------------------------------------------------------ #

movies = {
        "Inception" : ["M", "E"],
        "The Matrix" : ["M", "A"],
        "Interstellar"     : ["M","A","E"],
        "The Dark Knight"    : ["E"],
    }

def movie_program():
    print("This is Today's schedule:")
    for movie in movies:
        print(f"\"{movie}\": has these slots Available:")
        for i in range(0, len(movies[movie])):
            print(f"{movies[movie][i]}")
        print()

def ask():
    title = input(f"Select a Movie: ")
    if title in movies:
        time = input(f"select a Show time: ")
        if time in movies[title]:
            print("This time slot is available")
            print()
            return True
        else:
            print("This time slot is not available")
            return False
    else:
        print("Movie is not available")
        return False
    
def seats(pref):
    number = int(input(f"Enter number of tickets:"))
    if pref == "y":
        cost = number*24
    else:
        cost = number*12
    print(f"Total cost: ${cost}")
    return input(f"confirm your Booking? y/n: ")

def main():
    movie_program()
    flag = ask()
    if flag:
        print("Cost for the regular seat is $12 per person")
        print("Cost for the VIP seat is $24 per person")
        seat = input(f"Do you want VIP seat y/n: ")
        final = seats(seat)
        if final == "y":
            print(f"Ticket Booked Successfully!!!")
        else:
            print(f"Please try again with different option")
    else:
        print(f"Please try again with different option")

if __name__ == "__main__":
    main()
