#!/usr/bin/python3

### import mysql.connector
import db_setup
from db_setup import cursor

DB_NAME = 'test_MySQL_database'

def create_database():
	cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	print("Database {} created!".format(DB_NAME))

create_database()
