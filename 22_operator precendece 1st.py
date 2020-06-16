a = False == False or True
b = False == (False or True)
c = (False == False) or True

x = 5==6 == 5==8 or 60==60
y = 1==2 == (3==4 or 8==8)
z = (9==90 == 2>8) or 3<4
print(a)
print(b)
print(c)
print(x)
print(y)
print(z)