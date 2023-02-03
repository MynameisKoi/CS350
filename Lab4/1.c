#include <stdio.h>
#include <stdlib.h>

// find out whether a given number is a prime number or not
int isPrime(int n){
    if(n == 1){
        return 0;
    }
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int n;
    printf("enter any number: ");
    scanf("%d", &n);
    if (isPrime(n)) printf("prime number?: Yes\n");
    else printf("prime number?: No\n");

    return 0;
}