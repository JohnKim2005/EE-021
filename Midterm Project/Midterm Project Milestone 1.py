
birthYear = ""
currentYear = 2024

print("What is your Full Name?")
fullName = input(" > ")

while birthYear == "":
    print("\nWhat is your Year of Birth?")
    birthYear = input(" > ")
    if not birthYear.isdigit():
        print("\nPlease input a valid number as the birth year.", end = "")
        birthYear = ""
    elif int(birthYear) > currentYear:
        print("\nPlease input a year that is not in the future.", end = "")
        birthYear = ""
age = currentYear - int(birthYear)


print("\nYour name is " + fullName + " and you are " + str(age) + " years old.")