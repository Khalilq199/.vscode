operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
if operator == "+":
    print(f"Your answer is {num1 + num2}")
elif operator == "-":
    print(f"Your answer is {num1 - num2}")
elif operator == "*":
    print(f"Your answer is {num1 * num2}")
elif operator == "/":
    print(f"Your answer is {num1 / num2}")
else:
    print(f"{operator} is not a valid operator")