def is_leap(years):
    leap = False
    if years%4 == 0:
        if years%100 == 0:
            if years%400 == 0:
                leap = True 
    return leap

if is_leap(1800):
    print("Its leap year")
else:
    print("not a leap")