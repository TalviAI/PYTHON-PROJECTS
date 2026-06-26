num1 = float(input("Enter a 1st number: "))
optr = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter a 2nd number: "))

if optr == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif optr == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif optr == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif optr == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif optr == '%':
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print(f"'{optr}' is invalid.")