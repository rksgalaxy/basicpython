'''Creating a Function'''

#def means defining function def always contain :
#1 No argument/parameter function
def My_function():
    print('Welcome home')


My_function()

print('12')


#2 Functions With one arguments
def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("This")
print_with_exclamation("Is")
print_with_exclamation("My")
print_with_exclamation("College")


def print_square_of(Number):
    # print(int(Number)*int(Number))
    print(int(Number) ** 2)


x = input("Enter a Number N= ")
print_square_of(x)


# table print
def print_table_of(Num):
    # X = int(input('enter any Number '))
    for P in range(1, 11):
        z = Num * P
        print(z)


t = int(input("Enter a number to print table"))
print_table_of(t)


#3 function with two argument
def print_two_added_number(Num1,Num2):
    print(int(Num1)+ int(Num2))

Num1 = input('Enter First Number \n Num1 =  ')
Num2 = input('Enter Second Number \n Num2 = ')
print_two_added_number(Num1,Num2)
