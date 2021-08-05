"""
    练习14
"""
import requests
import time
import random

headers = {'User-Agent': "Mozilla/5.0(WindowsNT10.0;Win64;x64)" +
                         "AppleWebKit/537.36(KHTML,likeGecko)" +
                         "Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

with open('bili_user_info.csv', 'w') as f:
    f.write(','.join(['用户编号', '用户名', '用户等级', '是否存在\n']))
    for i in range(1, 501):
        time.sleep(random.randint(0, 2))
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(i)
        r = requests.get(url=url, headers=headers)
        result = r.json()
        print(i)
        if result['code'] != 0:
            f.write(','.join([str(i), '', '', '用户已注销\n', ]))
        else:
            data = result['data']
            f.write(','.join([str(data['mid']),
                              str(data['name']),
                              str(data['level']),
                              '用户存在\n',
                              ]
                             )
                    )
