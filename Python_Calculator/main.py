import calc
calc_functions = {"add","sub","div","mult"}
while(True):
    choice = input("Choose from: add,sub,div,mult:\n")
    if choice in calc_functions:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        if choice == "add":
            print(calc.add(a,b))
        elif choice == "sub":
            print(calc.sub(a,b))
        elif choice == "div":
            print(calc.div(a,b))
        elif choice == "mult":
            print(calc.mult(a,b))
        repeat = input("Would you like to make another operation?\nYes/No\n")
        if repeat.lower() != "yes":
            print("Process terminated")
            break
    else:
        print("Please enter a correct choice from the options provided")
    