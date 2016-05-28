# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPN',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=20, verbose_name='密码')),
                ('real_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('department', models.CharField(max_length=20, verbose_name='部门')),
                ('email', models.EmailField(max_length=254, verbose_name='邮件地址')),
                ('u_time', models.DateTimeField(verbose_name='密码更新时间')),
                ('lock_status', models.BooleanField(verbose_name='锁定')),
            ],
        ),
    ]