import math as m
from graphics import *
from time import sleep

def main1():
    while True:
        try:
            hours = float(input("Enter how many hours where worked: "))
            if hours < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    while True:
        try:
            wage = float(input("Enter your wage: "))
            if wage < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")
    if hours == 0 or wage == 0:
        print("sorry to hear you did not make any money, ------------------------------------------------------------------------------------------------------------------ it would be kind of common sence to know that you did not make anything tho, since you ya know have 0 hours worked or a wage of 0 an hour, but anywasy")
        pay = 0
    if hours <= 40:
        pay = hours * wage
    else:
        regularPay = 40 * wage
        overtime = hours - 40
        overtimepay = (overtime * (wage*1.5))
        pay = regularPay + overtimepay
        print("Total pay is", pay, "with you working", overtime, " hours overtime", "earning you",overtimepay,"in overtime pay")
    print("Total pay is", pay, "you did not earn overtime")
main1()

def main2():
    while True:
        try:
            grade = float(input("Enter the grade as a 0-5: "))
            if grade < 0 or grade > 5:
                print("enter a number between 0 and 5")
                continue
            break
        except ValueError:
            print("enter a number")
    if grade == 5:
        print("A")
    elif grade == 4:
        print("B")
    elif grade == 3:
        print("C")
    elif grade == 2:
        print("D")
    else:
        print("F")
main2()

def main3():
    while True:
        try:
            grade = float(input("Enter the grade as a 0-100: "))
            if grade < 0 or grade > 100:
                print("enter a number between 0 and 100")
                continue
            break
        except ValueError:
            print("enter a number")
    if 90 <= grade:
        print("A")
    elif 80 <= grade <= 89:
        print("B")
    elif 70 <= grade <= 79:
        print("C")
    elif 60 <= grade <= 69:
        print("D")
    else:
        print("F")
main3()

def main4():
    while True:
        try:
            creds = float(input("Enter the Credits you have: "))
            if creds < 0 :
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")
    if creds < 7:
        print("you are a Freshman")
    elif 7 <= creds < 16:
        print("you are a Sophomore")
    elif 16 <= creds < 26:
        print("you are a Junior")
    else:
        print("you are a Senior")
main4()

def main5():
    while True:
        try:
            weight = float(input("Enter the weight you have in lbs: "))
            if weight < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    while True:
        try:
            height = float(input("Enter the height you have in inches: "))
            if height < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    BMI = (weight * 703)/(height ** 2)
    if BMI < 19:
        print("you are underweight!")
    elif 19 <= BMI <= 25:
        print("you are in a health weight range look at you go!")
    else:
        print("you are overweight, go on a diet...")
main5()

def main6():
    while True:
        try:
            speedLimit = float(input("Enter the speed limit: "))
            if speedLimit < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")
    while True:
        try:
            clockSpeed = float(input("Enter the clock speed: "))
            if clockSpeed < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    speedingPenelty = 50
    overLimitPeneltyEachMileOver = 5
    over90Penelty = 200
    fine = 0
    
    if clockSpeed > 90:
        fine = fine + over90Penelty
    if clockSpeed > speedLimit:
        milesOver = clockSpeed - speedLimit
        fine = fine + (speedingPenelty + (milesOver * overLimitPeneltyEachMileOver))
        print("Illigal driving fines due $",fine)
    else:
        print("Everything is Legal")
main6()

def main7():

    while True:
        while True:
            try:
                startTimeHours = int(input("Enter the start Time Hour in 24 hour format: "))
                if startTimeHours < 0 or startTimeHours > 24:
                    print("enter a number over 0 and under 24")
                    continue
                break
            except ValueError:
                print("enter a number")
        while True:
            try:
                startTimeMinets = int(input("Enter the start Time Min: "))
                if startTimeMinets < 0 or startTimeMinets > 60 :
                    print("enter a number over 0")
                    continue
                break
            except ValueError:
                print("enter a number")
        print("The time you entered is:",startTimeHours,":",startTimeMinets)
        yOrN = str(input("is this correct? (Yes/No you can hit anything to restart)"))
        if yOrN == "Yes" or yOrN == "yes":
            break
        else:
            print("okay, you will be prompted to re-enter")

    while True:
        while True:
            try:
                endTimeHours = int(input("Enter the end Time Hour in 24 hour format: "))
                if endTimeHours < 0 or endTimeHours > 24:
                    print("enter a number over 0")
                    continue
                break
            except ValueError:
                print("enter a number")
        while True:
            try:
                endTimeMinets = int(input("Enter the end Time Min: "))
                if endTimeMinets < 0 or endTimeMinets > 60:
                    print("enter a number over 0")
                    continue
                break
            except ValueError:
                print("enter a number")
        print("The time you entered is:", startTimeHours, ":", startTimeMinets)
        yOrN = str(input("is this correct? (Yes/No you can hit anything to restart)"))
        if yOrN == "Yes" or yOrN == "yes":
            break
        else:
            print("okay, you will be prompted to re-enter")

    regularRate = 12.50
    late9PMrate = 11.50
    lateRateStart = 21 # 9:00Pm in regular non US time

    #min convertion for easy math
    startMin = startTimeHours * 60 + startTimeMinets
    endMin = endTimeHours * 60 + endTimeMinets
    ninePM = late9PMrate * 60

    if endMin <= ninePM:
        totalMin = endMin - startMin
        cost = (totalMin / 60)*regularRate
    elif startMin >= ninePM:
        totalMin = endMin - startMin
        cost = (totalMin / 60)*late9PMrate
    else:
        minBef9 = ninePM - startMin
        costBef9 = (minBef9 / 60)*regularRate

        minAft9 = endMin - ninePM
        costAft9 =  (minAft9 / 60)* late9PMrate

        cost = costAft9 + costBef9
    print("The bill is ", cost)

