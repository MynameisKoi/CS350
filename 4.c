#include <stdio.h>

int main() {
    char ans[] = {'b', 't', 'h', 'd'};
    // array with 4 values 'd', 'h', 'b', 't'
    char arr[] = {'t', 'b', 'd', 'h'};
    int m,n,o,p;

    // display 4 students under 4 statements
    // m = (ans[0] == 'd' || ans[3] == 'h' || ans[2] == 'b');
    // n = (ans[0] == 'h' || ans[3] == 'd' || ans[1] == 'b' || ans[2] == 't');
    // o = (ans[3] == 'h' || ans[2] == 'd');
    // p = (ans[0] == 'b' || ans[3] == 't' || ans[1] == 'h' || ans[2] == 'd');

    // swap and permute all possible combinations of ans to check if all m n o p true
    // if so, print the ans
    for(int i = 0; i < 4; i++) {
        ans[0] = arr[i];
        for(int j = 0; j < 4; j++) {
            if (j == i) continue;
            ans[1] = arr[j];
            for(int k = 0; k < 4; k++) {
                if (k == i || k == j) continue;
                ans[2] = arr[k];
                for(int l = 0; l < 4; l++) {
                    if (l == i || l == j || l == k) continue;
                    ans[3] = arr[l];
                    m = (ans[0] == 'd' || ans[3] == 'h' || ans[2] == 'b');
                    n = (ans[0] == 'h' || ans[3] == 'd' || ans[1] == 'b' || ans[2] == 't');
                    o = (ans[3] == 'h' || ans[2] == 'd');
                    p = (ans[0] == 'b' || ans[3] == 't' || ans[1] == 'h' || ans[2] == 'd');
                    if(m && n && o && p) {
                        printf("Size sequence from big to small: %c > %c > %c > %c\n", ans[0], ans[1], ans[2], ans[3]);
                    }
                }
            }
        }
    }



    return 0;
}
