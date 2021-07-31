"""
    练习9
"""
import re
from collections import Counter

f = open('TheOldManAndtheSea.txt', 'r')
word_dict = {}
numTen = []
for line in f.readlines():
    line = re.sub(r',.:;?"\'()', ' ', line)
    line.lower()
    word_list = line.split()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
f.close()

count = Counter(word_dict)
print(count.most_common()[:10])
