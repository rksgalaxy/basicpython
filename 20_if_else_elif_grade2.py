n = 5000
if n >= 2000:
    print('Moive + Trip')
elif n >= 1500:
    print("Trip")
elif n >= 1000:
    print('movie')
else:
    print('Thinking')
    if n >= 500:
        print('Park')
    else:
        print("Home")
