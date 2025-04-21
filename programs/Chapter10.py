from os.path import *
from graphics import *

def main1():
    def writeNumbersToFile(filename, numbers):
        with open(filename, "w") as outfile:
            for num in numbers:
                outfile.write(str(num) + '\n')
    fileName = input("Enter the file name: ").strip()
    numbers = []

    print("Enter numbers and then press enter to finish")
    while True:
        numIn = input("Enter a number: ").strip()
        if numIn == "":
            break
        try:
            num = float(numIn)
            numbers.append(num)
            print(f"added {num} to file")
        except ValueError:
            print(f"{numIn} is not a valid number")
            continue
    try:
        writeNumbersToFile(fileName, numbers)
        print(f"Sucsesfully write {len(numbers)} numbers to {fileName}")
    except IOError:
        print(f"cant read file {fileName}")
        return

main1()

def main2():

    fileName = input("Enter the file name: ").strip()

    leg = []
    totalMiles = 0
    totalGas = 0

    try:
        with open(fileName, "r") as infile:
            lines = infile.readlines()
            if not lines:
                print("file empty")
                return
            lineNum = 1
            firstLine = lines[0].strip()
            try:
                startingOdometer = int(firstLine)
                if startingOdometer < 0:
                    print("starting odometer cant be negative")
                    return
            except ValueError:
                print(f"invalid imput {firstLine} on line {lineNum}")
                return
            for lineNum, line in enumerate(lines[1:],2):
                if line.strip() == "":
                    continue
                parts = line.strip().split()
                if len(parts) != 2:
                    print(f"invalid format {line.strip()} on line {lineNum}")
                    continue
                odometerStr, gasStr = parts
                try:
                    currentOdometer = float(odometerStr)
                    gas = float(gasStr)
                    if currentOdometer < startingOdometer:
                        print(f"odometer {currentOdometer} in line {lineNum} needas to be more than the last reading {startingOdometer}")
                        continue
                    if gas <= 0:
                        print(f"gas {gas} in line {lineNum} neds to be positive")
                        continue
                    miles = currentOdometer - startingOdometer
                    leg.append((miles, gas))
                    totalMiles += miles
                    totalGas += gas
                    startingOdometer = currentOdometer
                    mpg = miles / gas
                    print(f"prossesed leg: {miles:.1f} miles, {gas:.1f} gallons, {mpg:.1f} miles per gallon")
                except ValueError:
                    print(f"invalid numbers {odometerStr} {gasStr} on line {lineNum}")
                    continue
    except IOError:
        print(f"cant read file {fileName}")
        return 

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

main2()

def main3():
    heatingDay = 0
    coolingDay = 0

    fileName = input("Enter the file name: ").strip()
    
    try:
        with open(fileName, "r") as infile:
            for lineNum, line in enumerate(infile, 1):
                if line.strip() == "":
                    continue
                tempStr = line.strip()
                try:
                    temp = float(tempStr)
                except ValueError:
                    print(f"invalid temp {tempStr} on line {lineNum}")
                    continue
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
    except IOError:
        print(f"cant read file {fileName}")

    print("Total Days")
    print(f"Total Heaating Days: {heatingDay:.1f}")
    print(f"Total Cooling Days: {coolingDay:.1f}")

main3()

def main4():

    win = GraphWin("line plotting", 400, 400)
    win.setCoords(0, 0, 200, 200)
    screenX = 0
    screenY = 200

    done = Rectangle(Point(5, 5), Point(30, 15))
    done.setFill("grey")
    done.draw(win)
    doneLable = Text(Point(17, 10), "Done")
    doneLable.draw(win)

    points = []
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXsquared = 0
    n = 0

    fileName = input("Enter the file name: ").strip()
    
    try:
        with open(fileName, "r") as infile:
            for lineNum, line in enumerate(infile, 1):
                if line.strip() == "":
                    continue
                parts = line.strip(),split()
                if len(parts) != 2:
                    print(f"error on line {lineNum}: {line.strip()}")
                    continue
                xStr, yStr = parts
                try:
                    x = float(xStr)
                    y = float(yStr)
                    if not (0 <= x <= 200 and 0 <= y <= 200):
                        print(f"cords {x} {y} in line {lineNum} must be between 0 - 200")
                        continue
                except ValueError:
                    print(f"invalid cords {xStr} {yStr} in line {lineNum}")
                    continue
                print(f"Point: {x} {y}")
                point = Circle(Point(x, y), 1)
                point.setFill("blue")
                point.draw(win)

                points.append((x, y))
                n += 1
                sumX += x
                sumY += y
                sumXY += x * y
                sumXsquared += x * x
    except IOError:
        print(f"cant read {fileName}")
        win.close()
        return 
    
    if n < 2:
        print("atleast 2 points are needed")
        win.close()
        return 

    xBar = sumX / n
    yBar = sumY / n

    numerator = sumXY - n * xBar * yBar
    denominator = sumXsquared - n * xBar * xBar
    m = numerator / denominator

    yLeft = yBar + m * (0 - xBar)  # x is left edge at 0
    yRight = yBar + m * (200 - xBar)  # x is right edge at 200

    line = Line(Point(screenX, yLeft), Point(screenY, yRight))
    line.setOutline("red")
    line.setWidth(2)
    line.draw(win)

    win.getMouse()
    win.close()

