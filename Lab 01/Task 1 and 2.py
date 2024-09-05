import time # Importing time module to get access to the sleep function to delay between Task/Questions 



# Task 1
print("Task 1: Breadboard Layout\n")

print("  +V       A  B  C  D   GND") # Printing Breadboard
print("| + | 1 |--o--o--o--o--| G |")
print("| + | 2 |--o--o--o--o--| G |")
print("| + | 3 |--o--o--o--o--| G |")
print("| + | 4 |--o--o--o--o--| G |")

time.sleep(1) # Delay so it doesnt send the previous print further up before there is a chance to see it




# Task 2 Question 1
print("\n\n\n Task 2: User Interaction with Breadboard")

strInput = ""
while strInput == "" : # While loop to get the correct Input
    print("\nWould you like a Resistor or LED at the \"A1\" - \"B2\" Location?") # Input Question
    print("Input must be either L or R")
    print(" > ", end='')
    strInput = input().upper() # Input forced Uppercase so it is easier to do the if statement and also to plug into the Breadboard
    if strInput not in ["L","R"] : # If statement to check if the input is in a list containing only "L" and "R"
        strInput = ""

print()
print("  +V       A  B  C  D   GND") # Printing Breadboard with either LED or Resistor
print("| + | 1 |--"+strInput+"1-o--o--o--| G |")
print("| + | 2 |--o--"+strInput+"2-o--o--| G |")
print("| + | 3 |--o--o--o--o--| G |")
print("| + | 4 |--o--o--o--o--| G |")

time.sleep(1) # Delay so it doesnt send the previous print further up before there is a chance to see it




# Task 2 Question 2
print("\n\n\nShow a Full Circuit that includes Supply-LED-Resistor-GND\n")

print("  +V       A  B  C  D   GND") # Printing Breadboard with Full Circuit
print("| + | 1 |--+--L1-o--o--| G |")
print("| + | 2 |--o--L2-R1-o--| G |")
print("| + | 3 |--o--o--R2-G--| G |")
print("| + | 4 |--o--o--o--o--| G |")

time.sleep(1) # Delay so it doesnt send the previous print further up before there is a chance to see it




# Task 2 Question 3
print("\n\n\nTime Taken : 25 Minutes") # To be fair, I have experience in Python (AP CSP)