
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulo(x, y):
    return x % y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulo")
while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4' ,'5'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print(" error! Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(a, "+", b, "=", add(a, b))
        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))
        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))
        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))
        elif choice == '5':
            print(a, "%", b, "=", modulo(a, b))  
        repeat= input("wanna do next calculation? (yes/no): ")
        if repeat == "no":
          break
    else:
        print("Invalid Input.enter 1 or 2 or 3 or 4 since we have only four basic arithmetic operation calculation")
