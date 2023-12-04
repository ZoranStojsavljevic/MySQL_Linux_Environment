#!/usr/bin/python3

import mysql.connector

config = {
	'user': 'root',
	'password': 'Password_7',
	'host': '127.0.0.1',
	'port': '3306',
}

db = mysql.connector.connect(**config)
cursor=db.cursor()
