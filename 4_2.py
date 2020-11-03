# 第4章-2 统计素数并求和 (20分)
# 本题要求统计给定整数M和N区间内素数的个数并对它们求和。

# 输入格式:
# 输入在一行中给出两个正整数M和N（1≤M≤N≤500）。

# 输出格式:
# 在一行中顺序输出M和N区间内素数的个数以及它们的和，数字间以空格分隔。

# 输入样例:
# 10 31
# 输出样例:
# 7 143

def is_prime(num):  # determine the num is prime or not
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        return num

M, N = map(int, input().split())
count = 0
addition = 0
if M < 2:
    M = 2

for i in range(M, N + 1):
    out = is_prime(i)
    if out is not None:
        count += 1
        addition += out
print(count, addition)