main7()

def main8():
    while True:
        try:
            age = float(input("Enter your age: "))
            if age < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    while True:
        try:
            yearCitizen = float(input("Enter your years of citizenship: "))
            if yearCitizen < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    #eligability as a senate and house

    if age >= 25:
        if yearCitizen >= 7:
            print("eligable for represenative")
        else:
            print("your old enough but have not been a citizen long enough")
    elif age >= 30:
        if yearCitizen >= 9:
            print("eligable for Senate")
        else:
            print("your old enough but have not been a citizen long enough")
    else:
        print("your not eligable for any position")

main8()

def main9():
    while True:
        try:
            year = int(input("Enter a year between 1982 and 2048 to find out what day easter is: "))
            if year < 1982 or year > 2048:
                print("enter a year between 1982 - 2048")
                continue
            break
        except ValueError:
            print("enter a number")

    a = year%19
    b = year%4
    c = year%7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7

    if (d + e) > 9:
        print("easter falls on April", (d+e-9))
    else:
        print("eater will be on March", (22+d+e))
main9()

def main10():
    while True:
        try:
            year = int(input("Enter a year between 1982 and 2048 to find out what day easter is: "))
            if year < 1900 or year > 2099:
                print("enter a year between 1900 - 2099")
                continue
            break
        except ValueError:
            print("enter a number")

    a = year%19
    b = year%4
    c = year%7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7

    if year == 1954 or 1981 or 2049 or 2076:
        d = d -7
        if (d + e) > 9:
            print("easter falls on April", (d+e-9))
        else:
            print("eater will be on March", (22+d+e))
    else:
        if (d + e) > 9:
            print("easter falls on April", (d+e-9))
        else:
            print("eater will be on March", (22+d+e))
main10()

