#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    printf("Enter the first string: ");
    scanf("%s", str1);
    printf("Enter the second string: ");
    scanf("%s", str2);

    int freq1[26] = {0}, freq2[26] = {0};
    int i;

    // Update frequency of characters in the first string
    for (i = 0; str1[i] != '\0'; i++) {
        freq1[str1[i] - 'a']++;
    }

    // Update frequency of characters in the second string
    for (i = 0; str2[i] != '\0'; i++) {
        freq2[str2[i] - 'a']++;
    }

    // Check if the two arrays have the same frequency of characters
    // If they do, then they are anagrams
    for (i = 0; i < 26; i++) {
        if (freq1[i] != freq2[i]) {
            printf("Result: No");
            return 0;
        }
    }

    printf("Result: Yes");
    return 0;
}
