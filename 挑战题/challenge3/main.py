"""
    挑战题3
"""
import datetime
import pandas as pd


def main():
    data = pd.read_csv("class_register.data")
    # 统计出所有参与签到的学生姓名
    name_list = []
    for name in data['打卡身份']:
        if name not in name_list:
            name_list.append(name)
    # print('所有参与签到的学生姓名:')
    # for i in name_list:
    #     print(i, end=' ')

    date_list = []  # 求日期的列表
    for row in data['提交时间（自动）']:
        date = row.split(' ')
        if date[0] not in date_list:
            date_list.append(date[0])
    # 求各个日期的上下午的打卡时间的列表：日期-上下午-时间
    times_list = [[[] for j in range(2)] for i in range(len(date_list))]
    for row in data['提交时间（自动）']:
        date = row.split(' ')
        time1 = date[1].split(':')
        noon = int(time1[0])  # 8~12:上午，13~17:下午
        if 7 < noon < 12:
            index1 = 0
        elif 13 < noon < 18:
            index1 = 1
        index2 = date_list.index(date[0])  # 日期顺序
        times_list[index2][index1].append(row)

    number = 0      # 打卡次数
    median_list = [[] for i in range(len(date_list))]   # 求中位数
    for each in times_list:
        for i in each:
            num_list = []
            for j in i:
                date = j.split(' ')
                num_list.append(date[1])
                index = date_list.index(date[0])
            median = str(pd.to_timedelta(num_list).median())
            if median == 'NaT':
                median_list[index].append('')
            else:
                number = number + 1
                time1 = median.split(' ')
                median_list[index].append(date[0] + ' ' + time1[2][:8])

    date_list.append('打卡时间有问题次数')
    date_list.append('缺卡次数')

    register_df = pd.DataFrame(0, index=date_list, columns=name_list)
    register_df.loc['缺卡次数'] = number
    for i in range(len(data)):
        stu = data.loc[i]
        date = stu['提交时间（自动）'].split(' ')
        time1 = date[1].split(':')
        noon = int(time1[0])  # 8~12:上午，13~17:下午
        if 7 < noon < 12:
            index1 = 0
        elif 13 < noon < 18:
            index1 = 1
        index = date_list.index(date[0])
        time_f = datetime.datetime.strptime(stu['提交时间（自动）'], '%Y-%m-%d %H:%M:%S')
        median = datetime.datetime.strptime(median_list[index][index1], '%Y-%m-%d %H:%M:%S')
        add = median + datetime.timedelta(minutes=5)
        minus = median - datetime.timedelta(minutes=5)
        if minus <= time_f <= add:
            loc1 = register_df.loc[date[0], stu['打卡身份']]
            register_df.loc[date[0], stu['打卡身份']] = loc1 + 1
            loc2 = register_df.loc['缺卡次数', stu['打卡身份']]
            register_df.loc['缺卡次数', stu['打卡身份']] = loc2 - 1
        else:
            loc1 = register_df.loc['打卡时间有问题次数', stu['打卡身份']]
            register_df.loc['打卡时间有问题次数', stu['打卡身份']] = loc1 + 1
            loc2 = register_df.loc['缺卡次数', stu['打卡身份']]
            register_df.loc['缺卡次数', stu['打卡身份']] = loc2 - 1
    # print(register_df)
    register_df.to_csv('class_register_result.data')


if __name__ == '__main__':
    main()