main4()

def main5():

    fileName = input("Enter the file name: ").strip()
    students = []

    try:
        with open(fileName, "r") as infile:
            for lineNum, line in enumerate(infile, 1):
                if line.strip() == "":
                    continue
                parts = line.strip().split()
                if len(parts) != 2:
                    print(f"invaid on line {lineNum}: {line.strip()}")
                    continue
                name, gradeStr = parts
                try:
                    grade = int(gradeStr)
                    if grade < 0 or grade > 100:
                        print(f"invaid grade {gradeStr} for {name} on line {lineNum} it needs to be 0 - 100")
                        continue
                except ValueError:
                    print(f"Invalid grade {gradeStr} for {name} on line {lineNum}")
                    continue
                print(f"added student name {name} and grade {grade}")
                students.append((name, grade))
    except IOError:
        print(f"Cant read file {fileName}")

    if not students:
        print("No valud student data")
        return
    
    numStudents = len(students)
    winHeight = numStudents * 50 + 50
    winWidth = 600
    win = GraphWin("Student Grades", winWidth, winHeight)

    barHeight = 20
    xStart = 100  # left side of bars
    yStart = 30  # top of bar 1
    maxGrade = 100

    for i, (name, grade) in enumerate(students):
        yPosition = yStart + i * 50  # 50 inbetween bars
        lable = Text(Point(xStart - 50, yPosition + barHeight / 2), name)
        lable.draw(win)
        barLenght = grade * (winWidth - 200) / maxGrade
        bar = Rectangle(Point(xStart, yPosition), Point(xStart + barLenght, yPosition + barHeight))
        bar.setFill("blue")
        bar.draw(win)

    win.getMouse()
    win.close()

main5()

def main6():
    def firstVowel(word):
        vowels = "aeiouAEIOU"
        if not word:
            return -1
        for i in range(len(word)):
            if (word[i] in vowels) or (i > 0 and word[i] in "yY"):
                return i
        return len(word)

    def translateWordToPl(word):
        if not word:
            return ""
        indexx = firstVowel(word)
        if indexx == 0:
            return word + "way"
        elif indexx == len(word):
            return word + "ay"
        else:
            return word[indexx:] + word[:indexx] + "ay"

    def translatePhraseToPl(phrase):
        words = phrase.split()
        translatedWords = [translateWordToPl(word) for word in words]
        return " ".join(translatedWords)

    inputPath = input("Enter path for english file: ").strip()
    outputPath = input("Enter path for saving LF file with .lf at the end: ").strip()

    try:
        with open(inputPath, "r") as infile:
            content = infile.read()
    except IOError:
        print(f"Error cant read {inputPath}")
        return

    translated = translatePhraseToPl(content)

    try:
        with open(outputPath, "w") as outfile:
            outfile.write(translated)
        print(f"Done saved {inputPath} translated to {outputPath}")
    except IOError:
        print(f"Cant wrie to {outputPath}")


    phrase = input("Enter a phrase: ")
    translated = translatePhraseToPl(phrase)
    print(f"Pig Latin: {translated}")
main6()

