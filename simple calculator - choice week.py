#iCan - Basic calculator
#2/29/20204
#Brandon Paquette

def calculator():
    num1 = input("Enter your first number: ")
    num1 = float(num1)
    operator = input("pleas enter your operator(+, -, *, or /): ")
    num2 = input("Enter your second number: ")
    num2 = float(num2)
    
    if operator == '+':
        answer = float(num1 + num2)
        print(str(answer))
    elif operator == '-':
        answer = float(num1 - num2)
        print (str(answer))
    elif operator == '*':
        answer = float(num1 * num2)
        print (str(answer))
    elif operator == '/':
        if num2 != 0:
            answer = float(num1 / num2)
            print (str(answer))
        else:
            print("the second number cannot be a zero")
            calculator()
    else:
        print("there was an error with your inputs :(")
        calculator()

def modulo():
     num1 = input("Enter your first number: ")
     num1 = float(num1)
     num2 = input("Enter your second number: ")
     num2 = float(num2)
     answer = int(num1 % num2)
     print(str(answer))

def lobby():
        userPick = input("press 1 to open the calculator code and press 2 if you want to open modulo code : ")
        if userPick == '1':
            calculator()
        elif userPick == '2':
            modulo()
        else:
            print ("there was an error, please enter your choice again")
while True:
    lobby()
