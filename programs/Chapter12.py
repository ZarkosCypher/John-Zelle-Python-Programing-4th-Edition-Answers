import math as m
import random
from codecs import replace_errors
from math import *
from button import *
from graphics import *
from gpa1 import Student, makeStudent


def main1():
    # cball1.py
    def main():
        angle = float(input("Enter the launch angle (in degrees): "))
        vel = float(input("Enter the initial velocity (in meters/sec): "))
        h0 = float(input("Enter the initial height (in meters): "))
        time = float(input(
            "Enter the time interval between position calculations: "))

        # convert angle to radians
        theta = radians(angle)

        # set the initial position and velocities in x and y directions
        xpos = 0
        ypos = h0
        xvel = vel * cos(theta)
        yvel = vel * sin(theta)
        
        maxHeight = h0
        
        # loop until the ball hits the ground
        while ypos >= 0.0:
            # calculate position and velocity in time seconds
            xpos = xpos + time * xvel
            yvel1 = yvel - time * 9.8
            ypos = ypos + time * (yvel + yvel1) / 2.0
            yvel = yvel1
            
            if ypos > maxHeight:
                maxHeight = ypos

        print(f"\nDistance traveled: {xpos:0.1f} meters.")
        print(f"max height is {maxHeight:0.1f} Meters")
    main()
main1()

def main2():
    win = GraphWin("avegae calc", 400, 400)

    Text(Point(100,50), "Score 1:").draw(win)
    Text(Point(100,80), "Score 2:").draw(win)
    Text(Point(100,110), "Score 3:").draw(win)

    entry1 = Entry(Point(200, 50), 10)
    entry1.setText("0.0")
    entry1.draw(win)
    entry2 = Entry(Point(200,80), 10)
    entry2.setText("0.0")
    entry2.draw(win)
    entry3 = Entry(Point(200,110),10)
    entry3.setText("0.0")
    entry3.draw(win)

    resultLable = Text(Point(200, 160), "Aveage: ")
    resultLable.draw(win)

    calculateButton = Button(win, Point(150,210), 100, 30, "Calc Average")
    calculateButton.activate()
    quitButton = Button(win, Point(250, 210), 80, 30, "Quit")
    quitButton.activate()

    while True:
        click = win.getMouse()
        if calculateButton.clicked(click):
            try:
                score1 = float(entry1.getText())
                score2 = float(entry2.getText())
                score3 = float(entry3.getText())

                average = (score1+ score2 + score3) / 3

                resultLable.setText(f"Average: {average:.2f}")
            except ValueError:
                resultLable.setText("Error: invalic numbers")
        elif quitButton.clicked(click):
            break
    win.close()

    #def main12re():
    #    print("Average of 3 scores.")
    #    one = float(input("enter score 1: "))
    #    two = float(input("enter score 2: "))
    #    three = float(input("enter score 3: "))
    #    average = (one + two + three) / 3
    #    print("the average is ", average)
    #main12re()
main2()

def main3():
    win = GraphWin("door game", 400, 400)

    Text(Point(200,50), "Click on a door and guess").draw(win)

    door1 = Button(win, Point(100, 150), 80, 30, "Door1")
    door1.activate()
    door2 = Button(win, Point(200, 150), 80, 30, "Door2")
    door2.activate()
    door3 = Button(win, Point(300, 150), 80, 30, "Door3")
    door3.activate()

    quitButton =  Button(win, Point(200,300), 80, 30, "quit")
    quitButton.activate()

    resultLabel = Text(Point(200,100), "")
    resultLabel.draw(win)

    doors = [door1, door2, door3]
    winningDoor = random.choice(doors)

    while True:
        click = win.getMouse()
        if door1.clicked((click)):
            if door1 == winningDoor:
                resultLabel.setText("You win!")
            else:
                resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
        elif door2.clicked((click)):
            if door2 == winningDoor:
                resultLabel.setText("You win!")
            else:
                resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
        elif door3.clicked((click)):
            if door3 == winningDoor:
                resultLabel.setText("You win!")
            else:
                resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
        elif quitButton.clicked(click):
            break

    win.close()

