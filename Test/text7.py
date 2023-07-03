from FunctionAndVariableDetection.ValueScanner import analyze_type



# 示例代码
c_code = '''
   int add(int a, int b) {
       c = a + b - 1;
       printf(c);
       return c;
   }
   '''
print(analyze_type(c_code))
