#include <stdio.h>

int main(){
    int n, x;
    x = 1;
    printf("Enter the number of lines you want to print: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", x);
            x++;
        }
        printf("\n");
    }
}