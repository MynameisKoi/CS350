// print stars
#include <stdio.h>
int main(){
    for (int i = 0; i <= 3; i++){
        for (int a = i; a <= 3; a++) printf(" ");
        for (int a = 0; a <= 2*i; a++) printf("*");
        for (int a = i; a <= 3; a++) printf(" ");
        printf("\n");
    }
    for (int i = 1; i <= 3; i++){
        for (int a = 0; a <= i; a++) printf(" ");
        for (int a = 6; a >= 2*i; a--) printf("*");
        for (int a = 0; a <= i; a++) printf(" ");
        printf("\n");
    }
    return 0;
}
