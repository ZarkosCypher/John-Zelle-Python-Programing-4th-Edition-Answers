import math
from graphics import *

def main0():
    win = GraphWin()
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    win.close()
main0()

def main1():
    win = GraphWin("window", 500, 500)
    print("click arround to draw 10 squares")
    for i in range(10):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    print("click again to quit")
    win.getMouse()
    win.close()
main1()

def main2():
    win = GraphWin("window", 500, 500)
    print("heres a picture!")
    def circles(color: str, size: int):
        shape = Circle(Point(100, 100), size)
        shape.setOutline(color)
        shape.setFill(color)
        shape.draw(win)

    circles("black", 60)
    circles("white", 50)
    circles("black", 40)
    circles("blue", 30)
    circles("red", 20)
    circles("yellow", 10)
    print("click again to quit")
    win.getMouse()
    win.close()
main2()

def main3():
    win = GraphWin("window", 500, 500)
    print("heres a picture")
    def face(x: int, y: int , size: int, color: str):
        shape = Circle(Point(x, y), size)
        shape.setOutline(color)
        shape.setFill(color)
        shape.draw(win)
    face(200, 200, 100, "black") #head
    face(150, 150, 20, "red") # eye 1 left?
    face(250, 150, 20, "red") # eye 2 right?
    face(200,200, 10, "pink") #nose
    print("click again to quit")
    win.getMouse()
    win.close()
main3()

def main4():
    win = GraphWin("window", 500, 500)
    print("heres a picture")
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
    #snowman
    balls(100,100,20,"white","black")#head
    balls(100,150,30,"white","black")#body
    balls(100,220,40,"white","black")#feet???
    #snowman face
    balls(90,100,5,"black","black")
    balls(110,100,5,"black","black")
    balls(100,113,5,"black","black")
    #snowman buttons
    balls(100,145,5,"black","black")
    balls(100,170,5,"black","black")
    balls(100,200,5,"black","black")
    #tree
    square(300,165,20,90,"brown","black")#stem of a tree
    square(300,190,70,10,"green","black")#bottom leaves
    square(300,160,60,10,"green","black")#
    square(300,130,50,10,"green","black")#
    square(300,100,40,10,"green","black")#
    square(300,70,30,10,"green","black")#top leaves

    print("click again to quit")
    win.getMouse()
    win.close()
main4()

def main5():
    win = GraphWin("window", 500, 500)
    print("heres a picture")
    def balls(x: int, y: int):
        shape = Circle(Point(x, y), 10)
        shape.setOutline("black")
        shape.setFill("white")
        shape.draw(win)

    def die(x: int, y: int):
        shape = Rectangle(Point(x - 50, y - 50), Point(x + 50, y + 50))
        shape.setOutline("black")
        shape.setFill("red")
        shape.draw(win)

    die(100,100)#1
    balls(100,100)#center

    die(210,100)#2
    balls(210-25,100+25)#bottom
    balls(210+25,100-25)#top

    die(320, 100)#3
    balls(320-25,100+25)#bottom
    balls(320+25,100-25)#top
    balls(320,100)#middle

    die(100, 210)#4
    balls(100-25,210+25)#botom left
    balls(100+25,210-25)#top right
    balls(100+25,210+25)#bottom right
    balls(100-25,210-25)#top left

    die(210, 210)#5
    balls(210-25,210+25)#bottom left
    balls(210+25,210-25)#top right
    balls(210+25,210+25)#bottom right
    balls(210-25,210-25)#top left
    balls(210,210)#center

    #extra one for fun! if you want removed just delete to the comment that says delete to here!
    die(320, 210)#6
    balls(320-25,210+25)#bottom left
    balls(320+25,210-25)#top right
    balls(320+25,210+25)#bottom right
    balls(320-25,210-25)#top left
    balls(320-25,210)#center left
    balls(320+25,210)#center right
    #delete to here!
    print("click again to quit")
    win.getMouse()
    win.close()
main5()

def main6():
    win = GraphWin("window", 500, 500)
    win.setCoords(0, 0, 4, 4)  # Set coordinate system
    print("follow the instructions on screen")
    # text on screen
    Text(Point(1, 3.5), "Principal ($):").draw(win)
    Text(Point(1, 3), "Annual Interest Rate (APR):").draw(win)

    # Entry input fields
    principal_entry = Entry(Point(2.5, 3.5), 10)
    principal_entry.setText("0.0")  # Default
    principal_entry.draw(win)

    apr_entry = Entry(Point(2.5, 3), 10)
    apr_entry.setText("0.0")  # Default 
    apr_entry.draw(win)

    # calculate button
    button = Text(Point(2, 2.5), "Calculate")
    button.draw(win)
    Rectangle(Point(1.5, 2.3), Point(2.5, 2.7)).draw(win)  # Button 

    win.getMouse() 

    # Retrieve values from entries
    principal = float(principal_entry.getText())
    apr = float(apr_entry.getText())

    #value for 5 years
    years = 5
    for i in range(years):
        principal = principal * (1 + apr)

    # Display result
    Text(Point(2, 1.5), f"Future Value: ${principal:.2f}").draw(win)

    win.getMouse()  
    win.close()
main6()

