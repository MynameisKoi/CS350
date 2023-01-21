// find the greatest in 3 numbers from keyboard input
#include <stdio.h>
int main()
{
    int a, b, c;
    printf("Enter value for a, b & c: ");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b && a > c) printf("a is the greatest number.", a);
    if (b > a && b > c) printf("b is the greatest number.", b);
    if (c > a && c > b) printf("c is the greatest number.", c);
    return 0;
}