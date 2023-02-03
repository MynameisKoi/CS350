#include <stdio.h>
#include <stdlib.h>

// print Fibonacci series for given number from keyboard input
int main(){
    int n, a = 0, b = 1, c;
    printf("Read the integers from keyboard: ");
    scanf("%d", &n);
    printf("Fibonacci series: ");
    for(int i = 0; i <= n; i++){
        printf("%d ", a);
        c = a + b;
        a = b;
        b = c;
    }
    printf("\n");

    return 0;
}