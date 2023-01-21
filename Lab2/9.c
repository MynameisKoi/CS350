// Input a number, such as n from keyboard and display their sum from 1 to n by using loops
#include <stdio.h>
int main(){
    int n, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) sum += i;
    printf("Sum = %d", sum);
    return 0;
}