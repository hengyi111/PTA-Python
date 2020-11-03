# 第4章-10 最大公约数和最小公倍数 (15分)
# 本题要求两个给定正整数的最大公约数和最小公倍数。

# 输入格式:
# 输入在一行中给出两个正整数M和N（≤1000）。

# 输出格式:
# 在一行中顺序输出M和N的最大公约数和最小公倍数，两数字间以1空格分隔。

# 输入样例:
# 511 292
# 输出样例:
# 73 2044

M, N = map(int, input().split())
yue = M
bei = N
for i in list(range(1, M+1))[::-1]:
    if M % i == 0 and N % i == 0:
        yue = i
        break
flag = True
while flag:
    bei += 1
    if bei % M == 0 and bei % N == 0:
        break
print(yue, bei)