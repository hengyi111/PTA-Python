# 第4章-27 二维数组中每行最大值和每行和 (10分)
# 求一个3*3二维数组中每行的最大值和每行的和。

# 输入格式:
# 在一行中输入9个小于100的整数，其间各以一个空格间隔

# 输出格式:
# 输出3行3列的二维数组，并在每行后面分别输出每行最大值和每行元素的和，每个数据输出占4列。

# 输入样例:
# 3 6 5 9 8 2 1 4 5
# 输出样例:
#    3   6   5   6  14
#    9   8   2   9  19
#    1   4   5   5  10

a = list(map(int, input().split()))
m = []
mid = []
amax = 0
asum = 0
for i in a:
    mid.append(i)
    if i > amax:
        amax = i
    asum += i
    if len(mid) == 3:
        mid.extend([amax,asum])
        m.append(mid)
        mid = []
        amax = 0
        asum = 0

for i in m:
    for j in i:
        print("{:4d}".format(j), end='')
    print()