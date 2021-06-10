from django.db.models import *

# Create your models here.
# 讀者資料
class Reader(Model):
    realname = CharField('姓名', max_length=32)
    tel = CharField('聯絡電話', max_length=255)
    email = CharField('座位編號', max_length=60)

    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.email, 
            self.tel
        )