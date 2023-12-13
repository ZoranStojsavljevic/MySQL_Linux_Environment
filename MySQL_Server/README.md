## Fedora 39 MySQL server installation
* [installing-mysql](https://docs.fedoraproject.org/en-US/quick-docs/installing-mysql-mariadb)
* [yum-repo-installing-mysq](https://dev.mysql.com/doc/refman/8.0/en/linux-installation-yum-repo.html#yum-repo-installing-mysq)

### [1] Remove mariadb server and mariadb server utils

	[vuser@fedora39-ssd-2TB ~]$ sudo dnf rm mariadb-server-utils

	[vuser@fedora39-ssd-2TB ~]$ sudo dnf rm mariadb-server

### [2] Installing MySQL server version 8.0.35-1.fc39

	### (obsolete) [vuser@fedora39-ssd-2TB ~]$ sudo dnf install mysql-community-server
	[vuser@fedora39-ssd-2TB ~]$ sudo dnf install community-mysql-server.x86_64

	==========================================================================================
	Package				Architecture	Version		Repository	Size
	==========================================================================================
	Installing:
	 community-mysql-server		x86_64		8.0.35-1.fc39	updates		 17M
	Installing dependencies:
	 community-mysql		x86_64		8.0.35-1.fc39	updates		3.1M
	 community-mysql-common		x86_64		8.0.35-1.fc39	updates		 76k
	 community-mysql-errmsg		x86_64		8.0.35-1.fc39	updates		504k
	 mariadb-connector-c-config	noarch		3.3.5-2.fc39	fedora		8.8k
	 mecab				x86_64		0.996-5.fc39	fedora		356k
	 mysql-selinux			noarch		1.0.10-1.fc39	updates		 35k
	 protobuf-lite			x86_64		3.19.6-6.fc39	fedora		258k

	Transaction Summary
	==========================================================================================
	Install  8 Packages

	Total download size: 21 M
	Installed size: 179 M
	Is this ok [y/N]: y
	Downloading Packages:
	(1/8): mariadb-connector-c-config-3.3.5-2.fc39.noarch.rpm	117 kB/s | 8.8 kB  00:00
	(2/8): mecab-0.996-5.fc39.x86_64.rpm				2.0 MB/s | 356 kB  00:00
	(3/8): protobuf-lite-3.19.6-6.fc39.x86_64.rpm			1.4 MB/s | 258 kB  00:00
	(4/8): community-mysql-common-8.0.35-1.fc39.x86_64.rpm		209 kB/s |  76 kB  00:00
	(5/8): community-mysql-8.0.35-1.fc39.x86_64.rpm			2.6 MB/s | 3.1 MB  00:01
	(6/8): mysql-selinux-1.0.10-1.fc39.noarch.rpm			777 kB/s |  35 kB  00:00
	(7/8): community-mysql-errmsg-8.0.35-1.fc39.x86_64.rpm		436 kB/s | 504 kB  00:01
	(8/8): community-mysql-server-8.0.35-1.fc39.x86_64.rpm		4.7 MB/s |  17 MB  00:03
	------------------------------------------------------------------------------------------
	Total								5.0 MB/s |  21 MB  00:04

### [3] IMPORTANT pitfall solution! Can't start mysql after upgrade

	[vuser@fedora39-ssd-2TB ~]$ sudo service mysqld restart
	Redirecting to /bin/systemctl restart mysqld.service
	Job for mysqld.service failed because the control process exited with error code.
	See "systemctl status mysqld.service" and "journalctl -xeu mysqld.service" for details.
	[vuser@fedora39-ssd-2TB ~]$

Since the MySQL server's /etc and /var config files changed over
the Time, please, check the following net page for possible solutions!
* [job for mysqld service failed](https://stackoverflow.com/questions/42317139/job-for-mysqld-service-failed-see-systemctl-status-mysqld-service/77589044#77589044)

#### Solution which worked for me

	[vuser@fedora39-ssd-2TB ~]$ cd /var/lib/mysql
	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ sudo mkdir '#innodb_redo'
	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ sudo chown mysql:mysql' #innodb_redo'
	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ sudo service mysqld restart
	Redirecting to /bin/systemctl restart mysqld.service

This solution worked!

### [4] [Still OPTIONAL] Installing a community-mysql-libs package

NOt installed  yet. Still exploring the minimal environment for
the MySQL server environment (ONLY bare minimum for now):

	[vuser@fedora39-ssd-2TB ~]$ sudo dnf install community-mysql-libs
	==========================================================================================
	Package				Architecture	Version		Repository	Size
	==========================================================================================
	Installing:
	 community-mysql-libs		x86_64		8.0.35-1.fc39	updates		1.2M

	Transaction Summary
	==========================================================================================
	Install  1 Packages

	Total download size: 1.2 M
	Installed size: 6.5 M
	Is this ok [y/N]: n
	Operation aborted.

	[vuser@fedora39-ssd-2TB ~]$

### [5] Enabling the Default flag for MySQL Server to start upon boot

	[vuser@fedora39-ssd-2TB ~]$ sudo systemctl enable mysqld

	[vuser@fedora39-ssd-2TB ~]$ dnf repolist enabled | grep mysql

### [6] Starting MySQL Server

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

### [7] Configuring MySQL before the first use

	[vuser@fedora39-ssd-2TB ~]$ sudo mysql_secure_installation
	Securing the MySQL server deployment.

	Connecting to MySQL using a blank password.

	VALIDATE PASSWORD COMPONENT can be used to test passwords
	and improve security. It checks the strength of password
	and allows the users to set only those passwords which are
	secure enough. Would you like to setup VALIDATE PASSWORD component?

	Press y|Y for Yes, any other key for No: y

	There are three levels of password validation policy:

	LOW    Length >= 8
	MEDIUM Length >= 8, numeric, mixed case, and special characters
	STRONG Length >= 8, numeric, mixed case, special characters and dictionary file

	Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
	Please set the password for root here.

	=====>> Please, do note that the default passwd is: 'password' <<=====

	New password: '***********'

	Re-enter new password: '***********'

	Estimated strength of the password: 50 
	Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
	By default, a MySQL installation has an anonymous user,
	allowing anyone to log into MySQL without having to have
	a user account created for them. This is intended only for
	testing, and to make the installation go a bit smoother.
	You should remove them before moving into a production
	environment.

	Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
	Success.

	Normally, root should only be allowed to connect from
	'localhost'. This ensures that someone cannot guess at
	the root password from the network.

	Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
	Success.

	By default, MySQL comes with a database named 'test' that
	anyone can access. This is also intended only for testing,
	and should be removed before moving into a production
	environment.

	Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
	 - Dropping test database...
	Success.

	 - Removing privileges on test database...
	Success.

	Reloading the privilege tables will ensure that all changes
	made so far will take effect immediately.

	Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
	Success.

	All done!

### [8] Grep for the initial MySQL server password

	[vuser@fedora39-ssd-2TB ~]$ sudo cat /var/log/mysql/mysqld.log | grep password
	2023-11-24T17:36:57.899774Z 6 [Warning] [MY-010453] [Server] root@localhost is created
	with an empty password ! Please consider switching off the --initialize-insecure option.
	2023-11-26T16:57:53.208612Z 11 [Warning] [MY-013360] [Server] Plugin sha256_password
	reported: ''sha256_password' is deprecated and will be removed in a future release.
	Please use caching_sha2_password instead'

### [9] Entering MySQL server

	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ mysql -uroot -p

	Enter password:
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

### [10] Changing password

	### Enter MySQL server via CLI:
	[vuser@fedora39-ssd-2TB:/var/lib/mysql]$ mysql -uroot -p

	### For mysql database server version 5.7.6 or newer use the following syntax:
	ALTER USER 'user'@'hostname' IDENTIFIED BY 'newPass';
	UPDATE mysql.user SET Password=PASSWORD('new-password-here') WHERE USER='user-name-here

	### Practical implementation
	mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Password_7';

### [11] Removing MySQL server

	Suggestion to remove MySQL server with te following:

	[vuser@fedora39-ssd-2TB ~]$ sudo dnf remove {community-mysql-server|mariadb-server}

