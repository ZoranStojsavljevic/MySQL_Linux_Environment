## Native MySQL commands executed on the server (mysql> prompt)

### MySQL_Server mysql> login

[vuser@fedora39-ssd-2TB ~]$ projects/github/MySQL_Linux_Environment/MySQL_Server$ mysql -uroot -p
Enter password: Password_7

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.35 Source distribution

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

### SHOW DATABASES; command (show all databases on MySQL server)

mysql> SHOW DATABASES;

	+---------------------+
	| Database            |
	+---------------------+
	| acme                |
	| giraffe             |
	| information_schema  |
	| mysql               |
	| performance_schema  |
	| sys                 |
	| test_MySQL_database |
	| test_SQL_Database   |
	| test_database       |
	+---------------------+
	9 rows in set (0.04 sec)

Please, do note that acme and giraffe databases are custom created:

	+---------------------+
	| Database            |
	+---------------------+
	| acme                |
	| giraffe             |
	+---------------------+

All others belong to the default MySQL server:

	+---------------------+
	| Database            |
	+---------------------+
	| information_schema  |
	| mysql               |
	| performance_schema  |
	| sys                 |
	| test_MySQL_database |
	| test_SQL_Database   |
	| test_database       |
	+---------------------+

### Custom created <database_name> manipulation

	+---------------------+
	| Database            |
	+---------------------+
	| acme                |
	| giraffe             |
	+---------------------+

#### <database_name> acme

##### Select <database_name> acme

mysql> USE acme;

	Database changed

##### Show tables in <database_name> acme

mysql> SHOW TABLES in acme;

	+----------------+
	| Tables_in_acme |
	+----------------+
	| logs           |
	+----------------+
	1 row in set (0.00 sec)

##### Describe <database_name> acme <table_name> logs row formats

mysql> DESCRIBE logs;

	+---------+--------------+------+-----+-------------------+-------------------+
	| Field   | Type         | Null | Key | Default           | Extra             |
	+---------+--------------+------+-----+-------------------+-------------------+
	| id      | int          | NO   | PRI | NULL              | auto_increment    |
	| text    | varchar(250) | NO   |     | NULL              |                   |
	| user    | varchar(250) | NO   |     | NULL              |                   |
	| created | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
	+---------+--------------+------+-----+-------------------+-------------------+
	4 rows in set (0.01 sec)

##### Print all rows from the <table_name> logs

mysql> SELECT * FROM logs;

	+----+---------------------------------+------+---------------------+
	| id | text                            | user | created             |
	+----+---------------------------------+------+---------------------+
	|  1 | Adding record to the table_name | Brad | 2023-12-07 20:07:31 |
	|  2 | Updated log                     | Jeff | 2023-12-07 20:07:31 |
	|  3 | Adding record to the table_name | Jane | 2023-12-07 20:07:31 |
	|  4 | Adding record to the table_name | Brad | 2023-12-08 04:37:03 |
	+----+---------------------------------+------+---------------------+
	4 rows in set (0.01 sec)

#### <database_name> giraffe

##### Select <database_name> giraffe

mysql> USE giraffe;

	Database changed

##### Show tables in <database_name> giraffe

mysql> SHOW TABLES in giraffe;

	+-------------------+
	| Tables_in_giraffe |
	+-------------------+
	| student           |
	+-------------------+
	1 row in set (0.01 sec)

##### Describe <database_name> giraffe <table_name> student row formats

mysql> DESCRIBE student;

	+------------+-------------+------+-----+---------+----------------+
	| Field      | Type        | Null | Key | Default | Extra          |
	+------------+-------------+------+-----+---------+----------------+
	| student_id | int         | NO   | PRI | NULL    | auto_increment |
	| name       | varchar(20) | NO   |     | NULL    |                |
	| major      | varchar(20) | YES  | UNI | NULL    |                |
	+------------+-------------+------+-----+---------+----------------+
	3 rows in set (0.00 sec)

##### Print all rows from the <table_name> student

mysql> SELECT * FROM student;

	+------------+------+-----------+
	| student_id | name | major     |
	+------------+------+-----------+
	|          1 | Jack | Biology   |
	|          2 | Kate | Sociology |
	+------------+------+-----------+
	2 rows in set (0.00 sec)

### Native <database_name> manipulation

	+---------------------+
	| Database            |
	+---------------------+
	| information_schema  |
	| mysql               |
	| performance_schema  |
	| sys                 |
	| test_MySQL_database |
	| test_SQL_Database   |
	| test_database       |
	+---------------------+

#### <database_name> information_schema

##### Select <database_name> information_schema

mysql> USE information_schema;

	Database changed

##### Show tables in <database_name> information_schema

