from django.db import models

# Create your models here.
class Board(models.Model):
    # num int primary key auto_increment -> 언어자체에서 증가, 수동으로 할때에는 insert into~(1, 'hong')
    num = models.AutoField(primary_key=True) # 자동증가하는 경우
    name = models.CharField(max_length=30) # 작성자
    pass1 = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)  # 한글 2000자
    regdate = models.DateTimeField() # 작성날짜
    readcnt = models.IntegerField(default=0)
    file1 = models.CharField(max_length=100)

    # toString()
    def __str__(self):
        return str(self.num)+':'+self.subject # 게시물번호, 제목