def main7():
    def findVowels(word):
        vowels = "aeiouAEIOU"
        if not word:
            return -1
        for i in range(len(word)):
            if (word[i] in vowels) or (i > 0 and word[i] in "yY"):
                return i
        return len(word)

    def translateWord(word):
        if not word:
            return ""
        indexx = findVowels(word)
        if indexx == len(word):
            return word + "lf"
        firstVowel = word[indexx]
        return word[:indexx + 1] + "lf" + firstVowel + word[indexx + 1:]

    def translatePhrase(phrase):
        words = phrase.split()
        translatedWords = [translateWord(word) for word in words]
        return " ".join(translatedWords)

    inputPath = input("Enter path for english file: ").strip()
    outputPath = input("Enter path for saving LF file with .lf at the end: ").strip()
    
    try:
        with open(inputPath, "r") as infile:
            content = infile.read()
    except IOError:
        print(f"Error cant read {inputPath}")
        return 
    
    translated = translatePhrase(content)
    
    try:
        with open(outputPath, "w") as outfile:
            outfile.write(translated)
        print(f"Done saved {inputPath} translated to {outputPath}")
    except IOError:
        print(f"Cant wrie to {outputPath}")
            
    phrase = input("Enter a phrase: ")
    translated = translatePhrase(phrase)
    print(f"Translated: {translated}")
main7()

def main8():
    def findVowels(word):
        vowels = "aeiouAEIOU"
        if not word:
            return -1
        for i in range(len(word)):
            if (word[i] in vowels) or (i > 0 and word[i] in "yY"):
                return i
        return len(word)

    def translateWord(word):
        if not word:
            return ""
        indexx = findVowels(word)
        if indexx == len(word):
            return word + "lf"
        firstVowel = word[indexx]
        return word[:indexx + 1] + "lf" + firstVowel + word[indexx + 1:]

    def translatePhrase(phrase):
        words = phrase.split()
        translatedWords = [translateWord(word) for word in words]
        return " ".join(translatedWords)

    currentDir = os.getcwd()
    succcessCount = 0
    try:
        for filename in os.listdir(currentDir):
            if filename.lower().endswith(".txt"):
                inputPath = os.path.join(currentDir, filename)
                outputFilename = os.path.splitext(filename)[0]+ ".lf"
                outputPath = os.path.join(currentDir, outputFilename)

                try:
                    with open(inputPath, "r") as infile:
                        content = infile.read()
                except IOError:
                    print(f"Cant read file {inputPath}")
                    continue

                translated = translatePhrase(content)

                try:
                    with open(outputPath, "w") as outfile:
                        outfile.write(translated)
                    print(f"Tranlated {inputPath} to {outputPath}")
                    succcessCount += 1
                except IOError:
                    print(f"Cant write to {outputPath}")
                    continue
    except OSError:
        print(f"Cant acsses Dir {currentDir}")
        return

    print(f"Done translating {succcessCount} files")

    phrase = input("Enter a phrase: ")
    translated = translatePhrase(phrase)
    print(f"Translated: {translated}")
main8()

def main9():
    def censor(inputFile, outputFile):
        try:
            infile = open(inputFile, "r")
            text = infile.read()
            infile.close()
        except IOError:
            print("Input file cant be read.")
            return
        words = text.split()
        censoredWords = []

        for word in words:
            clean = ""
            for char in word:
                if char.isalpha():
                    clean += char
            if len(clean) == 4:
                newWord = ""
                startCount = 0
                for char in word:
                    if char.isalpha() and startCount < 4:
                        newWord += "*"
                        startCount += 1
                    else:
                        newWord += char
                censoredWords.append(newWord)
            else:
                censoredWords.append(word)
        censoredText = " ".join(censoredWords)

        try:
            outfile = open(outputFile, "w")
            outfile.write(censoredText)
            outfile.close()
            print("Done censeoring")
        except IOError:
            print("Cant save file")

    #When testing you need to have it named text.txt or chnage it acordingly with you tests
    censor("test.txt", "finished.txt")
main9()

def main10():
    def censor(inputFile, censorFile, outputFile):
        try:
            banned = open(censorFile, "r")
            bannedWords = banned.read().split()
            banned.close()
        except IOError:
            print("Cant open file")
            return

        bannedClean = []
        for word in bannedWords:
            cleaned = ""
            for char in word:
                if char.isalpha():
                    cleaned += char
            if cleaned:
                bannedClean.append(cleaned.lower())

        try:
            infile = open(inputFile, "r")
            text = infile.read()
            infile.close()
        except IOError:
            print("Input file cant be read.")
            return

        words = text.split()
        censoredWords = []
        for word in words:
            clean = ""
            for char in word:
                if char.isalpha():
                    clean += char
            clean = clean.lower()
            if clean in bannedClean:
                starCount = len(clean)
                newWord = ""
                starUsed = 0
                for char in word:
                    if char.isalpha() and starUsed < starCount:
                        newWord += "*"
                        starUsed += 1
                    else:
                        newWord += char
                censoredWords.append(newWord)
            else:
                censoredWords.append(word)
        censoredText = " ".join(censoredWords)

        try:
            outfile = open(outputFile, "w")
            outfile.write(censoredText)
            outfile.close()
            print("Done censeoring")
        except IOError:
            print("Cant save file")

    #When testing you need to have it named text.txt or chnage it acordingly with you tests
    censor("test.txt", "BannedWords.txt", "finished.txt")
