"""
    练习2
"""


def cal(a, b):
    return a * b / 2


a = int(input("请输入直角三角形的第一条直角边边长："))
b = int(input("请输入直角三角形的第二条直角边边长："))
print("直角三角形的面积为", cal(a, b))
