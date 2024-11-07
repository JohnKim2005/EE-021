# Python code template for lab 08, EE 021
import numpy as np

# 1a. Create an empty array that has three rows and three columns. 
# Print the array.
num_rows = 3
num_cols = 3
################################################################################
# The empty function initializes an empty array, and it contains random values.
my_array = np.empty([num_rows,num_cols]) # replace None with your actual code.
################################################################################
print(my_array)



#################################################################################
# 1b. Fill up the array with all zeros. Must use for loops for this task.
# Hint: Use two nested for loops to iterate over the rows and columns of the array.
# Hint: Use the range function to create an iterable sequence of 
# numbers from 0 to the number of rows or columns.

for i in range(num_rows):
    for j in range(num_cols):
        my_array[i][j] = 0
#################################################################################





#################################################################################
# 1c. Update the values at all indices of the array with 
# values equal to the following 3 x 3 matrix: 
# Print the updated array with a \t (tab) separator between elements.
# [-1, 0, 1],
# [-2, 0, 2],
# [-1, 0, 1]
# You must update the already existing my_array variable, not create a new one.
my_array[0][0] = -1
my_array[0][2] = 1
my_array[1][0] = -2
my_array[1][2] = 2
my_array[2][0] = -1
my_array[2][2] = 1
#################################################################################


#################################################################################
# Print the updated array with a \t (tab) separator between elements.
print("Updated array is")
for i in range(num_rows):
    for j in range(num_cols):
        print(my_array[i][j], end = '\t')
    print()
