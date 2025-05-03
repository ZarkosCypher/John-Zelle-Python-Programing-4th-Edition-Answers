from random import *
import time
from collections.abc import Hashable
from math import trunc
from random import random, randrange
import math as m
from graphics import *

def main1():
    def choice(myList):
        if not myList:
            raise ValueError("List is empty")
        randomIndex = random.randrange(len(myList))
        return myList[randomIndex]

    random.seed(int(time.time()))

    testlist = ["apple", "grape", "chery", "bannana", "strawbery"]
    print(testlist)
    for _ in range(8):
        chosen = choice(testlist)
        print(chosen)
main1()

def main2():
    random.seed(int(time.time()))

    def shuffle(myList):
        if len(myList) <= 1:
            return
        for i in range(len(myList) - 1, 0, -1):
            j = random.randrange(i+1)
            myList[i], myList[j] = myList[j], myList[i]

    testlist = ["apple", "grape", "chery", "bannana", "strawbery"]
    print(testlist)
    shuffle(testlist)
    print(testlist)
    shuffle(testlist)
    print(testlist)
    shuffle(testlist)
    print(testlist)

main2()

def main3():
    def main():
        printIntro()
        probA, probB, n, numMatches = getInputs()
        winsA, winsB = simMatches(numMatches, n, probA, probB)
        printSummary(winsA, winsB)

    def printIntro():
        print("This program simulates a game of racquetball between two")
        print('players called "A" and "B".  The abilities of each player is')
        print("indicated by a probability (a number between 0 and 1) that")
        print("the player wins the point when serving. Player A always")
        print("has the first serve.\n")
        print("player A plays even and player B plays odd")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins a serve?: "))
        b = float(input("What is the prob. player B wins a serve?: "))
        n = int(input("How many games per match (odd number 5 for best of 5)?: "))
        while n % 2 == 0:
            print("enter an odd number")
            n = int(input("How many games per match (odd number 5 for best of 5)?: "))
        numMatches = int(input("How many matches to simulate?: "))
        return a, b, n, numMatches

    def simMatches(numMatches, n, probA, probB):
        winsA = winsB = 0
        for i in range(numMatches):
            winsAinMatch, winsBinMatch = simOneMatch(n, probA, probB)
            if winsAinMatch > winsBinMatch:
                winsA += 1
            else:
                winsB += 1
        return winsA, winsB

    def simOneMatch(n, probA, probB):
        winsA = winsB = 0
        maxWins = (n + 1) // 2
        for gameNum in range(1, n + 1):
            firstServer = "A" if gameNum % 2 == 1 else "B"
            scoreA, scoreB = simOneGame(probA, probB, firstServer)
            if scoreA > scoreB:
                winsA += 1
            else:
                winsB += 1
            if winsA >= maxWins or winsB >= maxWins:
                break
        return winsA, winsB

    def simOneGame(probA, probB, firstServer):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = firstServer
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
        return scoreA, scoreB

    def gameOver(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return a == 15 or b == 15

    def printSummary(winsA, winsB):
        # Prints a summary of wins for each player.
        n = winsA + winsB
        print("\nGames simulated:", n)
        print(f"Wins for A: {winsA} ({winsA / n:0.1%})")
        print(f"Wins for B: {winsB} ({winsB / n:0.1%})")

    main()
main3()

def main4():
    def main():
        printIntro()
        probA, probB, n, numMatches = getInputs()
        winsA, winsB, shutoutsA, shutoutsB = simMatches(numMatches, n, probA, probB)
        printSummary(winsA, winsB, shutoutsA, shutoutsB)

    def printIntro():
        print("This program simulates a game of racquetball between two")
        print('players called "A" and "B".  The abilities of each player is')
        print("indicated by a probability (a number between 0 and 1) that")
        print("the player wins the point when serving. Player A always")
        print("has the first serve.\n")
        print("player A plays even and player B plays odd")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins a serve?: "))
        b = float(input("What is the prob. player B wins a serve?: "))
        n = int(input("How many games per match (odd number 5 for best of 5)?: "))
        while n % 2 == 0:
            print("enter an odd number")
            n = int(input("How many games per match (odd number 5 for best of 5)?: "))
        numMatches = int(input("How many matches to simulate?: "))
        return a, b, n, numMatches

    def simMatches(numMatches, n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(numMatches):
            winsAinMatch, winsBinMatch, shutoutsAinMatch, shutoutsBinMatch = simOneMatch(n, probA, probB)
            if winsAinMatch > winsBinMatch:
                winsA += 1
            else:
                winsB += 1
            shutoutsA += shutoutsAinMatch
            shutoutsB += shutoutsBinMatch
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneMatch(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        maxWins = (n + 1) // 2
        for gameNum in range(1, n + 1):
            firstServer = "A" if gameNum % 2 == 1 else "B"
            scoreA, scoreB = simOneGame(probA, probB, firstServer)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
            if winsA >= maxWins or winsB >= maxWins:
                break
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGame(probA, probB, firstServer):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = firstServer
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
        return scoreA, scoreB

    def gameOver(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return a == 15 or b == 15

    def printSummary(winsA, winsB, shutoutsA, shutoutsB):
        # Prints a summary of wins for each player.
        n = winsA + winsB
        print("\nGames simulated:", n)
        print(f"Wins for A: {winsA} ({winsA / n:0.1%})")
        print(f"Shutouts for A: {shutoutsA} ({shutoutsA/winsA:0.1%} of wins)" if winsA > 0 else "Shutouts for A: 0 (0.0% of wins)")
        print(f"Wins for B: {winsB} ({winsB / n:0.1%})")
        print(f"Shutouts for B: {shutoutsB} ({shutoutsB/winsB:0.1%} of wins)" if winsB > 0 else "Shutouts for B: 0 (0.0% of wins)")

    main()
main4()

def main5():
    def main():
        printIntro()
        probA, probB, n = getInputs()
        winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
        printSummary(winsA, winsB, shutoutsA, shutoutsB)

    def printIntro():
        print("This program simulates a game of vollyball between two")
        print('players called "A" and "B".  The abilities of each player is')
        print("indicated by a probability (a number between 0 and 1)")
        print("only serving team can score games played to 15")
        print("points need to be won by atleast 2. A serves first.\n")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins a serve?: "))
        while not 0 <= a <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            a = float(input("What is the prob. player A wins a serve?: "))
        b = float(input("What is the prob. player B wins a serve?: "))
        while not 0 <= b <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            b = float(input("What is the prob. player A wins a serve?: "))
        n = int(input("How many games to simulate: "))
        while n <= 0:
            print("Number of games needs ot be positive and above 0")
            n = int(input("How many games to simulate: "))
        return a, b, n

    def simNGames(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(n):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGame(probA, probB):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = "A"
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
        return scoreA, scoreB

    def gameOver(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return (a >= 15 or b >= 15) and abs(a - b) >= 2

    def printSummary(winsA, winsB, shutoutsA, shutoutsB):
        # Prints a summary of wins for each player.
        n = winsA + winsB
        print("\nGames simulated:", n)
        print(f"Wins for A: {winsA} ({winsA / n:0.1%})")
        print(f"Shutouts for A: {shutoutsA} ({shutoutsA/winsA:0.1%} of wins)" if winsA > 0 else "Shutouts for A: 0 (0.0% of wins)")
        print(f"Wins for B: {winsB} ({winsB / n:0.1%})")
        print(f"Shutouts for B: {shutoutsB} ({shutoutsB/winsB:0.1%} of wins)" if winsB > 0 else "Shutouts for B: 0 (0.0% of wins)")

    main()
main5()

def main6():
    def main():
        printIntro()
        probA, probB, n = getInputs()
        winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
        printSummary(winsA, winsB, shutoutsA, shutoutsB)

    def printIntro():
        print("This program simulates a game of vollyball between two")
        print('players called "A" and "B".  The abilities of each player is')
        print("indicated by a probability (a number between 0 and 1)")
        print("only serving team can score games played to 25")
        print("points need to be won by atleast 2. A serves first.\n")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins a serve?: "))
        while not 0 <= a <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            a = float(input("What is the prob. player A wins a serve?: "))
        b = float(input("What is the prob. player B wins a serve?: "))
        while not 0 <= b <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            b = float(input("What is the prob. player A wins a serve?: "))
        n = int(input("How many games to simulate: "))
        while n <= 0:
            print("Number of games needs ot be positive and above 0")
            n = int(input("How many games to simulate: "))
        return a, b, n

    def simNGames(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(n):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGame(probA, probB):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = "A"
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if random() < probA:
                scoreA += 1
                serving = "A"
            else:
                scoreB += 1
                serving = "B"
        return scoreA, scoreB

    def gameOver(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

    def printSummary(winsA, winsB, shutoutsA, shutoutsB):
        # Prints a summary of wins for each player.
        n = winsA + winsB
        print("\nGames simulated:", n)
        print(f"Wins for A: {winsA} ({winsA / n:0.1%})")
        print(f"Shutouts for A: {shutoutsA} ({shutoutsA/winsA:0.1%} of wins)" if winsA > 0 else "Shutouts for A: 0 (0.0% of wins)")
        print(f"Wins for B: {winsB} ({winsB / n:0.1%})")
        print(f"Shutouts for B: {shutoutsB} ({shutoutsB/winsB:0.1%} of wins)" if winsB > 0 else "Shutouts for B: 0 (0.0% of wins)")

    main()
main6()

def main7():
    def main():
        printIntro()
        probA, probB, n = getInputs()
        winsAsideout,winsBsideout, shutoutsAsideout, shutoutsBsideout = simNGamesSideout(n, probA, probB)

        winsArally, winsBrally, shutoutsArally, shutoutsBrally = simNGamesRally(n, probA, probB)
        printSummary(winsAsideout, winsBsideout, shutoutsAsideout, shutoutsBsideout,
                     winsArally, winsBrally, shutoutsArally, shutoutsBrally, n, probA, probB)

    def printIntro():
        print("Bla Bla Bla compaires the 2 programs scoring")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins?: "))
        while not 0 <= a <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            a = float(input("What is the prob. player A wins a serve?: "))

        b = float(input("What is the prob. player B wins?: "))
        while not 0 <= b <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            b = float(input("What is the prob. player A wins a serve?: "))

        n = int(input("How many games to simulate: "))
        while n <= 0:
            print("Number of games needs ot be positive and above 0")
            n = int(input("How many games to simulate: "))
        return a, b, n

    def simNGamesSideout(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(n):
            scoreA, scoreB = simOneGameSideout(probA, probB)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGameSideout(probA, probB):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = "A"
        scoreA = 0
        scoreB = 0
        while not gameOverSideout(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving ="A"
        return scoreA, scoreB

    def gameOverSideout(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return (a >= 15 or b >= 15) and abs(a - b) >= 2

    def simNGamesRally(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(n):
            scoreA, scoreB = simOneGameRally(probA, probB)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGameRally(probA, probB):
        serving = "A"
        scoreA = 0
        scoreB = 0
        while not gameOverRally(scoreA, scoreB):
            if random() < probA:
                scoreA += 1
                serving = "A"
            else:
                scoreB += 1
                serving = "B"
        return scoreA, scoreB

    def gameOverRally(a, b):
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

    def printSummary(winsAsideout, winsBsideout, shutoutsAsideout, shutoutsBsideout,
                     winsArally, winsBrally, shutoutsArally, shutoutsBrally, n, probA, probB):
        print(f"comparison of the 2 scoring systems wiht {n} games simulated\n")

        print(f"side out: winsof A: {winsAsideout} ({winsAsideout/n:0.1%}) with {shutoutsAsideout} shutouts ({shutoutsAsideout/winsAsideout:0.1%} of wins)" if winsAsideout > 0 else "Shutouts for A: 0 (0.0% of wins)")
        print(f"side out: winsof B: {winsBsideout} ({winsBsideout/n:0.1%}) with {shutoutsBsideout} shutouts ({shutoutsBsideout/winsBsideout:0.1%} of wins)" if winsBsideout > 0 else "Shutouts for B: 0 (0.0% of wins)")

        print(f"rally: winsof A: {winsArally} ({winsArally/n:0.1%}) with {shutoutsArally} shutouts ({shutoutsArally/winsArally:0.1%} of wins)" if winsArally > 0 else "rally for A: 0 (0.0% of wins)")
        print(f"rally: winsof B: {winsBrally} ({winsBrally/n:0.1%}) with {shutoutsBrally} shutouts ({shutoutsBrally/winsBrally:0.1%} of wins)" if winsBrally > 0 else "rally for B: 0 (0.0% of wins)")

        winPctSideout = winsAsideout / n
        winPctRally = winsArally / n
        print("Comparing advantage results:")
        print(f"team A win percentage with side out: {winPctSideout:0.1%}")
        print(f"team A win percentage with rally: {winPctRally:0.1%}")
        diffrence = winPctRally - winPctSideout
        if abs(diffrence) < 0.05:
            print("scoring has not significant effect on team A advantage")
        elif diffrence > 0:
            print(f"rally scoring increases teams A advantage by {diffrence:0.01%}")
        else:
            print(f"rally scoring decreases teams A advantage by {diffrence:0.01%}")
    main()
main7()

def main8():
    def main():
        printIntro()
        probA, probB, n = getInputs()
        winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
        printSummary(winsA, winsB, shutoutsA, shutoutsB)

    def printIntro():
        print("This program simulates a game of table tennis")

    def getInputs():
        # Returns the three simulation parameters
        a = float(input("What is the prob. player A wins a serve?: "))
        while not 0 <= a <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            a = float(input("What is the prob. player A wins a serve?: "))
        b = float(input("What is the prob. player B wins a serve?: "))
        while not 0 <= b <= 1:
            print("prob must be inbetween 0 and 1 (a decimal .5 is 50% chnace)")
            b = float(input("What is the prob. player A wins a serve?: "))
        n = int(input("How many games to simulate: "))
        while n <= 0:
            print("Number of games needs ot be positive and above 0")
            n = int(input("How many games to simulate: "))
        return a, b, n

    def simNGames(n, probA, probB):
        winsA = winsB = shutoutsA = shutoutsB = 0
        for i in range(n):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                winsA += 1
                if scoreB == 0:
                    shutoutsA += 1
            else:
                winsB += 1
                if scoreA == 0:
                    shutoutsB += 1
        return winsA, winsB, shutoutsA, shutoutsB

    def simOneGame(probA, probB):
        # Simulates a single game or racquetball between players whose
        #    abilities are represented by the probability of winning a serve.
        # Returns final scores for A and B
        serving = "A"
        scoreA = 0
        scoreB = 0
        pointsPlayed = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
            pointsPlayed += 1
            if pointsPlayed % 2 == 0:
                serving = "B" if serving == "A" else "A"
        return scoreA, scoreB

    def gameOver(a, b):
        # a and b represent scores for a racquetball game
        # Returns True if the game is over, False otherwise.
        return (a >= 11 or b >= 11) and abs(a - b) >= 2

    def printSummary(winsA, winsB, shutoutsA, shutoutsB):
        # Prints a summary of wins for each player.
        n = winsA + winsB
        print("\nGames simulated:", n)
        print(f"Wins for A: {winsA} ({winsA / n:0.1%})")
        print(f"Shutouts for A: {shutoutsA} ({shutoutsA / winsA:0.1%} of wins)" if winsA > 0 else "Shutouts for A: 0 (0.0% of wins)")
        print(f"Wins for B: {winsB} ({winsB / n:0.1%})")
        print(f"Shutouts for B: {shutoutsB} ({shutoutsB / winsB:0.1%} of wins)" if winsB > 0 else "Shutouts for B: 0 (0.0% of wins)")

    main()
main8()

def main9():
    def rollDice():
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        return die1 + die2

    def oneGame():
        firstRoll = rollDice()
        if firstRoll in [2, 3, 12]:
            return False
        elif firstRoll in [7, 11]:
            return True
        else:
            point = firstRoll
            while True:
                roll = rollDice()
                if roll == point:
                    return True
                elif roll == 7:
                    return False

    def simGames(n):
        wins = 0
        for i in range(n):
            if oneGame():
                wins += 1
        return wins

    def summery(wins, n):
        print(f"{n} games simulated")
        print(f"Wins: {wins} ({wins/n:0.1%})")
        print(f"Win probability: {wins/n}:.3f")

    n = int(input("How many games do you want to sim?: "))
    wins = simGames(n)
    summery(wins, n)
main9()

def main10():
    def drawCards():
        rank = randrange(0, 13)
        if rank == 0:
            return 1, True
        elif rank >= 10:
            return 10, False
        else:
            return rank + 1, False

    def oneGame():
        total = 0
        hasAce = False
        while total < 17:
            cardValue, isAce = drawCards()
            total += cardValue
            if isAce:
                hasAce = True
            if hasAce and 17 <= total + 10 <= 21:
                total += 10
        return total > 21

    def simGames(n):
        busts = 0
        for i in range(n):
            if oneGame():
                busts += 1
        return busts

    def summary(busts, n):
        print(f"{n} games simulated")
        print(f"dealers busts: {busts} ({busts/n:0.1%})")
        print(f"probability of dealer busting {busts/n:.3f}")

    n = int(input("How many games do you want to sim?: "))
    busts = simGames(n)
    summary(busts, n)
main10()

def main11():
    def drawCards():
        rank = randrange(0, 13)
        if rank == 0:
            return 1, True
        elif rank >= 10:
            return 10, False
        else:
            return rank + 1, False

    def oneGame(startValue, startIsAce):
        total = startValue
        hasAce = startIsAce
        while total < 17:
            cardValue, isAce = drawCards()
            total += cardValue
            if isAce:
                hasAce = True
            if hasAce and 17 <= total + 10 <= 21:
                total += 10
        return total > 21

    def simGames(n, startValue, startIsAce):
        busts = 0
        for i in range(n):
            if oneGame(startValue, startIsAce):
                busts += 1
        return busts

    def summary(bustsAtStart, n):
        print(f"{n} games simulated")
        print("card name | dealer busts | probability")
        for start_Value in range(1, 11):
            bustss = bustsAtStart[start_Value]
            prob = bustss/n
            cardName = "Ace" if start_Value == 1 else "10" if start_Value == 10 else str(start_Value)
            print(f"{cardName:<13} | {bustss:<5} | {prob:0.3f} ({prob:0.1%})")

    n = int(input("How many games do you want to sim?: "))
    bustsAtStart = {}
    for startValue in range(1, 11):
        isAce = (startValue == 1)
        busts = simGames(n, startValue, isAce)
        bustsAtStart[startValue] = busts
    summary(bustsAtStart, n)
main11()

def main12():
    def simDarts(n):
        hits = 0
        for i in range(n):
            if inCircle():
                hits += 1
        return hits

    def inCircle():
        x = 2 * random() - 1
        y = 2 * random() - 1
        return x*x + y*y <= 1

    def summary(hits, n):
        estimatedPi = 4 * hits / n
        print(f"{n} darts thrown")
        print(f"hits: {hits} ({hits/n:0.1%}), estimate of pi: {estimatedPi:.6f}, actual value of pi: {m.pi:.6f}, estimate error: {abs(estimatedPi - m.pi):.6f}")

    n = int(input("How many games do you want to sim?: "))
    summary(simDarts(n), n)
main12()

def main13():
    def fiveOfKind():
        dice = [randrange(1, 7) for _ in range(5)]
        return all(die == dice[0] for die in dice) #if all 5 dic are the same

    def rolls(n):
        hits = 0
        for i in range(n):
            if fiveOfKind():
                hits += 1
        return hits

    def summary(hits, n):
        estimateProb = hits/n
        theoreticalProb = 6 / 6**5
        print(f"{n} rolls simulated")
        print(f"five of a kind rolls: {hits} ({hits/n:0.3%}), estimate: {estimateProb:.6f}, theoretical probability: {theoreticalProb:0.6f}, estimate error: {abs(estimateProb - theoreticalProb):.6f}")

    n = int(input("How many games do you want to sim?: "))
    summary(rolls(n), n)
main13()

def main14():
    def simAvgWalks(n, trials):
        totalDistance = 0
        totalHeads = 0
        for i in range(trials):
            distance, heads = walk(n)
            totalDistance += distance
            totalHeads += heads
        return totalDistance / trials, totalHeads / trials

    def walk(n):
        distance = 0
        heads = 0
        for i in range(n):
            if flip():
                heads += 1
                distance += 1
            else:
                distance -= 1
        return distance, heads

    def flip():
        #heads +1(true) tails -1(false)
        return choice((True, False))

    def summary(n, trials, distance, heads, avgDist, avgHead):
        print(f"{n} total steps")
        print(f"distance of {distance}, with a total of {heads} heads first game")
        print(f"{trials} total trials")
        print(f"average distance of {avgDist}, with and average of {avgHead}")

    n = int(input("How many games do you want to sim?: "))
    trials = int(input("How many trials of the game do you want to sim?: "))
    distance, heads = walk(n)
    avgDistance, avgHeads = simAvgWalks(n, trials)
    summary(n, trials, distance, heads, avgDistance, avgHeads)
main14()

def main15():
    def getInputs():
        while True:
            try:
                n = int(input("How many squares are in the siewalk: "))
                if n < 2:
                    print("Number must be over 2")
                    continue
                break
            except ValueError:
                print("Enter a valid number")
        return n

    def walk(n):
        visits = [0] * n
        position = n // 2
        heads = 0
        totalSteps = 0
        visits[position] += 1
        while 0 <= position < n:
            if flip():
                heads += 1
                position += 1
            else:
                position -= 1
            totalSteps += 1
            if 0 <= position < n:
                visits[position] += 1
            else:
                break
        return visits, totalSteps, heads

    def flip():
        return choice((True, False))

    def summary(n, visits, totalSteps, heads):
        #window setup
        winWidth = max(800, n * 50)
        winHeight = 600
        win = GraphWin(f"Histogram for {n} squares", winWidth, winHeight)
        win.setBackground("black")

        #bar dimentions
        margin = 40
        barWidth = (winWidth - 2 * margin) / n
        maxHeight = winHeight - 2 * margin
        maxVisits = max(visits) if max(visits) > 0 else 1 #stops division of 0

        #drawing bars
        for i in range(n):
            height = (visits[i] / maxVisits) * maxHeight if maxVisits > 0 else 0
            x1 = margin + i * barWidth
            y1 = winHeight - margin #bottom bar
            x2 = x1 + barWidth * 0.9 #narow for spacing
            y2 = y1 - height #top

            bar = Rectangle(Point(x1, y1), Point(x2, y2))
            bar.setFill("blue")
            bar.draw(win)

            label = Text(Point((x1 + x2) / 2, y1 + 20), f"Square {i}")
            label.setTextColor("white")
            label.draw(win)

            countLabel = Text(Point((x1 + x2) /2, y2 - 20), f"{visits[i]}")
            countLabel.setTextColor("white")
            countLabel.draw(win)

        print(f"sidewalk of {n} squares 0 to {n-1}")
        print(f"total steps {totalSteps} and total of {heads} heads")

        win.getMouse()
        win.close()

    n = getInputs()
    visits, totalSteps, heads = walk(n)
    summary(n, visits, totalSteps, heads)
main15()

def main16():
    def getInputs():
        while True:
            try:
                n = int(input("How many steps to take: "))
                if n < 1:
                    print("Number must be over 1")
                    continue
                break
            except ValueError:
                print("Enter a valid number")

        while True:
            try:
                trials = int(input("How many trials to run: "))
                if n < 1:
                    print("Number must be over 1")
                    continue
                break
            except ValueError:
                print("Enter a valid number")
        return n, trials

    def walk(n):
        x, y = 0, 0
        for i in range(n):
            direction = choice(["up", "down", "left", "right"])
            if direction == "up":
                y += 1
            elif direction == "down":
                y -= 1
            elif direction == "left":
                x -= 1
            elif direction == "right":
                x += 1
        return m.sqrt(x**2 + y**2)

    def simulateWalks(n, trials):
        totalDistance = 0
        for i in range(trials):
            distance = walk(n)
            totalDistance += distance
        return totalDistance / trials

    def summary(n, trials, avgDistance):
        print(f"steps per walk {n}")
        print(f"trials {trials}")
        print(f"average distance was {avgDistance:.3f}")

    n, trials = getInputs()
    avgDistance = simulateWalks(n, trials)
    summary(n, trials, avgDistance)

main16()

def main17():
    def getInputs():
        while True:
            try:
                n = int(input("How many steps to take: "))
                if n <= 0:
                    print("must be above 0")
                    continue
                break
            except ValueError:
                print("enter a number")
        return n
    def walk(n:int):
        winWidth = 600
        winHeight = 600
        win = GraphWin(f"random walk {n} steps", winWidth, winHeight)
        win.setBackground("black")

        #breaking down 600 x 600 to 100x100
        gridSize = 100
        scale = winWidth / gridSize #6px per grid
        offsetX = winWidth / 2 #center is 300, 300
        offsetY = winHeight / 2

        #starting spot of middle of the map
        x, y = 50.0, 50.0
        trajectory = [(x, y)]

        #draws staring dot
        start = Circle(Point(offsetX, offsetY), 3)
        start.setFill("red")
        start.draw(win)

        #does the walking and draws as it walks
        for i in range(n):
            angle = random() * 2 * m.pi
            x += m.cos(angle)
            y += m.sin(angle)
            trajectory.append((x, y))

            #draws lines where it travels
            x1, y1 = trajectory[-2]
            x2, y2 = trajectory[-1]
            p1 = Point(x1 * scale, winHeight - y1 * scale)
            p2 = Point(x2 * scale, winHeight - y2 * scale)
            line = Line(p1,p2)
            line.setFill("blue")
            line.draw(win)

            #"animation"
            time.sleep(0.05)

        #draw final point
        finalX, finalY = trajectory[-1]
        final = Circle(Point(finalX * scale, winHeight - finalY * scale), 3)
        final.setFill("green")
        final.draw(win)

        #lables of location
        startLable = Text(Point(offsetX + 20, winHeight - offsetY + 20), "start (50,50)")
        startLable.setTextColor("white")
        startLable.draw(win)

        finalLabel = Text(Point(finalX * scale + 20, winHeight - finalY * scale + 20),f"end ({finalX:.1f},{finalY:.1f})")
        finalLabel.setTextColor("white")
        finalLabel.draw(win)

        win.getMouse()
        win.close()

    n = getInputs()
    walk(n)

main17()

#def main18()
#main18()
