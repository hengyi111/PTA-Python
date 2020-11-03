# 第4章-6 输出前 n 个Fibonacci数 (15分)
# 本题要求编写程序，输出菲波那契（Fibonacci）数列的前N项，每行输出5个，题目保证输出结果在长整型范围内。Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列，例如：1，1，2，3，5，8，13，...。

# 输入格式:
# 输入在一行中给出一个整数N（1≤N≤46）。

# 输出格式:
# 输出前N个Fibonacci数，每个数占11位，每行输出5个。如果最后一行输出的个数不到5个，也需要换行。

# 如果N小于1，则输出"Invalid."

# 输入样例1:
# 7
# 输出样例1:
#           1          1          2          3          5
#           8         13
# 输入样例2：
# 0
# 输出样例2：
# Invalid.


def fib(number):  # generate fib numbers
    a, b, c = 0, 1, 1
    if number <= 2:
        return 1
    else:
        for _ in range(number-2):
            a = b
            b = c
            c = a + b
        return c

N = int(input())

if N < 1:
    print("Invalid.")
else:
    for i in range(1, N+1):
        print("{:11d}".format(fib(i)), end="")
        if i % 5 == 0:
            print("")
