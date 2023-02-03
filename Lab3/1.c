#include <stdio.h>

int main(){
    int n;
    printf("Enter a number of array's size for a series of numbers saving: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter a series of numbers: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
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
    // print the array
    printf("After sorting, output sequence: ");
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    return 0;
}