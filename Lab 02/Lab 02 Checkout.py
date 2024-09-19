print('Please orient so that the 3 band side goes to the Left and the 1 band side goes to the Right.')
print('If the bands are equally spaced, the gold or silver band should be on the right side.\n')

#  Black \n Red \n Brown \n Orange \n Yellow \n Green \n Blue \n Purple \n Gray \n White \n Gold \n Silver"
# Ohms Symbol : \u03A9



print('Please input the first (Left to Right) color by name or by number.')
print('Please choose from \n1. Brown \n2. Red \n3. Orange \n4. Yellow \n5. Green \n6. Blue \n7. Purple \n8. Gray \n9. White')
firstColor = input('> ').lower()
firstValue = 0

if firstColor in ['brown', '1'] :
    firstValue = 1
elif firstColor in ['red', '2'] :
    firstValue = 2
elif firstColor in ['orange', '3'] :
    firstValue = 3
elif firstColor in ['yellow', '4'] :
    firstValue = 4
elif firstColor in ['green', '5'] :
    firstValue = 5
elif firstColor in ['blue', '6'] :
    firstValue = 6
elif firstColor in ['purple', '7'] :
    firstValue = 7
elif firstColor in ['gray', '8'] :
    firstValue = 8
elif firstColor in ['white', '9'] :
    firstValue = 9
else :
    print('The input is not a valid input. Please try again.')
    exit()



print('Please input the second (Left to Right) color by name or by number.')
print('Please choose from \n0. Black \n1. Brown \n2. Red \n3. Orange \n4. Yellow \n5. Green \n6. Blue \n7. Purple \n8. Gray \n9. White')
secondColor = input('> ').lower()
secondValue = 0

if secondColor in ['black', '0'] :
    secondValue = 0
elif secondColor in ['brown', '1'] :
    secondValue = 1
elif secondColor in ['red', '2'] :
    secondValue = 2
elif secondColor in ['orange', '3'] :
    secondValue = 3
elif secondColor in ['yellow', '4'] :
    secondValue = 4
elif secondColor in ['green', '5'] :
    secondValue = 5
elif secondColor in ['blue', '6'] :
    secondValue = 6
elif secondColor in ['purple', '7'] :
    secondValue = 7
elif secondColor in ['gray', '8'] :
    secondValue = 8
elif secondColor in ['white', '9'] :
    secondValue = 9
else :
    print('The input is not a valid input. Please try again.')
    exit()



print('Please input the third (Left to Right) color by name or by number.')
print('Please choose from \n0. Black \n1. Brown \n2. Red \n3. Orange \n4. Yellow \n5. Green \n6. Blue \n7. Purple \n8. Gray \n9. White \n10. Gold \n11. Silver \n12. Pink')
thirdColor = input('> ').lower()
thirdValue = 0

if thirdColor in ['black', '0'] :
    thirdValue = 1
elif thirdColor in ['brown', '1'] :
    thirdValue = 10
elif thirdColor in ['red', '2'] :
    thirdValue = 100
elif thirdColor in ['orange', '3'] :
    thirdValue = 1000
elif thirdColor in ['yellow', '4'] :
    thirdValue = 10000
elif thirdColor in ['green', '5'] :
    thirdValue = 100000
elif thirdColor in ['blue', '6'] :
    thirdValue = 1000000
elif thirdColor in ['purple', '7'] :
    thirdValue = 10000000
elif thirdColor in ['gray', '8'] :
    thirdValue = 100000000
elif thirdColor in ['white', '9'] :
    thirdValue = 1000000000
elif thirdColor in ['gold', '10'] :
    thirdValue = 0.1
elif thirdColor in ['silver', '11'] :
    thirdValue = 0.01
elif thirdColor in ['pink', '12'] :
    thirdValue = 0.001
else :
    print('The input is not a valid input. Please try again.')
    exit()


print('\n\n')
print(str(firstValue)+", "+str(secondValue)+", "+str(thirdValue))