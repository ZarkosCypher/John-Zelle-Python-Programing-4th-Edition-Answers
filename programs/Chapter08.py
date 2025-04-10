from graphics import *

def main1():
    gradeTable = "FFDCBA"

    while True:
        try:
            score = int(input("enter a number: "))
            if 0 <= score <= 5:
                grade = gradeTable[score]
                print(f"The grade is: {grade}")
                break
            else:
                print("Enter a number above 0 and blow 5")
                continue
            break
        except ValueError:
            print("Enter a valid number")
main1()

def main2():
    gradeTable = "FDCBA"

    while True:
        try:
            score = int(input("Enter a number: "))
            if 0 <= score <= 100:
                if score < 60:
                    index = 0
                else:
                    index = (score - 60) // 10 + 1
                    if index > 4:
                        index = 4
                grade = gradeTable[index]
                print(f"The grade is: {grade}")
                break
            else:
                print("Enter a number above 0 and blow 100")
                continue
            break
        except ValueError:
            print("Enter a valid number")
main2()

def main3():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    acronym = "".join(letter[0].upper() for letter in words)
    print(f"The acronym is {acronym}")
main3()

def main4():
    name = input("Enter a name: ")
    total = 0
    for letter in name.upper():
        if letter.isalpha():
            value = ord(letter) - ord("A") + 1 #sets A to 0 and then puts it in place 1
            total += value
    print(f"The numeric value of {name} is: {total}")
main4()

def main5():
    #literly already made it that does that in question 4
    fullName = input("Enter a name: ")
    total = 0
    for letter in fullName.upper():
        if letter.isalpha():
            value = ord(letter) - ord("A") + 1 #sets A to 0 and then puts it in place 1
            total += value
    print(f"The numeric value of {fullName} is: {total}")
main5()

def main6():
    plaintext = input("Enter the plaintext: ")
    while True:
        try:
            key = int(input("Enter the key + to encode - to decode: "))
            break
        except ValueError:
            print("Invalid input enter a number!")
    def shift(ch,key):
        return chr(ord(ch)+key)
    encoded = ""
    for ch in plaintext:
        encoded += shift(ch, key)
    print(f"Result:{encoded}")
main6()

def main7():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwkyz"

    plaintext = input("Enter the text: ")
    while True:
        try:
            key = int(input("Enter the key + to encode - to decode: "))
            break
        except ValueError:
            print("Invalid input enter a number!")
    def shift(ch, key):
        if ch in alphabet:
            oldPos = alphabet.index(ch)
            newPos = (oldPos + key) % len(alphabet)
            return alphabet[newPos]
        return ch
    result = ""
    for ch in plaintext:
        result += shift(ch, key)

    print(f"Result: {result}")
main7()

def main8():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwkyz"

    plaintext = input("Enter plaintext: ")
    passphrase = input("Enter the passphrase (letters only): ")
    mode = input("Enter 'encode' or 'decode': ").lower()

    def getShift(char):
        if char.isupper():
            return ord(char) - ord("A") + 1
        elif char.islower():
            return ord(char) - ord("a") + 1
        return 0

    def shiftCh(ch, shift, decode=False):
        if ch.isalpha():
            alphabet = upper if ch.isupper() else lower
            base = ord("A") if ch.isupper() else ord("a")
            oldPos = ord(ch) - base
            if decode:
                newPos = (oldPos - shift) % 26
            else:
                newPos = (oldPos + shift) % 26
            return alphabet[newPos]
        return ch
    passphraseShift = [getShift(ch) for ch in passphrase if ch.isalpha()]
    if not passphraseShift:
        print("passphrase must have atleast one letter")
        exit()
    result = ""
    passIndex = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = passphraseShift[passIndex]
            result += shiftCh(ch, shift, decode=(mode == "decode"))
            passIndex = (passIndex + 1) % len(passphraseShift)
        else:
            result += ch
    print(f"Result: {result}")
main8()

def main9():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    print(f"There are {len(words)} words in that phrase")
main9()

