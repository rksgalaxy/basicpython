words = ["hello","world","spams","eggs"]
counter = 0 #counter is vaariable here
max_index= len (words)
while counter < max_index:
    word = words[counter]
    print(word +"!" )
    counter= counter +1

#by for loop
#words = ["hello","world","spams","eggs"]
for p in words:
    print(p)
for p in words:
   print(p + '?')


#words = ["hello","world","spams","eggs"]
for d in range(len(words)):
    print(words[d]+'..')
