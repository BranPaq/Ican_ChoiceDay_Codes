#exponent calculator
#expCalc is the first challenge, pattern is the second, between is the third, primes is the fourth, and factorial is challenge 5
def expCalc():
    while True:
        num = input("Please enter your base number: ")
        num = float(num)
        exp = input("please input your exponent number: ")
        exp = float(exp)
        print("the answer is: ",num**exp)

#pattern print
def pattern():
    while True:
        ans = input("would you like to see the secret pattern Y/N: ")
        if ans == 'Y' or ans == 'y':
            print("1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5")
        elif ans == 'N' or ans == 'n':
            print ("okay I did not like you anyways, I will go see someone else!")
            break
        else:
            print("there was an error. Try again")

#prints all numbers between two chosen numbers
def between():
    num1 = input("please input your first number: ")
    num1 = int(num1)
    num2 = input("please input your second number: ")
    num2 = int(num2)
    for num in range(num1, num2, +1):
        print(num)

#prints prime numbers between two chosen numbers
def primes():
    num1 = input("enter your first number: ")
    num1 = int(num1)
    num2 = input("enter your second number: ")
    num2 = int(num2)
    for num in range(num1, num2):
        if num % 2 != 0:
            print(num)
            continue

#prints factorial thing idk its challenge 5
def factorial():
    num = input("what number would you like to get the factorial?!? from: ")
    for n in num:
        print(n *n)
factorial()
