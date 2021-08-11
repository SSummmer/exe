### 项目说明
查看前1500名bilibili用户的相关信息，并将其某些信息进行交叉对比，借此以此分析b站相关用户情况

---
### 项目环境

python 3.8.10， macOS BigSur 11.4\
python库：django 3.2.6, requests 2.25.1, pandas 3.8.1, matplotlib 3.4.2

---
### 项目文件包说明

web 包是django项目文件\
web/user_generator.py 将bili_user_info.csv中的数据导入到django项目中\
web/run.shell 是在本地运行该程序的脚本文件
get_userinfo.py 是获取前1500名b站用户数据的爬虫文件\
bili_user_info.csv 是存放爬虫获得的用户数据的csv文件\
userinfo_png.py 是获取相关数据图表的pyhton文件，获得的图表存放在 web/biliuserinfo/static 中以供调用

---
### 项目操作说明
1. 在终端进入 bilibiliDjango/web ，运行 python manage.py runserver ；或直接运行 web/run.shell 使该项目在本地运行
2. 点击 http://127.0.0.1:8000/ 跳转到网页，再在网址上输入 '/admin/' 进入后台管理界面，输入 '/'biliuserinfo/'  进入网站首页；\
或直接在浏览器输入网址 http://127.0.0.1:8000/biliuserinfo/ 或 http://127.0.0.1:8000/admin/
3. 若进入后台管理界面，后台管理员的用户名：admin 密码：123456
4. 若进入网站首页即 "Bilibili用户信息" 界面，可在左侧看到bilibili用户的mid、用户名及个性签名，点击 "mid 用户名" 可进入详情页面，左下侧有分页栏可供选择；\
    右上侧有粉丝数排行前十的用户的mid和用户名，点击 "mid" 或 "用户名" 也可进入详情页面；\
    右下侧有一bilibili用户信息分析的图例，点击图片下方的 "查看更多相关信息按钮" 可跳转浏览更多关于用户信息的分析
5. 若进入用户信息的详情页面，主页会显示用户的详细信息，可点击下方按钮选择上一位或下一位用户，\
   也可点击右上方 "返回bilibili户信息首页" 返回网站首页
6. 若进入 "Bilibili用户信息分析" 界面，可看到将用户某些信息进行交叉对比获得的图表，\
   点击右上方 "返回bilibili户信息首页" 也可返回网站首页