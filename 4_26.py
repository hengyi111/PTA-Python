# 第4章-26 求1!+3!+5!+……+n! (10分)
# 求1!+3!+5!+……+n!的和，要求用循环嵌套设计，n<12。

# 输入格式:
# 输入在一行中给出一个不超过12的正整数n。

# 输出格式:
# 在一行中按照格式“n=n值,s=阶乘和”的顺序输出，其中阶乘和是正整数。

# 输入样例:
# 5
# 输出样例:
# n=5,s=127

n = int(input())
result = 0
for i in range(1, n+1, 2):
    out = 1
    for j in range(1, i+1):
        out *= j
    result += out

print("n={},s={}".format(n, result))