def main11():
    while True:
        try:
            year = int(input("Enter a year: "))
            if year < 0:
                print("enter a year over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("is leap year")
            else:
                print("is not leap year")
        else:
           print("is leap year year")
    else:
        print("it is not leap year")

main11()

def main12():
    date = str(input("Enter a date in the format month/day/year: "))

    monthS, dayS, yearS = date.split("/")
    month = int(monthS)
    day = int(dayS)
    year = int(yearS)

    #months days
    #1 31
    #2 28 or 29
    #3 31
    #4 30
    #5 31
    #6 30
    #7 31
    #8 31
    #9 30
    #10 31
    #11 30
    #12 31

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leapyear = True
            else:
                leapyear = False
        else:
            leapyear = True
    else:
        leapyear = False

    if month > 12:
        print("month is wrong enter a month 1-12")
    else:
        if day > 31:
            print("date is wrong dates cant be over 31")
        elif month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
            print("month 4 6 9 and 11 dont have more than 30 days")
        elif month == 2 and leapyear and day > 29:
            print("month 2 does not have more tha 29 days on a leap year")
        elif month == 2 and not leapyear and day > 28:
            print("month 2 does not have more than 28 days on a non leap year")
        else:
            print("date is correct")

main12()

def main13():
    date = str(input("Enter a date in the format month/day/year: "))

    monthS, dayS, yearS = date.split("/")
    month = int(monthS)
    day = int(dayS)
    year = int(yearS)

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leapyear = True
            else:
                leapyear = False
        else:
            leapyear = True
    else:
        leapyear = False

    if month > 12:
        print("month is wrong enter a month 1-12")
    else:
        if day > 31:
            print("date is wrong dates cant be over 31")
        elif month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
            print("month 4 6 9 and 11 dont have more than 30 days")
        elif month == 2 and leapyear and day > 29:
            print("month 2 does not have more tha 29 days on a leap year")
        elif month == 2 and not leapyear and day > 28:
            print("month 2 does not have more than 28 days on a non leap year")
        else:
            print("date is correct")

    dayNum = 31*(month - 1)+day
    if month == 2:
        if leapyear:
            dayNum = dayNum - (4 * (month) + 23)//10+1
        else:
            dayNum = dayNum - (4 *(month) + 23)//10
    else:
        dayNum = 31 * (month - 1) + day
    print("the numeric date is", dayNum)
main13()

def main14():
    #this one is from the original i did have another version but was not sure what one to use since chapter 4 is not graded yet
    win = GraphWin("window", 500, 500)
    win.setCoords(-100, -100, 100, 100)
    print("input data in to the terminal for results on a circles intersection")
    print("this program calculates the intersection of a circle with a horizontal line")
    r = float(input("what is the radious of the circle?: "))
    circle = Circle(Point(0, 0), r)
    circle.setOutline("black")
    circle.draw(win)

    while True:
        try:
            y = float(input("Where does the line cross on the y axes?: "))
            if (r < y) or (r < -y):
                print("enter a number that is lower than", r, "and above", -r)
                continue
            break
        except ValueError:
            print("enter a number")

    line = Line(Point(-r-10, y), Point(r+10, y))
    line.setOutline("green")
    line.setWidth(2)
    line.draw(win)

    x = m.sqrt(r ** 2 - y ** 2)
    intersection = (-x, y), (x, y)
    print("The intersection is at ", -x,y, "and", x,y)

    intp1 = Circle(Point(-x, y), 0.5)
    intp2 = Circle(Point(x, y), 0.5)
    intp1.setFill("red")
    intp1.draw(win)
    intp2.setFill("red")
    intp2.draw(win)

    print("click again to quit")
    win.getMouse()
    win.close()
main14()

def main15():
    win = GraphWin("window", 400, 400)
    win.setCoords(-100, -100, 100, 100)
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

    midx, midy = (x1 + x2) / 2, (y1 + y2) / 2
    point = Circle(Point(midx, midy), 0.5)
    point.setFill("cyan")
    point.draw(win)

    if (x2-x1) == 0:
        slope = "Vertical"
    if (y2-y1) == 0:
        slope = "Horizontal"
    else:
        slope = (y2 - y1) / (x2 - x1)
    lenght = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("the lenght is ", lenght)
    print("the slope is ", slope)

    print("click again to quit")
    win.getMouse()
    win.close()
main15()

def main16():
    win = GraphWin("window", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    def circle(r,color):
        c = Circle(Point(0,0),r)
        c.setOutline("Black")
        c.setFill(color)
        c.setWidth(1)
        c.draw(win)
    circle(6,"black")
    circle(5,"white")
    circle(4,"black")
    circle(3,"blue")
    circle(2,"red")
    circle(1,"yellow")

    for i in range (5):
        arrow = win.getMouse()
        x = arrow.getX()
        y = arrow.getY()
        z = m.sqrt(x**2 + y**2)
        total = 0
        if 5 >= z > 4:
            point = 1
            total = point + total
        elif 4 >= z > 3:
            point = 3
            total = point + total
        elif 3 >= z > 2:
            point = 5
            total = point + total
        elif 2 >= z > 1:
            point = 7
            total = point + total
        elif 1 > z:
            point = 9
            total = point + total
        else:
            point = 0
            print("You missed!")
        print("Points:",point,"Total:",total)

    print("click again to quit")
    win.getMouse()
    win.close()
main16()

def main17():
    win = GraphWin("Bouncing Ball", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    shape = Circle(Point(0, -80), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    dx = 1
    dy = 1

    for i in range(10000):
        #update(50)
        sleep(0.02)
        c = shape.getCenter()
        if c.getX() > 80:
            dx = -1
        elif c.getX() < -80:
            dx = 1
        elif c.getY() > 80:
            dy = -1
        elif c.getY() < -80:
            dy = 1
        shape.move(dx, dy)

main17()

def main18():
    #using Chapter 3 Program 1
    print("This calculates the volume and surface area from a spheres radius.")
    while True:
        try:
            radius = float(input("Enter the radius: "))
            if radius < 0:
                print("enter a number over 0")
                continue
            break
        except ValueError:
            print("enter a number")

    volume = (4/3) * m.pi * radius ** 3
    area = 4 * m.pi * radius ** 2
    print("The volume is,", volume, "and the area is,", area)

main18()
