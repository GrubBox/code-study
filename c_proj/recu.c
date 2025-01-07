
#include <stdio.h>

void printString(char* str) {
    if (*str == '\0') {
        return; // Base case: end of string
    } else {
        printf("%c", *str); // Print current character
        printString(++str); // Recur with the next character in the string
    }
}

int main() {
    char str[] = "Hello, World!";
    printString(str);
    return 0;
}
