import math as m
from graphics import *
from time import sleep

def main1():
    initialInvestment = 1
    investment = initialInvestment
    investRate = 0.1 #convert % so 100 = 1 and 50 = 0.5
    i = 0
    while investment < (initialInvestment * 2):
        investment = investment + (investment * investRate)
        print(investment)
        i = i +1
    print(f"done it has doubled after {i} runs")
main1()

def main2():
    def syr(x):
        while x != 1:
            print(x)
            if x%2 == 0:
                x = x//2 #is even
            else:
                x = 3*x+1 #is odd

    while True:
        try:
            number = int(input("enter a number: "))
            if number < 1:
                print("Enter a number above 0")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    syr(number)
    print("Program is done running")

main2()

def main3():
    while True:
        try:
            number = int(input("enter a number: "))
            if number <= 2:
                print("Enter a number above 2")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    def prime(n):
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                return False
        return True

    if prime(number):
        print(number,"is prime")
    else:
        print(number,"is not prime")
main3()

def main4():
    while True:
        try:
            number = int(input("enter a number: "))
            if number <= 2:
                print("Enter a number above 2")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    def prime(n):
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                return False
        return True

    primeList = []
    for numb in range(2, number + 1):
        if prime(numb):
            primeList.append(numb)

    if primeList:
        print(f"Prime numbers to {number} are: {primeList}")
        print(f"Total prime numbers found: {len(primeList)}")
    else:
        print("no prime numbers found")

main4()

def main5():
    while True:
        try:
            number = int(input("enter a number: "))
            if number <= 2:
                print("Enter a number above 2")
                continue
            if number % 2 != 0:
                print("Enter an even number")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    def prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, number):
        if prime(i):
            j = number - i
            if prime(j):
                print(f"{number} = {i} + {j}")
                break
main5()

def main6():
    while True:
        try:
            m = int(input("enter a number: "))
            if m <= 0:
                print("Enter a number above 0")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    while True:
        try:
            n = int(input("enter a number: "))
            if n <= 0:
                print("Enter a number above 0")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    origM = m
    origN = n

    while m != 0:
        n, m = m, n % m
        #/\ I have no idea what this does i just copied it from the book
    print(f"the GCD of {origM} and {origN} is {n}")
main6()

def main7():
    while True:
        try:
            startingOdometer = int(input("enter starting odomiter: "))
            if startingOdometer < 0:
                print("Enter a number above 0")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    leg = []
    totalMiles = 0
    totalGas = 0

    print("Enter data for each leg or (enter 2 times to finish)")
    while True:
        odometerInput = input("Current odemeter reading: ")
        if odometerInput == "":
            break

        gasInput = input("Gallons of gas used: ")
        if gasInput == "":
            break

        try:
            currentOdometer = float(odometerInput)
            gas = float(gasInput)

            if currentOdometer < startingOdometer:
                print("Odometer needs to be more than the last reading")
                continue
            if gas <= 0:
                print("Gas needs to be positive")
                continue

            miles = currentOdometer - startingOdometer
            leg.append((miles, gas))
            totalMiles += miles
            totalGas += gas
            startingOdometer = currentOdometer

        except ValueError:
            print("Enter valid numbers for both values")
            continue

    if not leg:
       print("No leg entries")
    else:
        print("Fule eficeny report:")
        print("-" * 50)
        for i, (miles, gas) in enumerate(leg, 1):
            mpg = miles / gas
            print(f"Leg: {i} {miles:.1f} miles, {gas:.1f} gallons, {mpg:.1f} MPG")
        totalMPG = totalMiles / totalGas
        print("-" * 50)
        print(f"Total: {totalMiles:.1f} miles, {totalGas:.1f} gallons, {totalMPG:.1f} MPG")
main7()

def main8():
    heatingDay = 0
    coolingDay = 0

    while True:
        try:
            mes = int(input("Enter how many mesumrments you have to input: "))
            if mes < 0:
                print("Enter a number above 0")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    for i in range(mes):
        temp = float(input("Enter the daily average temp: "))
        if temp < 60:
            tempUnder = 60 - temp
            heatingDay += tempUnder
            print(f"Added {tempUnder:.1f} cooling degree days")
        elif temp > 80:
            tempOver = temp - 80
            coolingDay += tempOver
            print(f"Added {tempOver:.1f} heating degree days")
        else:
            print("No degree days added (temp is not over 80 or under 60)")

    print("Total Days")
    print(f"Total Heaating Days: {heatingDay:.1f}")
    print(f"Total Cooling Days: {coolingDay:.1f}")
main8()

