from django.db import models

# Create your models here.
class Board(models.Model) :
    ACTIVITY_CHOICES = {
        ('1', '대변'),
        ('2', '소변'),
        ('3', '방귀')
    }

    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    choice = models.CharField(max_length=80, choices=ACTIVITY_CHOICES, null=True)
    image = models.ImageField(upload_to='board/', blank=True, null=True)

    def __str__(self) :
        return self.author.username