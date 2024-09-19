# Write your pseudo code for the lab assignment task 2 
# Task 2 is to find the number of 100 ohm resistors needed to reach the desired voltage

# Write your code for task 1 first: ask the user for an input voltage.
'''
Tell the User about what the input should be (Desired Voltage)
Take an input of the Desired Voltage
'''

# What do you need to define as constant values before beginning?
#### I would need to define variables for all constant values in the circuit, for example,...
'''
Input Voltage should be 5 Volts
Desired Voltage should be the input fromt he user
Resistor last should be 100 ohms
Resistive Total should be 0 ohms (R_n) (Resistors between Point A and B on the Lab page Circuit)
'''

# What is the initial output voltage? (You may use the formula in the lab assignment)
# Or simply think about this: if you have two resistors of equal value to start with then the output voltage will be 2.5V. Why?
'''
Output Voltage is Input Voltage() * (R_last / (R_last + R_n)) (At the start should be 5V since I am starting with no resistors between point A and B)
'''

# Do you need to add more 100 ohm resistors?
'''
Is the Input Voltage less than Desired Voltage?
if not then we should add one more 100 ohm resistor
'''

# What happens when you add one more 100 ohm resistor? What is the output value?
'''
the out put should decrease
'''

# Until when, would you keep adding more 100 ohm resistors?
'''
until the Input Voltage is less than or equal to the Desired Voltage or you use up all 10 of the 100 ohm resistors.
if not either go aback to adding more 100 ohm resistors
'''

# What other code you might need?
'''
Clean up like Comments and Math for turning the Resistive Total at R_n to number of Resistors.
The Break out and printing of the lack of resistors if nessessary (Limit of 10 resistors)
'''

# Print out the final answers
'''
Print out the Number of 100 Ohm resistors and The Total Resistance of the 100 ohm resistors in series
Print out the Output Voltage
'''