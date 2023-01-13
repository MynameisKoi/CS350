// calculate sum of 5 subjects and find percentage
#include <stdio.h>
int main()
{
    int a,b,c,d,e,sum;
    float per;
    printf("Enter marks of 5 subjects: ");
    scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
    sum=a+b+c+d+e;
    per=sum/5.0;
    printf("Sum = %d\n",sum);
    printf("Percentage = %.3f",per);
    return 0;
}