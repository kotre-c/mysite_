from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField('标题', max_length=100)
    text = models.TextField('正文', max_length=2000)
    tags = models.CharField('标签', max_length=50)
    img = models.ImageField('图片', upload_to='blog/img/Y/m/d/', null=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    is_pub = models.BooleanField('是否发布', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    text = models.CharField('评论', max_length=200)
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('修改时间', auto_now=True)
    is_pub = models.BooleanField('是否公开', default=False)

    def __str__(self):
        return self.name + "评论了：" + self.text

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
