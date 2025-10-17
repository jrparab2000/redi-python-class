numbers = []

while True:
    user_input = input("Please enter a number: ")
    if user_input.lower() == 'x':
        print("Done")
        break
    numbers.append(int(user_input))
    print(numbers)

total = sum(numbers)
average = total/len(numbers)
print(f"The sum is {total} and average is {average}")
