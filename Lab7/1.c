#include <stdio.h>

int main(){
    printf("Enter 2-dimensional array size: ");
    int a, b;
    scanf("%d %d", &a, &b);
    int arr1[a][b];
    int arr2[b][a];
    printf("Enter numbers for each element in 2 arrays: ");
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
            scanf("%d", &arr1[i][j]);
        }
    }
    for(int i = 0; i < b; i++){
        for(int j = 0; j < a; j++){
            scanf("%d", &arr2[i][j]);
        }
    }

    int arr3[a][a];
    for(int i = 0; i < a; i++){
        for(int j = 0; j < a; j++){
            arr3[i][j] = 0;
            for(int k = 0; k < b; k++){
                arr3[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }

    printf("Result: \n");
    for(int i = 0; i < a; i++){
        for(int j = 0; j < a; j++){
            printf("%d ", arr3[i][j]);
        }
        printf("\n");
    }
    return 0;
}