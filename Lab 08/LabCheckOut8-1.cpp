// C++ code template for lab check out 08, EE 021

#include <iostream>

using namespace std;

int main() {
    ////////////////////////////////////////////////////////////////////////////
    // 2a. Create an empty array that has two rows and two columns.
    // Print the array.
    const int num_rows = 2;
    const int num_cols = 2;
    // Declare my_array in the next line with the given number of rows and columns.
    // The line below declares a 2x2 array. Fix this line to declare a num_rows x num_cols array.
    int my_array[num_rows][num_cols]; // Fix this with correct variable reference for rows and columns


    ////////////////////////////////////////////////////////////////////////////

    // Print the array, code provided to you. 
    // Make sure that you understand the use of for loops to print the array.
    cout << "Empty array:" << endl;
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            cout << my_array[i][j] << "\t";
        }
        cout << endl;
    }

    ////////////////////////////////////////////////////////////////////////////
    // 2b. Fill up the array with all zeros. Must use for loops for this task.
    // Similar to 1a, you may use loops to fill up the array with zeros.
    

    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            // Fill up the array with zeros.
            my_array[i][j] = 0;
        }
    }
    //////////////////////  //////////////////////////////////////////////////////
    // 2c. Update the values at all indices of the array with 
    // values equal to the following 3 x 3 matrix: 
    // [7, 9],
    // [1, 5] 
    // You must update the already existing my_array variable, not create a new one.

    my_array[0][0] = 7;
    my_array[0][1] = 9;
    my_array[1][0] = 1;
    my_array[1][1] = 5;
    ////////////////////////////////////////////////////////////////////////////


    ////////////////////////////////////////////////////////////////////////////
    // Print the updated array with a \t (tab) separator between elements.
    cout << "Updated array:" << endl;
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            cout << my_array[i][j] << "\t";
        }
        cout << endl;
    }
    ////////////////////////////////////////////////////////////////////////////
}