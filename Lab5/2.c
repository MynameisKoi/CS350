#include <stdio.h>
#include <stdlib.h>

int main() {
    int numbers[100]; // assuming the input list size is not more than 100
    int i, n, max_odd = -1, min_even = -1;

    printf("Enter a series of integers, separated by spaces (enter 'q' to quit): ");
    i = 0;
    while(scanf("%d", &n) == 1 && i < 100) {
        numbers[i++] = n;
    }
    int len = i;

    for(i = 0; i < len; i++) {
        if(numbers[i] % 2 != 0) { // odd number
            if(max_odd == -1 || numbers[i] > max_odd) {
                max_odd = numbers[i];
            }
        } else { // even number
            if(min_even == -1 || numbers[i] < min_even) {
                min_even = numbers[i];
            }
        }
    }

    if(max_odd == -1 || min_even == -1) {
        printf("Could not find both a maximum odd number and a minimum even number in the list.");
    } else {
        int result = abs(max_odd - min_even);
        printf("The absolute value of the difference between the maximum odd number and minimum even number is: %d", result);
    }

    return 0;
}
