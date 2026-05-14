n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Addition =", n1 + n2)

elif op == "-":
    print("Subtraction =", n1 - n2)

elif op == "*":
    print("Multiplication =", n1 * n2)

elif op == "/":
    if n2 != 0:
        print("Division =", n1 / n2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid Operator")
