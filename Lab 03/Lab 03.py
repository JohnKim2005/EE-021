print("Please type the Desired Voltage in the form of 'x.xxx'. It must be between 5V and 0V.")
desiredVoltage = float(input('> '))
V_in = 5.

if (desiredVoltage > 5) :
    print("Your Input Value is Larger than the Input Voltage. Please Try again with an input above 0V and below 5V.")
    exit
elif (desiredVoltage < 0) :
    print("Your Input Value is Negative. Please Try again with an input above 0V and lower than 5V")
    exit

# Question 2
r_last = 100.
v_out = 5.
r_n = 0
v_prev = 5.
r_prev = 0
r = 100
print ("Question 2")
while (v_out > desiredVoltage and r_prev <= r * 10) :
    r_n += r
    v_out = V_in * (r_last/(r_last+r_n))
    if (v_out < desiredVoltage) :
        if abs(desiredVoltage-v_out) < abs(desiredVoltage-v_prev) :
            v_prev = v_out
            r_prev = r_n
    else :
        v_prev = v_out
        r_prev = r_n

if (r_prev > r * 10) :
    print("You need more than 10 " + str(r) + "\u03A9 resistors and you ran out....")
else :
    r_num = int(r_prev/r)
    print ("The Output Voltage will be " + str(round(v_prev,3)) + "V with " + str(r_num) + " " + str(r) + "\u03A9 Resistors totaling " + str(r_prev) + "\u03a9.")



# Question 3
print ("Question 3")
r_last = 3700
v_out = 5.
r_n = 0
v_prev = 5.
r_prev = 0
r = 1000
while (v_out > desiredVoltage and r_prev <= r * 10) :
    r_n += r
    v_out = V_in * (r_last/(r_last+r_n))
    if (v_out < desiredVoltage) :
        if abs(desiredVoltage-v_out) < abs(desiredVoltage-v_prev) :
            v_prev = v_out
            r_prev = r_n
    else :
        v_prev = v_out
        r_prev = r_n

if (r_prev > r * 10) :
    print("You need more than 10 " + str(r) + "\u03A9 resistors and you ran out....")
else :
    r_num = int(r_prev/r)
    print ("The Output Voltage will be " + str(round(v_prev,3)) + "V with " + str(r_num) + " " + str(r) + "\u03A9 Resistors totaling " + str(r_prev) + "\u03a9.")



# Question 5
print ("Question 5")
r_last = 1000
v_out = 5.
r_n = 0
v_prev = 5.
r_prev = 0
r = 100
while (v_out > desiredVoltage) :
    r_n += r
    v_out = V_in * (r_last/(r_last+r_n))
    if (v_out < desiredVoltage) :
        if abs(desiredVoltage-v_out) < abs(desiredVoltage-v_prev) :
            v_prev = v_out
            r_prev = r_n
    else :
        v_prev = v_out
        r_prev = r_n

r_num = int(r_prev/r)
print ("The Output Voltage will be " + str(round(v_prev,3)) + "V with " + str(r_num) + " " + str(r) + "\u03A9 Resistors totaling " + str(r_prev) + "\u03a9.")