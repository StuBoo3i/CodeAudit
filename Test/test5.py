from FunctionAndVariableDetection.ValueScanner import value_scanner

if __name__ == "__main__":
    # 示例代码
    source_code = """
    int add(int a, int b) {
        int c;
        c = a + b - 1;
        printf("%d", c);
        return c;
    }
    """
    print('----------------------------------------------------')
    print(value_scanner(source_code))