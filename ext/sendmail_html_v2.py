#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/13 21:41

# ----------------------------------------
# 本程序只是实现了简单的认证发信
# 基本思路是连接服务器，认证，发信
# 需要定义邮件相关信息
# ########################################
import smtplib

# 定义邮件服务器地址以及端口
SMTP_HOST = 'smtp.163.com'
SMTP_PORT = '25'
# 定义发件人，密码，收件人
MAIL_USER = 'xxxxxx@163.com'
PASSWD = 'xxxxxx'
MAIL_TO = 'xxxxxx@xxx.com'
# 定义邮件主题，内容
MAIL_SUB = '测试邮件'
MAIL_CON = '''
Hi, python:

	最近好吗？好久不见.
	<br><br>
	This is an e-mail message to be sent in HTML format

	<b>This is HTML message.</b>
	<h1>This is headline.</h1>

'''

message = """From: {0}
To: {1}
MIME-Version: 1.0
Content-type: text/html
Subject: {2}
{3}
""".format(MAIL_USER, MAIL_TO, MAIL_SUB, MAIL_CON)

try:
	smtpObj = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
	smtpObj.login(MAIL_USER, PASSWD)
	smtpObj.sendmail(MAIL_USER, MAIL_TO, message.encode('GBK'))
	print('Successfully send email !')
	smtpObj.quit()

except smtplib.SMTPException as e:
	print(e)
	print('Error: unable to send mail !')
