#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行表示可以直接当脚本执行，如./test.py
'彻底删除mac app'

__author__ = 'david.liu'
import commands
import sys

def cleanup(appName):
#    print('your type:',appName);
    shell = 'mdfind -name '+appName
    (status,output) = commands.getstatusoutput(shell)
    if status == 0 and isinstance(output,str):
         fileNames = output.split('\n')
         print('找到如下文件：>>>>>>>>>>>>>>>>>>')
         for name in fileNames:
            print(name)
         typeName = raw_input('输入y执行删除，输入其他放弃:')
         if typeName == 'y':
              for name in fileNames:
                  deleteShell = 'rm -rif '+name
                  (stauts,output) = commands.getstatusoutput(deleteShell)
                  if status == 0:
                     print('成功删除:'+name)
                  else:
                     print('删除文件失败:'+name)
                     break
    else:
        print(status,output)


if __name__ == '__main__':
    args = sys.argv;
    if len(args) <= 1:
        print('请输入需要卸载应用程序名称,例如：python uninstallMacApp.py QQ');
    else:
        cleanup(args[1])
