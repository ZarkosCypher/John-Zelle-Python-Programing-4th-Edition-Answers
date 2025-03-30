from os import times_result
from graphics import *
from time import sleep

#extra creddit assingment each worth 10 points
#Build a forest. For every click of the mouse, a new tree is created where the mouse is clicked.
def forrest():
    win = GraphWin("window", 500, 500)
    def balls(x: int, y: int, size: int, color: str, outline: str):
        shape = Circle(Point(x, y), size)
        shape.setOutline(outline)
        shape.setFill(color)
        shape.draw(win)
    def square(x: int, y: int, thicc: int, long: int, color: str, outline: str):
        shape = Rectangle(Point(x - thicc, y - long), Point(x + thicc, y + long))
        shape.setOutline(outline)
        shape.setFill(color)
        shape.draw(win)
    #tree
    def tree(x,y):
        square(x,y+165-70,20,90,"brown","black")#stem of a tree
        square(x,y+190-70,70,10,"green","black")#bottom leaves
        square(x,y+160-70,60,10,"green","black")#
        square(x,y+130-70,50,10,"green","black")#
        square(x,y+100-70,40,10,"green","black")#
        square(x,y+70-70,30,10,"green","black")#top leaves
    tree(300,70)

    for i in range(10):
        p = win.getMouse()
        tree(p.getX(),p.getY())

    print("click again to quit")
    win.getMouse()
    win.close()
forrest()

#Simulate gravity. A ball falling from the top of the window and hitting the bottom of the window at 9.8m/s^2
def fallingBall():
    win = GraphWin("Falling Ball", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    shape = Circle(Point(0, 80), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    velocity = 0
    gravity = 9.8
    pxPerMtr = 10
    dt = 0.05

    for i in range(1000):
        velocity += gravity * dt
        dy = -velocity * dt * pxPerMtr

        c = shape.getCenter()
        newY = c.getY() + dy

        if newY - 20 < -100:
            shape.move(0, -100 + 20 - c.getY())
            break
        else:
            shape.move(0, dy)

        update(50)
        sleep(0.02)

    print("click again to quit")
    win.getMouse()
    win.close()
fallingBall()

#Simulate elasticity in the ball above. When the ball hits a side or the bottom of the window, the ball should contract. When it bounces up, have it expand
def fallingBallWithElasticity():
    win = GraphWin("Falling Ball", 400, 400)
    win.setCoords(-100, -100, 100, 100)
    
    #incase you want to move arround (chaning x will throw it in that direction)
    windowTop_YCord = 100
    ballOnXCord = 0
    windowBottom = -100

    radius = 20
    shape = Circle(Point(ballOnXCord, windowTop_YCord-radius), radius)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    velocity = 0
    gravity = -9.8
    pxPerMtr = 10
    dt = 0.05

    normalRadius = 20
    minRadius = 15
    maxRadius = 25
    energyLoss = 1.37
    isContracting = False
    isExpanding = False

    for i in range(1000):
        print(velocity)

        velocity += gravity * dt
        dy = velocity * dt * pxPerMtr

        c = shape.getCenter()
        newY = c.getY() + dy

        if newY - radius < windowBottom+1:
            shape.move(0, windowBottom + radius - c.getY())
            velocity = abs(velocity) * energyLoss
            isContracting = True
            isExpanding = False

        elif isContracting:
            print("contracting")
            radius = max(minRadius, radius - 1)
            shape.undraw()
            shape = Circle(c, radius)
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            if radius <= minRadius:
                print("done contracting")
                isContracting = False
                isExpanding = True

        elif isExpanding:
            print("expanding")
            radius = min(maxRadius, radius + 1)
            shape.undraw()
            shape = Circle(c, radius)
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            if radius >= maxRadius:
                print("done expanding")
                isExpanding = False
                radius = normalRadius

        elif velocity == 0:
            radius = normalRadius
            print("stopped velocity 0")
            break

        else:
            shape.move(ballOnXCord, dy)

        update(50)
        sleep(0.02)
    print("click again to quit")
    win.getMouse()
    win.close()
fallingBallWithElasticity()



#examples from class
"""
class Tree:
    def __init__(self, win, x, y):
        #Inicialize a tree with a triangular top and a rectangular trunk
        self.win = win
        self.x = x
        self.y = y

        #create the top part (triangle)
        self.triangle = Polygon(
            Point(x-40,y),
            Point(x+40,y),
            Point(x,y-80)
        )

        self.triangle.setFill("green")

        #create the trunk (rectangle)
        self.trunk = Rectangle(
            Point(x-15,y),
            Point(x+15,y+30)
        )
        self.trunk.setFill("brown")

    def draw(self):
        #Draw The Tree
        self.triangle.draw(self.win)
        self.trunk.draw(self.win)

#from Tree import *
def drawForest():
    print(" ")
drawForest()


class Square:
    def __init__(self,win,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.win = win
        self.square = self.Rectangle = Rectangle(self.p1,self.p2)

    def draw(self):
        self.square.draw(self.win)
    def move(self,dx,dy):
        self.square.move(dx,dy)
#from Square import *
def drawSquareMoving():
    win = GraphWin("Moving Square", 1300,1300)
    x1 = 50
    y1 = 50
    x2 = 100
    y2 = 100

    square = Square(win, Point(x1,y1), Point(x2,y2))
    square.draw()

    for dx,dy in zip(range(0,45,1),range(0,45,1)):
        time.sleep(0.05)
        square.move(dx,dy)
        if dx == 44:
            for dx,dy in zip(range(-45,0,1),range(-45,0,1)):
                time.sleep(0.05)
                square.move(dx,dy)
            break
    input("Press enter to quit")
"""