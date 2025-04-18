def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"Result: {result}")

calculator()
