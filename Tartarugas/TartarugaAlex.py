import turtle

wn = turtle.Screen()
wn.bgcolor("black")         # define a cor de fundo da janela

alex = turtle.Turtle()
alex.color("lightgreen")               # alex fica azul
alex.pensize(3)                  # define a espessura da caneta

alex.left(90)
alex.forward(120)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.left(140)
alex.forward(100)

wn.exitonclick()