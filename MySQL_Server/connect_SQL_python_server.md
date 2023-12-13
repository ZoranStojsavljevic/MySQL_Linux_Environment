## Connect MySQL server installation

This procedure for restarting a service mysqld (MySQL server)
after an initial installation is done every time after rebooting
and bringing up Fedora from scratch.

### [1] [OPTIONAL] Enabling the Default flag for MySQL Server to start upon boot

	[vuser@fedora39-ssd-2TB ~]$ sudo systemctl enable mysqld

	[vuser@fedora39-ssd-2TB ~]$ dnf repolist enabled | grep mysql

### [2] Starting MySQL Server

	[vuser@fedora39-ssd-2TB ~]$ sudo systemctl restart mysqld

	[vuser@fedora39-ssd-2TB ~]$ systemctl status mysqld
	● mysqld.service - MySQL 8.0 database server
	     Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; preset: disabled)
	    Drop-In: /usr/lib/systemd/system/service.d
	             └─10-timeout-abort.conf
	     Active: active (running) since Sat 2023-12-02 20:45:32 CET; 56min ago
	    Process: 283459 ExecStartPre=/usr/libexec/mysql-check-socket (code=exited, status=0/SUCCESS)
	    Process: 283482 ExecStartPre=/usr/libexec/mysql-prepare-db-dir mysqld.service (code=exited, status=0/S>
	   Main PID: 283517 (mysqld)
	     Status: "Server is operational"
	      Tasks: 38 (limit: 14130)
	     Memory: 363.5M
	        CPU: 969ms
	     CGroup: /system.slice/mysqld.service
	             └─283517 /usr/libexec/mysqld --basedir=/usr

	[vuser@fedora39-ssd-2TB ~]$

### [3] Entering MySQL server

	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ mysql -uroot -p

	Enter password: Password_7
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 8
	Server version: 8.0.35 Source distribution

	Copyright (c) 2000, 2023, Oracle and/or its affiliates.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql> system pwd
	/var/lib/mysql
	mysql>

### [4] [OPTIONAL] Changing password

	### Enter MySQL server via CLI:
	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ mysql -uroot -p

	### For mysql database server version 5.7.6 or newer use the following syntax:
	ALTER USER 'user'@'hostname' IDENTIFIED BY 'newPass';
	UPDATE mysql.user SET Password=PASSWORD('new-password-here') WHERE USER='user-name-here

	### Practical implementation
	mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Password_7';
