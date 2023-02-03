#include <stdio.h>

int main() {
    int n = 5, i;
    int arr[5];
    int max = 0;

    printf("Enter elements for array: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    printf("maximum number = %d\n", max);

    return 0;
}
