# 第5章-1 输出星期名缩写 (70分)
# 输入一个1到7的数字，输出对应的星期名的缩写。
# 1	Mon	
# 2	Tue
# 3 Wed
# 4 Thu
# 5	Fri
# 6	Sat
# 7 Sun

# 输入格式:
# 输入1到7之间数字

# 输出格式:
# 输出对应的星期名的缩写

# 输入样例:
# 在这里给出一组输入。例如：

# 1
# 输出样例:
# 在这里给出相应的输出。例如：

# Mon

a = int(input())
days = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
print(days[a])