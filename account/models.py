from django.db import models
from board.models import Board
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    nickname = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='account/', blank=True, null=True)
    big_score = models.IntegerField(default=0, verbose_name = "대변점수")
    small_score = models.IntegerField(default=0, verbose_name = "소변점수")
    gas_score = models.IntegerField(default=0, verbose_name = "방귀점수")
    total_score = models.IntegerField(default=0, verbose_name = "총합")

class history(models.Model) :
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self) :
        return self.board.body