def main7():
    win = GraphWin("window", 400, 400)
    win.setCoords(-10,-10,10,10)
    print("input data in to the terminal for results on a circles intersection")
    print("this program calculates the intersection of a circle with a horizontal line")
    r = int(input("what is the radious of the circle?: "))
    y = float(input("Where does the line cross on the y axes?: "))

    circle = Circle(Point(0,0),r)
    circle.setOutline("black")
    circle.draw(win)

    line = Line(Point(-10,y),Point(10,y))
    line.setOutline("green")
    line.setWidth(2)
    line.draw(win)

    x = math.sqrt(r**2 - y**2)
    intersection = (-x,y),(x,y)
    print("The intersection is at ",-x,x)

    intp1 = Circle(Point(-x,y),0.5)
    intp2 = Circle(Point(x,y),0.5)
    intp1.setFill("red")
    intp1.draw(win)
    intp2.setFill("red")
    intp2.draw(win)

    print("click again to quit")
    win.getMouse()
    win.close()
main7()

def main8():
    win = GraphWin("window", 400, 400)
    win.setCoords(-10,-10,10,10)
    print("click 2 points to find the center of the line")
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    line = Line(point1, point2)
    line.setWidth(2)
    line.draw(win)

    midx, midy = (x1 + x2)/2, (y1 + y2)/2
    point = Circle(Point(midx,midy),0.5)
    point.setFill("cyan")
    point.draw(win)

    lenght = math.sqrt((x2 -x1)**2 + (y2 - y1)**2)
    slope = (y2 - y1)/(x2 - x1)

    print("the lenght is ",lenght)
    print("the slope is ", slope)

    print("click again to quit")
    win.getMouse()
    win.close()
main8()

def main9():
    win = GraphWin("window", 400, 400)
    win.setCoords(-10,-10,10,10)
    print("click 2 oposing points to draw a rectangle")
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = (point1.getX())
    x2 = (point2.getX())
    y1 = (point1.getY())
    y2 = (point2.getY())

    rect = Rectangle(point1, point2)
    rect.draw(win)

    area = ((x2-x1)*(y2-y1))
    perimiter = 2*((x2-x1)+(y2-y1))
    print("the area is ",abs(area), " and the absperimiter is ",abs(perimiter))

    print("click again to quit")
    win.getMouse()
    win.close()
main9()

def main10():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    print("click 3 points to draw a triangle")
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    x1 = (point1.getX())
    x2 = (point2.getX())
    x3 = (point3.getX())
    y1 = (point1.getY())
    y2 = (point2.getY())
    y3 = (point3.getY())

    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    c = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    perimiter = a + b + c

    s = perimiter/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point1)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)

    print("the area is ",abs(area)," the perimiter is ",abs(perimiter))

    print("click again to quit")
    win.getMouse()
    win.close()
main10()

def main11():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    print("To draw your house cick from right to left for the first bace of the house, then click inside the bace to build a door up tp the hight, then click to buld a window, then click to build a roof!")

    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    rect = Rectangle(point1,point2)
    rect.draw(win)

    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()

    rectWidth = x2 - x1
    door = Rectangle(Point(x3-(1/10 * rectWidth),y1),Point(x3+(1/10 * rectWidth),y3))
    door.draw(win)

    point4 = win.getMouse()
    x4 = point4.getX()
    y4 = point4.getY()

    winWidth = 1/20 * rectWidth
    window = Rectangle(Point((x4-winWidth), (y4-winWidth)), Point((x4+winWidth), (y4+winWidth)))
    window.draw(win)

    point5 = win.getMouse()
    line1 = Line(point2, point5)
    line2 = Line(point5, Point(x1,y2))
    line1.draw(win)
    line2.draw(win)

    print("click again to quit")
    win.getMouse()
    win.close()
main11()

def main12():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    print("To build your face you need to click the center of where you want your head to be, then click where you want your head to rach out to, then click how big you want your nose to be from the center(click on the left side), then click where you want your lefy eye to be, then clic where you want your mouth to be located")

    point1 = win.getMouse() # center head and nose
    x1 = point1.getX()
    y1 = point1.getY()

    point2 = win.getMouse() # radius of the head
    x2 = point2.getX()
    y2 = point2.getY()

    headR = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    head = Circle(Point(x1, y1), headR)
    head.draw(win)

    point3 = win.getMouse() # lower left of the icosalise triangle
    x3 = point3.getX()
    y3 = point3.getY()

    x3r = 2 * x1 - x3
    nose = Polygon(Point(x1, y1), Point(x3, y3), Point(x3r, y3))
    nose.draw(win)

    point4 = win.getMouse() # center of the left eye duplicating it to the right making it 1/10th of the head
    x4 = point4.getX()
    y4 = point4.getY()

    eyeRad = headR / 10
    leftEye = Circle(Point(x4, y4), eyeRad)
    rightEye = Circle(Point(2 * x1 - x4, y4), eyeRad)
    leftEye.draw(win)
    rightEye.draw(win)

    point5 = win.getMouse() # lower left of the oval, centared horizontaly with the same radious as the eyes
    x5 = point5.getX()
    y5 = point5.getY()

    mouthWidth = abs(2 * (x1 - x5))
    mouthHeight = eyeRad
    mouthCenterX = x1
    mouthCenterY = y5 + mouthHeight / 2
    mouth = Oval(Point(mouthCenterX - mouthWidth / 2,mouthCenterY - mouthHeight / 2),Point(mouthCenterX + mouthWidth / 2, mouthCenterY + mouthHeight / 2))
    mouth.draw(win)

    print("click again to quit")
    win.getMouse()
    win.close()
main12()