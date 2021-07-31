"""
    练习12
"""
import random
import time


def bet(l=[]):
    for n in range(6):
        red = random.randint(1, 33)
        l.append(red)
        print("red:", red)
        time.sleep(3)
    time.sleep(5)
    blue = random.randint(1, 16)
    print("blue:", blue)
    l.append(blue)


if __name__ == '__main__':
    result = []
    bet(result)
    t = time.strftime("%Y年%m月%d日开奖", time.localtime())
    filename = t + '.txt'
    num = '中奖号码：' + str(result)
    print(num)
    with open(filename, 'w') as f:
        f.write(num)
