#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode

config = {
	'user': 'root',
	'password': 'Password_7',
	'host': 'localhost',
	'port': '3306',
	'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor=db.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
	print(x)

DB_NAME = 'acme'

TABLES = {}

TABLES['logs'] = (
	"CREATE TABLE `logs` ("
	" `id` int(11) NOT NULL AUTO_INCREMENT,"
	" `text` varchar(250) NOT NULL,"
	" `user` varchar(250) NOT NULL,"
	" `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
	" PRIMARY KEY (`id`)"
	") ENGINE=InnoDB"
)

def create_database():
	cursor.execute(
		"CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	print("Database {} created!".format(DB_NAME))

def create_tables():
	cursor.execute("USE {}".format(DB_NAME))

	for table_name in TABLES:
		table_description = TABLES[table_name]
		try:
			print("Creating table ({}) ".format(table_name), end="")
			cursor.execute(table_description)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
				print("Already Exists")
			else:
				print(err.msg)

def delete_table(mydb, delete_flag):
	mycursor = mydb.cursor()
	if True == delete_flag:
		sql = "DROP TABLE logs"
		mycursor.execute(sql)
		print("DROP TABLE logs")
	else:
		print("TABLE logs not deleted")

create_database()
delete_table(db, False)
create_tables()

def add_record(text, user):
	sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
	cursor.execute(sql, (text, user,))
	db.commit()
	record_id = cursor.lastrowid
	print("Added record {}".format(record_id))
	return str(cursor.lastrowid)

def get_record(id):
	sql = ("SELECT * FROM logs WHERE id = %s")
	cursor.execute(sql, (id,))
	result = cursor.fetchone()

	for row in result:
		print(row, " ", end="")
	print("\n")

def get_records():
	sql = ("SELECT * FROM logs ORDER BY created DESC")
	cursor.execute(sql)
	result = cursor.fetchall()

	for row in result:
		print(row)

def update_record(id, text):
	sql = ("UPDATE logs SET text = %s WHERE id = %s")
	cursor.execute(sql, (text, id))
	db.commit()
	print("Record updated")

def delete_record(id):
	sql = ("DELETE FROM logs WHERE id = %s")
	cursor.execute(sql, (id,))
	db.commit()
	print("Single record removed", id)

def delete_records(id, max_id):
	print('DELETE FROM logs WHERE id BETWEEN', id, 'AND', last_id)
	sql = ('DELETE FROM logs WHERE id >= %s')
	cursor.execute(sql, (id,))
	db.commit()
	print("Deleted records FROM", id, "TO", max_id)

last_id = add_record('Adding record to the table_name', 'Brad')
print('last id added', last_id)
last_id = add_record('Adding record to the table_name', 'Jeff')
print('last id added', last_id)
last_id = add_record('Adding record to the table_name', 'Jane')
print('last id added', last_id)

get_records()

get_record(2)

### This function should NOT be used (commented out)
delete_records(5, last_id)

get_records()

delete_table(db, False)

update_record(2, 'Updated log')

### delete_record(1)
### delete_record(2)

get_record(2)
