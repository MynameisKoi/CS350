#include <stdio.h>

int main(){
    // merge 1 dimensional array, excluding repeating element
    int a, b;
    printf("Enter the size of 1st array: ");
    scanf("%d", &a);
    int arr1[a];
    printf("Enter each element: ");
    for(int i = 0; i < a; i++){
        scanf("%d", &arr1[i]);
    }
    printf("Enter the size of 2nd array: ");
    scanf("%d", &b);
    int arr2[b];
    printf("Enter each element: ");
    for(int i = 0; i < b; i++){
        scanf("%d", &arr2[i]);
    }
    int arr3[a+b];
    int count = 0;
    for(int i = 0; i < a; i++){
        arr3[count] = arr1[i];
        count++;
    }
    for(int i = 0; i < b; i++){
        int flag = 0;
        for(int j = 0; j < a; j++){
            if(arr2[i] == arr1[j]){ // check if any repeating element in array
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            arr3[count] = arr2[i];
            count++;
        }
    }
    printf("Result: ");
    for(int i = 0; i < count; i++){
        printf("%d ", arr3[i]);
    }
    return 0;
}