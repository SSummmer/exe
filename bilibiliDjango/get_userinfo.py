"""
    获取前1500名b站用户数据
"""
import requests
import time
import random

headers = {'User-Agent': "Mozilla/5.0(WindowsNT10.0;Win64;x64)" +
                         "AppleWebKit/537.36(KHTML,likeGecko)" +
                         "Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

with open('bili_user_info.csv', 'w') as f:
    f.write(','.join(['用户编号', '用户名', '性别', '用户等级', '个性签名', '会员', '粉丝勋章', '关注数', '粉丝数\n']))
    for i in range(1, 1501):
        time.sleep(random.randint(0, 2))
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(i)
        url1 = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp'.format(i)
        r = requests.get(url=url, headers=headers)
        r1 = requests.get(url=url1, headers=headers)
        result = r.json()
        result1 = r1.json()
        if result['code'] != 0:
            pass
            # f.write(','.join([str(i), '', '', '用户已注销\n', ]))
        else:
            data = result['data']
            data1 = result1['data']
            vip = data['vip']
            label = vip['label']
            fans_medal = data['fans_medal']
            if '\n' in str(data['sign']):
                str3 = str(data['sign']).replace('\n', ' ')
            elif '\r' in str(data['sign']):
                str3 = str(data['sign']).replace('\r', ' ')
            elif ',' in str(data['sign']):
                str3 = str(data['sign']).replace(',', ' ')
            else:
                str3 = str(data['sign'])
            if label['text'] is None:
                str1 = ''
            else:
                str1 = str(label['text'])
            if fans_medal['medal'] is None:
                str2 = ''
            else:
                str2 = str(fans_medal['medal']['medal_name'])
            f.write(','.join([str(data['mid']),
                              str(data['name']),
                              str(data['sex']),
                              str(data['level']),
                              str3,
                              str1,
                              str2,
                              str(data1['following']),
                              str(data1['follower']) + '\n',
                              ]
                             )
                    )
