#include <stdio.h>

int main(){
    // remove duplicate element in an array
    int a;
    printf("Enter the size of array: ");
    scanf("%d", &a);
    int arr[a];
    printf("Enter numbers for each element: ");
    for(int i = 0; i < a; i++){
        scanf("%d", &arr[i]);
    }
    int count = 0;
    for(int i = 0; i < a; i++){
        int flag = 0;
        for(int j = 0; j < i; j++){
            if(arr[i] == arr[j]){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            arr[count] = arr[i];
            count++;
        }
    }
    printf("Result: ");
    for(int i = 0; i < count; i++){
        printf("%d ", arr[i]);
    }
    
    return 0;
}