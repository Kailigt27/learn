if exists(select *from sys.databases  where name='DBTEST')
     drop database DBTEST
--�������ݿ�
create database DBTEST
on --�����ļ�
(
      name='DBTEST',--�߼�����
	  filename='C:\learnsql\DBTEST.mdf',--����·��������
	  size=5MB,--�ļ��ĳ�ʼ��С
	  filegrowth=2MB--�ļ���������ʽ,����д��С��Ҳ����д�ٷֱ�
)
log on--��־�ļ�
(
      name='DBTEST_LOG',--�߼�����
	  filename='C:\learnsql\DBTEST_LOG.ldf',--����·��������
	  size=5MB,--�ļ��ĳ�ʼ��С
	  filegrowth=2MB--�ļ���������ʽ,����д��С��Ҳ����д�ٷֱ�
)
create database DBTEST1