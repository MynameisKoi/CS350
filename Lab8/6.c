#include <stdio.h>
#include <string.h>

int main() {
    char sentence[1000];
    printf("Enter a sentence: ");
    fgets(sentence, 1000, stdin);

    // Remove white spaces
    int i, j;
    for(i = 0, j = 0; sentence[i] != '\0'; i++) {
        if(sentence[i] != ' ' && sentence[i] != '\t' && sentence[i] != '\n') {
            sentence[j] = sentence[i];
            j++;
        }
    }
    sentence[j] = '\0';

    // Replace "." with ":"
    for(i = 0; sentence[i] != '\0'; i++) {
        if(sentence[i] == '.') {
            sentence[i] = ':';
        }
    }

    printf("Modified sentence: %s", sentence);

    return 0;
}
