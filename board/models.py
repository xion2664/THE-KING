from django.db import models

# Create your models here.
class Board(models.Model) :
    
    # account앱의 User모델 ForeignKey
    author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    # 글 생성 날짜, 시간
    created_at = models.DateTimeField()
    # 생리활동 3가지 선택
    choice = models.CharField(max_length=10)
    # 생리활동 이미지
    image = models.ImageField(upload_to='board/', blank=True, null=True)
    # 생리활동 내용
    body = models.TextField(null=True)
 
    def __str__(self) :
        return self.author.username

