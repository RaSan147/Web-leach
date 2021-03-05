
from bs4 import BeautifulSoup as bs
import requests
from os import makedirs,system
from os.path import exists, isdir
from platform import system as os_name
from threading import Thread as Process
import sys
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




if not exists('data/projects.db'):
	writer('projects.db','a','','data')
all_list=[]
def list_writer(link, web_starts, types, file_link_starts,n):
	global all_list
	page = requests.get(link,headers=headers)
	soup=bs(page.content, 'html.parser')
	
	li1=(link.get('src') for link in soup.find_all('img') if (link.get('src').startswith(file_starts) and link.get('src').endswith(types)))
	for i in li1:
		all_list+=[[i,n]]


img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')
pas=0
Project=input('Enter Batch download directory (Project name): ')
if Project in open('data/projects.db').read().split('\n'):
	print('project found')
	system('ls')
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
	soup=bs(page.content, 'lxml')
	start=input("Links Starts With: ")
	li1=[link.get('href') for link in soup.find_all('a') if link.get('href').startswith(start)]
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
		locs=i.replace(start,'',1)
		if locs[0]=='/':
			locs=locs[1:]
		sub_dirs+=[locs]

		#print(link)
		#print(sub_dirs)
		list_writer(i,start, file_types, file_starts,n)
		
		#print(i)
		n+=1
		#sys.stdout.write("\033[2K")
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



'''Sao manga rip
https://sword-artonline.com/
https://sword-artonline.com/manga/
image
https://1.bp.blogspot.com/
'''
