#include <stdio.h>
#include <math.h>

int main() {
    int n, pieces;

    printf("Enter how many cuts you want: ");
    scanf("%d", &n);

    pieces = (pow(n, 2) + n + 2) / 2;

    printf("Pieces will be: %d\n", pieces);

    return 0;
}
