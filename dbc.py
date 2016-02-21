#!/usr/bin/env python

import pymysql
conn = pymysql.connect(host='192.168.214.12',
                       port=3306, user='test',
                       passwd='test23', db='testDB')
cur = conn.cursor()
cur.execute('SELECT * from jieINFO')


for i in cur.fetchall():
	print(i)

conn.close()

