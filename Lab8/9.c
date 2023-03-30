#include <stdio.h>

int* get_array() {
    static int my_array[] = {1, 2, 3, 4, 5}; // declare and initialize the array
    return my_array; // return the array from the function
}

int main() {
    int *result_array; // declare a pointer to an integer array
    result_array = get_array(); // assign the returned array to the pointer

    // print the returned array
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(result_array + i));
    }

    return 0;
}
