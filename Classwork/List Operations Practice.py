R1_color = input('Give three colors on a resistor separated by comma\n> ').lower()
R1_list = R1_color.replace(" ", "").split(',')
R2_color = input('Give three colors on a resistor separated by comma\n> ').lower()
R2_list = R2_color.replace(" ", "").split(',')
ResistorValue = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'purple':7,'gray':8,'white':9,'gold':-1,'silver':-2,'pink':-3}

R1_Value = [ResistorValue[R1_list[0]],ResistorValue[R1_list[1]],ResistorValue[R1_list[2]]]
R2_Value = [ResistorValue[R2_list[0]],ResistorValue[R2_list[1]],ResistorValue[R2_list[2]]]
ResistList = []
ResistList.append((R1_Value[0]*10 + R1_Value[1])*pow(10,R1_Value[2]))
ResistList.append((R2_Value[0]*10 + R2_Value[1])*pow(10,R2_Value[2]))

print(ResistList)



resistor_values[r1_list[0]]