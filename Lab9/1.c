#include <stdio.h>

int removeDuplicates(int arr[], int n) {
    // loop through each element of the array
    for (int i = 0; i < n; i++) {
        // compare the current element with all subsequent elements
        for (int j = i + 1; j < n;) {
            // if a duplicate is found, shift all subsequent elements to the left
            if (arr[j] == arr[i]) {
                for (int k = j; k < n - 1; k++) {
                    arr[k] = arr[k + 1];
                }
                n--; // decrement the size of the array
            } else {
                j++; // move to the next element
            }
        }
    }
    return n; // return the new array size
}

int main() {
    int arr[] = {1, 2, 3, 3, 4, 4, 5, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    int a = removeDuplicates(arr, n);

    printf("Array after removing duplicates: ");
    for (int i = 0; i < a; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
