# 第4章-16 jmu-python-判断是否构成三角形 (10分)
# 输入三角形的三边，判断是否能构成三角形。若能构成输出yes，否则输出no。

# 输入格式:
# 在一行中直接输入3个整数，3个整数之间各用一个空格间隔，没有其他任何附加字符。

# 输出格式:
# 直接输出yes或no，没有其他任何附加字符。

# 输入样例1:
# 3 4 5
# 输出样例1:
# yes
# 输入样例2:
# 1 2 3
# 输出样例2:
# no


a, b, c = map(int, input().split())
if a+b > c and a+c > b and b+c > a:
    print("yes")
else:
    print("no")