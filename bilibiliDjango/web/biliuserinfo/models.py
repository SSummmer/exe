from django.db import models


# Create your models here.
class BiliUser(models.Model):
    mid = models.IntegerField(primary_key=True)  # 用户mid
    name = models.TextField()  # 用户姓名
    sex = models.TextField()  # 用户性别
    level = models.IntegerField()  # 用户等级
    sign = models.TextField()  # 用户个性签名
    vip = models.TextField()  # 是否为大会员
    fans_medal = models.TextField()  # 用户粉丝勋章
    following = models.IntegerField()  # 用户关注数
    follower = models.IntegerField()  # 用户粉丝数

    def __str__(self):
        return self.mid
