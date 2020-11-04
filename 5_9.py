# 第5章-9 求矩阵鞍点的个数 (30分)
# 一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。

# 本题要求编写程序，求一个给定的n阶方阵的鞍点。

# 输入格式： 输入第一行给出一个正整数n（1≤n≤6）。随后n行，每行给出n个整数，其间以空格分隔。

# 输出格式： 鞍点的个数

# 输入样例1：

# 4  
# 1 7 4 1   
# 4 8 3 6
# 1 6 1 2
# 0 7 8 9
# 输出样例1：

# 1
# 输入样例2：

# 2
# 1 7
# 4 1
# 输出样例2：

# 0
# 输入样例3：

# 3
# 4    7    8
# 1    3    3
# 2    3    1
# 输出样例3：

# 2

n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

count = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == max(mat[i]) and mat[i][j] == min([x[j] for x in mat]):
            count += 1
print(count)