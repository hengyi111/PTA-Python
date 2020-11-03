# 第3章-18 输出10个不重复的英文字母 (30分)
# 随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。 如没有10个英文字母，显示信息“not found”

# 输入格式:
# 在一行中输入字符串

# 输出格式:
# 在一行中输出最左边的10个不重复的英文字母或显示信息“not found"

# 输入样例1:
# 在这里给出一组输入。例如：

# poemp134
# 输出样例1:
# 在这里给出相应的输出。例如：

# not found
# 输入样例2
# 在这里给出一组输入。例如：

# This is a test example
# 输出样例2:
# 在这里给出相应的输出。例如：

# Thisaexmpl

str1 = input()
a = ''
for i in str1:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        if (i.lower() not in a) and (i.upper() not in a):
            a += i
if len(a) < 10:
    print("not found")
else:
    print(a[0:10])
