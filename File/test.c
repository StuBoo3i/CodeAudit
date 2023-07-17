#include <stdio.h>
#include <malloc.h>

int add(int a, int b) {
    int c = a + b - 1;
    printf("%d", &c);
    return c;
}

void hello() {
    printf("Hello, world!");
}

void func2() {
    char* str = malloc(10 * sizeof(char));
}

int main() {
    hello();
    func2();
    return 0;
}