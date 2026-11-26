print("Welcome to the Calculator!")
n = int(input("How many numbers do you want to calculate? "))
v = []
for i in range(n):
    a = float(input(f"Enter number {i+1}: "))
    v.append(a)
h = input("Enter the operation (+, -, *, /): ")
if h == "+":
    result = sum(v)
    print("The result is:", result)
elif h == "-":
    result = v[0]
    for j in range(1, len(v)):
        result -= v[j]
    print("The result is:", result)
elif h == "*":
    result = 1
    for j in v:
        result *= j
    print("The result is:", result)
elif h == "/":
    result = v[0]
    for j in range(1, len(v)):
        if v[j] == 0:
            print("Error: Division by zero is not allowed.")
            break
        result /= v[j]
    else:
        print("The result is:", result)
else:
    print("Invalid operation.")
print("Thank you for using the Calculator!")