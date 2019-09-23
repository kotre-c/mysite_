from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    SEX_CHOICES = (
        ('M', '男'),
        ('W', '女')
    )
    DEGREE_CHOICES = (
        ('0', '小学'),
        ('1', '初中'),
        ('2', '高中'),
        ('3', '专科'),
        ('4', '本科'),
        ('5', '硕士'),
        ('6', '博士'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', choices=SEX_CHOICES, max_length=4, default='男')
    birthday = models.DateField('生日')
    phone = models.CharField('电话', max_length=20)
    school = models.CharField('毕业学校', max_length=50)
    degree = models.CharField('学历', choices=DEGREE_CHOICES, max_length=4, default='小学')
    website = models.CharField('网站', null=True, blank=True, max_length=40)
    mail = models.EmailField('邮箱')
    remark = models.TextField('自我介绍', max_length=2000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '个人信息'
        verbose_name_plural = verbose_name


class Program(models.Model):
    name = models.CharField('技能', max_length=50)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='技能')
    level = models.CharField('掌握程度', max_length=20)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.program.name

    class Meta:
        verbose_name = '技能表'
        verbose_name_plural = verbose_name


class Experience(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    company = models.CharField('公司', max_length=50)
    started = models.DateField('入职时间', null=False)
    ended = models.DateField('离职时间', null=True, blank=True)
    position = models.CharField('职位', default='总经理', max_length=20)
    description = models.TextField('职位介绍', max_length=2000)
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.started)+"入职"+self.company+"担任"+self.position

    class Meta:
        verbose_name = '履历'
        verbose_name_plural = verbose_name


class Education(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    college = models.CharField('学校名称', max_length=50)
    started = models.DateField('入学时间', null=False)
    ended = models.DateField('毕业时间', null=True, blank=True)
    major = models.CharField('专业', max_length=50)
    description = models.TextField('专业描述', max_length=2000)
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.started)+"入学于"+self.college

    class Meta:
        verbose_name = '教育经历'
        verbose_name_plural = verbose_name


class Project(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField('项目名', max_length=100)
    img = models.ImageField('图片', upload_to='img/')
    tags = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
