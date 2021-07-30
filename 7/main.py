"""
    练习7
"""
a = eval(input("请输入一个整数或浮点数："))
if type(a) == type(1):
    print("输入的数是整数")
elif type(a) == type(1.1):
    print("输入的数是浮点数")
