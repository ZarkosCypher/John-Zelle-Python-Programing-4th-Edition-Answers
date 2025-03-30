import math as m
from graphics import *

def main1():
    def lyrics(animal: str,sound: str):
        print("Old MacDonal had a farm, Ee-igh, Ee-igh, Oh!")
        print("And on that farm he had a", animal,"Ee-igh, Ee-igh, Oh!")
        print("with a", sound, sound, "here and a ", sound, sound, "there.")
        print("Here a", sound, "there a", sound, "everywhere a", sound, sound, ".")
        print("Old MicDonald had a farm, Ee-ih, Ee-ig, Oh!")
        print(" ")
    lyrics("pig","oink")
    lyrics("cow","moo")
    lyrics("cat","meow")
    lyrics("dog","woof")
    lyrics("duck","quack")
main1()

def main2():
    def ants(verse):
        verse1 = "The ants go marching one by one, hurrah! hurrah!"
        print(verse1)
        print(verse1)
        print("The ants go marching one by one,")
        print(verse)
        print("and they all go marching down...")
        print("In the ground...")
        print("To get out...")
        print("Of the rain.")
        print("Boom! Boom! Boom!")
    ants("The little one stops to suck his thumb,")
    ants("The little one stops to tie his shoe,")
main2()

def main3():
    def sphereArea(radius):
        area = 4*m.pi*radius**2
        return area
    def sphereVolume(radius):
        volume = (4/3)*m.pi*radius**3
        return volume
    print(sphereArea(10))
    print(sphereVolume(10))
main3()

