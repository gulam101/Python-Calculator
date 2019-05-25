# this function adds two numbers

def add (x, y):
    return x + y

# this next function subtracts two nymbers
def subtract (x, y):
    return x - y

# This function allow the user to multiple two numbers together
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


##### we will know add in the select function whitch will allow the user to select his/her option in order to get the functions working

print("~~~~~~~~~~~~~~~~~~~~~~~~~Mr Wizard The Funny Calculator!!!~~~~~~~~~~~~~~~")
print("Please select an operation in order to run the calculator!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Puzzle")

# this will allow the user to input his/her command
print("Please input your choice at the bottom!")
choice = input("Enter choice(1/2/3/4/5):")

print("For this to work you must input a number of your choice!")
num1 = int(input("Enter first number:   "))
print("Please input your second number!")
num2 = int(input("Enter second number:  "))

if choice == '1':
    print(num1,"+" ,num2, "=", add(num1,num2))
    

if choice == '2':
        print(num1,"-" ,num2, "=", subtract(num1,num2))

if choice == '3':
    print(num1, "*" ,num2, "=", multiply(num1,num2))

if choice == '4':
    print(num1, "/" ,num2, "=", divide(num1,num2))

if choice == '5':
    print("999999999999999999999999999999999999999999999999999999999999999999999100000000000000000000000000000000000000000000000000000000000000000000")
    print("the value is high that i don't know the answer! Goodbye!")



        
        
