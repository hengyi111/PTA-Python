# 第4章-29 找出不是两个数组共有的元素 (20分)
# 给定两个整型数组，本题要求找出不是两者共有的元素。

# 输入格式:
# 输入分别在两行中给出两个整型数组，每行先给出正整数N（≤20），随后是N个整数，其间以空格分隔。

# 输出格式:
# 在一行中按照数字给出的顺序输出不是两数组共有的元素，数字间以空格分隔，但行末不得有多余的空格。题目保证至少存在一个这样的数字。同一数字不重复输出。

# 输入样例:
# 10 3 -5 2 8 0 3 5 -15 9 100
# 11 6 4 8 2 6 -5 9 0 100 8 1
# 输出样例:
# 3 5 -15 6 4 1

a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = a[0]
n = b[0]
a = a[1:]
b = b[1:]
out = []
for i in a:
    if i not in b and i not in out:
        out.append(i)

for j in b:
    if j not in a and j not in out:
        out.append(j)

print(*out, sep=' ')