# Generated by Django 2.1.10 on 2019-09-21 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=50, verbose_name='学校名称')),
                ('started', models.DateField(verbose_name='入学时间')),
                ('ended', models.DateField(blank=True, null=True, verbose_name='毕业时间')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('description', models.TextField(max_length=2000, verbose_name='专业描述')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('is_delete', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '教育经历',
                'verbose_name_plural': '教育经历',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='公司')),
                ('started', models.DateField(verbose_name='入职时间')),
                ('ended', models.DateField(blank=True, null=True, verbose_name='离职时间')),
                ('position', models.CharField(default='总经理', max_length=20, verbose_name='职位')),
                ('description', models.TextField(max_length=2000, verbose_name='职位介绍')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('is_delete', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '履历',
                'verbose_name_plural': '履历',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='技能')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='项目名')),
                ('img', models.ImageField(upload_to='img/', verbose_name='图片')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Program', verbose_name='标签')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, verbose_name='掌握程度')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Program', verbose_name='技能')),
            ],
            options={
                'verbose_name': '技能表',
                'verbose_name_plural': '技能表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('M', '男'), ('W', '女')], default='男', max_length=4, verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('school', models.CharField(max_length=50, verbose_name='毕业学校')),
                ('degree', models.CharField(choices=[('0', '小学'), ('1', '初中'), ('2', '高中'), ('3', '专科'), ('4', '本科'), ('5', '硕士'), ('6', '博士')], default='小学', max_length=4, verbose_name='学历')),
                ('website', models.CharField(blank=True, max_length=40, null=True, verbose_name='网站')),
                ('mail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('remark', models.TextField(max_length=2000, null=True, verbose_name='自我介绍')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '个人信息',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.UserInfo', verbose_name='用户'),
        ),
    ]
