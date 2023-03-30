#include <stdio.h>
#include <string.h>

// write a program that sorts a list in alphabetic order
int main(){
    char str[100][100], temp[100];
    int i, j, n;

    printf("Enter number of strings: ");
    scanf("%d", &n);

    printf("Enter %d strings: ", n);
    for(i = 0; i < n; i++) {
        scanf("%s", str[i]);
    }

    // sort the strings
    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(strcmp(str[i], str[j]) > 0) {
                strcpy(temp, str[i]);
                strcpy(str[i], str[j]);
                strcpy(str[j], temp);
            }
        }
    }

    printf("Alphabetical list: ");
    for(i = 0; i < n; i++) {
        printf("%s \n", str[i]);
    }

    return 0;
}