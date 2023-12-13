### Connecting MySQL Python Client to MySQL server

#### [1] MySQL Python server MUST be active (running)

	[vuser@fedora39-ssd-2TB ~]$ systemctl status mysqld
	● mysqld.service - MySQL 8.0 database server
	     Loaded: loaded (/usr/lib/systemd/system/mysqld.service; disabled; preset: disabled)
	    Drop-In: /usr/lib/systemd/system/service.d
	             └─10-timeout-abort.conf
	     Active: active (running) since Mon 2023-12-11 14:54:37 CET; 1h 50min ago
	    Process: 13226 ExecStartPre=/usr/libexec/mysql-check-socket (code=exited, status=0/SUCCESS)
	    Process: 13248 ExecStartPre=/usr/libexec/mysql-prepare-db-dir mysqld.service (code=exited, status=0/SUCCESS)
	   Main PID: 13284 (mysqld)
	     Status: "Server is operational"
	      Tasks: 40 (limit: 14144)
	     Memory: 428.2M
	        CPU: 46.936s
	     CGroup: /system.slice/mysqld.service
	             └─13284 /usr/libexec/mysqld --basedir=/usr
	[vuser@fedora39-ssd-2TB ~]$

If not, the following Linux command must be executed:

	[vuser@fedora39-ssd-2TB ~]$ sudo systemctl restart mysqld	

#### [2] A function to connect to MySQL Server (connect.py)

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

#### Connect results (MySQL Python Client to MySQL server)

	[vuser@fedora39-ssd-2TB ~]$ nano connect.py
	[vuser@fedora39-ssd-2TB ~]$ python
	Python 3.12.0 (main, Oct  2 2023, 00:00:00) [GCC 13.2.1 20230918 (Red Hat 13.2.1-3)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import connect
	MySQL Database connection successful
	>>>
