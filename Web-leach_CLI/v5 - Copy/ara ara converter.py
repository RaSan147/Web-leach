'''with open('ara ara codes.txt') as f:
	alls=f.read().split()

with open('ara ara on fire.txt', 'w') as f:
	for i in range(len(alls)):
		f.write('%i nh %s\nnh %s\ny\n\n'%(i, alls[i], alls[i]))
		print(i)'''

import os, webbrowser,threading
import subprocess, time
def open_server():
	subprocess.run(['py','-m', 'http.server'] , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
t_server = threading.Thread(target=open_server)

t_server.start()
time.sleep(2)
webbrowser.open('http://localhost:8000/Download_projects/0%20nh%20245503/0%20nh%20245503.html')