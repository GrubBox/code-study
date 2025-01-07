#include <stdio.h>

int main() {
    int a = 10;
    float b = 5.5;

    /* Implicit conversion from int to float */
    float c = a + b;

    printf("Result: %f\n", c);

    return 0;
}
