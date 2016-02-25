#!/usr/bin/env python

import pymysql

#设置数据库地址
DB_host = '192.168.214.88'

#设置数据库名称
DB_name = 'testDB'
#必须不加引号
DB_port = 3306
#设置数据库用户
DB_user = 'test'
#设置密码
DB_pass = 'test123'

#定义数据库信息
conn = pymysql.connect(host=DB_host,
                       port=DB_port, user=DB_user,
                       passwd=DB_pass, db=DB_name)
#打开游标
cur = conn.cursor()
#执行sql语句
cur.execute('SELECT * from students')


for i in cur.fetchall():
	print(i)

#关闭游标
conn.close()


