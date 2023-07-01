#include <stdio.h>
#include <stdlib.h>
void func2() {
    // 示例函数2
    char* str = malloc(10 * sizeof(char));
    // 使用分配的内存
    // 没有调用free函数
}
void func1() {
    // 示例函数1
    int* ptr = malloc(sizeof(int));
    // 使用分配的内存
    free(ptr);
}
// 其他函数...
