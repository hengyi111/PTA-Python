# 第4章-14 统计字符 (15分)
# 本题要求编写程序，输入10个字符，统计其中英文字母、空格或回车、数字字符和其他字符的个数。

# 输入格式:
# 输入为10个字符。最后一个回车表示输入结束，不算在内。

# 输出格式:
# 在一行内按照

# letter = 英文字母个数, blank = 空格或回车个数, digit = 数字字符个数, other = 其他字符个数
# 的格式输出。

# 输入样例:
# aZ &
# 09 Az
# 输出样例:
# letter = 4, blank = 3, digit = 2, other = 1

s = []; count = 0
letters = 0; space = 0;digit = 0;others = 0
while True:  # 用死循环来读入回车
    b = list(input())
    count = count + 1  # 统计回车个数
    s.extend(b)
    if len(s) + count > 10:
        count -= 1  # 最后一个回车不算
        break

c = list()
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print("letter = {}, blank = {}, digit = {}, other = {}".format(letters,space+count,digit,others))
