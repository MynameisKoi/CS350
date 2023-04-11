# include <stdio.h>

int main(){
    int size, rotation;
    printf("Enter an array size: ");
    scanf("%d", &size);
    printf("Enter number of rotation: ");
    scanf("%d", &rotation);
    int arr[size];
    printf("Enter numbers for your array: ");
    for(int i = 0; i < size; i++){
        scanf("%d", &arr[i]);
    }
    printf("Results: ");
    // Take the 'rotation' last numbers in the array and put them on first
    for(int i = size - rotation; i < size; i++){
        printf("%d ", arr[i]);
    }
    for(int i = 0; i < size - rotation; i++){
        printf("%d ", arr[i]);
    }
}