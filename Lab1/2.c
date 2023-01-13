// find area and circumferences of circle
#include <stdio.h>
#include <math.h>
int main()
{
    float r,area,circumference;
    printf("Enter radius of a circle: ");
    scanf("%f",&r);
    area=M_PI*r*r;
    circumference=2*M_PI*r;
    printf("Area = %.3f\n", area);
    printf("Circumference = %.3f\n", circumference);
    return 0;
}