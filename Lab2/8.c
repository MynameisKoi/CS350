// Display arithmetic operator using switch case.
#include <stdio.h>
int main(){
    int op;
    float a, b;
    printf("Enter two numbers: ");
    scanf("%f %f", &a, &b);
    printf("Enter 1 for sum \n2 for multiply \n3 for subtraction \n4 for division: ");
    scanf("%d", &op);
    switch (op){
        case 1: printf("sum = %.2f", a + b); break;
        case 2: printf("product = %.2f", a * b); break;
        case 3: printf("difference = %.2f", a - b); break;
        case 4: printf("quotient = %.2f", a / b); break;
        default: printf("Invalid operator!");
    }
    return 0;
}