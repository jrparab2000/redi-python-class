#function signature is "def greet(name):"
#function calling greet("my name is Jayesh")
# ------------------------------------------------------------------ #

def repeat_it(times, text):
    for index in range(1,times +1):
        print(f"{index} - {text}")


# repeat_it(10,"I will work")
# repeat_it(20,"I am Jayesh")
# ------------------------------------------------------------------ #

def initialize(temperature: int):
    print("Water kettle simulation")
    print(f"Starting temperature: {temperature}C")

def shut_down():
    print("Kettle has reached the boiling point")
    print("Water is ready")

def heating(temperature_start,heating_increment):
    temperature = temperature_start
    while temperature <= 100:
        temperature += heating_increment
        if temperature <= 25:
            status = "cool"
        elif temperature <= 40:
            status = "getting warm"
        elif temperature <= 65:
            status = "hot"
        elif temperature < 100:
            status = "Almost boiling"
        else:
            status = "boiling"
        print(f"Current water status = {status} and current temperature {temperature}")


def water_kettle(temperature_start,heating_increment):
    initialize(temperature_start)
    heating(temperature_start,heating_increment)
    shut_down() 

# water_kettle(100,5)
# ------------------------------------------------------------------ #

def initialize_rocket():
    print("NASA MISSION CONTROL")
    print("Initiating launch sequence...")
    print("All system nominal. Begin countdown")
    print()

def count_down():
    for numbers in range(10,0,-1):
        if numbers == 10:
            print(f"T-minus {numbers}: Main engine start")
        elif numbers == 5:
            print(f"T-minus {numbers}: GO for Launch")
        elif numbers == 3:
            print(f"T-minus {numbers}: SRB ignition")
        else:
            print(f"T-minus {numbers}")

def lift_off():
    print("T-minus 0: Liftoff")
    print()
    print("Eagle has wings")

def rocket():
    initialize_rocket()
    count_down()
    lift_off()

# rocket()

# ------------------------------------------------------------------ #

# Favourite movie:
# 1. terminator 2 
# 2. interstellar
# 3. blacklist
# 4. Home alone
# 5. the pursuit of happiness

# showtime:
# M, A, E

# Features:
# 1. Available movies and timings
# 2. seats - number of tickets, 1st class/ vip/ dbox
# 3. ticket prices - 18 EUR, 25 EUR
# 4. Show them the booking conformation

# ------------------------------------------------------------------ #

movies = {
        "Terminator 2" : ["Morning", "Evening"],
        "Interstellar" : ["Morning", "Afternoon"],
        "Blacklist"     : ["Morning","Afternoon","Evening"],
        "Home alone"    : ["Evening"],
        "the pursuit of happiness" : ["Morning", "Afternoon"]
    }

def movie_program():
    print("This is Today's schedule:")

    for movie in movies:
        print(f"{movie} has these slots Available:")
        for i in range(0, len(movies[movie])):
            print(f"{movies[movie][i]}")
        print()

def ask():
    title = input(f"Select a Movie: ")
    if title in movies:
        time = input(f"Show time: ")
        if time in movies[title]:
            print("Time is available")
            seats = input(f"Choose a seat: ")
        else:
            print("Time is not available")
            return None
    else:
        print("Movie not available")
        return None
    

movie_program()
ask()