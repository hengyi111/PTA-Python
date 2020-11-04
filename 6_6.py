# 第6章-6 求指定层的元素个数 (40分)
# 输入一个嵌套列表，再输入层数，求该层的数字元素个数。

# 输入格式:
# 第一行输入列表 第二行输入层数

# 输出格式:
# 在一行中输出元素个数

# 输入样例:
# 在这里给出一组输入。例如：

# [1,2,[3,4,[5,6],7],8]
# 3
# 输出样例:
# 在这里给出相应的输出。例如：

# 2

s = input()
n = int(input())

level = 0
count = 0
for i in range(len(s)):
    # print(s[i])
    if s[i] == '[':
        level += 1
    elif s[i] == ']':
        level -= 1

    if level == n and s[i].isdigit():
        count += 1
print(count)



