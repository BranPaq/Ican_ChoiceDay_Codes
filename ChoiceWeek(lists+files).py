def challenge1():
    playerList = input("enter the number you would like to reverse: ")
    reverse = ""
    for i in range(len(playerList)):
        reverse += playerList[len(playerList) - 1 - i]
    print(reverse)
challenge1()
