"""
    练习8
"""


def encode(pwd):
    l = []
    for i in range(len(pwd)):
        if pwd[i] == ' ':
            l.append(chr(32))
        else:
            c = ord(pwd[i]) + 3
            l.append(chr(c))
    print(l)


def decode(pwd):
    for i in range(len(pwd)):
        if pwd[i] == ' ':
            print(' ', end='')
        else:
            c = ord(pwd[i]) - 3
            print(chr(c), end='')


print("1. 加密")
print("2. 解密")
choice = int(input("选择需要的功能："))
if choice == 1:
    pwd = input("原码：")
    print("加密后的密文:", end='')
    encode(pwd)
elif choice == 2:
    pwd = input("密文：")
    print("原码：", end='')
    decode(pwd)
else:
    print("选项输入错误！")
