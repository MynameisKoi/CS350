#include <stdio.h>
#include <stdlib.h>

// Use bitwise AND operator between two integers
int main(){
    int a,b,c;
    printf("Read the integers from keyboard: ");
    scanf("%d %d", &a, &b);
    c = a & b;
    printf("The answer after ANDing is: %d\n", c);

    return 0;
}