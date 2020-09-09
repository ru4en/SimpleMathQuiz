import random #
import os

def clear():
    os.system("clear")

def Add():
    num = (int(random.randint(0,99999)))
    num1 = (int(random.randint(0,99999)))
    print("Addition")
    print("")
    print(num, "+")
    print(num1)
    print("")
    aAns = str(num + num1)
#    print(aAns)
    ans = str(input(":"))
    if ans == aAns:
        clear()
        print ("Correct Answer!")
        Add()
    elif ans == "q":
        clear()
        main()
    else:
        clear()
        print("Wrong Answer! Correct Answer is ", aAns)
        Add()


def Sub():
    num = (int(random.randint(0,99999)))
    num1 = (int(random.randint(0,9999)))
    print("Subtraction")
    print("")
    print(num, "_")
    print(num1)
    print("")
    aAns = str(num - num1)
#    print(aAns)
    ans = str(input(":"))
    if ans == aAns:
        clear()
        print ("Correct Answer!")
        Sub()
    elif ans == "q":
        clear()
        main()
    else:
        clear()
        print("Wrong Answer! Correct Answer is ", aAns)
        Sub()

def Mult():
    num = (int(random.randint(0,99)))
    num1 = (int(random.randint(0,99)))
    print("Multipication")
    print("")
    print(num, " *")
    print(num1)
    print("")
    aAns = str(num * num1)
#    print(aAns)
    ans = str(input(":"))
    if ans == aAns:
        clear()
        print ("Correct Answer!")
        Mult()
    elif ans == "q":
        clear()
        main()
    else:
        clear()
        print("Wrong Answer! Correct Answer is ", aAns)
        Mult()

def Div():
    num = (int(random.randint(0,999)))
    num1 = (int(random.randint(0,99)))
    print("Division")
    print("")
    print("NOTE: put 2 desimal places. EG N.nn ")
    print(" if answer is a Whole number put 0 after desimal place EG N.0")
    print("")
    print("   ______")
    print(num1,"|", num)
    print("")

    aAns = float(num / num1)
    aAns = round(aAns, 2)
    aAns = str(aAns)
#    print(aAns)
    ans = str(input(":"))
    if ans == aAns:
        clear()
        print ("Correct Answer!")
        Div()
    elif ans == "q":
        clear()
        main()
    else:
        clear()
        print("Wrong Answer! Correct Answer is ", aAns)
        Div()

def Bin():
    num = (int(random.randint(0,255)))
#    print(num)
    print("Binary Conversion")
    print("")
    bina = bin(num).replace("0b", "")
    num = str(num)
    print(bina)
    print("")
    ans = str(input(":"))
    if ans == num:
        clear()
        print("Correct Answer!")
        Bin()
    elif ans == "q":
        clear()
        main()
    else:
        clear()
        print("Wrong Answer! Correct Answer was", num)
        Bin()

def main():
    clear()
    print ("Choose the type of arithmetic quiz")
    print ("1   Addition")
    print ("2   Subtraction")
    print ("3   Multipication")
    print ("4   Division")
    print ("5   Binary Conversion")
    print ("Q   To Go Back")

    quizType = input(":")

    if quizType == "1":
        clear()
        Add()
    elif quizType == "2":
        clear()
        Sub()
    elif quizType == "3":
        clear()
        Mult()
    elif quizType == "4":
        clear()
        Div()
    elif quizType == "5":
        clear()
        Bin()
    else:
        print("end")
        clear()

main()
