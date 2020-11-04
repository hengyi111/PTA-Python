# 第6章-5 列表元素个数的加权和(1) (40分)
# 输入一个嵌套列表，嵌套层次不限，根据层次，求列表元素的加权个数和。第一层每个元素算一个元素，第二层每个元素算2个元素，第三层每个元素算3个元素，第四层每个元素算4个元素,...,以此类推！

# 输入格式:
# 在一行中输入一个列表。

# 输出格式:
# 在一行中输出加权元素个数值。

# 输入样例:
# 在这里给出一组输入。例如：

# [1,2,[3,4,[5,6],7],8]
# 输出样例:
# 在这里给出相应的输出。例如：

# 15

a = eval(input())

def recursion(base, level):
    s = 0
    for i in base:
        if isinstance(i, int):
            s += level
        elif isinstance(i, list):
            s += recursion(i, level+1)
    return s
print(recursion(a, 1))

