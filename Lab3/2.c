#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    printf("Enter a number of array's size for a series of numbers saving: ");
    scanf("%d", &n);
    int arr[n];
    int ans[n];
    printf("Enter a series of numbers: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    int *odd = malloc(n * sizeof(int));
    int *even = malloc(n * sizeof(int));
    int j = 0, k = 0;

    // sort the array
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(arr[i] > arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // separate odd and even number
    for(int i = 0; i < n; i++){
        if(arr[i] % 2 == 0){
            even[j++] = arr[i];
        }
        else{
            odd[k++] = arr[i];
        }
    }

    // merge odd and even number
    for(int i = 0; i < n; i++){
        if(i < k){
            ans[i] = odd[i];
        }
        else{
            ans[i] = even[i-k];
        }
    }


    // print the array
    printf("After sorting, output sequence: ");
    for(int i = 0; i < n; i++){
        printf("%d ", ans[i]);
    }
    return 0;
}