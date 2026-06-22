# Simple Calculator

while True:
    print("---- Simple Calculator ----")
    print(" 1 . Addition")
    print(" 2 . Subtraction")
    print(" 3 . Muliplication ")
    print(" 4 . Division ")
    print(" 5 . Exit ")

    choice = int(input("Enter your Choice "))

    if choice == 5:
        print("Calculator Closed")
        break

    num1 = float(input("enter first Number"))
    num2 = float(input("enter second Number"))

    if choice == 1:
        print("Result : ",num1+num2)
    elif choice == 2:
        print("Result : ",num1-num2)
    elif choice == 3:
        print("Result : ",num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result : ",num1 / num2)
        else :
            print(" Cann't divide by Zero")
    else:
        print("Invalid Choice")