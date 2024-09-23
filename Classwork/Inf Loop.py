num1 = 1
num2 = 1
num3 = 0
print(num1)
print(num2)
while True:
    num3 = num2 + num1
    print(num3)
    cont = input("Continue? Y/N\n>").lower
    if cont == "n":
        break
    num1 = num2
    num2 = num3
    