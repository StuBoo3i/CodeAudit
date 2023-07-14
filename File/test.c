#include <stdio.h>

int add(int a, int b) {
    int c = a + b - 1;
    printf(c);
    return c;
}

void hello() {
    printf("Hello, world!");
}

int main() {
    hello();
    return 0;
}