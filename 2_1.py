# 第2章-1 计算 11+12+13+...+m (30分)
# 输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值。

# 输入格式:
# 在一行输入一个正整数m。

# 输出格式:
# 在一行中按照格式“sum = S”输出对应的和S.

# 输入样例:
# 在这里给出一组输入。例如：

# 90 
# 输出样例:
# 在这里给出相应的输出。例如：

# sum = 4040

m = int(input())
S = 0
for i in range(11, m+1):
    S += i
print(f"sum = {S}")
