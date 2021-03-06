# 第6章-8 输出全排列 (20分)
# 输入整数n（3<=n<=7）,编写程序输出1,2,...,n整数的全排列，按字典序输出。

# 输入格式:
# 一行输入正整数n。

# 输出格式:
# 按字典序输出1到n的全排列。每种排列占一行，数字间无空格。

# 输入样例:
# 在这里给出一组输入。例如：

# 3
# 输出样例:
# 在这里给出相应的输出。例如：

# 123
# 132
# 213
# 231
# 312
# 321

import itertools
a = int(input())
for i in itertools.permutations(range(1, a+1), a):
    for j in i:
        print(j, sep='', end='')
    print()