main10()

def main11():
    def censor(inputFile, censorFile, outputFile):
        try:
            banned = open(censorFile, "r")
            bannedWords = banned.read().split()
            banned.close()
        except IOError:
            print("Cant open file")
            return

        bannedClean = []
        for word in bannedWords:
            cleaned = ""
            for char in word:
                if char.isalpha():
                    cleaned += char
            if cleaned:
                bannedClean.append(cleaned.lower())

        try:
            infile = open(inputFile, "r")
            text = infile.read()
            infile.close()
        except IOError:
            print("Input file cant be read.")
            return

        words = text.split()
        censoredWords = []
        for word in words:
            clean = ""
            for char in word:
                if char.isalpha():
                    clean += char
            clean = clean.lower()
            if clean in bannedClean:
                starCount = len(clean)
                newWord = ""
                starUsed = 0
                for char in word:
                    if char.isalpha() and starUsed < starCount:
                        newWord += "*"
                        starUsed += 1
                    else:
                        newWord += char
                censoredWords.append(newWord)
            else:
                censoredWords.append(word)
        censoredText = " ".join(censoredWords)

        try:
            outfile = open(outputFile, "w")
            outfile.write(censoredText)
            outfile.close()
            print("Done censeoring")
        except IOError:
            print("Cant save file")

    def censorDirectory(inputDir, censorFile):
        outputDir =  os.path.join(inputDir, "censored")
        try:
            os.makedirs(outputDir, exist_ok=True)
        except OSError:
            print(f"Cant create dir {outputDir}")
            return

        successCount = 0
        try:
            for filename in os.listdir(inputDir):
                if filename.lower().endswith(".txt"):
                    inputPath = os.path.join(inputDir, filename)
                    outputPath = os.path.join(outputDir, filename)
                    censorPath = os.path.join(inputDir, censorFile)
                    censor(inputPath, censorPath, outputPath)
                    successCount += 1
        except OSError:
            print(f"Cant access dir {inputDir}")
            return
        print(f"Done censoring {successCount} files")

    censorDirectory(r"C:","BannedWords.txt")
main11()

def main12():
    def readQuiz(filePath):
        try:
            infile = open(filePath, "r")
            lines = infile.readlines()
            infile.close()
        except IOError:
            print("Cant open quiz file")
            return None
        quiz = []
        i = 0
        while i < len(lines):
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            if i >= len(lines):
                break
            if i + 4 >= len(lines):
                print("Incomplete question in file")
                return None
            question = lines[i].strip()
            answers = []
            correct = -1

            for j in range(4):
                answer = lines[i + j + 1].strip()
                if answer.startswith("*"):
                    correct = j
                    answer = answer[1:].strip()
                answers.append(answer)
            if correct == -1:
                print("No answer marked with * infront")
                return None
            quiz.append((question, answers, correct))
            i += 5
        return quiz

    def runQuiz(quiz):
        if not quiz:
            print("No questions to show")
            return 0

        score = 0
        for i, (question, answers, correct) in enumerate(quiz, 1):
            print(f"Question {i}: {question}")
            for j, answer in enumerate(answers):
                print(f" {chr(97 + j)}. {answer}")

            while True:
                response = input("Your answer can be (a b c d): ").lower().strip()
                if response in ["a", "b", "c", "d"]:
                    userIndex = ord(response) - ord("a")
                    break
                print("you need to choose a b c or d")
            if userIndex == correct:
                print("Correct")
                score += 1
            else:
                print(f"Wrong, answr is {chr(97 + correct)}. {answers[correct]}")
        return score

    filePath = input("Enter file path of quiz: ").strip()
    quiz = readQuiz(filePath)
    if quiz is None:
        return
    score = runQuiz(quiz)
    print(f"quiz is done, yoru score is: {score}/{len(quiz)}")
main12()
