# 第3章-5 字符转换 (15分)
# 本题要求提取一个字符串中的所有数字字符（'0'……'9'），将其转换为一个整数输出。

# 输入格式：
# 输入在一行中给出一个不超过80个字符且以回车结束的字符串。

# 输出格式：
# 在一行中输出转换后的整数。题目保证输出不超过长整型范围。

# 输入样例：
# free82jeep5
# 输出样例：
# 825

# solution 1
s = input()
numbers = ""
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        numbers += s[i]
print(int(numbers))

# solution 2
from functools import reduce
s = input()
out = reduce(lambda x, y: x+y, [i for i in s if '0' <= i <= '9'])
print("{:d}".format(int(out)))


