import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setpos(-100,-200)
turtle.pendown()
turtle.pencolor("#4ba925")

axion = "FX"
axmTemp = ""

itr = 15
dl = 3
angl = 90

translate={"+":"+", "-":"-", "F":"F", "X":"X+YF+", "Y":"-FX-Y" }
for n in range(itr):
    for ch in axion:
        axmTemp += translate[ch]
    axion = axmTemp
    axmTemp = ""
for ch in axion:
    if   ch == "+":
        turtle.right(angl)
    elif ch == "-":
        turtle.left(angl)
    elif ch == "F":
        turtle.forward(dl)

turtle.update()
turtle.mainloop()