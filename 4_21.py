# 第4章-21 判断上三角矩阵 (15分)
# 上三角矩阵指主对角线以下的元素都为0的矩阵；主对角线为从矩阵的左上角至右下角的连线。

# 本题要求编写程序，判断一个给定的方阵是否上三角矩阵。

# 输入格式：
# 输入第一行给出一个正整数T，为待测矩阵的个数。接下来给出T个矩阵的信息：每个矩阵信息的第一行给出一个不超过10的正整数n。随后n行，每行给出n个整数，其间以空格分隔。

# 输出格式：
# 每个矩阵的判断结果占一行。如果输入的矩阵是上三角矩阵，输出“YES”，否则输出“NO”。

# 输入样例：
# 2
# 3
# 1 2 3
# 0 4 5
# 0 0 6
# 2
# 1 0
# -8 2
# 输出样例：
# YES
# NO

T = int(input())

for yy in range(T):
    n = int(input())
    count = 0
    a = []
    for ii in range(n):
        a.append(list(map(int, input().split())))
    for t in range(n):
        for y in range(n):
            if t > y:
                if a[t][y] == 0:
                    count += 1
    if count == n * (n - 1) / 2:
        print("YES")
    else:
        print("NO")



