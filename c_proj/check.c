
#include <stdio.h>

int main() {
    char string[] = " ABCDEFGH"; // String to search
    char character = 'z'; // Character to search for
    int found = 0;

    // Check if character is present in string
    for (int i = 0; string[i] != '\0'; i++) {
        if (string[i] == character) {
            found = 1;
            break;
        }
    }

    // Display result
    if (found) {
        printf("'%c' is present in the string.\n", character);
    } else {
        printf("'%c' is not present in the string.\n", character);
    }

    return 0;
}
