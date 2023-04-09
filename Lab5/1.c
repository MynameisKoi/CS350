#include <stdio.h>

int main(){
    printf("Enter total number of Petri dishes: ");
    int n;
    scanf("%d", &n);
    printf("Enter Petri dish label, original bacterial number, new bacterial number after one hour reproduction:\n");
    int label[n], original[n], new[n];
    for(int i = 0; i < n; i++){
        scanf("%d %d %d", &label[i], &original[i], &new[i]);
    }

    // check the production rate
    float rate[n];
    for(int i = 0; i < n; i++){
        rate[i] = (float)new[i] / original[i];
    }

    // suppose that PR of A sub-species is ~100X, and of B is ~10X
    // decide what species the PR belongs to
    int arrA[n], arrB[n];
    for(int i = 0; i < n; i++){
        if(rate[i] >= 100){
            arrA[i] = 1;
            arrB[i] = 0;
        }
        else{
            arrA[i] = 0;
            arrB[i] = 1;
        }
    }

    // count the number of 1 in A and B array
    int countA = 0, countB = 0;
    for(int i = 0; i < n; i++){
        if(arrA[i] == 1){
            countA++;
        }
        else{
            countB++;
        }
    }

    int A[countA], B[countB], a=0, b=0;
    for(int i = 0; i < n; i++){
        if(arrA[i] == 1){
            A[a] = label[i];
            a++;
        }
        else{
            B[b] = label[i];
            b++;
        }
    }

    // print A and B
    // printf("A sub-species Petri dish labels are ");
    // for(int i = 0; i < countA; i++){
    //     printf("%d ", A[i]);
    // }
    // printf("\n");
    // printf("B sub-species Petri dish labels are ");
    // for(int i = 0; i < countB; i++){
    //     printf("%d ", B[i]);
    // }
    // printf("\n");

    // sort the A and B array by the PR of label[i]
    int temp;
    int sizeA = sizeof(A) / sizeof(A[0]);
    int sizeB = sizeof(B) / sizeof(B[0]);
    for(int i = 0; i < countA; i++){
        for(int j = i+1; j < countA; j++){
            if(rate[A[i]-1] > rate[A[j]-1]){
                temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
    }
    for(int i = 0; i < countB; i++){
        for(int j = i+1; j < countB; j++){
            if(rate[B[i]-1] > rate[B[j]-1]){
                temp = B[i];
                B[i] = B[j];
                B[j] = temp;
            }
        }
    }

    // print the result
    printf("%d in A sub-species and Petri dish labels from smaller to bigger PR are ", sizeA);
    for(int i = 0; i < sizeA; i++){
        printf("%d ", A[i]);
    }
    printf("\n");
    printf("%d in B sub-species and Petri dish labels from smaller to bigger PR are ", sizeB);
    for(int i = 0; i < sizeB; i++){
        printf("%d ", B[i]);
    }

};