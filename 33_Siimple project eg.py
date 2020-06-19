print("Enter '1' to Add two number")
print("Enter '2' to Subtract two number")
print("Enter '3' to Multiply two number")
print("Enter '4' to Divide two number")
print("Enter 'Q' to End the program")
user_input = input('Choose options  ')
if user_input == "Q":
    print("Good Bye")
    exit()
elif user_input == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(result)

elif user_input == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(result)

elif user_input == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(result)

elif user_input == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    result1 = num1 % num2
    if result1 == 0.0:
        print(result)
    else:
        print("Quotient = " + str(result))
        print("Reminder = " + str(result1))

