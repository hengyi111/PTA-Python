# 第7章-1 词频统计 (30分)
# 请编写程序，对一段英文文本，统计其中所有不同单词的个数，以及词频最大的前10%的单词。

# 所谓“单词”，是指由不超过80个单词字符组成的连续字符串，但长度超过15的单词将只截取保留前15个单词字符。而合法的“单词字符”为大小写字母、数字和下划线，其它字符均认为是单词分隔符。

# 输入格式:
# 输入给出一段非空文本，最后以符号#结尾。输入保证存在至少10个不同的单词。

# 输出格式:
# 在第一行中输出文本中所有不同单词的个数。注意“单词”不区分英文大小写，例如“PAT”和“pat”被认为是同一个单词。

# 随后按照词频递减的顺序，按照词频:单词的格式输出词频最大的前10%的单词。若有并列，则按递增字典序输出。

# 输入样例：
# This is a test.

# The word "this" is the word with the highest frequency.

# Longlonglonglongword should be cut off, so is considered as the same as longlonglonglonee.  But this_8 is different than this, and this, and this...#
# this line should be ignored.
# 输出样例：（注意：虽然单词the也出现了4次，但因为我们只要输出前10%（即23个单词中的前2个）单词，而按照字母序，the排第3位，所以不输出。）
# 23
# 5:this
# 4:is

import re
import collections
import sys
words = "".join([line for line in sys.stdin])
words = re.compile(r"\w+", re.I).findall(words.lower().split('#')[0])
words = [each.strip() for each in words]
words = list(map(lambda each: each[0:15] if len(each) > 15 else each, words))
counter = collections.Counter(words)
rank = sorted(counter.items(), key=lambda each: (-each[1], each[0]), reverse=False)
print(len(rank))
for each in rank[0:int(0.1*len(rank))]:
    print("{}:{}".format(each[1], each[0]))
