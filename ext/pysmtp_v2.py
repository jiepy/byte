#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/13 19:26
# ----------------------------------------
# 本程序只是实现了简单的认证发信
# 基本思路是连接服务器，认证，发信
# 需要定义邮件相关信息
# 此版本是在v1的基础上增加了附件功能
# ########################################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# 定义邮件服务器地址以及端口
SMTP_HOST = 'smtp.163.com'
SMTP_PORT = '25'
# 定义发件人，密码，收件人
MAIL_USER = 'monitor_jie@163.com'
PASSWD = 'admin@123'
MAIL_TO = 'baiyaozi@7lk.com'
# 定义邮件主题，内容
MAIL_SUB = '附件测试邮件'
MAIL_CON = '''
Hi, python:

	最近好吗？好久不见.
'''

msgRoot = MIMEMultipart('related')

att = MIMEText(open("E:\Xiaomi\如何学习新技术.jpg", 'rb').read(), 'base64', 'GBK')
att['Content-type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename ="如何学习新技术.jpg"'
msgRoot.attach(att)

full_att = msgRoot.as_string()

# message = """From: {0}
# To: {1}
# Subject: {2}
# {3}
# {4}
# """.format(MAIL_USER, MAIL_TO, MAIL_SUB, MAIL_CON, full_att)

try:
	smtpObj = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
	smtpObj.login(MAIL_USER, PASSWD)
	smtpObj.sendmail(MAIL_USER, MAIL_TO, full_att)
	print('Successfully send email !')
	smtpObj.quit()

except smtplib.SMTPException as e:
	print(e)
	print('Error: unable to send mail !')
