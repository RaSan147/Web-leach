
from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
from os import devnull as os_devnull, system as os_system

from sys import exit as sys_exit,executable as sys_executable
from sys import stdout as sys_stdout
port = 8080
cd = 'Download_projects'
_latest_filename = 'test'
print(['python', '_server000_.py', str(port), '-d', cd])
subprocess_call(['python', '_server000_.py', str(port), '-d', cd])
subprocess_call(['7z.exe', 'e', '-y', '-plock', './data/.temp/'+_latest_filename+'.zip'])#, stdin=open(os_devnull), start_new_session=True, stdout=subprocess_DEVNULL, stderr=subprocess_DEVNULL)
