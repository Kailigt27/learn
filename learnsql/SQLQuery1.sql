if exists(select *from sys.databases  where name='DBTEST')
     drop database DBTEST
--创建数据库
create database DBTEST
on --数据文件
(
      name='DBTEST',--逻辑名称
	  filename='C:\learnsql\DBTEST.mdf',--物理路径和名称
	  size=5MB,--文件的初始大小
	  filegrowth=2MB--文件的增长方式,可以写大小，也可以写百分比
)
log on--日志文件
(
      name='DBTEST_LOG',--逻辑名称
	  filename='C:\learnsql\DBTEST_LOG.ldf',--物理路径和名称
	  size=5MB,--文件的初始大小
	  filegrowth=2MB--文件的增长方式,可以写大小，也可以写百分比
)
create database DBTEST1