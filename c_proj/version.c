
#include <stdio.h>

int main() {
    #if defined(__STDC__)
        #if __STDC_VERSION__ >= 201112L
            printf("C11 or later\n");
        #elif __STDC_VERSION__ >= 199901L
            printf("C99\n");
        #else
            printf("Pre-C99\n");
        #endif
    #else
        printf("Not C standard compliant\n");
    #endif

    return 0;
}
