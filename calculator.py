# programming a simple caluclator 

# add
def add (x, y):
    return x + y

# subtract
def subtract(x, y):
    return x - y

# multiply
def multiply(x, y):
    return x * y

# divide
def divide(x, y):
    return x / y


print("Select Operation:")
print("+")
print("-")
print("*")
print("/")

while True:
    # get input
    choice = input("Enter Operation: ")

    # check input
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("First: "))
        num2 = float(input("Second: "))

    if choice == '+':
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '-':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1,num2))


    # send off message
    next_calc = input("Want to do another? (y/n): ")
    if next_calc == "n":
        print("thanks, k bye")
        break

    else:
        print("Invalid Input")