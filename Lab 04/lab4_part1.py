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
