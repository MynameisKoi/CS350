#include <stdio.h>

int main(){
    printf("Enter size of array: ");
    int n;
    scanf("%d", &n);
    int arr[n];
    printf("Enter each element for the given array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // find the max value in the array
    int max = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // check the element frequency in the array
    int freq[max];
    for (int i = 0; i <= max; i++) {
        freq[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }

    printf("Frequency for each element: ");
    for (int i = 0; i <= max; i++) {
        if (freq[i] != 0) {
            printf("%d-%d ", i, freq[i]);
        }
    }

    return 0;
}