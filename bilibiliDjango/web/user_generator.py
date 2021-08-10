import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
django.setup()


from biliuserinfo.models import BiliUser


def main():
    filename = '/Users/xiayubing/PycharmProjects/code/bilibiliDjango/bili_user_info.csv'
    user_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            user_list.append(line)
    for line in user_list:
        if line[0] == '用户编号':
            pass
        else:
            user = BiliUser()
            user.mid = line[0]
            user.name = line[1]
            user.sex = line[2]
            user.level = line[3]
            user.sign = line[4]
            user.vip = line[5]
            user.fans_medal = line[6]
            user.following = line[7]
            user.follower = line[8]
            user.save()


if __name__ == "__main__":
    main()