main3()

def main4():
    win = GraphWin("door game", 400, 400)

    Text(Point(200,50), "Click on a door and guess").draw(win)

    door1 = Button(win, Point(100, 150), 80, 30, "Door1")
    door1.activate()
    door2 = Button(win, Point(200, 150), 80, 30, "Door2")
    door2.activate()
    door3 = Button(win, Point(300, 150), 80, 30, "Door3")
    door3.activate()

    quitButton =  Button(win, Point(200,300), 80, 30, "quit")
    quitButton.activate()

    resultLabel = Text(Point(200,100), "")
    resultLabel.draw(win)

    scoreLabel = Text(Point(200,250), "Wins: 0 Losses: 0")
    scoreLabel.draw(win)

    wins = 0
    losses= 0
    doors = [door1, door2, door3]

    while True:
        winningDoor = random.choice(doors)
        resultLabel.setText("")

        while True:
            click = win.getMouse()
            if door1.clicked(click):
                if door1 == winningDoor:
                    resultLabel.setText("You win!")
                    wins += 1
                else:
                    resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
                    losses += 1
                break
            elif door2.clicked(click):
                if door2 == winningDoor:
                    resultLabel.setText("You win!")
                    wins += 1
                else:
                    resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
                    losses += 1
                break
            elif door3.clicked(click):
                if door3 == winningDoor:
                    resultLabel.setText("You win!")
                    wins += 1
                else:
                    resultLabel.setText(f"Haha you loose {winningDoor.getLabel()} was the wining door")
                    losses += 1
                break
            elif quitButton.clicked(click):
                win.close()
                return
        scoreLabel.setText(f"Wins: {wins} Losses: {losses}")
        win.getMouse()
main4()

def main5():
    # gpa1.py
    #    Program to find student with highest GPA

    class Student:

        def __init__(self, name, hours, qpoints):
            self.name = name
            self.hours = float(hours)
            self.qpoints = float(qpoints)

        def getName(self):
            return self.name

        def getHours(self):
            return self.hours

        def getQPoints(self):
            return self.qpoints

        def gpa(self):
            return self.qpoints / self.hours

        def addGrade(self, gradePoint, credits):
            self.hours += float(credits)
            self.qpoints += float(gradePoint) * float(credits)

    def makeStudent(infoStr): #skiping using this one for troubleshooting purposes
        # infoStr is a tab-separated line: name hours qpoints
        # returns a corresponding Student object
        name, hours, qpoints = infoStr.split("\t")
        return Student(name, hours, qpoints)

    def main():
        student = Student("bob joe", 0, 0)
        print("enter student info, press enter to finish or type done")
        while True:
            grade = input("Enter student grade (0.0 - 4.0): ")
            if grade.lower() == "done" or grade == "":
                break
            try:
                gradePoint = float(grade)
                credits = float(input("Enter credits for corse: "))
                if gradePoint > 4 or gradePoint < 0 or credits < 0:
                    print("grade and credits must be over 0 and gradepoint cant be over 4")
                    continue
                student.addGrade(gradePoint, credits)
            except ValueError:
                print("enter a number")
        gpa = student.gpa()
        print(f"Final GPA: {gpa:.2f}")
    main()
main5()

