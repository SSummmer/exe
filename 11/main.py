"""
    练习11
"""
import random

def bet(l = []):
    for n in range(6):
        red = random.randint(1, 33)
        l.append(red)
    blue = random.randint(1, 16)
    l.append(blue)


if __name__ == '__main__':
    num = int(input("请输入您所需要的随机注数量："))
    list1 = []
    for i in range(num):
        list2 = []
        bet(list2)
        list1.append(list2)
    while True:
        print("1. 保存到文件中")
        print("2. 直接输出在页面上")
        c = int(input("请选择如何处理结果："))
        if c == 1:
            result = ''
            f = open('double_color_ball.txt', 'w+')
            for i in range(len(list1)):
                result = str(i+1) + ':' + str(list1[i])
                f.writelines(result)
            f.close()
            print("保存成功!")
            break
        elif c == 2:
            for i in range(len(list1)):
                print(str(i+1) + ':' + str(list1[i]))
            break
        else:
            print("请输入正确序号！")
