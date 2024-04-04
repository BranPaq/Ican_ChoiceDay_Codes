import turtle

wn = turtle.Screen()
wn.title("Cookier Clicker")
wn.bgpic("C:\\Users\\iCan Student\\Pictures\\space back 2.gif")

wn.register_shape("C:\\Users\\iCan Student\\Pictures\\cookie.gif")
cookie = turtle.Turtle()
cookie.shape("C:\\Users\\iCan Student\\Pictures\\cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("tomato")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)
wn.mainloop()
