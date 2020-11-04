# 第6章函数-3 使用函数统计指定数字的个数 (20分)
# 本题要求实现一个统计整数中指定数字的个数的简单函数。

# CountDigit(number,digit )

# 其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。

# 函数接口定义：
# 在这里描述函数接口。例如：
# CountDigit(number,digit ),返回digit出现的次数
# 裁判测试程序样例：

# /* 请在这里填写答案 */

# number,digit=input().split()
# number=int(number)
# digit=int(digit)
# count=CountDigit(number,digit )
# print("Number of digit 2 in "+str(number)+":",count)
# 输入样例：
# 在这里给出一组输入。例如：

# -21252 2
# 输出样例：
# 在这里给出相应的输出。例如：

# Number of digit 2 in -21252: 3

def CountDigit(number, digit):
    count = 0
    for i in str(number):
        if i == str(digit):
            count += 1
    return count