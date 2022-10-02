import turtle

def koch(lenght, t):
    if lenght > 6:
        ln = lenght // 3
        koch(ln, t)
        t.left(70)
        koch(ln, t)
        t.right(140)
        koch(ln, t)
        t.left(70)
        koch(ln, t)
    else:
        t.fd(lenght)
        t.left(70)
        t.fd(lenght)
        t.right(140)
        t.fd(lenght)
        t.left(70)
        t.fd(lenght)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    lenght = 150
    t.ht()
    koch(lenght, t)
    myWin.exitonclick()

if __name__ == '__main__':
    main()