#: *****************************************************************************
#:                    This code was created by Ratul Hasan                     *
#:                     So comlpete credit goes to him(me)                      *
#: *****************************************************************************
#: Sharing this code without my permission is not allowed                      *
#: *****************************************************************************
#: This code was created based on IDLE, Pydroid(Android), qPython(Android) etc.*
#: So most online/web site based idle(i.e: Sololearn) can't run this code      *
#: properly.                                                                   *
#: *****************************************************************************
#: If there is any error or you want to help please let me know.               *
#: e-mail: wwwqweasd147@gmail.com                                              *
#: *****************************************************************************

from re import search
# from bs4 import BeautifulSoup as bs
# 
from os import makedirs
from os.path import exists, isdir
from platform import system as os_name
from threading import Thread as Process
import sys
import subprocess


parser='html.parser'

os_name=os_name()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def loc(x, os_name=os_name):
	"""to fix dir problem"""
	if os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')
def get_file_ext(x):
	return x.split('.')[-1]
def get_file_name(x):
	return loc(x,'linux').split('/')[-1]

def reader(direc):
	with open(loc(direc)) as f:
		return f.read()
print(isdir('data/projects/Sao manga rip'))

def writer(fname, mode, data, dir=0):
	if dir == 0:
		with open(fname, mode) as file:
			file.write(data)
	else:
		locs=loc(dir)
		if exists(locs):
			if locs.endswith('/'):
				with open(loc(locs + fname), mode) as f:
					f.write(data)
			else:
				with open(loc(locs + '/' + fname), mode) as f:
					f.write(data)
		else:
			makedirs(locs)
			writer(fname, mode, data, locs)

def install(pack, alias=0):
	"""Just install package"""

	if alias == 0:
		alias = pack

	subprocess.call([sys.executable, "-m", "pip", "install", "--user",'--disable-pip-version-check','--quiet', pack])

try:
	import requests
except:
	install('requests')
	import requests
try:
	from bs4 import BeautifulSoup as bs
except:
	install('beautifulsoup4')
	from bs4 import BeautifulSoup as bs


def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

done=0
def distribute(lists,task_id):
	global total,done, errors
	task_id=str(task_id)
	if exists('data/projects/'+Project+'/t'+task_id+'.txt'):
		res=eval(open('data/projects/'+Project+'/t'+task_id+'.txt').read())
		
	else:
		res=0
	done+=res
	for i in lists:
		#sys.stdout.write("\033[2K")
		delete_last_line()
		print('Downloadng ['+ str(done+1) + '/'+str(total)+']')
		
		#sys.stdout.flush()
		
		if lists.index(i)>=res:
			try:
				writer(get_file_name(i[0]),'wb',requests.get(i[0], headers=headers).content,'Projects/'+Project+'/'+sub_dirs[i[1]])
				writer('t'+task_id+'.txt', 'w',str(res),'data/projects/'+Project)
			except requests.ConnectionError:
				writer('errors.txt', 'a',str(i)+'\n','data/projects/'+Project)
				errors+=1
			res+=1
			done+=1


import time

if not exists('data/projects.db'):
	writer('projects.db','a','','data')
all_list=set([])
do_all=0
starts=''
def list_writer(link, web_starts, types, file_link_starts,n):
	global all_list

					
	page = requests.get(link,headers=headers)
	soup=bs(page.content, parser)
	# print(page.content)
	# time.sleep(10000)
	# li=[]
	for imgs in soup.find_all('img'):
		http=imgs.get('src')
		if http== None:
			http=imgs.get('data-src')
		if search('^'+file_starts, str(http))!=None and http.endswith(types):
			if http.startswith('//i') and '.imggur.net' in http:
				http="https:"+http
			all_list.add((http,n))
			# li+=[http]
		# print(http)
	# li1=(link.get('src')  if  )
	# for i in li1:
	# 	print(i, search(file_starts, i)!=None)
		


img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')
pas=0
Project=input('Enter Batch download directory (Project name): ')
if Project in open('data/projects.db').read().split('\n'):
	print('project found')
	#system('ls')
	if exists('data/projects/'+Project+'.proj') and exists('data/projects/'+Project+'.list'):
		#try:
		with open('data/projects/'+Project+'.proj') as f:
			print('db found')
			#db=
			dats=f.read().split('\n')
			link=dats[0]
			start=dats[1]
			file_types=dats[2]
			file_starts=dats[3]
			sub_dirs=eval(dats[4]) #sub directory list
		with open('data/projects/'+Project+'.list') as f:
			x=str(f.read())
			print('list found')
		exec("all_list="+x)
		#print(x)
		print('realoaded')
		pas=1
		'''except:
			pas=0
			print('error')'''

		
		#download_files(listx,state)
	else:
		pas=0
		print('not found')
