from django.db.models import *
# from datetime import datetime

# Create your models here.
# 工具函式：轉換上傳檔案的檔名
# def pname(instance, filename):
#     # 將上傳的檔案的主檔名變更為 UNIX_TIMESTAMP 的形式，保留副檔名，例：
#     #   測試主檔名1.jpeg -> 1581260567.jpeg
#     #   書籍封面2.png    -> 1581263943.png
#     ext = filename.split('.')[-1]   # 取得原始副檔名
#     timefmt = "%s." + ext   # '%s' 標記對 strftime() 表示 UNIX TIMESTAMP
#     return now().strftime(timefmt)  # 取得現在時間，再依 timefmt 格式轉成字串

# 圖書
class Book(Model):
    title = CharField('書名', max_length=255)
    author = CharField('作者', max_length=255)
    publisher = CharField('出版社', max_length=255)
    preface = ImageField('封面圖片')

    def __str__(self):
        return "{}: {}".format(self.author, self.title)