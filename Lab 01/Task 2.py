import time

strInput = ""
while strInput == "" :
    print("Would you like a Resistor or LED at the \"A1\" - \"B2\" Location?")
    print("Input must be either L or R")
    strInput = input().upper()
    if strInput not in ["L","R"] :
        strInput = ""

print("  +V       A  B  C  D   GND")
print("| + | 1 |--"+strInput+"1-o--o--o--| G |")
print("| + | 2 |--o--"+strInput+"2-o--o--| G |")
print("| + | 3 |--o--o--o--o--| G |")
print("| + | 4 |--o--o--o--o--| G |")

time.sleep(1)

print("\n\n\nShow a Full Circuit that includes Supply-LED-Resistor-GND\n")

print("  +V       A  B  C  D   GND")
print("| + | 1 |--+--L1-o--o--| G |")
print("| + | 2 |--o--L2-R1-o--| G |")
print("| + | 3 |--o--o--R2-G--| G |")
print("| + | 4 |--o--o--o--o--| G |")

time.sleep(1)

print("Time Taken : 20 Minutes") # To be fair, I have experience in Python (AP CSP)