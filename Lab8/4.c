#include <stdio.h>

void reverse_string(char *);

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    printf("Result: ");
    reverse_string(str);

    return 0;
}

void reverse_string(char *str) {
    int length = 0;
    char *end = str;

    // Find the end of the string
    while (*end != '\0') {
        end++;
        length++;
    }

    // Reverse the string
    char *start = str;
    end--;
    while (end > start) {
        char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }

    printf("%s\n", str);
}
