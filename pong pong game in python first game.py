from tkinter import font
import turtle 
window = turtle.Screen()

window.title("pong by gaurav@morey ")

window.bgcolor("black")

window.setup(width=800, height=600)

window.tracer(0)

# score 
score_a = 0

score_b = 0 


## padal A 

paddle_a =turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("square")

paddle_a.color("red")

paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_a.penup()

paddle_a.goto(-350 , 0)

## padal B

paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.color("green")

paddle_b.shapesize(stretch_wid=5, stretch_len=1)

paddle_b.penup()

paddle_b.goto(350 , 0)

## ping pong ball 

ball =turtle.Turtle()

ball.speed(0)

ball.shape("square")

ball .color("yellow")

ball .penup()

ball .goto(0 , 0)

ball.dx = 0.5

ball.dy = -0.5


# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0 player B : 0 ", align = "center", font = ("courler",24,"normal"))



## function 

def paddle_a_up():
    y = paddle_a.ycor()

    y += 40

    paddle_a.sety(y)

def paddle_a_down():
    y =paddle_a.ycor()

    y -= 40

    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()

    y += 40

    paddle_b.sety(y)

def paddle_b_down():
    y =paddle_b.ycor()

    y -= 40

    paddle_b.sety(y)

    ##keybord binding

window.listen()
window.onkeypress(paddle_a_up,"w")

window.onkeypress(paddle_a_down,"s")  

window.onkeypress(paddle_b_up,"Up")

window.onkeypress(paddle_b_down,"Down")  

##main game loops

while True:
    window.update()

##move the ball 

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

#border checking 

    if ball.ycor() > 290:

        ball.sety(290)

        ball.dy *= -1

    if ball.ycor() < -290:

        ball.sety(-290)

        ball.dy *= -1
    
    if ball.xcor() > 390:

        ball.goto(0,0)

        ball.dx *= -1

        score_a +=1

        pen.clear()

        pen.write("player A: {} player B : {} ".format(score_a, score_b), align = "center", font = ("courler",24,"normal"))

    if ball.xcor() < -390:

        ball.goto(0,0)

        ball.dx *= -1

        score_b += 1

        pen.clear()

        pen.write("player A: {} player B : {} ".format(score_a, score_b), align = "center", font = ("courler",24,"normal"))

    # paddle and ball colisions

    if ( ball.xcor() > 340 and ball.xcor() < 350 ) and ( ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if ( ball.xcor() < -340 and ball.xcor() < -350 ) and ( ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1       


