import turtle

score_a = 0
score_b = 0

wn = turtle.Screen()
wn.title("pong")
wn.setup(width=800, height=600)
wn.bgcolor("white")
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.05
ball.dy = 0.05

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write("Player A :{}   Player B : {}".format(score_a, score_b), align="center", font=("courier", 24, 'normal'))


def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)


# Define a function to move the paddle down
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)


# Define a function to move the paddle up
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)


# Define a function to move the paddle down
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

Playing = True
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor () + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1 

    elif ball.ycor() < -290:
        