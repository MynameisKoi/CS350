#include <stdio.h>

int *biggest_of_two(int *a, int *b) {
    if (*a > *b) {
        return a;
    } else {
        return b;
    }
}

int *biggest_of_three(int *a, int *b, int *c) {
    if (*a > *b) {
        if (*a > *c) {
            return a;
        } else {
            return c;
        }
    } else {
        if (*b > *c) {
            return b;
        } else {
            return c;
        }
    }
}

int main() {
    int num1, num2, num3;
    int *result;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);
    result = biggest_of_two(&num1, &num2);
    printf("The biggest number is: %d\n", *result);

    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    result = biggest_of_three(&num1, &num2, &num3);
    printf("The biggest number is: %d\n", *result);

    return 0;
}