if pas==0:

	link=input("Enter the link: ")
	page = requests.get(link, headers=headers)
	soup=bs(page.content, parser)
	start=input("Links Starts With: ")
	li1=set([link.get('href') for link in soup.find_all('a')])
	if start=='': start=link

	file_types1=input("Enter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg,mp3) or just write the category (ie: image, music, video): ")
	if file_types1=='image':
		file_types=img
	else:
		file_types= tuple(i.strip(i) for i in file_types1.split(','))

	file_starts=input("File Links Starts With (if known or need to be specified): ")
	path=Project[:]

	#if start[-1'/'): start+='/'
	#if start.startswith(): start=start[1:]
	sub_dirs=[]
	len_li1=str(len(li1))
	n=0
	print('\n\n')
	for i in li1:
		delete_last_line()
		print('Indexing ['+ str(n+1) + '/'+len_li1+'] '+i)
		
		#sys.stdout.flush()
		#print(link)
		locs=i
		if locs[-1]=='/':
			locs=locs[:-1]
		sub_dirs+=[locs.split('/')[-1]]
		
		
		if  do_all==0 and i.startswith('/'):
			print("Partial link detected - ",link,"\nSearching for home page.")
			#print(start)
			HP=search('(https?://[^/]*)',start)
			#print(HP)
			if HP!=None:
				print("Home page detected: ", HP.group())
				io= input("Is this the homepage? \n(y for yes\nn for no\na for all)\n")
				if io=="a":
					do_all=1
					io='y'
				if io=='y':
					starts=HP.group()
				elif io=='n':
					starts= input("Enter the home page: ")
					io2=input('Is it for all other links?(y/n)')
					if io2=='y': 
						do_all=1
					elif io2!='n':
						print("Invalid input!")
						raise InterruptedError
				else:
					print("Invalid input!")
					raise InterruptedError
		
		
		#print(link)
		#print(sub_dirs)
		if (starts+i).startswith(start):
			list_writer(starts+i,start, file_types, file_starts,n)
		
		#print(i)
		n+=1
		#sys.stdout.write("\033[2K")
	all_list=list(all_list)
	writer('projects.db','a',Project+'\n','data')
	writer(Project+'.list','w',str(all_list),'data/projects')
	writer(Project+'.proj','a',link+'\n','data/projects')
	writer(Project+'.proj','a',start+'\n','data/projects')
	writer(Project+'.proj','a',str(file_types)+'\n','data/projects')
	writer(Project+'.proj','a',file_starts+'\n','data/projects')
	writer(Project+'.proj','a',str(sub_dirs)+'\n','data/projects')
print('\n\n')
total=len(all_list)


if exists('data/projects/'+Project+'/t'+'errors.txt'):
	errors=len(open('data/projects/'+Project+'/t'+'errors.txt').readlines())
else:
	errors=0

#print(all_list)

t11= Process(target=distribute, args=(all_list[::10],1))
t2= Process(target=distribute, args=(all_list[1::10],2))
t3= Process(target=distribute, args=(all_list[2::10],3))
t4= Process(target=distribute, args=(all_list[3::10],4))
t5= Process(target=distribute, args=(all_list[4::10],5))
t6= Process(target=distribute, args=(all_list[5::10],6))
t7= Process(target=distribute, args=(all_list[6::10],7))
t8= Process(target=distribute, args=(all_list[7::10],8))
t9= Process(target=distribute, args=(all_list[8::10],9))
t10= Process(target=distribute, args=(all_list[9::10],10))

##sleep(.5)

t11.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t11.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

with open('data/projects/'+Project+'/errors.txt') as f:
	errs= [eval(i) for i in f.readlines()]
	distribute(errs,11)

'''Sao manga rip
https://sword-artonline.com/
https://sword-artonline.com/manga/
image
https://1.bp.blogspot.com/
'''

'''Accel world
https://www.mangareader.net/accel-world

image
//i\d+.imggur.net/accel-world/
'''
'''Accel world
https://mangapill.com/manga/99/accel-world
https://mangapill.com/chapters/99-100
image
https://cdn.read7deadlysins.com/file/mangap/99/100
'''