mysql> SHOW TABLES in information_schema;

	+---------------------------------------+
	| Tables_in_information_schema          |
	+---------------------------------------+
	| ADMINISTRABLE_ROLE_AUTHORIZATIONS     |
	| APPLICABLE_ROLES                      |
	| CHARACTER_SETS                        |
	| CHECK_CONSTRAINTS                     |
	| COLLATIONS                            |
	| COLLATION_CHARACTER_SET_APPLICABILITY |
	| COLUMNS                               |
	| COLUMNS_EXTENSIONS                    |
	| COLUMN_PRIVILEGES                     |
	| COLUMN_STATISTICS                     |
	| ENABLED_ROLES                         |
	| ENGINES                               |
	| EVENTS                                |
	| FILES                                 |
	| INNODB_BUFFER_PAGE                    |
	| INNODB_BUFFER_PAGE_LRU                |
	| INNODB_BUFFER_POOL_STATS              |
	| INNODB_CACHED_INDEXES                 |
	| INNODB_CMP                            |
	| INNODB_CMPMEM                         |
	| INNODB_CMPMEM_RESET                   |
	| INNODB_CMP_PER_INDEX                  |
	| INNODB_CMP_PER_INDEX_RESET            |
	| INNODB_CMP_RESET                      |
	| INNODB_COLUMNS                        |
	| INNODB_DATAFILES                      |
	| INNODB_FIELDS                         |
	| INNODB_FOREIGN                        |
	| INNODB_FOREIGN_COLS                   |
	| INNODB_FT_BEING_DELETED               |
	| INNODB_FT_CONFIG                      |
	| INNODB_FT_DEFAULT_STOPWORD            |
	| INNODB_FT_DELETED                     |
	| INNODB_FT_INDEX_CACHE                 |
	| INNODB_FT_INDEX_TABLE                 |
	| INNODB_INDEXES                        |
	| INNODB_METRICS                        |
	| INNODB_SESSION_TEMP_TABLESPACES       |
	| INNODB_TABLES                         |
	| INNODB_TABLESPACES                    |
	| INNODB_TABLESPACES_BRIEF              |
	| INNODB_TABLESTATS                     |
	| INNODB_TEMP_TABLE_INFO                |
	| INNODB_TRX                            |
	| INNODB_VIRTUAL                        |
	| KEYWORDS                              |
	| KEY_COLUMN_USAGE                      |
	| OPTIMIZER_TRACE                       |
	| PARAMETERS                            |
	| PARTITIONS                            |
	| PLUGINS                               |
	| PROCESSLIST                           |
	| PROFILING                             |
	| REFERENTIAL_CONSTRAINTS               |
	| RESOURCE_GROUPS                       |
	| ROLE_COLUMN_GRANTS                    |
	| ROLE_ROUTINE_GRANTS                   |
	| ROLE_TABLE_GRANTS                     |
	| ROUTINES                              |
	| SCHEMATA                              |
	| SCHEMATA_EXTENSIONS                   |
	| SCHEMA_PRIVILEGES                     |
	| STATISTICS                            |
	| ST_GEOMETRY_COLUMNS                   |
	| ST_SPATIAL_REFERENCE_SYSTEMS          |
	| ST_UNITS_OF_MEASURE                   |
	| TABLES                                |
	| TABLESPACES                           |
	| TABLESPACES_EXTENSIONS                |
	| TABLES_EXTENSIONS                     |
	| TABLE_CONSTRAINTS                     |
	| TABLE_CONSTRAINTS_EXTENSIONS          |
	| TABLE_PRIVILEGES                      |
	| TRIGGERS                              |
	| USER_ATTRIBUTES                       |
	| USER_PRIVILEGES                       |
	| VIEWS                                 |
	| VIEW_ROUTINE_USAGE                    |
	| VIEW_TABLE_USAGE                      |
	+---------------------------------------+
	79 rows in set (0.05 sec)

##### Describe <database_name> information_schema <table_name> PROCESSLIST row formats

	mysql> DESCRIBE PROCESSLIST;

	+---------+-----------------+------+-----+---------+-------+
	| Field   | Type            | Null | Key | Default | Extra |
	+---------+-----------------+------+-----+---------+-------+
	| ID      | bigint unsigned | NO   |     |         |       |
	| USER    | varchar(32)     | NO   |     |         |       |
	| HOST    | varchar(261)    | NO   |     |         |       |
	| DB      | varchar(64)     | YES  |     |         |       |
	| COMMAND | varchar(16)     | NO   |     |         |       |
	| TIME    | int             | NO   |     |         |       |
	| STATE   | varchar(64)     | YES  |     |         |       |
	| INFO    | varchar(65535)  | YES  |     |         |       |
	+---------+-----------------+------+-----+---------+-------+
	8 rows in set (0.00 sec)
