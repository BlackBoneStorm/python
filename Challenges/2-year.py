# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.


def is_year_leap():
    print("Is year leap?")

    leapYear = int(input("Enter the number of days: "))

    if leapYear == 366:
        return True
    elif leapYear == 365:
        return False
    else:
        print("Year can have 365 or 366 days. Try again.")


print(is_year_leap())
