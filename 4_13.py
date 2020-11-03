# 第4章-13 求误差小于输入值的e的近似值 (20分)
# 自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。ei代表前i项求和。输入误差范围error,当
# ei+1-ei<error,则表示e的近似值满足误差范围。

# 输入格式:
# 在一行输入误差范围。

# 输出格式:
# 在一行输出e的近似值（保留6位小数）。

# 输入样例1:
# 在这里给出一组输入。例如：

# 0.01
# 输出样例1:
# 在这里给出相应的输出。例如：

# 2.716667
# 输入样例2:
# 在这里给出一组输入。例如：

# 0.000000001
# 输出样例2:
# 在这里给出相应的输出。例如：

# 2.718282

def fac(n):  # calculate factorial 
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def result(m):  # calculate sum
    out = 0
    for i in range(m):
        out += 1.0 /fac(i)
    return out

error = float(input())
e2 = 2
e1 = 1
n = 1
while e2 - e1 >= error:
    e2 = result(n+1)
    e1 = result(n)
    n += 1

print(f"{e2:.6f}")