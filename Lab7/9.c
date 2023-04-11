#include <stdio.h>

int main() {
    int n, k, i, j, temp;
    printf("Enter size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter numbers for each element: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter desired kth smallest element: ");
    scanf("%d", &k);

    // Sort the array
    for (i = 0; i < n; i++) {
        for (j = i+1; j < n; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // Find the kth smallest element
    int count = 1;  // Initialize count to 1 since we're looking for the kth smallest element
    int prev = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] != prev) {
            count++;
            if (count == k) {
                printf("Result of %dth smallest element: %d", k, arr[i]);
                break;
            }
            prev = arr[i];
        }
    }
    if (count < k) {
        printf("Error: There are only %d distinct elements in the array", count);
    }

    return 0;
}
