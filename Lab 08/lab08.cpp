// C++ code template for lab08, EE 021

#include <iostream>

using namespace std;

int main() {
    ////////////////////////////////////////////////////////////////////////////
    // 2a. Create an empty array that has three rows and three columns.
    // Print the array.
    const int num_rows = 3;
    const int num_cols = 3;
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
            my_array[i][j] = 0;
        }
    }

    ////////////////////////////////////////////////////////////////////////////
    // 2c. Update the values at all indices of the array with 
    // values equal to the following 3 x 3 matrix: 
    // [-1, 0, 1],
    // [-2, 0, 2],
    // [-1, 0, 1]
    // You must update the already existing my_array variable, not create a new one.

    my_array[0][0] = -1;
    my_array[0][2] = 1;
    my_array[1][0] = -2;
    my_array[1][2] = 2;
    my_array[2][0] = -1;
    my_array[2][2] = 1;
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
    

    ////////////////////////////////////////////////////////////////////////////
    // 2d. Find the value in the array that is exactly equal to 2, and change it to 4.
    // Only find the first occurrence of 2 in the array and change it to 4.
    // Hint: Combine the two for loops with an if statement.
    // Hint: Use the break statement to exit the loop once you find the first occurrence.
    bool done = false;
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            if (my_array[i][j] == 2) {
                my_array[i][j] = 4;
                done = true;
                break;
            }
        }
        if (done) {
            break;
        }
    }

    ////////////////////////////////////////////////////////////////////////////



    ////////////////////////////////////////////////////////////////////////////
    // 2e. Retrieve data at 1,2 index of the array and print it.
    // Fix this line to print the data at 1,2 index.
    cout << "Data at (1, 2): " << my_array[1][2] << endl; 
    ////////////////////////////////////////////////////////////////////////////


    ////////////////////////////////////////////////////////////////////////////
    // 2f. Update the value at the 2,2 index of the array and print the updated array.
    my_array[2][2] = 32;
    ////////////////////////////////////////////////////////////////////////////


    ////////////////////////////////////////////////////////////////////////////
    cout << "Updated array:" << endl;
    // Print the updated array with a \t (tab) separator between elements.

    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            cout << my_array[i][j] << "\t";
        }
        cout << endl;
    }
    ////////////////////////////////////////////////////////////////////////////
    


    ////////////////////////////////////////////////////////////////////////////
    // 2g. Add two more rows and two more columns to create a new array.
    // Fill up the array with the values in my_array, and new rows and columns as 0s.
    const int new_num_rows = num_rows + 2;
    const int new_num_cols = num_cols + 2;
    int new_array[new_num_rows][new_num_cols];
    // Fill the new array with same elements as in my_array, and other elements as 0

    for (int i = 0; i < new_num_rows; i++) {
        for (int j = 0; j < new_num_cols; j++) {
            if (i < num_rows && j < num_cols) {
                new_array[i][j] = my_array[i][j];
            } else {
                new_array[i][j] = 0;
            }
        }
    }

    ////////////////////////////////////////////////////////////////////////////


    ////////////////////////////////////////////////////////////////////////////   
    // Print the updated array with a \t (tab) separator between elements.
    cout << "New array:" << endl;
    
    for (int i = 0; i < new_num_rows; i++) {
        for (int j = 0; j < new_num_cols; j++) {
            cout << new_array[i][j] << "\t";
        }
        cout << endl;
    }
    ////////////////////////////////////////////////////////////////////////////
}