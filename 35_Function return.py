def print_square_cube_of(Number):
    # print(int(Number)*int(Number))
    z = int(Number) ** 2
    c = int(Number) ** 3
    print(z)
    return z, c


x = input("Enter a Number N= ")
p = print_square_cube_of(x)

print(p)
print(type(p))


