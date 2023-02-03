#include <stdio.h>
#include <stdlib.h>

// print sum of series 1 + 1/2 + 1/3 + 1/4 + ... + 1/n which n's value is from keyboard
int main(){
    int n;
    printf("Read the integers from keyboard: ");
    scanf("%d", &n);
    float sum = 0;
    for(int i = 1; i <= n; i++){
        sum += 1.0/i;
    }
    printf("Sum of reciprocal of n: %.3f\n", sum);

    return 0;
}