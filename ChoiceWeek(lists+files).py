def challenge1():
    playerList = input("enter the number you would like to reverse: ")
    reverse = ""
    for i in range(len(playerList)):
        reverse += playerList[len(playerList) - 1 - i]
    print(reverse)
#challenge1()


def challenge2():
    parameters = input("enter your numbers(will print unique values: ")
    unique = []
    for i in parameters:
        if parameters.count(i) == 1:
            unique.append(i)
        print(unique)
#challenge2()


def challenge3():
    nums = [1, 5, 7, 7, 8, 7, 4, 5]
    for i in nums:
        if nums.count(i) == 3:
            print("True", i, "appears 3 times")
        else:
            print("false", i, "appears less than 3 times")
#challenge3()
