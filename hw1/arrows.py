import turtle

def rotate_left():
    turtle.left(20)

def rotate_right():
    turtle.right(20)

def move():
    turtle.fd(20)



turtle.onkeypress(move, "Up")
turtle.onkeypress(rotate_left, "Left")
turtle.onkeypress(rotate_right, "Right")
turtle.listen()
turtle.mainloop()