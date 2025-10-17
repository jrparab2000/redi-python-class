user_input = int(input("input a number "))
squares = {}

for numbers in range(1, user_input +1):
    square = numbers**2
    squares[numbers] = square

print(squares)