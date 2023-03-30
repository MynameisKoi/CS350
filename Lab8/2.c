#include <stdio.h>

void div_rem(int a, int b, int *quotient, int *remainder) {
    *quotient = a / b;
    *remainder = a % b;
}

int main() {
    int num1, num2, quotient, remainder;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);
    div_rem(num1, num2, &quotient, &remainder);
    printf("%d divided by %d is %d with a remainder of %d.\n", num1, num2, quotient, remainder);

    return 0;
}