def main6():
    # gpa1.py
    #    Program to find student with highest GPA

    class Student:

        def __init__(self, name, hours, qpoints):
            self.name = name
            self.hours = float(hours)
            self.qpoints = float(qpoints)

        def getName(self):
            return self.name

        def getHours(self):
            return self.hours

        def getQPoints(self):
            return self.qpoints

        def gpa(self):
            return self.qpoints / self.hours

        def addGrade(self, gradePoint, credits):
            self.hours += float(credits)
            self.qpoints += float(gradePoint) * float(credits)

        def addLetterGrade(self, letterGrade, credits):
            gradeConvertion = {"A":4.0, "A-":3.7, "B+":3.3, "B":3.0, "B-":2.7, "C+":2.3, "C":2.0, "C-":1.7, "D+":1.3, "D":1.0, "D-":0.7, "F":0.0}
            letterGrade = letterGrade.strip().upper()
            if letterGrade not in gradeConvertion:
                raise ValueError(f"Invalid letter: {letterGrade}")
            gradePoint = gradeConvertion[letterGrade]
            self.addGrade(gradePoint, credits)

    def makeStudent(infoStr): #skiping using this one for troubleshooting purposes
        # infoStr is a tab-separated line: name hours qpoints
        # returns a corresponding Student object
        name, hours, qpoints = infoStr.split("\t")
        return Student(name, hours, qpoints)

    def main():
        student = Student("bob joe", 0, 0)
        print("enter student info, press enter to finish or type done")
        while True:
            grade = input("Enter student grade (A-F): ")
            if grade.lower() == "done" or grade == "":
                break
            try:
                credits = float(input("Enter credits for corse: "))
                if credits < 0:
                    print("credits must be over 0 ")
                    continue
                student.addLetterGrade(grade, credits)
            except ValueError as e:
                if str(e).startswith("Invalid letter: "):
                    print(f"Invalid letter {grade} needs to be A-F")
                else:
                    print("enter a number for credits")
                continue
        gpa = student.gpa()
        print(f"Final GPA: {gpa:.2f}")
    main()
main6()

def main7():
    # gpasort.py
    #    A program to sort student information into GPA order.
    def readStudents(filename):
        with open(filename, 'r') as infile:
            students = [makeStudent(line) for line in infile]
        return students

    def writeStudents(students, filename):
        # students is a list of Student objects
        with open(filename, 'w') as outfile:
            for s in students:
                print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                      file=outfile)

    def main():
        print("This program sorts student grade information by GPA")
        filename = input("Enter the name of the data file: ")
        data = readStudents(filename)
        
        decorated = [(student.gpa(), student) for student in data]
        decorated.sort(reverse=True)
        data = [student for _, student in decorated]
        
        filename = input("Enter a name for the output file: ")
        writeStudents(data, filename)
        print("The data has been written to", filename)
    main()
main7()

def main8():
    # gpasort.py
    #    A program to sort student information into GPA order.
    def readStudents(filename):
        with open(filename, 'r') as infile:
            students = [makeStudent(line) for line in infile]
        return students

    def writeStudents(students, filename):
        # students is a list of Student objects
        with open(filename, 'w') as outfile:
            for s in students:
                print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                      file=outfile)

    def main():
        print("This program sorts student grade information by GPA")
        filename = input("Enter the name of the data file: ")
        data = readStudents(filename)


        while True:
            field = input("Enter field to sort by (gpa, name, or credits)").lower()
            if field in ["gpa", "name", "credits"]:
                break
            else:
                print("Invalid selection choose from the provided catigoroes")

        if field == "gpa":
            decorated = [(student.gpa(), student) for student in data]
            decorated.sort(reverse=True)
        elif field == "name":
            decorated = [(student.getName(), student) for student in data]
            decorated.sort(reverse=False)
        elif field == "credits":
            decorated = [(student.getHours(), student) for student in data]
            decorated.sort(reverse=True)

        data = [student for _, student in decorated]

        filename = input("Enter a name for the output file: ")
        writeStudents(data, filename)
        print("The data has been written to", filename)
    main()
main8()

def main9():
    # gpasort.py
    #    A program to sort student information into GPA order.
    def readStudents(filename):
        with open(filename, 'r') as infile:
            students = [makeStudent(line) for line in infile]
        return students

    def writeStudents(students, filename):
        # students is a list of Student objects
        with open(filename, 'w') as outfile:
            for s in students:
                print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                      file=outfile)

    def main():
        print("This program sorts student grade information by GPA")
        filename = input("Enter the name of the data file: ")
        data = readStudents(filename)


        while True:
            field = input("Enter field to sort by (gpa, name, or credits): ").lower()
            if field in ["gpa", "name", "credits"]:
                break
            else:
                print("Invalid selection choose from the provided catigoroes")

        while True:
            order = input("Enter sort order (ascending, descending): ")
            if order in ["ascending", "descending"]:
                break
            print("Invalid answer use options provided")

        reverse = (order == "descending")

        if field == "gpa":
            decorated = [(student.gpa(), student) for student in data]
        elif field == "name":
            decorated = [(student.getName(), student) for student in data]
        elif field == "credits":
            decorated = [(student.getHours(), student) for student in data]

        decorated.sort(reverse=reverse)

        data = [student for _, student in decorated]

        filename = input("Enter a name for the output file: ")
        writeStudents(data, filename)
        print("The data has been written to", filename)
    main()
