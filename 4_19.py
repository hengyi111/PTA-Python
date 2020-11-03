# 第4章-19 矩阵运算 (20分)
# 给定一个n×n的方阵，本题要求计算该矩阵除副对角线、最后一列和最后一行以外的所有元素之和。副对角线为从矩阵的右上角至左下角的连线。

# 输入格式:
# 输入第一行给出正整数n（1<n≤10）；随后n行，每行给出n个整数，其间以空格分隔。

# 输出格式:
# 在一行中给出该矩阵除副对角线、最后一列和最后一行以外的所有元素之和。

# 输入样例:
# 4
# 2 3 4 1
# 5 6 1 1
# 7 1 8 1
# 1 1 1 1
# 输出样例:
# 35

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
N = n - 1
# 除副对角线、最后一列和最后一行以外的所有元素
for j in range(n):
    matrix[j][N-j] = 0
    matrix[j][N] = 0
    matrix[N][j] = 0
out = 0
# print(matrix)
for q in matrix:
    out += sum(q)
print(out)