### MySQL Python Client Examples

Shows some excerpts from Brad's MySQL Python Client course:

https://www.youtube.com/watch?v=BHwgnGEhYG8&t

The full examples presented/shown by Brad are here (I do my
own formats/interpretations to better understand the code):

https://gist.github.com/bradtraversy/5ea2fa59776ddc8cf45c536be65d4f86

I did modify this code to intro a bit more compexity, just to
get an idea what I am facing. The code needs to be polished,
so this is NOT a final version of the code in: python_mysql.py
example. Also, I might add other examples.

Please, do note that I did NOT use any MySQL Python Client IDE,
rather using normal Python shell. As for now prefering a Python
Client minimal environment.

I potentially might introduce Python Client IDE for Fedora
(later). Maybe/if?

#### Example execution of db_create (simplistic example)

	.../MySQL_Linux_Environment/MySQL_Clients/MySQL_Python_Client_Examples$ uname -a
	Linux fedora39-ssd-2TB 6.6.2-201.fc39.x86_64 [_snap_]

	.../MySQL_Linux_Environment/MySQL_Clients/MySQL_Python_Client_Examples$ python
	Python 3.12.0 (main, Oct  2 2023, 00:00:00) [GCC 13.2.1 20230918 (Red Hat 13.2.1-3)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import db_create
	Database test_MySQL_database created!
	>>>

#### Example execution of python_mysql (more complex example)

	.../MySQL_Linux_Environment/MySQL_Clients/MySQL_Python_Client_Examples$ python
	Python 3.12.0 (main, Oct  2 2023, 00:00:00) [GCC 13.2.1 20230918 (Red Hat 13.2.1-3)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import python_mysql
	Database acme created!
	TABLE logs not deleted
	Creating table (logs) Added record 1
	last id added 1
	Added record 2
	last id added 2
	Added record 3
	last id added 3
	(1, 'Adding record to the table_name', 'Brad', datetime.datetime(2023, 12, 7, 20, 7, 31))
	(2, 'Adding record to the table_name', 'Jeff', datetime.datetime(2023, 12, 7, 20, 7, 31))
	(3, 'Adding record to the table_name', 'Jane', datetime.datetime(2023, 12, 7, 20, 7, 31))
	2  Adding record to the table_name  Jeff  2023-12-07 20:07:31

	TABLE logs not deleted
	Record updated
	2  Updated log  Jeff  2023-12-07 20:07:31

	>>>
