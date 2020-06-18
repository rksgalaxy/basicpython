# append functions - add the items to list
nums = [1, 2, 3]
nums.append(4)
print(nums)

names = ['Rishikesh', 'Kumar']
names.append('Sundaram')
print(names)

# len functions - count the numbers of items in the list

Names = ['Rishikesh', 'Kumar', 'Sundaram', 'TIger', 'Shroff']
print(len(Names))

# insert method - It is like append function to add items at any position

nam = ['Rakesh', 'Brother']
print(len(nam))
index = 1
nam.insert(index, 'Is')
print(nam)
print(len(nam))

# index method  it returns the number of index

customer = ['amit', 'Babloo', 'chhotu', 'Dilip', 'Rakesh', 'prakash', 'panchal', 'Ronny']
print(customer.index("Babloo"))
print(customer.index('Ronny'))

# max(list) , min(list) , list.count(obj) , list.remove(obj) , list.reverse()
print('woking in functions maxx min  count remove reverse')

r = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 22, 23.21, 22]
print(max(r))
print(min(r))
print(r.count(22))
print(r.remove(25))
print(r)
print(r.reverse())
print(r)


p= list('Rishikesh')
print(p)
p.reverse()
print(p)
L = ''
for d in p:
    L= L+d
    print(L)
print(L)

#join function add all the element of list
e= list('Amritesh')
e. reverse()
print(''.join(e))

