### MySQL Python Client Installation

This section shows installation and use of another MySQL client
based on Python's connector using pip (phyton installer program)
as an installer.

What is a pip? A package-management system written in Python and
it is used to install and manage software packages. The Python
Software Foundation recommends using pip for installing Python
applications and its dependencies during deployment.

#### [1] Install mysql connector python (Python as front-end/client for MySQL)

	[vuser@fedora39-ssd-2TB ~]$ pip install mysql-connector-python
	Defaulting to user installation because normal site-packages is not writeable
	Collecting mysql-connector-python
	  Obtaining dependency information for mysql-connector-python from https://files.pythonhosted.org/packages/21/2c/5235acb1b7ac496bfb81d377f65defa51b31ac5b2deb2478b0ef44aa98aa/mysql_connector_python-8.2.0-cp312-cp312-manylinux_2_17_x86_64.whl.metadata
	  Downloading mysql_connector_python-8.2.0-cp312-cp312-manylinux_2_17_x86_64.whl.metadata (2.1 kB)
	Collecting protobuf<=4.21.12,>=4.21.1 (from mysql-connector-python)
	  Using cached protobuf-4.21.12-cp37-abi3-manylinux2014_x86_64.whl (409 kB)
	Downloading mysql_connector_python-8.2.0-cp312-cp312-manylinux_2_17_x86_64.whl (31.6 MB)
	   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 31.6/31.6 MB 16.7 MB/s eta 0:00:00
	Installing collected packages: protobuf, mysql-connector-python
	Successfully installed mysql-connector-python-8.2.0 protobuf-4.21.12
	[vuser@fedora39-ssd-2TB ~]$

#### [2] Install connect (pip install connect)

	[vuser@fedora39-ssd-2TB ~]$ pip install connect
	Defaulting to user installation because normal site-packages is not writeable
	Collecting connect
	  Using cached connect-0.2.tar.gz (2.0 kB)
	  Preparing metadata (setup.py) ... done
	Building wheels for collected packages: connect
	  Building wheel for connect (setup.py) ... done
	  Created wheel for connect: filename=connect-0.2-py3-none-any.whl size=2219 sha256=5179ab73ad907e3cb2441795f066245ddbe0aa87b26add9fbef555248391c938
	  Stored in directory: /home/vuser/.cache/pip/wheels/67/6b/7e/c29e41445a70ca2450d61b6854a781612cfa0d413951c6fb6d
	Successfully built connect
	Installing collected packages: connect
	Successfully installed connect-0.2
	[vuser@fedora39-ssd-2TB ~]$

#### Using normal Python shell

Please, do note that I did NOT use any MySQL Python Client IDE,
rather using normal Python shell. As for now prefering a Python
Client minimal environment.

I potentially might introduce Python Client IDE for Fedora
(later). Maybe/if?

### MySQL Python Client Verification

#### The initial test program for MySQL python client verification

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

#### The test program results

	[vuser@fedora39-ssd-2TB ~]$ nano connect.py
	[vuser@fedora39-ssd-2TB ~]$ python
	Python 3.12.0 (main, Oct  2 2023, 00:00:00) [GCC 13.2.1 20230918 (Red Hat 13.2.1-3)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import connect
	MySQL Database connection successful
	>>>
