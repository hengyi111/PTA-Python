# 第6章-3 列表或元组的数字元素求和 (20分)
# 求列表中数字和,列表中嵌套层次不限2层

# 输入格式:
# 在一行中输入列表或元组

# 输出格式:
# 在一行中输出数字的和

# 输入样例:
# 在这里给出一组输入。例如：

# [11,2,[3,7],(68,-1),"123",9]
# 输出样例:
# 在这里给出相应的输出。例如：

# 99

def recursion(base):
    s = 0
    for i in base:
        if isinstance(i, int):
            s += i
        elif isinstance(i, list) or isinstance(i, tuple):
            s += recursion(i)
    return s
a = eval(input())
print(recursion(a))
