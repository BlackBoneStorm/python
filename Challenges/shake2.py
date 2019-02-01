

def arithmetic():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    def show_result():
        print("Result is", result)

    if operator == "+":
        result = a + b
        show_result()
    elif operator == "-":
        result = a - b
        show_result()
    elif operator == "*":
        result = a * b
        show_result()
    elif operator == "/":
        result = a / b
        show_result()s
    else:
        print("Unknown Operation")


print(arithmetic())
