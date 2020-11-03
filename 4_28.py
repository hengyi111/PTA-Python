# 第4章-28 矩阵转置 (10分)
# 将一个3×3矩阵转置（即行和列互换）。

# 输入格式:
# 在一行中输入9个小于100的整数，其间各以一个空格间隔。

# 输出格式:
# 输出3行3列的二维数组，每个数据输出占4列。

# 输入样例:
# 1 2 3 4 5 6 7 8 9
# 输出样例:
#    1   4   7
#    2   5   8
#    3   6   9

a = list(map(int, input().split()))
out = []
mid = []
for i in a:
    mid.append(i)
    if len(mid) == 3:
        out.append(mid)
        mid = []

matrix = out

# 做转置
# 相当于在for j in range(4)的循环中执行[row[j] for row in m]
T_matrix = [[row[j] for row in matrix] for j in range(3)]

for i in T_matrix:
    for j in i:
        print("{:4d}".format(j), end='')
    print()
