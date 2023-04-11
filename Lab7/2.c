#include <stdio.h>

int main(){
    // swap 2 numbers by pointer
    int a,b;
    printf("Enter 2 numbers a & b: ");
    scanf("%d %d", &a, &b);
    int *pa = &a;
    int *pb = &b;
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
    printf("After swapping by pointer, a = %d, b = %d", a, b);
    return 0;

}