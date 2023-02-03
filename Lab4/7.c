#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    float ave;
    printf("Enter length of array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter each element in array: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    for(int i = 0; i < n; i++){
        ave += arr[i];
    }
    ave /= n;
    printf("Average of array: %.3f\n", ave);

    return 0;
}