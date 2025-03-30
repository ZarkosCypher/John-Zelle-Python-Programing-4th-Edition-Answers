import math
from wsgiref.simple_server import demo_app


def main():

    def p1():
        print("This calculates the volume and surface area from a spheres radius.")
        radius = float(input("Enter the radius: "))
        volume = (4/3) * math.pi * radius ** 3
        area = 4 * math.pi * radius ** 2
        print("The volume is,", volume, "and the area is,", area)
    p1()

    def p2():
        print("This calculates the cost per square inch of a circular pizza given the diameter and price.")
        diameter = float(input("What is the diameter of the pizza?: "))
        cost = float(input("What is the cost of the pizza?: "))
        radius = diameter / 2
        area = math.pi * radius ** 2
        cost_pr_sqr_inch = cost / area
        print("The cost per square inch is,", cost_pr_sqr_inch)
    p2()

    def p3():
        print("This program computes the molecular weight of a carbohydrate based on the number of hydrogen carbon and oxygen atoms in the molecule.")
        h = 1.00794
        c = 12.0107
        o = 15.9994
        h_count = int(input("How many Hydrogen atoms are in the molecule?: "))
        c_count = int(input("How many Carbon atoms are in the molecule?: "))
        o_count = int(input("How many Oxygen atoms are in the molecule?: "))
        weight = (h_count * h) + (c_count * c) + (o_count * o)
        print("The weight is ", weight, "in grams per mole")
    p3()

    def p4():
        print("This program determines the distance to a lightning bolt strike based on the time elapsed between the flash and sound.")
        sound_speed = 1100 #feet per second
        feet_per_mile = 5280 #feet
        seconds = float(input("Enter the amount of time it took in seconds: "))
        distance_feet = sound_speed * seconds
        distance_mile = distance_feet / feet_per_mile
        print("There is about ", distance_mile, "miles between you and the lightning strike.")
    p4()

    def p5():
        print("This will calculate the cost of your Konditorei Coffee Shop order.")
        coffee = 15.50 #$ per lbs
        shipping = 0.99 #$ per lbs
        fixed_rate = 4.50 #$ fixed fee
        order = float(input("Enter how many Pounds (lbs) of coffee would you like to buy?: "))
        amount_due = fixed_rate + (order * shipping) + (coffee * order)
        print("The amount due is $", amount_due)
    p5()

    def p6():
        print("This program calculates the slope of a line through two non-vertical points entered.")
        x1 = float(input("enter the x1: "))
        y1 = float(input("enter the y1: "))
        x2 = float(input("enter the x2: "))
        y2 = float(input("enter the y2: "))
        slope = (y2 - y1) / (x2 - x1)
        print("The slope is ", slope)
    p6()

    def p7():
        print("This program will determine the distance of the 2 points you have entered")
        x1 = float(input("enter the x1: "))
        y1 = float(input("enter the y1: "))
        x2 = float(input("enter the x2: "))
        y2 = float(input("enter the y2: "))
        distance = math.sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("the distance is ", distance)
    p7()

    def p8():
        print("This program takes a four digit year and then returns the epact.")
        year = int(input("Enter a 4 digit year: "))
        c = year // 100
        epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
        print("The epact is", epact)
    p8()

    def p9():
        print("This program calculates the area of a triangle given the length of the 3 sides")
        a = float(input("enter the length of side a: "))
        b = float(input("enter the length of side b: "))
        c = float(input("enter the length of side c: "))
        s = (a + b + c)/2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("The area is ", area)
    p9()

    def p10():
        print("This will determine a length of a ladder for a certain height while leaning")
        height = float(input("Enter the height required: "))
        degrees = float(input("Enter the angle in degrees the ladder needs to be to be stable: "))
        angel_radians = (math.pi / 180) * degrees
        length = height / math.sin(angel_radians)
        print("The height of the ladder needed is ", length)
    p10()

    def p11():
        print("This program finds the sum of the first n natural numbers if provided by you.")
        n = int(input("Enter how many n numbers to add: "))
        total = 1
        for i in range(n):
            total = total + i
        print("The total is ", total)
    p11()

    def p12():
        print("This program finds the sum and cubes of the first n natural numbers if provided by you.")
        n = int(input("Enter how many n numbers to add and cube: "))
        total = 1
        for i in range(n):
            total = total + i
            total = total ** 3
        print("The total is ", total)
    p12()

    def p13():
        print("This prints a sum of how ever many numbers you want.")
        how_many = int(input("How many numbers do you want to add?: "))
        total = 0
        for i in range(how_many):
            x = float(input("Enter a number to add: "))
            total += x
        print("the total is ", total)
    p13()

    def p14():
        print("This prints a average of how ever many numbers you want.")
        how_many = int(input("How many numbers do you want to add?: "))
        total = 0
        for i in range(how_many):
            x = float(input("Enter a number to add: "))
            total += x
        average = total / how_many
        print("the average is ", average)
    p14()

    def p15():
        n = int(input("enter the number:"))

        pi_approx = 0
        for i in range(n):
            denom = 2*i+1
            term = 4 /denom * (-1)**i
            pi_approx += term

        print("aproximation of pi with ",n,"is",pi_approx)
        print(f"real pi is {math.pi:.10f}")
    p15()

    def p16():
        num1 = 0
        num2 = 1

        n = int(input("enter what to go to in fibinachi: "))

        for i in range(2, n + 1):
            num1, num2 = num2, num1 + num2

        print("the fibinachi number is",num2)
    p16()

    def p17():
        #this assingment makes no sence but this is what i understood form it
        x = input("enter a value: ")
        y = input("enter how many times: ")

        guess = x / 2

        for i in range(y):
            guess = (guess + x / guess) / 2
        print("the program computed:",guess," and the diffrence from the real answer is:",(guess-math.sqrt(x)))

    p17()

main()