main9()

def main10():
    # gpasort.py
    #    A program to sort student information into GPA order.
    def readStudents(filename):
        with open(filename, 'r') as infile:
            students = [makeStudent(line) for line in infile]
        return students

    def writeStudents(students, filename):
        # students is a list of Student objects
        with open(filename, 'w') as outfile:
            for s in students:
                print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                      file=outfile)

    def main():
        win = GraphWin("Student sorter", 600, 600)

        Text(Point(300,50), "Enter filename and click a sort").draw(win)

        Text(Point(150,100), "Input File:").draw(win)
        inputFile = Entry(Point(300,100), 20)
        inputFile.draw(win)

        Text(Point(150,150),"Output File:").draw(win)
        outputFile = Entry(Point(300,150),20)
        outputFile.draw(win)

        gpaAscButton = Button(win, Point(150, 200), 150, 30, "GPA Ascending")
        gpaAscButton.activate()
        gpaDescButton = Button(win, Point(450, 200), 150, 30, "GPA Descending")
        gpaDescButton.activate()
        nameAscButton = Button(win, Point(150, 250), 150, 30, "Name Ascending")
        nameAscButton.activate()
        nameDescButton = Button(win, Point(450, 250), 150, 30, "Name Descending")
        nameDescButton.activate()
        creditsAscButton = Button(win, Point(150, 300), 150, 30, "Credits Ascending")
        creditsAscButton.activate()
        creditsDescButton = Button(win, Point(450, 300), 150, 30, "Credits Descending")
        creditsDescButton.activate()

        quitButton = Button(win, Point(300, 450), 100, 30, "Quit")
        quitButton.activate()

        resultLable = Text(Point(300, 400), "")
        resultLable.draw(win)

        while True:
            click = win.getMouse()

            inputfile = inputFile.getText().strip()
            outputfile = outputFile.getText().strip()

            if quitButton.clicked(click):
                break

            try:
                if inputfile == "" or outputfile == "":
                    resultLable.setText("Enter input and output filename")
                    continue
                data = readStudents(inputfile)

                if gpaAscButton.clicked(click):
                    decorated = [(student.gpa(), student) for student in data]
                    decorated.sort(reverse=False)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")
                elif gpaDescButton.clicked(click):
                    decorated = [(student.gpa(), student) for student in data]
                    decorated.sort(reverse=True)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")

                elif nameAscButton.clicked(click):
                    decorated = [(student.getName(), student) for student in data]
                    decorated.sort(reverse=False)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")
                elif nameDescButton.clicked(click):
                    decorated = [(student.getName(), student) for student in data]
                    decorated.sort(reverse=True)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")

                elif creditsAscButton.clicked(click):
                    decorated = [(student.getHours(), student) for student in data]
                    decorated.sort(reverse=False)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")
                elif creditsDescButton.clicked(click):
                    decorated = [(student.getHours(), student) for student in data]
                    decorated.sort(reverse=True)
                    data = [student for _, student in decorated]
                    writeStudents(data, outputfile)
                    resultLable.setText(f"qriten to {outputfile}")

                elif quitButton.clicked(click):
                    break

            except FileNotFoundError:
                resultLable.setText(f"File {inputFile} not found")
            except (PermissionError, IOError) as e:
                resultLable.setText(f"Error writing to {outputfile} : {str(e)}")
        win.close()
    main()
main10()

#def main11():
#main11()

#def main12():
#main12()

