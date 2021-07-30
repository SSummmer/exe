"""
    练习6
"""
l = []
num = 0
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k:
                l.append(i * 100 + j * 10 + k)
                num = num + 1
print("水仙花数：", l)
print("水仙花个数：", num)
