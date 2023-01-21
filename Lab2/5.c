// find whether given number is even or odd
#include <stdio.h>
int main()
{
    int n;
    printf("Enter any number to check even or odd: ");
    scanf("%d", &n);
    if (n % 2 == 0) printf("%d is even.", n);
    else printf("%d is odd.", n);
    return 0;
}