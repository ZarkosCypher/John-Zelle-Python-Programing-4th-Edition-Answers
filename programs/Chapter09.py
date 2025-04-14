import math as m
from graphics import *
from time import sleep


def main1():
    def getNumbers():
        nums = []
        xStr = input("Enter a number (<Enter> to quit) >> ")
        while xStr != "":
            x = float(xStr)
            nums.append(x)
            xStr = input("Enter a number (<Enter> to quit) >> ")
        return nums

    def mean(nums):
        if not nums:
            return None
        total = 0.0
        for num in nums:
            total = total + num
        return total / len(nums)

    def stdDev(nums):
        if not nums or len(nums) < 2:
            return None
        xbar = mean(nums)
        sumDevSq = 0.0
        for num in nums:
            dev = num - xbar
            sumDevSq = sumDevSq + dev * dev
        return m.sqrt(sumDevSq / len(nums) - 1)

    def meanStdDev(nums):
        if not nums:
            return None, None
        return mean(nums), stdDev(nums)

    def median(nums):
        if not nums:
            return None
        sorted_nums = nums.copy()
        sorted_nums.sort()
        size = len(sorted_nums)
        midPos = size // 2
        if size % 2 == 0:
            med = (sorted_nums[midPos] + sorted_nums[midPos - 1]) / 2.0
        else:
            med = sorted_nums[midPos]
        return med

    def outliers(nums, xbar, s):
        if not nums:
            return []
        outs = []
        for x in nums:
            if abs((x - xbar) / s) >= 3:
                outs.append(x)
            return outs

    print("This program computes mean, median and standard deviation.")

    data = getNumbers()
    if not data:
        print("No data entered")
        return

    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)

    print("\nThe mean is", xbar if xbar is not None else "No Data")
    print("The standard deviation is", std if std is not None else "No Data")
    print("The median is", med if med is not None else "No Data")

main1()

def main2():
    def count(mylist, x):
        count = 0
        for item in mylist:
            if item == x:
                count += 1
        print(count)

    def isin(mylist, x):
        found = False
        for item in mylist:
            if item == x:
                found = True
        if found:
            print("Item is in the list!")
        else:
            print("Item is not in the list.")

    def indexx(mylist, x):
        indx = 0
        for item in mylist:
            indx += 1
            if item == x:
                print(f"{x} located at index {indx}")

    def reverse(mylist):
        reversedlist = []
        for item in mylist:
            reversedlist.insert(0, item)
        print(f"reversed list {reversedlist}")
        return reversedlist

    def sort(mylist):
        sortedlist = mylist.copy()
        for i in range(1, len(sortedlist)):
            key = sortedlist[i]
            j = i - 1

            while j >= 0 and sortedlist[j] > key:
                sortedlist[j + 1] = sortedlist[j]
                j -= 1
            sortedlist[j + 1] = key
        print(f"Sorted list {sortedlist}")

    animals = ["cat", "dog", "monkey", "horse", "cat"]
    print(count(animals, "cat"))
    print(animals.count("cat"))
    isin(animals, "cat")
    isin(animals, "penguin")
    indexx(animals, "cat")
    reverse(animals)
    sort(animals)
main2()

def main3():
    def innerProd(x, y):
        if len(x) != len(y):
            return None
        if len(x) == 0:
            return None
        result = 0
        for i in range(len(x)):
            result += x[i] * y[i]
        return result

    x = [1,2,3]
    y = [4,5,6]

    print(innerProd(x, y))
main3()

def main4():
    def removeDuplicates(somelist):
        clean = []
        for item in somelist:
            if item not in clean:
                clean.append(item)
        return clean

    animals = ["cat", "dog", "monkey", "horse", "cat"]
    print(removeDuplicates(animals))

main4()