def main13():
    class Sphere:
        def __init__(self, radius):
            self.radius = float(radius)

        def getRadius(self):
            return self.radius

        def surfaceArea(self):
            return 4 * m.pi * self.radius ** 2

        def volume(self):
            return (4/3) * m.pi * self.radius ** 3
    def main():
        while True:
            try:
                radius = float(input("Enter radius: "))
                if radius < 0:
                    print("cant be a number bellow 0")
                    continue
                break
            except ValueError:
                print("enter a valid number")

        sphere = Sphere(radius)
        print(f"Volume {sphere.volume():.2f}")
        print(f"Surface Area {sphere.surfaceArea():.2f}")
    main()
main13()

def main14():
    class Cube:
        def __init__(self, side):
            self.side = float(side)

        def getSide(self):
            return self.side

        def surfaceArea(self):
            return 6 * self.side ** 2

        def volume(self):
            return self.side ** 3

    def main():
        while True:
            try:
                radius = float(input("Enter radius: "))
                if radius < 0:
                    print("cant be a number bellow 0")
                    continue
                break
            except ValueError:
                print("enter a valid number")

        cube = Cube(radius)
        print(f"Volume {cube.volume():.2f}")
        print(f"Surface Area {cube.surfaceArea():.2f}")
    main()
main14()

def main15():
    class PlayingCard:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def getRank(self):
            return self.suit

        def getSuit(self):
            return self.suit

        def value(self):
            if self.rank == 1:
                return 1
            elif self.rank >= 11:
                return 10
            return self.rank

        def __str__(self):
            rankNames = {1:"Ace", 11:"Jack", 12:"Queen", 13:"Kink"}
            suitNames = {"d":"Diamonds", "c":"Clubs","h":"Hearts", "s":"Spades"}
            rankStr = rankNames.get(self.rank, str(self.rank))
            suitStr = suitNames[self.suit]
            return f"{rankStr} of {suitStr}"

    def main():
        while True:
            try:
                n = int(input("Enter the numbers of cards to generate: "))
                if n < 0:
                    print("number cant be negitive")
                    continue
                break
            except ValueError:
                print("Invalid number")
        suits = ["d", "c", "h", "s"]
        for _ in range(n):
            rank = random.randint(1, 13)
            suit = random.choice(suits)
            card = PlayingCard(rank, suit)
            print(f"{card}: {card.value()}")
    main()

main15()

def main16():
    #YOU NEED TO LABLE CARDS 1s.png (for ace of spades) and 11h.png (for jack of hearts) ALSO MAKE A DIRECTORY CALLED cards and put the immages in the directory so its sctuctuire should be
    #pyhthon program.py
    #cards/ allfiles.png
    class PlayingCard:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def getRank(self):
            return self.suit

        def getSuit(self):
            return self.suit

        def value(self):
            if self.rank == 1:
                return 1
            elif self.rank >= 11:
                return 10
            return self.rank

        def __str__(self):
            rankNames = {1:"Ace", 11:"Jack", 12:"Queen", 13:"Kink"}
            suitNames = {"d":"Diamonds", "c":"Clubs","h":"Hearts", "s":"Spades"}
            rankStr = rankNames.get(self.rank, str(self.rank))
            suitStr = suitNames[self.suit]
            return f"{rankStr} of {suitStr}"

        def draw(self, win, center):
            filename = f"cards/{self.rank}{self.suit}.png"
            image = Image(center, filename)
            image.draw(win)

    def main():
        win = GraphWin("Card Hand", 800, 400)
        win.setBackground("green")

        suits = ["d", "c", "h", "s"]
        centers = [Point(100,150), Point(250, 150), Point(400, 150), Point(550,150), Point(700,150)]
        for center in centers:
            rank = random.randint(1, 13)
            suit = random.choice(suits)
            card = PlayingCard(rank, suit)
            card.draw(win, center)
        win.getMouse()
        win.close()
main16()

#def main17():
#main17()

#def main18():
#main18()

#def main19():
#main19()

#def main20():
#main20()

#def main21():
#main21()

#def main22():
#main22()

#def main23():
#main23()

#def main24():
#main24()
