"""
    练习17
"""
import pandas as pd

data = pd.read_csv('bilibili_user.csv', encoding='gbk')
data = data.dropna()

level = data['用户的等级']
bins = [-1, 1, 3, 5, 6]
level_counts = pd.cut(level, bins)
dummies = pd.get_dummies(level_counts)
dummies.columns = ['新用户', '普通用户', '老用户', '骨灰用户']
dummies.index = dummies.index + 1

print(dummies)
print('新用户:', dummies['新用户'].value_counts()[1])
print('普通用户:', dummies['普通用户'].value_counts()[1])
print('老用户:', dummies['老用户'].value_counts()[1])
print('骨灰用户:', dummies['骨灰用户'].value_counts()[1])
