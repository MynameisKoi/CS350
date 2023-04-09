#include <stdio.h>
#include <stdlib.h>

int main() {
    int row, col;
    printf("Enter size of row & column: ");
    scanf("%d %d", &row, &col);

    // Declare the 2D array
    int arr[row][col];

    // Take input from the user
    printf("Enter each element:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    // Count the number of malignant cells
    int malignant_count = 0;
    for (int i = 1; i < row-1; i++) {
        for (int j = 1; j < col-1; j++) {
            int test = arr[i][j];
            int up = arr[i-1][j];
            int down = arr[i+1][j];
            int left = arr[i][j-1];
            int right = arr[i][j+1];
            // compare the absolute difference between test and up down left right
            if (abs(test - up) > 10 && abs(test - down) > 10 && abs(test - left) > 10 && abs(test - right) > 10) {
                malignant_count++;
            }
        }
    }

    // Print the result
    printf("Result of malignant cell detection: %d\n", malignant_count);

    return 0;
}
