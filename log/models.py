from django.db.models import *
from book.models import *
from reader.models import *

# Create your models here.
class Log(Model):
    reader = ForeignKey(Reader, CASCADE)
    book = ForeignKey(Book, CASCADE)
    checkout = DateTimeField('借閱時間', auto_now_add=True)
    returned = DateTimeField('歸還時間', null=True)

    def __str__(self):
        return "{} | {} | {}".format(
            self.checkout, 
            self.reader.realname, 
            self.book.title
        )
