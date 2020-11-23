while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice =int(input("Enter Your Choice"))
    if(choice >=1 and choice <= 4):
        print("Enter Two  numbers: ")
        num1 = int(input())
        num2 = int(input())
        if choice ==1:
            res =num1 + num2
            print("Results =" ,res)
        elif choice == 2:
                res =num1 - num2
                print("Results =" ,res)
        elif choice == 3:
                res = num1 * num2
                print("Results =", res)

        elif choice == 4:
            res = num1 % num2
            print("Results =", res)

        elif choice == 5:
            exit()
            print("Results =", res)
    else:
        print("Wrong Input ")