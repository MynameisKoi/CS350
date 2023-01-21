// shift input data by three bits to the left
#include <stdio.h>
int main(){
    int n;
    printf("Read the integer from keyboard: ");
    scanf("%d", &n);
    printf("The left shifted data is = %d", n << 3);
    return 0;
}