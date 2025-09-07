def Addition(a,b):
    return a + b

def Subtraction(a,b):
    return a - b

def Multiplication(a,b):
    return a * b

def Division(a,b):
    if b != 0:
        return a / b
    else:
        return "Dividing with zero "
    
def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        print("Result:", Addition(a,b))
    elif operation == "-":
        print("Result:", Subtraction(a,b))
    elif operation == "*":
        print("Result:", Multiplication(a,b))
    elif operation == "/":
        print("Result:", Division(a,b))
    else:
        print("Invalid operation")
        
main()