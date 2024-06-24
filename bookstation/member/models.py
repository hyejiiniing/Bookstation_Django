from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=30, primary_key=True)
    member_password = models.CharField(max_length=30)
    member_name = models.CharField(max_length=20)
    member_gender = models.CharField(max_length=5)
    member_email = models.CharField(max_length=40)
    member_phone = models.CharField(max_length=25)
    member_zipcode = models.CharField(max_length=15)
    member_address1 = models.CharField(max_length=100)
    member_address2 = models.CharField(max_length=100, default='')  # 기본값 설정
    member_birthday = models.CharField(max_length=15)
    member_point = models.IntegerField(default=1000)
    member_totalPrice = models.IntegerField(default=0)
    reg_date = models.DateTimeField(default=timezone.now)
    grade_name = models.CharField(max_length=10, default='Bronze')

    def __str__(self):
        return self.member_id

