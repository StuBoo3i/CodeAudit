from FunctionAndVariableDetection.ValueScanner import value_scanner, p_value_to_SQL, scan_v_from_f
from Tools.FormatFunctionStatements import replace_comments



# 示例代码
c_code = '''
   int add(int a, int b) {
       //
    char* str = malloc(10 * sizeof(char));
    //
    //
   }
   '''
scan_v_from_f()

