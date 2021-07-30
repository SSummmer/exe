"""
    练习3
"""
num = int(input("请输入一个整数："))
if num < 1 or num > 10:
    print("请输出1-10以内的数字")
else:
    for i in range(1, num + 1):
        for j in range(1, num - i + 1):
            print(" ", end="")
        for k in range(1, i * 2):
            print("=", end="")
        print("")
