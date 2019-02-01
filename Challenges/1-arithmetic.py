# Простейшие арифметические операции (1)
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
# то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter operator: ")

    def show_result():
        print("Result is %.2f" % result)

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
        show_result()
    else:
        print("Unknown Operation")


print(arithmetic())
