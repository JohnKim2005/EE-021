
#include <iostream>

void main() {
    int nrows = 5;
    int ncols = 5;
    int arr[5][5] = {};

    for (int i=0; i<nrows; i++) {
        for (int j=0; j<ncols; j++) {
            arr[i][j] = i+j;
            std::cout << arr[i][j] << std::endl;
        }
    }
}