def main9():
    win = GraphWin("line plotting", 400,400)
    win.setCoords(0,0,200,200)
    screenX = 0
    screenY = 200

    done = Rectangle(Point(5,5), Point(30,15))
    done.setFill("grey")
    done.draw(win)
    doneLable = Text(Point(17,10), "Done")
    doneLable.draw(win)

    points = []
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXsquared = 0
    n = 0

    print("Click the plots on a graph to find the regression line and clikc done to fininish")

    while True:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        #click in the Done box
        if 5 <= x <= 30 and 5 <= y <= 15:
            break

        point = Circle(Point(x,y),1)
        point.setFill("blue")
        point.draw(win)

        points.append((x,y))
        n += 1
        sumX += x
        sumY += y
        sumXY += x * y
        sumXsquared += x * x

    if n >= 2:
        xBar = sumX / n
        yBar = sumY / n

        numerator = sumXY - n * xBar * yBar
        denominator = sumXsquared - n * xBar * xBar
        m = numerator / denominator

        yLeft = yBar + m * (0 - xBar) #x is left edge at 0
        yRight = yBar + m * (200 - xBar) #x is right edge at 200

        line = Line(Point(screenX,yLeft), Point(screenY, yRight))
        line.setOutline("red")
        line.setWidth(2)
        line.draw(win)

    win.getMouse()
    win.close()
main9()

def main10():
    def convertGray(image):
        width = image.getWidth()
        height = image.getHeight()

        for row in range(height):
            for col in range(width):
                r, g, b = image.getPixel(col,row)

                brightness = int(round(0.299 * r + 0.589 * g + 0.114 * b))
                image.setPixel(col, row, color_rgb(brightness, brightness, brightness))
            win.update()

    file = input("enter the name of the image file (GIF or PMM): ")
    try:
        img = Image(Point(0,0), file)
    except:
        print("Error cant load file, file needs to be GIF or PMM")
        return

    win = GraphWin("Image to grey", img.getWidth(), img.getHeight())
    img.move(img.getWidth()/2,img.getHeight()/2)
    img.draw(win)

    print("click to convert to grey")
    win.getMouse()

    convertGray(img)

    outputFile = input("Name the filename you want to save as: ")
    try:
        img.save(outputFile)
        print(f"Image saved as {outputFile}")
    except:
        print("Error cant save image")

    print("Click window to close")
    win.getMouse()
    win.close()
main10()

def main11():
    def convertNegative(image):
        width = image.getWidth()
        height = image.getHeight()

        for row in range(height):
            for col in range(width):
                r, g, b = image.getPixel(col, row)

                newR = 255 - r
                newG = 255 - g
                newB = 255 - b
                image.setPixel(col, row, color_rgb(newR, newG, newB))
            win.update()

    file = input("enter the name of the image file (GIF or PMM): ")
    try:
        img = Image(Point(0, 0), file)
    except:
        print("Error cant load file, file needs to be GIF or PMM")
        return

    win = GraphWin("Image to grey", img.getWidth(), img.getHeight())
    img.move(img.getWidth() / 2, img.getHeight() / 2)
    img.draw(win)

    print("click to convert to grey")
    win.getMouse()

    convertNegative(img)

    outputFile = input("Name the filename you want to save as: ")
    try:
        img.save(outputFile)
        print(f"Image saved as {outputFile}")
    except:
        print("Error cant save image")

    print("Click window to close")
    win.getMouse()
    win.close()
main11()

def main12():
    def handleKey(k, win):
        if k == "r":
            win.setBackground("pink")
        elif k == "w":
            win.setBackground("white")
        elif k == "g":
            win.setBackground("lightgray")
        elif k == "b":
            win.setBackground("lightblue")

    def handleClick(pt, win):
        entry = Entry(pt, 10)
        entry.draw(win)

        while True:
            key = win.getKey()
            if key == "Return":
                text = entry.getText()
                entry.undraw()
                Text(pt,text).draw()
                break
            elif key == "Escape":
                entry.undraw()
                break
        win.checkMouse()

        entry.undraw()
        Text(pt, entry.getText()).draw(win)
        win.checkMouse()

    win = GraphWin("Click and Type", 400, 400)
    while True:
        key = win.checkKey()
        if key == "q":
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()

main12()

def main13():
    win = GraphWin("Bouncing Ball", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    shape = Circle(Point(0, -80), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    dx = 1
    dy = 1
    speed = 1

    print("hot q to quit and up and down for speed and r g b to swap colors")

    while True:
        key = win.checkKey()
        if key == "q":
            break

        if key == "r":
            shape.setOutline("red")
            shape.setFill("red")
        elif key == "g":
            shape.setOutline("green")
            shape.setFill("green")
        elif key == "b":
            shape.setOutline("blue")
            shape.setFill("blue")

        elif key == "Up":
            speed = min(30,speed + 0.5)
        elif key == "Down":
            speed = max(0.5, speed - 0.5)

        #update(50)
        c = shape.getCenter()
        if c.getX() > 80:
            dx = -abs(dx)
        elif c.getX() < -80:
            dx = abs(dx)
        elif c.getY() > 80:
            dy = -abs(dx)
        elif c.getY() < -80:
            dy = abs(dx)
        shape.move(dx * speed, dy * speed)
        sleep(0.02)
    win.close()
main13()
