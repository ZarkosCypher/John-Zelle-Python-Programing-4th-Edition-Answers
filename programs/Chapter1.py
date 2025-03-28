##!!Teachers Feedback and Grade - 72% - Points deducted for missing paragraphs and for missing question 7 from the 4th edition.

print("Hello, world!")
#Hello, world!
print("Hello", "world!")
#Hello world!
print(3)
#3
print(3.0)
#3.0
print(2+3)
#5
print(2.0 + 3.0)
#5.0
print("2" + "3")
#23
print("2 + 3 =", 2 + 3)
#2 + 3 =5
print(2 * 3)
#6
print(2 ** 3)
#8
print(7 / 3)
#2.3333333333333335
print(7 // 3)
#2

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

def main3():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main3()
#the program runs difrently for both and the numbers on the second one end up smaller than the ones of the first one.

def main4():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

main4()

def main5():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    usr = eval(input("How many numbers should be printed?: "))
    for x in range(usr):
        x = 3.9 * x * (1 - x)
        print(x)

main5()

def main6a():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(100):
        x = 3.9 * x * (1 - x)
        print(x)

main6a()

def main6b():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(100):
        x = 3.9 * (x - x * x)
        print(x)

main6b()

def main6c():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for x in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)

main6c()

def main7():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    for x in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * x * (1 - x)
        print(x, y)

main7()
