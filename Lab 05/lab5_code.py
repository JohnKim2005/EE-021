import matplotlib.pyplot as plt
f_list = list(zip(open('timepoints.txt', 'r'), open('voltages.txt', 'r'), open('currents.txt', 'r')))
f_list.pop(0)
powerList = []
for time, volt, amp in f_list :
    powerList.append(float(volt) * float(amp))
    plt.scatter(volt,amp)
print("The maximum power value is", max(powerList), "watts.")
plt.show()