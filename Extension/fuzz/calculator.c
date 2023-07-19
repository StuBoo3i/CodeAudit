#include <stdio.h>

int add_numbers(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);
    int result = add_numbers(num1, num2);
    printf("Result: %d\n", result);
    return 0;
}