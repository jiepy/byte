import smtplib
from email.mime.text import MIMEText
import socket


class EasySendmail:
	''' e = ClassMail.EasySendmail(Port=25, auth=True)
	default smtp port : 25
	# 默认smtp的端口是25,若需要更改则设置port=xxx
	# 默认是认证发信，若要匿名发信则需设置auth=False
	'''
	def __init__(self, port=25, auth=True):
		self.port = port
		self.auth = auth

	@classmethod
	def setmail(cls, host, sender, passwd, mail_to, mail_sub, content):
		'''You must set attr:
		Host : mailServer exp: smtp.163.com
		Sender: mail from user
		Passwd: user passwd
		Mail_to: To user
		Mail_sub: mail subject
		content: message '''

		cls.host = host
		cls.sender = sender
		cls.passwd = passwd
		cls.mail_to = ';'.join(mail_to)
		cls.mail_sub = mail_sub
		cls.content = content

	@property
	def sendmail(self):
		'''sendmail: Start Connect server to send mail .'''
		self.message = """From: {0}
To: {1}
MIME-Version: 1.0
Content-type: text/plain
Subject: {2}

{3}
""".format(self.sender, self.mail_to, self.mail_sub, self.content)

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(10)
		try:
			s.connect((self.host, self.port))
			# print('Connect {0}:{1} successfuly !'.format(self.host, self.port))
		except Exception:
			print('Error: Can connect {0}:{1} !'.format(self.host, self.port))
		s.close()

		try:
			print(self.auth)
			smtpobj = smtplib.SMTP(self.host, self.port)
			if self.auth is True:
				smtpobj.login(self.sender, self.passwd)
			smtpobj.sendmail(self.sender, self.mail_to, self.message.encode('GBK'))
			print('Successfully send email !')
			smtpobj.quit()
		except smtplib.SMTPAuthenticationError as error:
			print(error)
			print('认证失败,请核对用户名和密码.')
		except smtplib.SMTPException as error:
			print(error)
			print('Error: unable to send mail !')
		except Exception as e:
			print(e)
