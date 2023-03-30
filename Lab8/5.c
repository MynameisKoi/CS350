#include <stdio.h>

int main() {
    char sentence[1000];
    int wordCount = 0;
    int charCounts[100]; // assume there is no more than 100 words in a sentence
    int charCount = 0;

    printf("Enter a sentence: ");
    fgets(sentence, 1000, stdin);

    // count the number of words
    for(int i = 0; sentence[i] != '\0'; i++) {
        if(sentence[i] == ' ' || sentence[i] == '\n') {
            charCounts[wordCount] = charCount;
            charCount = 0;
            wordCount++;
        } else {
            charCount++;
        }
    }

    printf("Total number of words: %d\n", wordCount);
    printf("Number of characters for each: ");

    for(int i = 0; i < wordCount; i++) {
        printf("%d ", charCounts[i]);
    }

    return 0;
}
