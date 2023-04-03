// find a program to get all permutations from a series of different numbers
#include <stdio.h>

// Function to swap two integers
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

// Recursive function to generate all permutations of an array
void permute(int arr[], int start, int end) {
    if (start == end) {
        // We have reached the end of the array, so print the permutation
        for (int i = 0; i <= end; i++) {
            printf("%d", arr[i]);
        }
        printf(" ");
    } else {
        // Generate all permutations by swapping each element with the first element
        for (int i = start; i <= end; i++) {
            swap(&arr[start], &arr[i]);
            permute(arr, start + 1, end);
            swap(&arr[start], &arr[i]); // backtrack
        }
    }
}

int main() {
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter each element for the given array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("All permutations: ");
    permute(arr, 0, n - 1);
    return 0;
}
