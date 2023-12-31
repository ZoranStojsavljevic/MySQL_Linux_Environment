#!/usr/bin/python3

import mysql.connector

def create_server_connection(host_name, user_name, user_password):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password
		)
		print("MySQL Database connection successful")
	except Error as err:
		print(f"Error: '{err}'")

	return connection

connection = create_server_connection('127.0.0.1', 'root', 'Password_7')
