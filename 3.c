#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);

    num % 3 == 0 ? printf("3") : 0;
    num % 5 == 0 ? printf(num % 3 == 0 ? ",5" : "5") : 0;
    num % 7 == 0 ? printf(num % 3 == 0 || num % 5 == 0 ? ",7\n" : "7\n") : 0;
    if (num % 3 != 0 && num % 5 != 0 && num % 7 != 0) {
        printf("NOT\n");
    }

    return 0;
}
