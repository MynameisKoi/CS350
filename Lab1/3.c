// find simple interest
#include <stdio.h>
int main(){
    float p,r,t,si;
    printf("Enter principal, rate of interest and time to find simple interest: ");
    scanf("%f%f%f",&p,&r,&t);
    si=p*r*t/100;
    printf("Simple interest = %.2f",si);
    return 0;
}