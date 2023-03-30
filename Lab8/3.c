#include <stdio.h>

int string_length(char *str) {
    int length = 0;

    while (*str != '\0') {
        length++;
        str++;
    }

    return length;
}

int main() {
    char str[100];
    int length;

    printf("Enter a string: ");
    scanf("%s", str);

    length = string_length(str);
    printf("The length of the given string %s is: %d\n", str, length);

    return 0;
}