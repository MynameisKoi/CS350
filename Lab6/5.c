#include <stdio.h>

// Function to print the hailstone sequence for a given number
void hailstone(int n) {
    // Print the starting number
    printf("%d ", n);

    // Loop until we reach the final pattern of 4-2-1
    while (n != 1) {
        // If the number is odd, compute the next number using 3n+1
        if (n % 2 == 1) {
            n = 3*n + 1;
        }
        // If the number is even, compute the next number using n/2
        else {
            n = n / 2;
        }
        // Print the next number in the sequence
        printf("%d ", n);
    }
}

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);

    // Print the hailstone sequence for the input number
    printf("Hailstone sequence: ");
    hailstone(n);

    return 0;
}
