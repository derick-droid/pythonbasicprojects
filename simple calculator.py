number1 = float(input("enter first number:  "))
operator = input("enter an operator:  ")
number2 = float(input("enter the second number: "))
if operator == "+":
    result = number2 + number1
    print(result)
elif operator == "-":
    result = number2 - number1
    print(result)
elif operator == "*":
    result = number2 * number1
    print(result)
elif operator == "/":
    result = number2 / number1
    print(result)
elif operator == "%":
    result = number2 % number1
    print(result)
elif operator == "//":
    result = number2 // number1
    print(result)
else:
    print("invalid operator ")