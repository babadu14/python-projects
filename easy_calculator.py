number1 = int(input("enter first number -> "))
operator = input("choose an operator (+, -, /, *, %, **, //) ")
number2 = int(input("enter second number -> "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "%":
    print(number1 % number2)
elif operator == "**":
    print(number1 ** number2)
elif operator == "//":
    print(number1 // number2)
else:
    print("error")
