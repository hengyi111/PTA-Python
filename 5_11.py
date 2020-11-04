# 第5章-11 字典合并 (40分)
# 字典合并。输入用字符串表示两个字典，输出合并后的字典,字典的键用一个字母或数字表示。注意：1和‘1’是不同的关键字！

# 输入格式:
# 在第一行中输入第一个字典字符串 在第二行中输入第二个字典字符串

# 输出格式:
# 在一行中输出合并的字典，输出按字典序。"1"的ASCII吗为49,大于1，排序时1在前，"1"在后，其它的也一样。

# 输入样例1:
# 在这里给出一组输入。例如：

# {1:3,2:5}
# {1:5,3:7} 
# 输出样例1:
# 在这里给出相应的输出。例如：

# {1:8,2:5,3:7}
# 输入样例2:
# 在这里给出一组输入。例如：

# {"1":3,1:4}
# {"a":5,"1":6}
# 输出样例2:
# 在这里给出相应的输出。例如：

# {1:4,"1":9,"a":5}

a = eval(input())
b = eval(input())

dic = b.copy()
for k, v in a.items():
    if k in dic.keys():
        dic[k] += v
    else:
        dic[k] = v

out = sorted(dic.items(), key=lambda x:x[0] if type(x[0])==int else ord(x[0]))
# out_d = dict()
# for i in out:
#     out_d[i[0]] = i[1]
# print(out_d)
c = 0
n = len(out)
print("{", end='')
for i in out:
    c += 1
    if type(i[0]) == type(1):
        print("{}:{}".format(i[0], i[1]), end='')
    else:
        print('"{}":{}'.format(i[0], i[1]), end='')
    if c!= n:
        print(',',end='')
print("}")