def main10():
    sentance = input("Enter a sentance: ")
    words = sentance.split()
    if not words:
        print("Nothing enetared")
    else:
        total = sum(len(letter) for letter in words)
        average = total / len(words)
        print(f"The average word length is {average:.2f} letters")
main10()

def main11():
    print("This porgram calculates the future value of an investment over a specific number of years.")
    principal = float(input("Enter the inicial principle: "))
    apr = float(input("Enter the annual interest rate as a decimal ex 0.05 is 5%: "))
    years = int(input("Enter the number of years: "))

    print("\nYear   Value")
    print("-"*20)

    print(f"{0:<4}  ${principal:,.2f}")

    for years in range(1, years + 1):
        principal = principal * (1 + apr)
        print(f"{years:<4}  ${principal:,.2f}")
main11()

def main12():
    def windchill(temp, vwind):
        if vwind > 3:
            return 25.74 + 0.6215*temp - 35.75*(vwind**0.16) + 0.4275 * temp * (vwind**0.16)
        return temp

    windSpeedRange = range(0, 51, 5)
    tempRange = range(-20, 61, 10)

    print("Wind MPH |", end=" ")
    for temp in tempRange:
        print(f"{temp:>5}", end=" ")
    print("\n" + "-" * (12 + 6 *len(tempRange)))
    for wind in windSpeedRange:
        print(f"{wind:>2} mph   |", end=" ")
        for temp in tempRange:
            value = windchill(temp, wind)
            print(f"{value:>5.1f}", end=" ")
        print()

main12()

def main13():
    numStudents = int(input("enter how many studnts: "))
    students = []
    for i in range(numStudents):
        name = str(input(f"Enter the name for student {i+1}: "))
        grade = int(input(f"Enter the score for {name}: "))
        while grade < 0 or grade > 100:
            print("grade needs to be between 0 - 100")
            grade = int(input(f"Enter the score for {name}: "))
        students.append((name, grade))

    winHeight = numStudents * 50 + 50
    winWidth = 600
    win = GraphWin("Student Grades",  winWidth, winHeight)

    barHeight = 20
    xStart = 100 #left side of bars
    yStart = 30 #top of bar 1
    maxGrade = 100

    for i, (name, grade) in enumerate(students):
        yPosition = yStart + i * 50 #50 inbetween bars
        lable = Text(Point(xStart - 50, yPosition + barHeight / 2), name)
        lable.draw(win)
        barLenght = grade * (winWidth - 200) / maxGrade
        bar = Rectangle(Point(xStart, yPosition),Point(xStart + barLenght, yPosition + barHeight))
        bar.setFill("blue")
        bar.draw(win)

    win.getMouse()
    win.close()
main13()

def main14():
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
            return word+"way"
        elif indexx == len(word):
            return word+"ay"
        else:
            return word[indexx:] + word[:indexx] + "ay"
    def translatePhraseToPl(phrase):
        words = phrase.split()
        translatedWords = [translateWordToPl(word) for word in words]
        return " ".join(translatedWords)

    phrase = input("Enter a phrase: ")
    translated = translatePhraseToPl(phrase)
    print(f"Pig Latin: {translated}")


    #TESTING
    print("Testing firstVowel")
    print(firstVowel("apple"))
    print(firstVowel("ship"))
    print(firstVowel("yes"))
    print(firstVowel("sky"))
    #TESTING
    print(translateWordToPl("apple"))
    print(translateWordToPl("ship"))
    print(translateWordToPl("yes"))
    print(translateWordToPl("sky"))
    #TESTING
    print(translatePhraseToPl("Harold don't talk in front of the kids we are getting a divorce"))
main14()

def main15():
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

    phrase = input("Enter a phrase: ")
    translated = translatePhrase(phrase)
    print(f"Translated: {translated}")

    # TESTING
    print("Testing firstVowel")
    print(findVowels("apple"))
    print(findVowels("ship"))
    print(findVowels("yes"))
    print(findVowels("sky"))
    # TESTING
    print(translateWord("apple"))
    print(translateWord("ship"))
    print(translateWord("yes"))
    print(translateWord("sky"))
    # TESTING
    print(translatePhrase("Harold don't talk in front of the kids we are getting a divorce"))
main15()
