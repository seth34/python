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

# 创建日志函数
def writeLogs(filename,contents):
  f = file(filename,'aw')
  f.write(contents)
  f.close()

today = backup_path + time.strftime('%Y-%m-%d')
fname = today + os.sep + time.strftime('%Y-%m-%d') + '_' + db_name + '.backup'

# 创建备份目录
if not os.path.exists(today):
   Msg = '-'*30 + time.strftime('%Y-%m-%d,%H:%M:%S') + '-'*30 + '\n'
   if(os.mkdir(today)) == None:
       Msg += '** 成功创建备份目录： ' + today + '\n\n'
       writeLogs(log_path,Msg)
   else:
       Msg += '!! 创建备份目录： ' + today + '失败，请检查目录是否可写！\n\n'
       writeLogs(log_path,Msg)
       sys.exit()

# 备份 CCIC2数据库
cmd_dump = "pg_dump -f %s %s" % \
               (fname,db_name)

writeLogs(log_path,cmd_dump + '\n')

# 执行备份命令
if os.system(cmd_dump) == 0:
   writeLogs(log_path,'数据备份为： ' + fname + '\n')
else:
   writeLogs(log_path,'数据备份失败！\n')
