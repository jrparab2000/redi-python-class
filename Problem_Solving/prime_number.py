def is_prime(number):
    for i in range(2,number-1):
        if number%i ==0:
            return False
    return True

def main():
    while True:
        numb = int(input("input a number: "))
        if(numb == 0)|(numb < 0):
            break
        if is_prime(numb):
            print("Its a prime")
        else:
            print("Ist not a prime")

if __name__ == "__main__":
    main()
        