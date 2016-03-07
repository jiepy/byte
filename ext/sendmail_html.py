#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/13 17:44
# ----------------------------------------

import smtplib
from email.mime.text import MIMEText

mailto_list = ["xxx@xxx.com"]
mail_host = "smtp.xxx.com"  # 设置服务器
mail_user = "xxxx@163.com"  # 用户名
mail_pass = "xxxxxxx"  # 口令


def send_mail(Mail_user, to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容

	msg = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
	msg['Subject'] = sub  # 设置主题
	msg['From'] = Mail_user
	msg['To'] = ";".join(to_list)

	try:
		s = smtplib.SMTP()
		s.connect(mail_host)  # 连接smtp服务器
		print('Connect mail server {0} OK ...'.format(mail_host))
		s.login(mail_user, mail_pass)  # 登陆服务器
		print('User {0} login successfuly ...'.format(mail_user))
		s.sendmail(Mail_user, to_list, msg.as_string())  # 发送邮件
		s.close()
		return True
	except Exception as e:
		print(e)
		return False


if __name__ == '__main__':
	if send_mail(mail_user, mailto_list, "Html Mail Test", "<a href='http://www.cnblogs.com/topicjie'>Geng Jie</a>"):
		print("Send Mail Successfuly !")
	else:
		print("Error: SendMail Fail !")