def main5():
    def squareEach(nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            
    test = [1,2,3,4,5]
    print(squareEach(test))
main5()

def main6():
    def toNumbers(strList):
        for i in range(len(strList)):
            try:
                strList[i] = float(strList[i])
            except (ValueError, TypeError):
                print(f"Invalid number {strList[i]} at index {i}")

    test = ["1","2","3","4","5"]
    print(toNumbers(test))
main6()

def main7():
    def toNumbers(strList):
        for i in range(len(strList)):
            try:
                strList[i] = float(strList[i])
            except (ValueError, TypeError):
                print(f"Invalid number {strList[i]} at index {i}")

    def squareEach(nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

    def sumOfSquare(strInput):
        total = 0.0
        for item in strInput:
            total += item
        return total

    user = str(input("Enter a few numbers seperated by a space: "))
    strlst = user.split()
    toNumbers(strlst)
    squareEach(strlst)
    print(sumOfSquare(strlst))

main7()

def main8():
    def primeFinder(n):
        numbers = list(range(2, n + 1))
        primes = []
        while numbers:
            prime = numbers[0]
            primes.append(prime)
            print(f"Found prime: {prime}")
            newNumber = []
            for num in numbers:
                if num % prime != 0:
                    newNumber.append(num)
                numbers = newNumber
        return primes

    while True:
        try:
            num = int(input("Enter a number: "))
            if num <= 2:
                print("Enter a number over 2")
                continue
            else:
                break
        except ValueError:
            print("Enter a valid number")

    primeFinder(num)

main8()

def main9():
    def makeSet(elements):
        #All items in elements without duplicates
        result = []
        for item in elements:
            if item not in result:
                result.append(item)
        return result

    def addElement(s, x):
        #Add x to s if it's not already in s
        if x not in s:
            s.append(x)

    def deleteElement(s, x):
        #Remove x from s if present
        if x in s:
            s.remove(x)

    def member(s, x):
        #True if x is in s False otherwise
        return x in s

    def intersection(s1, s2):
        #A new list containing elements common to s1 and s2
        result = []
        for item in s1:
            if item in s2 and item not in result:
                result.append(item)
        return result

    def union(s1, s2):
        #A new list containing all elements in s1 and s2 without duplicates
        result = s1.copy()
        for item in s2:
            if item not in result:
                result.append(item)
        return result

    def subtract(s1, s2):
        #A new list containing elements in s1 that are not in s2
        result = []
        for item in s1:
            if item not in s2 and item not in result:
                result.append(item)
        return result

    elementss = [1,2,2,3,4,4,5,5,5,5]
    s1 = makeSet(elementss)
    s2 = [3,4,5,6,7,7]

    print(f"makeSet({elementss}) = {s1}")
    print(f"s2 = {s2}")
    addElement(s1, 6)
    print(f"After addElement(s1, 6), s1 = {s1}")
    deleteElement(s1, 2)
    print(f"After deleteElement(s1, 2), s1 = {s1}")
    print(f"member(s1, 3) = {member(s1, 3)}")
    print(f"member(s1, 2) = {member(s1, 2)}")
    print(f"intersection(s1, s2) = {intersection(s1, s2)}")
    print(f"union(s1, s2) = {union(s1, s2)}")
    print(f"subtract(s1, s2) = {subtract(s1, s2)}")
main9()

def main10():
    win = GraphWin("Bouncing Face", 400,400)
    win.setCoords(-100,-100,100,100)

    def makeFace(centerX, centerY):
        faceParts = []
        head = Circle(Point(centerX, centerY), 20)
        head.setOutline("black")
        head.setFill("yellow")
        faceParts.append(head)

        leftEye = Circle(Point(centerX - 8, centerY + 8), 3)
        leftEye.setFill("black")
        faceParts.append(leftEye)

        rigtEye = Circle(Point(centerX + 8, centerY + 8), 3)
        rigtEye.setFill("black")
        faceParts.append(rigtEye)

        mouth = Oval(Point(centerX - 8, centerY - 8), Point(centerX + 8, centerY - 4))
        mouth.setFill("pink")
        faceParts.append(mouth)

        return faceParts

    def drawFace(faceParts, win):
        for part in faceParts:
            part.draw(win)

    def moveFace(faceParts, dx, dy):
        for part in faceParts:
            part.move(dx,dy)

    def getFaceCenter(faceParts):
        return faceParts[0].getCenter()

    face = makeFace(0, -80)
    drawFace(face, win)

    dx = 1
    dy = 1

    for i in range(10000):
        sleep(0.02)
        c = getFaceCenter(face)
        
        if c.getX() > 80:
            dx =-1
        elif c.getX() < -80:
            dx = 1
        elif c.getY() > 80:
            dy =-1
        elif c.getY() < -80:
            dy = 1
        moveFace(face, dx, dy)

main10()

def main11():
    def makeDeck():
        ranks = list(range(2,15))
        suits = ["S","C","H","D"]
        deck = [(rank,suit) for suit in suits for rank in ranks]
        return deck
    print(makeDeck())
main11()

def main12():
    def makeDeck():
        ranks = list(range(2, 15))
        suits = ["S", "C", "H", "D"]
        deck = [(rank, suit) for suit in suits for rank in ranks]
        return deck

    print(makeDeck())

    def straightFlush(cards):
        return flush(cards) and straight(cards)
    def fourOfAKind(cards):
        rank_counts = rankCounts(cards)
        return 4 in rank_counts.values()
    def fullHouse(cards):
        rank_counts = rankCounts(cards)
        return sorted(rank_counts.values()) == [2, 3]
    def flush(cards):
        return len(set(suit for _, suit in cards)) == 1
    def straight(cards):
        sortedRanks = sorted(rank for rank, _ in cards)
        if sortedRanks == list(range(sortedRanks[0], sortedRanks[0] + 5)):
            return  True
        if sortedRanks == [2, 3, 4, 5, 14]:
            return True
        return False
    def threeOfAKind(cards):
        rank_counts = rankCounts(cards)
        return 3 in rank_counts.values() and not (4 in rank_counts.values() or sorted(rank_counts.values()) == [2, 3])
    def twoPair(cards):
        rank_counts = rankCounts(cards)
        return sorted(rank_counts.values()) == [1, 2, 2]
    def pair(cards):
        rank_counts = rankCounts(cards)
        return sorted(rank_counts.values()) == [1, 1, 1, 2]
    def rankCounts(cards):
        rank_counts = {}
        for rank, _ in cards:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        return rank_counts

    test_hands = [
        #Straight flush: 10,J,Q,K,A of spades
        [(10, 's'), (11, 's'), (12, 's'), (13, 's'), (14, 's')],
        #Four of a kind: 7s and one 8
        [(7, 'c'), (7, 'd'), (7, 'h'), (7, 's'), (8, 'c')],
        #Full house: three 5s, two 9s
        [(5, 'c'), (5, 'd'), (5, 'h'), (9, 's'), (9, 'c')],
        #Flush: all hearts, non-consecutive
        [(2, 'h'), (4, 'h'), (6, 'h'), (8, 'h'), (10, 'h')],
        #Straight: 3,4,5,6,7 mixed suits
        [(3, 'c'), (4, 'd'), (5, 'h'), (6, 's'), (7, 'c')],
        #Three of a kind: three 4s
        [(4, 'c'), (4, 'd'), (4, 'h'), (2, 's'), (3, 'c')],
        #Two pair: two 8s, two 10s
        [(8, 'c'), (8, 'd'), (10, 'h'), (10, 's'), (2, 'c')],
        #Pair: two 6s
        [(6, 'c'), (6, 'd'), (2, 'h'), (3, 's'), (4, 'c')],
        #Straight flush: A,2,3,4,5 of clubs
        [(14, 'c'), (2, 'c'), (3, 'c'), (4, 'c'), (5, 'c')]
    ]

    categories = [
        ("Straight Flush", straightFlush),
        ("Four of a Kind", fourOfAKind),
        ("Full House", fullHouse),
        ("Flush", flush),
        ("Straight", straight),
        ("Three of a Kind", threeOfAKind),
        ("Two Pair", twoPair),
        ("Pair", pair)
    ]

    for i, hand in enumerate(test_hands, 1):
        print(f"\nHand {i}: {hand}")
        found = False
        for name, func in categories:
            if func(hand):
                print(f"-> {name}")
                found = True
                break
        if not found:
            print("-> High Card")
main12()

def main13():
    def bloodPressure(readings):
        normal = []
        elivated = []
        for systolic, diastolic in readings:
            if systolic < 120 and diastolic < 80:
                normal.append((systolic, diastolic))
            else:
                elivated.append((systolic, diastolic))
        return normal, elivated

    bloodReadings = [(100,70), (150,90), (110, 70), (120, 80), (119, 79)]
    normalReadings, elivatedReadings = bloodPressure(bloodReadings)
    print(f"Normal: {normalReadings}")
    print(f"Elivated: {elivatedReadings}")
main13()

def main14():
    def drawHistogram(counts):
        win = GraphWin("Score Counter", 800,400)
        maxCount = max(counts)
        if maxCount == 0:
            maxCount = 1

        win.setCoords(-1, -1,11, maxCount + 1)

        for score in range(11):
            bar = Rectangle(Point(score - 0.4, 0), Point(score + 0.4, counts[score]))
            bar.setFill("blue")
            bar.draw(win)

            lable = Text(Point(score, -0.5), str(score))
            lable.draw(win)

        return win

    def counting(scores):
        counts = [0] * 11
        for score in scores:
            if 0 <= score <= 10:
                counts[score] += 1
        return counts

    while True:
        try:
            inputStr = input("Enter scores seperated by spaces: ")
            scores = [int(score) for score in inputStr.split()]

            valid = all(0 <= score <= 10 for score in scores)
            if not valid:
                print("Enter scores between 0 - 10")
                continue
            break

        except ValueError:
            print("Enter a number")

    counted = counting(scores)
    win = drawHistogram(counted)

    win.getMouse()
    win.close
main14()
