#include <stdio.h>
#include <stdlib.h>

// count the number of 1 in binary representation for a decimal number
int count(int n){
    int count = 0;
    while(n){
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int main(){
    int n;
    printf("Enter decimal number: ");
    scanf("%d", &n);
    printf("There are %d ones in given decimal number", count(n));
}