def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def count_decimals(num_str):
    return len(num_str.split('.')[1]) if '.' in num_str else 0

def calculator():
    while True:
        print("\n***** Welcome To Python Calculator *****")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice not in ['1', '2', '3', '4']:
            print("Invalid option. Please choose a valid option.")
            continue

        num1_str = input("Enter the first number: ")
        num2_str = input("Enter the second number: ")

        num1 = float(num1_str)
        num2 = float(num2_str)

        # Count decimals of input numbers
        dec_places = max(count_decimals(num1_str), count_decimals(num2_str))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        # Print result
        if isinstance(result, str): #Kept check for special case where user tries to divide number by zero and result will be "Error: Division by zero"
            print(result)
        else:
            print(f"Result: {result:.{dec_places}f}")

#Run Code
calculator()