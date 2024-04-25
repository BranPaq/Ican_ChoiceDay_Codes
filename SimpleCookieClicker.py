import turtle
import time
import threading

#creates the window
wn = turtle.Screen()
wn.title("Cookier Clicker")
wn.bgpic("C:\\Users\\iCan Student\\Pictures\\space back 2.gif")

#makes the cookie
wn.register_shape("C:\\Users\\iCan Student\\Pictures\\cookie.gif")
cookie = turtle.Turtle()
cookie.shape("C:\\Users\\iCan Student\\Pictures\\cookie.gif")
cookie.speed(0)

#makes the cursor
wn.register_shape("C:\\Users\\iCan Student\\Pictures\\cursor.gif")
cursor = turtle.Turtle()
cursor.shape("C:\\Users\\iCan Student\\Pictures\\cursor.gif")
cursor.speed(0)
cursor.shapesize(0.5)
cursor.penup()
cursor.goto(400, 175)

#makes the grandma
wn.register_shape("C:\\Users\\iCan Student\\Pictures\\Grandmother.gif")
grandma = turtle.Turtle()
grandma.shape("C:\\Users\\iCan Student\\Pictures\\Grandmother.gif")
grandma.speed(0)
grandma.shapesize(0.5)
grandma.penup()
grandma.goto(400, -200)

#creates needed variable
clicks = 0
ownedCursors = 0
ownedGrandmas = 0
increase_clicks_time = 0

#print cookies on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("tomato")
pen.penup()
pen.goto(0, 200)
pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "normal"))

#print owned cursors on screen
penCursor = turtle.Turtle()
penCursor.hideturtle()
penCursor.color("tomato")
penCursor.penup()
penCursor.goto(-450, 200)
penCursor.write(f"Owned Cursors: {ownedCursors}", align="center", font=("Courier New", 32, "normal"))

#print owned grandmas
penGrandma = turtle.Turtle()
penGrandma.hideturtle()
penGrandma.color("tomato")
penGrandma.penup()
penGrandma.goto(-450, 0)
penGrandma.write(f"Owned Grandmas: {ownedGrandmas}", align="center", font=("Courier New", 32, "normal"))

#makes the interactions when clicked
#when cookie clicked
def clicked(x, y):
    global clicks, ownedCursors
    clicks += 1
    pen.clear()
    pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "normal"))
    clicks = clicks + ownedCursors

#when cursor is bought
def cursorBuy(x, y):
    global cursor, clicks, ownedCursors
    penCursor.clear()
    penCursor.write(f"Owned Cursors: {ownedCursors}", align="center", font=("Courier New", 32, "normal"))
    if clicks < 50:
        print("you dont have enough cookies to buy this")
    else:
        clicks -= 50
        ownedCursors += 1

#when grandma is clicked
def grandmaBuy(x, y):
    global increase_clicks_time, clicks, ownedGrandmas
    penGrandma.clear()
    penGrandma.write(f"Owned Grandmas: {ownedGrandmas}", align="center", font=("Courier New", 32, "normal"))
    if clicks < 100:
        print("you dont have enough cookies to buy this")
    else:
        clicks -= 100
        ownedGrandmas += 1
        increase_clicks_time += 1

#bought grandma actions
def grandmaAct():
    global clicks, increase_clicks_time
    while True:
        time.sleep(1)
        clicks += increase_clicks_time
        pen.clear()
        pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "normal"))

t1 = threading.Thread(target=grandmaAct, name="t1")
t1.start()

#runs the code
grandma.onclick(grandmaBuy)
cursor.onclick(cursorBuy)
cookie.onclick(clicked)
wn.mainloop()
