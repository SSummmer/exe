"""
    练习18
"""
import pandas as pd
import matplotlib.pyplot as plt
import pylab as mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False


def rating(data):
    ratings = data['Rating']
    print('电影数据评分的平均分：', ratings.mean())

    rating_list = list(ratings)
    distance = 1
    group_num = int((max(rating_list) - min(rating_list))) // distance
    plt.figure(figsize=(10, 10), dpi=80)
    plt.hist(ratings, bins=group_num)
    plt.xticks(list(range(1, 10))[::1])
    plt.title("rating的分布情况")
    plt.savefig("rating的分布情况.png")
    plt.show()


def runtime(data):
    run_time = data['Runtime (Minutes)']
    runtime_list = list(run_time)
    distance = 10
    group_num = int(max(runtime_list) - min(runtime_list)) // distance
    plt.figure(figsize=(10, 10), dpi=80)
    plt.hist(run_time, bins=group_num)
    plt.xticks(list(range(60, 200))[::10])
    plt.title("runtime的分布情况")
    plt.savefig("runtime的分布情况.png")
    plt.show()


def genre(data):
    genres = set()
    for each in data['Genre']:
        for i in each.split(','):
            genres.add(i)
    genre_list = list(genres)
    genre_df = pd.DataFrame(0, index=range(1, data.shape[0] + 1), columns=genre_list)
    row = 1
    for each in data['Genre']:
        temp = each.split(',')
        for i in temp:
            genre_df.loc[row, i] = 1
        row = row + 1
    print('电影分类情况：')
    print(genre_df)
    print('所有电影分类出现的次数：')
    for each in genre_list:
        count = genre_df[each].value_counts()[1]
        print(each + ':', count)


def main():
    data = pd.read_csv("IMDB-Movie-Data.csv")
    rating(data)
    runtime(data)
    genre(data)


if __name__ == '__main__':
    main()
