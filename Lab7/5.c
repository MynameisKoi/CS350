#include <stdio.h>
#include <string.h>

int main(){
    // study strcpy() and strrev() in c lang
    char str1[100];
    char str2[100];
    printf("Enter a string: ");
    gets(str1);
    strcpy(str2, str1); // strcpy() will copy str1 to str2
    printf("strcpy(): str1 = %s, str2 = %s\n", str1, str2);
    strrev(str1); // strrev() will reverse a string
    printf("strrev(): str1 = %s, str2 = %s\n", str1, str2);

    // check if a string is a palindrome
    printf("Enter a string: ");
    gets(str1);
    strcpy(str2, str1);
    strrev(str1);
    if(strcmp(str1, str2) == 0){
        printf("Palindrome");
    }
    else{
        printf("Not palindrome");
    }

    return 0;
}