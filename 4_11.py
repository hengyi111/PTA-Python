# 第4章-11 判断素数 (20分)
# 判断一个给定的正整数是否素数

# 输入格式:
# 输入在第一行给出一个正整数N（≤ 10），随后N行，每行给出一个小于1000000 的需要判断的正整数

# 输出格式:
# 对每个需要判断的正整数，如果它是素数，则在一行中输出Yes，否则输出No

# 输入样例:
# 在这里给出一组输入。例如：

# 2
# 11
# 111
# 输出样例:
# 在这里给出相应的输出。例如：

# Yes
# No

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return "No"
    else:
        return "Yes"

N = int(input())
out = []
for i in range(N):
    number = int(input())
    if number == 1:
        out.append("No")
    else:
        out.append(is_prime(number))
for i in out:
    print(i)