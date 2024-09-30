level = input('Choose Level (1 or 2)')

if level == '1':
    resistance = 120
    points = 0
    print('The Game Has Started. The Resistance is ' + str(resistance) + '\u03A9.')

    while True:
        voltage = float(input('Please Input a Voltage'))
        Amperage = float(input('Please Input a Current'))
        if resistance != int(voltage/Amperage):
            break
        points += 1
        if 'no' == input('Would you like to Continue?'):
            break
    print('Score:', points)
else :
    import random
    points = 0
    voltage = 100.0
    attempts = 3
    minRes = 50
    maxRes = 100
    resistance = random.uniform(minRes, maxRes)
    resistance = int(resistance)
    CorrectAmpere = voltage/resistance
    minAmp = CorrectAmpere * 0.9
    maxAmp = CorrectAmpere * 1.1
    print('The Game Has Started. The Voltage is ' + str(voltage) + 'Volts and Resistance is between ' + str(minRes) + '\u03A9 and ' + str(maxRes) + '\u03A9.')

    while True:
        Amperage = float(input('Please Input a Current'))
        if minAmp < Amperage and maxAmp > Amperage:
            points += 1
            resistance = random.uniform(minRes, maxRes)
            resistance = int(resistance)
            CorrectAmpere = voltage/resistance
            minAmp = CorrectAmpere * 0.9
            maxAmp = CorrectAmpere * 1.1
            attempts = 3
            if 'no' == input('Would you like to Continue?'):
                break
        else:
            attempts -= 1
        if attempts == 0:
            break
    print('Score:', points)
