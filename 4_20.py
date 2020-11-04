# 第4章-20 求矩阵各行元素之和 (15分)
# 本题要求编写程序，求一个给定的m×n矩阵各行元素之和。

# 输入格式：
# 输入第一行给出两个正整数m和n（1≤m,n≤6）。随后m行，每行给出n个整数，其间

# 以空格分隔。

# 输出格式：
# 每行输出对应矩阵行元素之和。

# 输入样例：
# 3 2
# 6 3
# 1 -8
# 3 12
# 输出样例：
# 9
# -7
# 15

m,n = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append([int(q) for q in input().split()])
for j in matrix:
    print(sum(j))