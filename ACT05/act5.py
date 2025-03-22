def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("The second number must be higher than the first number.")
        return None
    return sum(range(int(a), int(b) + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting program...")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            
            try:
                a, b = float(a), float(b)
                
                if choice == 'D':
                    result = divide(a, b)
                elif choice == 'E':
                    result = exponentiation(a, b)
                elif choice == 'R':
                    result = remainder(a, b)
                elif choice == 'F':
                    result = summation(a, b)
                
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Valid numeric values only.")
        else:
            print("Invalid choice. Please try again.")

main()
