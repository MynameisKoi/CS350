#include <stdio.h>

int factorial(int n){
        if(n == 0){
            return 1;
        }
        else{
            return n * factorial(n-1);
        }
}

int main(){
    // find factorial of a number using recursion
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Factorial = %d", factorial(n));
    return 0;
}