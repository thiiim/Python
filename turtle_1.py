from turtle import*

getscreen()
bgcolor("grey")
pencolor("white")
pensize(7)
shape("turtle")
fillcolor("black")
begin_fill()

pendown()
for i in range(4):
    forward(100)
    left(90)
penup()
forward(200)

pendown()
for i in range(7):
    forward(50)
    left(360/7)

penup()
backward(300)

pendown()
init_size = 7
for i in range(7):
    circle(init_size)
    init_size += 7

end_fill()

done()
