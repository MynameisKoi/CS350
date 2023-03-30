#include <stdio.h>

// write a program to concatenate 2 strings
int main(){
    char str1[100], str2[100], str3[100];
    int i, j;

    printf("Enter first string: ");
    scanf("%s", str1);

    printf("Enter second string: ");
    scanf("%s", str2);

    // copy str1 to str3
    for(i = 0; str1[i] != '\0'; i++) {
        str3[i] = str1[i];
    }

    // concatenate str2 to str3
    for(j = 0; str2[j] != '\0'; j++) {
        str3[i + j] = str2[j];
    }

    printf("After concatenation: %s", str3);

    return 0;
}