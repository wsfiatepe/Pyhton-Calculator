import re

print("Welcome to My Calculator")
print("Enter 'quit' to exit\n")

previous = 0
run = True
equation = ""


def calc():
    global run
    global previous
    global equation

    if previous == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye and Stay Safe")
        run = False
    else:
        equation = re.sub('[A-z,.:()""]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    calc()
