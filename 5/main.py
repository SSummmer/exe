"""
    练习5
"""
import turtle

t = turtle.Turtle(shape='turtle')
l = int(input("请输入等边三角形的边长："))
r = int(input("请输入圆的半径："))
t.penup()
t.goto(250, 200)
t.pendown()
t.forward(l)
t.left(120)
t.forward(l)
t.left(120)
t.forward(l)
t.penup()
t.home()
t.pendown()
t.circle(r)
turtle.mainloop()
