# print("Rishikesh", end= "")
# print("Is a Good Boy")
# print("I am Rks welcome","you to bhagalpur")
# #escape sequence
# print("Rishikesh \t \n \tKumar\n \t\tSundaram")

# # print Table  by range
# X = int(input('enter any Number '))
# Y = X
# print(Y)
# for i in range(9):
#     Y = X + Y
#     print(Y)
# # print("______________________")
# ## print Table by for loop
# X = int(input('enter any Number '))
# for P in range(1,11):
#     z = X * P
#     print(z)

'''
#1 input and output
a = int(input("Enter First Number"))
b = int(input("Enter second Number"))
print(a + b)


#2 input and output

print("Enter First Number")
Num1 = int(input())
print("Enter Second Number")
Num2 = int(input())
print(Num1 + Num2)


b = input("first no ")
c = input("second no ")
print(int(c)+ int(b))


r = [ "Rishikesh" ]
l = len(r)
print(l)
t = r[0]
print(t)
print(len(t))

# slicing of string
print(t[3:6])
print(t[::2])
print(t[::-1])
print(t[-1])
print(t[-3:-1])

#iterating over string
for f in t:
    print(f)
'''

t= (25,26,27)
print(t)
print(type(t))
print(t[1])
# t[1]= 29   error bcoz tuple cant be assign
print(t.index(25))

l = list(t)
l[1]= 29
print(l)
t=tuple(l)
print(t)