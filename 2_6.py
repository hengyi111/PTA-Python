# 第2章-6 求交错序列前N项和 (15分)
# 本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。

# 输入格式:
# 输入在一行中给出一个正整数N。

# 输出格式:
# 在一行中输出部分和的值，结果保留三位小数。

# 输入样例:
# 5
# 输出样例:
# 0.917

N = int(input())
S = 0.0
sign = 1
for i in range(N):
    S += sign * (i + 1) / (2 * i + 1)
    sign = -sign
print("{:.3f}".format(S))