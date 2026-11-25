
# ==========================================
# SIMPLE CALCULATOR AND GREETING BOT
# ==========================================

print("===== PYTHON BEGINNER PROJECT =====")

# Greeting Bot
print("\n--- Greeting Bot ---")

name = input("Enter your name: ")

if name.strip():
    print(f"Hello, {name}! Welcome to Python programming.")
else:
    print("Hello! Welcome to Python programming.")

# Simple Calculator
print("\n--- Simple Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")

print("\nThank you for using the program!")
