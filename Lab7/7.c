#include <stdio.h>

int main(){
    // print binomial coefficient table
    printf("Enter the order of binomial power expression: ");
    int n;
    scanf("%d", &n);
    int arr[n+1][n+1];
    printf("Results of printing on monitor: ");
    printf("1\n");
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= i; j++){
            if(j == 0 || j == i){
                arr[i][j] = 1;
            }
            else{
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
            }
        }
    }
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= i; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}