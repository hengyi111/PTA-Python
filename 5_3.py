# 第5章-3 四则运算（用字典实现） (30分)
# 四则运算（用字典实现），比较c语言的switch语句。

# 输入格式:
# 在一行中输入一个数字 在一行中输入一个四帜运算符(+,-,*,/) 在一行中输入一个数字

# 输出格式:
# 在一行中输出运算结果（小数保留2位）

# 输入样例1:
# 在这里给出一组输入。例如：

# 7
# /
# 3
# 输出样例1:
# 在这里给出相应的输出。例如：

# 2.33
# 输入样例2:
# 在这里给出一组输入。例如：

# 10
# /
# 0
# 输出样例2:
# 在这里给出相应的输出。例如：

# divided by zero

a = int(input())
cal = input()
b = int(input())

if cal == '/' and b == 0:
    print("divided by zero")
else:
    dic = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
    print("{:.2f}".format(dic[cal]))