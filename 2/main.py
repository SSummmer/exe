"""
    练习2
"""


def cal(a, b):
    c = a * b / 2
    print("直角三角形的面积为", c)


a = int(input("请输入直角三角形的第一条直角边边长："))
b = int(input("请输入直角三角形的第二条直角边边长："))
cal(a, b)
