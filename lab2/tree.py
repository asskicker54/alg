import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(branchLen/6) #Изменение толщины ветвей
        angle = random.randint(15, 45) #Изменение угла поворота черепахи
        length = random.randint(8, 22) #Изменение рекурсивной части branchLen
        
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - length, t)
        t.left(angle * 2)
        tree(branchLen - length, t)
        t.right(angle)
        t.backward(branchLen)
        
        t.color("brown")
    else:                   # Изменение цвета листьев
        t.color("orange")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t)
    myWin.exitonclick()

if __name__ == "__main__":
    main()