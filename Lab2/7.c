// use switch statement to display Monday to Sunday
#include <stdio.h>
int main(){
    char n;
    printf("enter m for Monday \nt for Tuesday \nw for Wednesday \nh for Thursday \n");
    printf("f for Friday \ns for Saturday \nu for Sunday: ");
    scanf("%c", &n);
    switch (n){
        case 'm': printf("Monday"); break;
        case 't': printf("Tuesday"); break;
        case 'w': printf("Wednesday"); break;
        case 'h': printf("Thursday"); break;
        case 'f': printf("Friday"); break;
        case 's': printf("Saturday"); break;
        case 'u': printf("Sunday"); break;
        default: printf("Invalid input!");
    }
    return 0;
}