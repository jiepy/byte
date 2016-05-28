from django.db import models

# Create your models here.

class VPN(models.Model):
    username = models.CharField(max_length=30, primary_key=True, verbose_name='用户名')
    passwd = models.CharField(max_length=20, verbose_name='密码')
    real_name = models.CharField(max_length=30, verbose_name='姓名')
    department = models.CharField(max_length=20, verbose_name='部门')
    email = models.EmailField(verbose_name='邮件地址')
    u_time = models.DateTimeField(verbose_name='密码更新时间')
    lock_status = models.BooleanField(verbose_name='锁定')

    def __str__(self):
        return self.username

class Check():

    def __init__(self, username, passwd):
        self.code = None
        self.username = username
        self.passwd = passwd

    @property
    def has_user(self):
        ''' 0 --  no_user
            1 --  has_user'''
        try:
            self.code = len(VPN.objects.filter(username=self.username))
            return self.code
        except Exception as e:
            return e

    @property
    def check_pass(self):
        '''3  -- auth pass
           4  -- auth error '''
        self.P = VPN.objects.filter(username=self.username)

        if self.P.values()[0]['passwd'] == self.passwd:
            return 3
        else:
            return 4
