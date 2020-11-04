# 第6章函数-5 使用函数求余弦函数的近似值 (20分)
# 本题要求实现一个函数，用下列公式求cos(x)近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）：

# cos (x) = x^0 / 0! - x^2 / 2! + x^4 / 4! - x^6 / 6! + ?

# 函数接口定义：funcos(eps,x ),其中用户传入的参数为eps和x；函数funcos应返回用给定公式计算出来，保留小数4位。

# 函数接口定义：
# 函数接口:
# funcos(eps,x ),返回cos(x)的值。
# 裁判测试程序样例：
# 在这里给出函数被调用进行测试的例子。例如：


# /* 请在这里填写答案 */

# eps=float(input())
# x=float(input())
# value=funcos(eps,x )
# print("cos({0}) = {1:.4f}".format(x,value))
# 输入样例：
# 在这里给出一组输入。例如：

# 0.0001
# -3.1
# 输出样例：
# 在这里给出相应的输出。例如：

# cos(-3.1) = -0.9991

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def funcos(eps0, x0):
    out = 0.0
    i = 0
    sign = 1
    while x0**i/factorial(i) >= eps0:
        out += sign * (x0**i/factorial(i))
        sign = -sign
        i += 2
    return out
