from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):

    title = models.CharField(max_length=300,verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',verbose_name='作者')
    body = models.TextField(verbose_name='内容')
    publish = models.DateTimeField(default=timezone.now,verbose_name='出版日期')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title