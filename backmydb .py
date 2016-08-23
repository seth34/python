#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import sys,os,time

db_user = 'postgres'
db_pwd = 'postgres'
db_port = '5432'
db_name = 'PVS'
backup_path = '/var/lib/pgsql/DB_dump'
cmd_path = '/usr/pgsql-9.4/bin/'
log_path = backup_path + '_log'

# ������־����
def writeLogs(filename,contents):
  f = file(filename,'aw')
  f.write(contents)
  f.close()

today = backup_path + time.strftime('%Y-%m-%d')
fname = today + os.sep + time.strftime('%Y-%m-%d') + '_' + db_name + '.backup'

# ��������Ŀ¼
if not os.path.exists(today):
   Msg = '-'*30 + time.strftime('%Y-%m-%d,%H:%M:%S') + '-'*30 + '\n'
   if(os.mkdir(today)) == None:
       Msg += '** �ɹ���������Ŀ¼�� ' + today + '\n\n'
       writeLogs(log_path,Msg)
   else:
       Msg += '!! ��������Ŀ¼�� ' + today + 'ʧ�ܣ�����Ŀ¼�Ƿ��д��\n\n'
       writeLogs(log_path,Msg)
       sys.exit()

# ���� CCIC2���ݿ�
cmd_dump = "pg_dump -f %s %s" % \
               (fname,db_name)

writeLogs(log_path,cmd_dump + '\n')

# ִ�б�������
if os.system(cmd_dump) == 0:
   writeLogs(log_path,'���ݱ���Ϊ�� ' + fname + '\n')
else:
   writeLogs(log_path,'���ݱ���ʧ�ܣ�\n')
