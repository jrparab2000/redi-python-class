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
# default parameters in the function

def write_greeting(name, age, language="en", do_print=False):
    if(do_print):
        if(language == "en"):
            print(f"Hello {name} and age  {age}")
        elif(language == "de"):
            print(f"Hallo {name} und age  {age}")


# write_greeting("jayesh", 25, language="de",do_print=True)
# write_greeting("Jayesh", 25, "en", True)
# write_greeting("Jayesh", 25, do_print=True)

# ------------------------------------------------------------------ #
# *names == use * to pass tuple 
# **metadata == use ** to pass dict

def greeting(msg, *names, do_print=False, **metadata):
    for name in names:
        message = f"{msg} {name}"
        if do_print:
            print(msg)
    print("metadata: ", metadata)



greeting("Hello nice to meet you",
    "Alice","BOB","Jayesh", "Shruti",
    do_print=True,
    sender="Jayesh",
    language="English",
    address="Texas"
)
        