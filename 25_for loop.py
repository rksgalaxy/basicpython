'''
    SYNTAX:
    for var_name in iterable:
        ...
        ...

    where iterable can be list[],tuples() or any object(dict{} ,set()) that can be iterate
'''
#printing odd number
for a in range (1,10,2):
    print(a)
print('-------------------------------------')
#print even number
for b in range(2,10,2):
    print(b)
#to show the list of range use the list function
print(list(range(0,20,3)))

#print 1 to 10
print("print one to ten")
for i in range(11):
    print(i)

#accessng list element using loop
n=['Amritesh',11 , 12]
for j in n:
    print(j)

print("print all element of list for float")

i=[1,11,111,2.0,11,22,33,55,33.98,4.1435]
for p in i:
    print(p)


words = ["hello","world","spams","eggs"]
counter = 0 #counter is vaariable here
max_index = len (words)
word = words[counter]
for counter in range(max_index,1):
    print(word +"!")
