# 第4章-30 找完数 (20分)
# 所谓完数就是该数恰好等于除自身外的因子之和。例如：6=1+2+3，其中1、2、3为6的因子。本题要求编写程序，找出任意两正整数m和n之间的所有完数。

# 输入格式：
# 输入在一行中给出2个正整数m和n（1<m≤n≤10000），中间以空格分隔。

# 输出格式：
# 逐行输出给定范围内每个完数的因子累加形式的分解式，每个完数占一行，格式为“完数 = 因子1 + 因子2 + ... + 因子k”，其中完数和因子均按递增顺序给出。若区间内没有完数，则输出“None”。

# 输入样例：
# 2 30
# 输出样例：
# 6 = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14


import math
def find_factor(f: int):  # 找到所有因子
    factor = [1]
    for ii in range(2, int(math.sqrt(f)) + 1):
        if f % ii == 0:
            factor.append(ii)
            factor.append(f//ii)
            factor.sort()
    return factor


m, n = map(int, input().split())
flag = False
for i in range(m, n + 1):
    if i == sum(find_factor(i)):
        print("{} = {}".format(i, ' + '.join([str(j) for j in find_factor(i)])))
        flag = True
if flag is False:
    print("None")


