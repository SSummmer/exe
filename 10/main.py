"""
    练习10
"""


def cal(a, b):
    return a * b / 2


try:
    a = int(input("请输入直角三角形的第一条直角边边长："))
    b = int(input("请输入直角三角形的第二条直角边边长："))
except Exception as e:
    print(e, "请输入合理的变量值")
else:
    print("直角三角形的面积为", cal(a, b))
