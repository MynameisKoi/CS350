#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    double sum = 0, mean, variance, sd;

    printf("Enter size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter numbers for each element: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    mean = sum / n;

    // Calculate variance
    sum = 0;
    for (i = 0; i < n; i++) {
        sum += pow(arr[i] - mean, 2);
    }
    variance = sum / n;

    // Calculate standard deviation
    sd = sqrt(variance);

    printf("Result of Standard Deviation: %lf", sd);

    return 0;
}
