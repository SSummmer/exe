"""
    对前1500名b站用户数据的分析；
    1.用户b站等级分布情况（饼图+柱状图）
    2.用户性别分布情况（饼图+柱状图）
    3.用户会员分布情况（饼图+柱状图）
    4.用户粉丝数分布（柱状图）
    5.用户的id和对应等级情况（散点图）
"""
import pandas as pd
import matplotlib.pyplot as plt
import pylab as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False


# 每一级的用户人数
def level_count(list1=[]):
    y_list = [0, 0, 0, 0, 0, 0]
    for i in range(1, len(list1)):
        num = int(list1[i])
        for j in range(0, 6):
            if num == j + 1:
                y_list[j] = y_list[j] + 1
    return y_list


# 用户b站等级分布情况（饼图）
def level_pie(level_list):
    y_list = [1, 2, 3, 4, 5, 6]
    x_list = level_count(level_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.pie(x_list, labels=y_list, autopct="%.2f%%")
    plt.title("前1500名用户的b站等级分布情况饼图")
    plt.savefig("./web/static/前1500名用户的b站等级分布情况饼图.png")
    # plt.show()


# 用户b站等级分布情况（柱状图）
def level_bar(level_list):
    x_list = [1, 2, 3, 4, 5, 6]
    y_list = level_count(level_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.bar(x_list, y_list, width=0.3, color=['r', 'g', 'b'])
    plt.title("前1500名用户的b站等级分布情况柱状图")
    plt.xlabel('用户等级')
    plt.ylabel('用户人数')
    plt.savefig("./web/static/前1500名用户的b站等级分布情况柱状图.png")
    # plt.show()


# 每一种性别的用户人数
def sex_count(list1=[]):
    y_list = [0, 0, 0]
    for i in range(1, len(list1)):
        if list1[i] == '男':
            y_list[0] = y_list[0] + 1
        elif list1[i] == '女':
            y_list[1] = y_list[1] + 1
        elif list1[i] == '保密':
            y_list[2] = y_list[2] + 1
    return y_list


# 用户性别分布情况（饼图）
def sex_pie(sex_list):
    y_list = ['男', '女', '保密']
    x_list = sex_count(sex_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.pie(x_list, labels=y_list, autopct="%.2f%%")
    plt.title("前1500名用户性别分布情况饼图")
    plt.savefig("./web/static/前1500名用户性别分布情况饼图.png")
    # plt.show()


# 用户性别分布情况（柱状图）
def sex_bar(sex_list):
    x_list = ['男', '女', '保密']
    y_list = sex_count(sex_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.bar(x_list, y_list, width=0.3, color=['r', 'g', 'b'])
    plt.title("前1500名用户性别分布情况柱状图")
    plt.xlabel('用户性别')
    plt.ylabel('用户人数')
    plt.savefig("./web/static/前1500名用户性别分布情况柱状图.png")
    # plt.show()


# 不同会员情况及其人数：年度大会员、十年大会员、无大会员
def vip_count(list1=[]):
    y_list = [0, 0, 0]
    for i in range(1, len(list1)):
        if list1[i] == '年度大会员':
            y_list[0] = y_list[0] + 1
        elif list1[i] == '十年大会员':
            y_list[1] = y_list[1] + 1
    y_list[2] = len(list1) - y_list[0] - y_list[1]
    return y_list


# 用户会员分布情况（饼图）
def vip_pie(vip_list):
    y_list = ['年度大会员', '十年大会员', '无大会员']
    x_list = vip_count(vip_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.pie(x_list, labels=y_list, autopct="%.2f%%")
    plt.title("前1500名用户性别分布情况饼图")
    plt.savefig("./web/static/前1500名用户性别分布情况饼图.png")
    # plt.show()


# 属于每一组粉丝数的用户人数:1~1000,1001~10000,10001~100000,100001~1000000
def follower_count(list1=[]):
    y_list = [0, 0, 0, 0]
    for i in range(1, len(list1)):
        num = int(list1[i])
        if 0 < num < 1001:
            y_list[0] = y_list[0] + 1
        elif 1000 < num < 10001:
            y_list[1] = y_list[1] + 1
        elif 10000 < num < 100001:
            y_list[2] = y_list[2] + 1
        elif 100000 < num < 1000001:
            y_list[3] = y_list[3] + 1
    return y_list


# 用户粉丝数分布情况（柱状图）:1~1000,1001~10000,10001~100000,100001~1000000
def follower_bar(follower_list):
    x_list = ['1~1000', '1001~10000', '10001~100000', '100001~1000000']
    y_list = follower_count(follower_list)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.bar(x_list, y_list, width=0.3, color=['r', 'g', 'b'])
    plt.xlabel('用户粉丝数')
    plt.ylabel('用户人数')
    plt.title("前1500名用户粉丝数分布情况柱状图")
    plt.savefig("./web/static/前1500名用户粉丝数分布情况柱状图.png")
    # plt.show()


# 用户的id和对应等级情况（散点图）
def level_scatter(data):
    x_list = []
    y_list = []
    for i in range(len(data)):
        user = data.loc[i]
        x_list.append(user['用户编号'])
        y_list.append(user['用户等级'])
    plt.figure(figsize=(100, 10), dpi=50)
    plt.scatter(x_list, y_list)
    plt.title("前1500名用户的id和对应等级散点图")
    plt.xlabel('用户id')
    plt.ylabel('用户等级(0代表用户不存在)')
    plt.savefig("./web/static/前1500名用户的id和对应等级散点图.png")
    # plt.show()


def main():
    filename = 'bili_user_info.csv'
    data = pd.read_csv(filename)
    level_list = list(data['用户等级'])
    sex_list = list(data['性别'])
    vip_list = list(data['会员'])
    follower_list = list(data['粉丝数'])
    level_pie(level_list)
    level_bar(level_list)
    sex_pie(sex_list)
    sex_bar(sex_list)
    vip_pie(vip_list)
    follower_bar(follower_list)
    level_scatter(data)


if __name__ == '__main__':
    main()
