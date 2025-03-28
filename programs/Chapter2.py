#convert.py
# a program to convirt celcius to ferinhight
def main1through2():
    print("Hello this is a program that converts C(celsius) to F(ferinhight)...")
    c = float(input("What is the celsius temp?: "))
    f = 9/5 * c + 32
    print("The temprature is", f, "degres ferinhight.")
    input("Press the <Enter> key to quit.")
main1through2()

def main3re():
    for i in range(100):
        print(i)
main3re()

#avg2.py
#a simple program to average exam scores
def main3():
    print("This program computes the average of the two exam scores.")
    score1 = float(input("Enter three scores, enter your firts score: "))
    score2 = float(input("Enter a score: "))
    score3 = float(input("Enter a score: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is: ", average)
main3()

def main4():
    for i in range (5):
        print("Hello this is a program that converts C(celsius) to F(ferinhight)...")
        c = float(input("What is the celsius temp?: "))
        f = 9/5 * c + 32
        print("The temprature is", f, "degres ferinhight.")
        input("Press the <Enter> key to enter your conversion. (max of 5)")
main4()

def main5():
    for i in range(10):
        print("Hello this is a program that converts C(celsius) to F(ferinhight) and prints out the numbers 0 to 100 every 10 degres.")
        c = i * 10
        f = 9/5 * c + 32
        print("The temprature is", c, "degrees celcius and", f, "degres ferinhight.")
    input("Press the <Enter> key to quit.")
main5()

#futval.py
#a program to compute the value of an invcensemt
def main6():
    print("This program calculates the future value")
    print("of a 10 year old invesment.")
    principal = float(input("Enter the inicial princiapl: "))
    apr = float(input("Enter the anual interest rate: "))
    years = int(input("enter the amount of years: "))
    for i in range(years):
        principal = principal * (1 + apr)
    print("The value in ", years, "years is:", principal)
main6()

def main7():
    print("This program calculates the future value")
    print("of a 10 year old invesment.")
    apr = float(input("Enter the anual interest rate: "))
    years = int(input("enter the amount of years: "))
    for i in range(years):
        yearlyprincipal = float(input("Enter the inicial princiapl: "))
        principal = yearlyprincipal * (1 + apr)
    print("The value in ", years, "years is:", principal)
main7()

def main8():
    print("This program calculates the future value")
    print("of a 10 year old invesment.")
    apr = float(input("Enter the anual interest rate: "))
    piriod = float(input("What is the piriod: "))
    principal = float(input("Enter the inicial princiapl: "))
    newrate = apr / piriod
    for i in range(10):
        principal = principal * (1 + newrate)

    print("The value in 10 years is:", principal)
main8()

def main9():
    print("This program converts F(ferinhight) to C(celcious)")
    f = float(input("Enter the F(feringight): "))
    c = (f - 32) * 5/9
    print("your degrees in C is ",c)
main9()

def main10():
    print("this converts kilomiters to miles.")
    kl = float(input("Enter the distance in kilomiters"))
    mi = kl / 1.609
    print("that is ", mi, "miles!")
main10()

def main11():
    print("this converts cm to inches")
    cm = float(input("enter the cm: "))
    inch = cm / 2.54
    print("that is ",inch, "inches!")
main11()

def main12():
    print("this is a calculator")
    for i in range(100):
        math = eval(input("enter a math equation: "))
        print("the answer is",math)
main12()

def main12re():
    print("Average of 3 scores.")
    one = float(input("enter score 1: "))
    two = float(input("enter score 2: "))
    three = float(input("enter score 3: "))
    average = (one+two+three)/3
    print("the average is ", average)
main12re()