try:
    a = float(input("Type first number: "))
    b = float(input("Type second number: "))
    c = a / b
    print("Result: %.2f" % c)
except (ValueError, ZeroDivisionError):
    print("Strings and division by zero are not available")
