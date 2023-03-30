#include <stdio.h>

int main() {
    int n, i, fact = 1;
    int *p = &fact; // pointer to the variable fact

    printf("Input a number: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        *p *= i; // multiply the pointer variable with the current value of i
    }

    printf("%d's factorial: %d", n, fact);

    return 0;
}
