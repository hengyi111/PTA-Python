# 第4章-15 换硬币 (20分)
# 将一笔零钱换成5分、2分和1分的硬币，要求每种硬币至少有一枚，有几种不同的换法？

# 输入格式:
# 输入在一行中给出待换的零钱数额x∈(8,100)。

# 输出格式:
# 要求按5分、2分和1分硬币的数量依次从大到小的顺序，输出各种换法。每行输出一种换法，格式为：“fen5:5分硬币数量, fen2:2分硬币数量, fen1:1分硬币数量, total:硬币总数量”。最后一行输出“count = 换法个数”。

# 输入样例:
# 13
# 输出样例:
# fen5:2, fen2:1, fen1:1, total:4
# fen5:1, fen2:3, fen1:2, total:6
# fen5:1, fen2:2, fen1:4, total:7
# fen5:1, fen2:1, fen1:6, total:8
# count = 4


# 这个是暴力方法，应该使用动态规划比较好
zong = int(input())
count = 0
out = []
for i in range(1, zong//5+1):
    for j in range(1, (zong-5*i)//2+1):
        for k in range(1, zong-5*i-2*j+1):
            if 5*i + 2*j + k == zong:
                count += 1
                out.append([i, j, k])

for i in out[::-1]:
    print(f"fen5:{i[0]}, fen2:{i[1]}, fen1:{i[2]}, total:{i[0]+i[1]+i[2]}")
print("count = {}".format(count))