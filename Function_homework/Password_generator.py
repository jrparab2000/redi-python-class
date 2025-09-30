import random

letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def get_character_pool(password_type):
    if password_type == 1:
        return letters
    elif password_type == 2:
        return letters +digits
    elif password_type == 3:
        return letters + digits + special
    elif password_type == 4:
        return letters + digits + special
    else:
        return ""
    
def generate_password(length, password_type):
    pool = get_character_pool(password_type)
    if password_type == 4:
        password = [
            random.choice(letters),
            random.choice(letters.upper()),
            random.choice(digits),
            random.choice(special)
        ]
        password += random.choices(pool, k=length - 4)
        random.shuffle(password)
        return "".join(password)
    return "".join(random.choices(pool, k=length))

def validate_password(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in special for c in password)

    score = 0
    if length >= 8: score += 20
    if length >= 12: score += 20
    if has_lower: score += 15
    if has_upper: score += 15
    if has_digit: score += 15
    if has_symbol: score += 15

    if score >= 85:
        strength = "Strong"
    elif score >= 60:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score

def display_menu():
    print("\nPassword Generator")
    print("=================")
    print("1. Generate Single Password")
    print("2. Generate Multiple Passwords")
    print("3. Check Password Strength")
    print("4. Exit")


def choose_password_type():
    print("\nPassword Types:")
    print("1. Simple (letters only)")
    print("2. Standard (letters + numbers)")
    print("3. Strong (letters + numbers + symbols)")
    print("4. Ultra-secure (all types + requirements)")
    while True:
        choice = int(input("Choose password type: "))
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print("Invalid choice. Try again.")


def get_password_length():
    while True:
        length = int(input("Enter password length (8–50): "))
        if 8 <= length <= 50:
            return length
        else:
            print("Length must be between 8 and 50.")


def generate_multiple_passwords():
    password_type = choose_password_type()
    length = get_password_length()
    count = int(input("How many passwords do you want to generate? "))

    print("\nGenerated Passwords:")
    for i in range(count):
        pwd = generate_password(length, password_type)
        strength, score = validate_password(pwd)
        print(f"{i+1}. {pwd}  -->  {strength} ({score}/100)")


def generate_single_password():
    password_type = choose_password_type()
    length = get_password_length()
    pwd = generate_password(length, password_type)
    strength, score = validate_password(pwd)

    print(f"\nGenerated Password: {pwd}")
    print(f"Password Strength: {strength} (Score: {score}/100)")


def check_password_strength():
    password = input("\nEnter a password to check: ")
    strength, score = validate_password(password)
    print(f"Password Strength: {strength} (Score: {score}/100)")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            generate_single_password()
        elif choice == "2":
            generate_multiple_passwords()
        elif choice == "3":
            check_password_strength()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        end = input("Would you like another password? (y/n): ")
        if(end.lower() == "n"):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
