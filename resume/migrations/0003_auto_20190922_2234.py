# Generated by Django 2.1.10 on 2019-09-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20190922_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('M', '男'), ('W', '女')], default='男', max_length=4, verbose_name='性别'),
        ),
    ]
