# 第4章-7 统计学生平均成绩与及格人数 (15分)
# 本题要求编写程序，计算学生们的平均成绩，并统计及格（成绩不低于60分）的人数。题目保证输入与输出均在整型范围内。

# 输入格式:
# 输入在第一行中给出非负整数N，即学生人数。第二行给出N个非负整数，即这N位学生的成绩，其间以空格分隔。

# 输出格式:
# 按照以下格式输出：

# average = 成绩均值
# count = 及格人数
# 其中平均值精确到小数点后一位。

# 输入样例:
# 5
# 77 54 92 73 60
# 输出样例:
# average = 71.2
# count = 4

N = int(input())
if N == 0:
    print(f"average = {N:.1f}\ncount = {N}")
else:
    score = list(map(int, input().split()))
    out = sum(score) / N
    count = len([i for i in score if i >= 60])
    print(f"average = {out:.1f}\ncount = {count}")