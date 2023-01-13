// convert temperature from centigrade to fahrenheit
#include <stdio.h>
int main()
{
    float c,f;
    printf("Enter temperature in centigrade: ");
    scanf("%f",&c);
    f=1.8*c+32;
    printf("Temperature in fahrenheit = %.2f",f);
    return 0;
}