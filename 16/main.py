#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    练习16
"""
import matplotlib.pyplot as plt
from pylab import mpl
import csv
from matplotlib.pyplot import MultipleLocator

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False


# 每一级的用户人数
def count(list1=[]):
    y_list = [0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 501):
        if list1[i][2] == '':
            y_list[6] = y_list[6] + 1
        else:
            num = int(list1[i][2])
            for j in range(0, 6):
                if num == j:
                    y_list[j] = y_list[j] + 1
    return y_list


def pie(x_list=[], y_list=[]):
    plt.figure(figsize=(10, 10), dpi=100)
    plt.pie(x_list, labels=y_list, autopct="%.2f%%")
    plt.title("前500名用户的b站等级分布情况饼图")
    plt.savefig("前500名用户的b站等级分布情况饼图.png")
    plt.show()


def bar(y_list=[], x_list=[]):
    plt.figure(figsize=(10, 10), dpi=100)
    plt.bar(x_list, y_list, width=0.3, color=['r', 'g', 'b'])
    plt.title("前500名用户的b站等级分布情况柱状图")
    plt.xlabel('用户等级')
    plt.ylabel('用户人数')
    plt.savefig("前500名用户的b站等级分布情况柱状图.png")
    plt.show()


def scatter(list1=[]):
    x_list = []
    y_list = []
    for i in range(1, 501):
        x_list.append(list1[i][0])
        if list1[i][2] == '':
            y_list.append(0)
        else:
            num = int(list1[i][2])
            y_list.append(num)
    plt.figure(figsize=(100, 10), dpi=50)
    plt.scatter(x_list, y_list)
    plt.title("前500名用户的id和对应等级散点图")
    plt.xlabel('用户id')
    plt.ylabel('用户等级(0代表用户不存在)')
    plt.savefig("前500名用户的id和对应等级散点图.png")
    plt.show()


def main():
    filename = 'bilibili_user.csv'
    list1 = []
    with open(filename, 'r', encoding='gbk') as f:
        lines = csv.reader(f)
        for line in lines:
            list1.append(line)
    list2 = count(list1)
    list3 = ['1', '2', '3', '4', '5', '6', '等级不存在']
    pie(list2, list3)
    bar(list2, list3)
    scatter(list1)


if __name__ == '__main__':
    main()
