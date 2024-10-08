# string = input("> ")
# for char in string :
#     print(char)
# for i in range(string.__len__()) :
#     print(string[-i],end="")

name1 = input("> ")
name2 = input("> ")
nameDict = zip(name1, name2)
for char1, char2 in nameDict:
    print(char1 + ", " + char2)