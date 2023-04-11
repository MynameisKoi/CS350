#include <stdio.h>

int main(){
    // study the difference between gets(), puts(), getchar(), and putchar() in C
    char str[100];
    // gets() and puts() will input and output the whole string into the variable
    printf("Enter a string: ");
    gets(str);
    printf("You entered 'gets(str)': ");
    puts(str);

    // getchar() and putchar() will input and output only 1 character
    printf("Enter a character: ");
    char c = getchar();
    printf("You entered 'getchar()': ");
    putchar(c);
    return 0;
}