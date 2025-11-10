def calculator():
    print("Welcome to the calculator.")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Choose an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("You tried to divide by zero. Invalid.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Try again.")
                continue

            print(f"The result is: {result}")

        except ValueError:
            print("That’s not a number. Try again.")

        cont = input("Do you want to calculate something else? (yes/no): ").lower()
        if cont != 'yes':
            print("Goodbye.")
            break

calculator()
