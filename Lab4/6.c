#include <stdio.h>

int main(){
    int a[6];
    int b[6];
    int c[2][3];

    printf("Enter value for matrix 1: ");
    for(int i = 0; i < 6; i++){
        scanf("%d", &a[i]);
    }
    printf("Enter value for matrix 2: ");
    for(int i = 0; i < 6; i++){
        scanf("%d", &b[i]);
    }
    // sum two matrix and form 2x3 matrix
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            c[i][j] = a[i*3+j] + b[i*3+j];
        }
    }

    printf("Sum of two matrix: \n");
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}