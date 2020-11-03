# 第4章-23 求矩阵的局部极大值 (15分)
# 给定M行N列的整数矩阵A，如果A的非边界元素A[i][j]大于相邻的上下左右4个元素，那么就称元素A[i][j]是矩阵的局部极大值。本题要求给定矩阵的全部局部极大值及其所在的位置。

# 输入格式：
# 输入在第一行中给出矩阵A的行数M和列数N（3≤M,N≤20）；最后M行，每行给出A在该行的N个元素的值。数字间以空格分隔。

# 输出格式：
# 每行按照“元素值 行号 列号”的格式输出一个局部极大值，其中行、列编号从1开始。要求按照行号递增输出；若同行有超过1个局部极大值，则该行按列号递增输出。若没有局部极大值，则输出“None 总行数 总列数”。

# 输入样例1：
# 4 5
# 1 1 1 1 1
# 1 3 9 3 1
# 1 5 3 5 1
# 1 1 1 1 1
# 输出样例1：
# 9 2 3
# 5 3 2
# 5 3 4
# 输入样例2：
# 3 5
# 1 1 1 1 1
# 9 3 9 9 1
# 1 5 3 5 1
# 输出样例2：
# None 3 5

M, N = map(int, input().split())

matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

out = []
for i in range(1, M-1):
    for j in range(1, N-1):
        if matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i+1][j] and matrix[i][j] > matrix[i][j-1] \
                and matrix[i][j] > matrix[i][j+1]:
            out.append([str(matrix[i][j]), str(i+1), str(j+1)])

if out:
    for i in out:
        print(" ".join(i))
else:
    print("None {} {}".format(M, N))
