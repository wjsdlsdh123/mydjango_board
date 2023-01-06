from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True) # integer(auto-increment)
    title = models.CharField(max_length=255) # varchar(255)
    content = models.TextField() # Text
    create_at = models.DateTimeField(auto_now_add=True) # 추가될 떄 defult로 현재시간
    # auto_now_add = True - save 될때마다 최초저장(insert)시에만 현재날짜(date.today())를 적용합니다.
    updated_at = models.DateTimeField(auto_now=True) # 추가 or 업데이트 될 때 defult로 현재시간
    # auto_now =True - save 될때마다 현재 날짜가(date.today())로 갱신됨.

class Comment(models.Model):
    board = models.ForeignKey("Board",on_delete=models.SET_NULL, null= True)
    content = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)