def main4():

    def sumN(n):
        for i in range(n):
            total = n * (n + 1) // 2
        print("The sum / n! is", total)
    def sumNCubes(n):
        for i in range(n):
            total = (n * (n + 1) // 2) ** 2
        print("The natural numbers summed and cubed is ", total)

    sumN(5)
    sumNCubes(3)
main4()

def main5():
    def area(diameter):
        return m.pi * (diameter/2)**2
    def costPerSQinch(area, cost):
        return cost / area
    print(area(10))
    print(costPerSQinch(area(10), 20))
main5()

def main6():
    def square(x):
        return x ** 2
    def distance(p1, p2):
        dist = m.sqrt(square(p2.getX()-p1.getX()) + square(p2.getY()-p1.getY()))
        return dist

    win = GraphWin("Draw a Triangle")
    win.setCoords(0,0,10,10)
    message = Text(Point(5,0.5), "Click on 3 points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText("the perimiter is: {0:0.2f}".format(perim))

    win.getMouse()
    win.close()

    a = distance(p1,p2)
    b = distance(p2,p3)
    c = distance(p3,p1)

    def triangleArea(a,b,c):
        s = (a + b + c) / 2
        return m.sqrt(s * (s - a) * (s - b) * (s - c))
    print("the area is :",triangleArea(a,b,c))
main6()

def main7():
    def fibinachi(n):
        num1 = 0
        num2 = 1
        for i in range(2, n + 1):
            num1, num2 = num2, num1 + num2
        print("the fibinachi number is", num2)
    fibinachi(10)
main7()

def main8():
    #this one made no sence so this is my understanding of it!
    def guessthing(xvalue,times):
        guess = xvalue / 2
        for i in range(times):
            guess = (guess + xvalue / guess) / 2
        print("the program computed:", guess, " and the diffrence from the real answer is:", (guess - m.sqrt(xvalue)))
    guessthing(10,50)
main8()

def main9():
    #center: point on window
    #size: how big in int
    #win: where it is being drawn

    def drawFace(center, size, win):
        headRad = size
        eyeRad =  size // 5
        eyeX = size // 3
        eyeY = size // 3
        mouthWidth = size // 2
        mouthHight = size //4

        head = Circle(center, headRad)
        head.setFill("white")
        head.setOutline("black")
        head.draw(win)

        leftEyePos = Point(center.getX() - eyeX, center.getY() - eyeY)
        leftEye = Circle(leftEyePos,eyeRad)
        leftEye.setFill("black")
        leftEye.draw(win)

        rightEyePos = Point(center.getX() + eyeX, center.getY() - eyeY)
        rightEye = Circle(rightEyePos,eyeRad)
        rightEye.setFill("black")
        rightEye.draw(win)
        
        mouthLeft = Point(center.getX() - mouthWidth//2, center.getY() + mouthHight)
        mouthRight = Point(center.getX() + mouthWidth//2, center.getY() + mouthHight)
        mouth =  Oval(mouthLeft,mouthRight)
        mouth.setFill("back")
        mouth.draw(win)
        
        #this one is more of an open mouthed one if that works better
        #mouth_top = Point(center.getX() - mouthWidth // 2, center.getY() + mouthWidth // 2)
        #mouth_bottom = Point(center.getX() + mouthWidth // 2, center.getY() + mouthHight * 2)
        #mouth = Oval(mouth_top, mouth_bottom)
        #mouth.setFill("red")
        #mouth.draw(win)

    x= 200
    y= 200
    centerPoint = Point(x,y)
    window = GraphWin("face", 400,400)
    drawFace(centerPoint, 100, window)
    drawFace(centerPoint, 200, window)
    drawFace(centerPoint, 150, window)

    window.getMouse()
    window.close()
main9()

def main10():
    def drawFace(center, size, win):
        headRad = size
        eyeRad = size // 5
        eyeX = size // 3
        eyeY = size // 3
        mouthWidth = size // 2
        mouthHight = size // 4

        head = Circle(center, headRad)
        head.setFill("white")
        head.setOutline("black")
        head.draw(win)

        leftEyePos = Point(center.getX() - eyeX, center.getY() - eyeY)
        leftEye = Circle(leftEyePos, eyeRad)
        leftEye.setFill("black")
        leftEye.draw(win)

        rightEyePos = Point(center.getX() + eyeX, center.getY() - eyeY)
        rightEye = Circle(rightEyePos, eyeRad)
        rightEye.setFill("black")
        rightEye.draw(win)

        mouthLeft = Point(center.getX() - mouthWidth // 2, center.getY() + mouthHight)
        mouthRight = Point(center.getX() + mouthWidth // 2, center.getY() + mouthHight)
        mouth = Oval(mouthLeft, mouthRight)
        mouth.setFill("back")
        mouth.draw(win)
    
    def anonymousizer():
        image = input("enter the image file name including its file extention: ")
        img = Image(Point(0,0),image)
        width = img.getWidth()
        height = img.getHeight()
        win = GraphWin("photo anon", width,height)
        img.move(width//2,height//2)#center 
        img.draw(win)
        
        faces = input("how many faces should be blocked?: ")
        
        for i in range(faces):
            print("face",i+1)
            print("click the center of the face to block!")
            center = win.getMouse()
            
            print("click the edge of the face to block!")
            edge = win.getMouse()
            
            dx =  abs(center.getX() - edge.getX())
            dy =  abs(center.getY() - edge.getY())
            size = int((dx**2 + dy**2)/2)
            
            drawFace(center,size,win)

        win.getMouse()
        win.close()
    
    anonymousizer()
main10()

def main11():
    def moveTo(shape,newCenter):
        currentCenter =  shape.getCenter()
        dx = newCenter.getX() - currentCenter.getX()
        dy = newCenter.getY() - currentCenter.getY()
        shape.move(dx,dy)

    win = GraphWin("Move", 400, 400)

    firstCenter = Point(200, 200)
    circle = Circle(firstCenter, 50)
    circle.setFill("black")
    circle.draw(win)

    for i in range(10):
        print("Click where to move the circle" )
        newCenter = win.getMouse()
        moveTo(circle, newCenter)

    win.getMouse()
    win.close()
main11()


