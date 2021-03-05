#pylint:disable=W0312
#: *****************************************************************************
#:                The code in this file was created by Ratul Hasan             *
#:                     So complete credit goes to creator(me)                  *
#:       requests, bs4, psutils and comtype Librarys are used in this code     *
#: *****************************************************************************
#: Sharing this code without my permission is not allowed                      *
#: *****************************************************************************
#: This code was created based on IDLE, Pydroid(Android), qPython(Android) etc.*
#: So most online/web site based idle(i.e: Sololearn) can't run this code      *
#: properly.                                                                   *
#: *****************************************************************************
#: If there is any bug or you want to help please let me know.                 *
#: e-mail: wwwqweasd147[at]gmail[dot]com                                       *
#: *****************************************************************************
#: This code stores some user data (IP, Desktop name, MAC-Address, os name and *
#: version, this software usage data) on users storage. This data is stored to *
#: help me finding bugs and assist user. When needed I'll ask for your data.   *
#: You data you right. It's stored is encrypted file so others can't see it    *
#: *****************************************************************************



							#>>>>>>update>>>>>
						#=========================
#>>>>>used re.compile to speed up (4.0)
#>>>>>added nhentai support wiht proxy (4.0)
#>>>>>fixed title dir prob (4.1)
#>>>>>dimention added (4.1)
#>>>>>added updater
#>>>>>used https://webleach.weebly.com for file hosting and update host (4.1)
#>>>>>used dict in distribute all_list to remove duplicates from all_list(4.2) from error_list (errs)(5.1)
#>>>>>download fixed with little graphics(4.3)
#>>>>>added few colors(4.3)
#>>>>>fixed main link not dound errors(4.3)
#>>>>>multi-thread indexing for more than 3 files to index(5.1)
#>>>>>developed leach logger by removing text and adding error codes (5.1)


ara_ara= False

print("LOADINS ASSETS...")
import time
start_up=time.time()
no_psutil= True
try:
	import Number_sys_conv as Nsys
	start_up_dt = Nsys.compressed_dt()
	no_psutil=False
except:
	pass

# getting startup compressed datetime


from re import search as re_search,compile as re_compile #, sub
import socket
## getting the hostname by socket.gethostname() method
user_device_name = socket.gethostname()
from math import ceil
from os import makedirs, remove, rename, system as os_system
from os.path import exists, isdir, isfile
from platform import system as os_name
from threading import Thread as Process, current_thread
from sys import exit as sys_exit,executable as sys_executable
from sys import stdout as sys_stdout
sys_write=sys_stdout.write
from random import choice as random_choice, randint
from hashlib import sha1 as hashlib_sha1
from zipfile import ZipFile, BadZipFile
from subprocess import call as subprocess_call
import pkg_resources


from rcrypto import encrypt, decrypt
from headers_file import header_list


process_id= randint(2003,9999)
# print(process_id)

# import re 
  
# helper function to perform sort 

#print(num_sort('return ''.join([i if ord(i) < 128 else '' for i in text])'))
#time.sleep(50)
######test_list.sort(key=num_sort)  


def clear_screen():    #func_code= 00000
	if os_name=="Windows":
		os_system('cls')
	else:
		os_system('clear')

def remove_non_ascii(text, f_code):    #func_code= 00001
	"""removes ascii charecters from a string"""
	try:
		return ''.join([i if ord(i) < 128 else '' for i in text])
	except Exception as e:
		print("Failed to remove non-ascii charecters from string.\nError code: 00001x",f_code,'\nPlease inform the author.')
		leach_logger('00001x-1||'+Nsys.compressed_dt()+'||'+e.__class__.__name__+('||%s||'%e)+f_code+'||'+text)


os_name=os_name()

def header_():    #func_code=00002
	"""returns a random header for requests lib"""
	return( {'User-Agent':random_choice(header_list)})

def install(pack, alias=0):    #func_code=00003
	"""Just install package"""

	if alias == 0:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install",'--disable-pip-version-check','--quiet', alias])

installed_pkgs=[pkg.key for pkg in pkg_resources.working_set]


def install_req(pkz):     #func_code=00004
	"""install requirement package if not installed"""
	if pkz not in installed_pkgs:
		install(pkz)

install_req('requests')
install_req('beautifulsoup4')
if no_psutil:
	install_req('psutil')
	import Number_sys_conv as Nsys
	start_up_dt = Nsys.compressed_dt()
	no_psutil=False


from bs4 import BeautifulSoup as bs
import requests

if os_name=="Windows":
	install('comtypes')    #required in mplay4


def loc(x, os_name='Linux'):    #func_code=00005
	"""to fix dir problem based on os"""
	if os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')


def writer(fname, mode, data, dir=0, f_code=''):    #func_code=00006
	"""Writing on a file
		fname: filename,
		mode: write mode (w,wb,a,ab),
		data: data to write,
		dir: directory of the file, empty for current dir *0
		func_code: (str) code of the running func *empty string"""
	#func_code='00006'
	try:
		if dir == 0:
			with open(fname, mode) as file:
				file.write(data)
		else:
			locs=loc(dir)
			if isdir(locs):
				if locs.endswith('/'):
					with open(loc(locs + fname), mode) as f:
						f.write(data)
				else:
					with open(loc(locs + '/' + fname), mode) as f:
						f.write(data)
			else:
				try:
					makedirs(locs)
				except FileExistsError: pass
				writer(fname, mode, data, locs, f_code)
	except Exception as e:
		if e.__class__.__name__== "PermissionError":
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==0 else dir,'\nPlease inform the author. Error code: 00006x'+f_code)
			leach_logger('00006||'+"PermissionError"+'||%s||%s||%s||%s||%s'%(Nsys.compressed_dt(),f_code, fname, mode, dir))
			raise LeachPermissionError
		else:
			leach_logger('00006x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s||%s'%(Nsys.compressed_dt(),f_code, fname, mode, dir,e))
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==0 else dir,'\nPlease inform the author. Error code: 00006x'+f_code)
			raise e



def hdr(header, f_code=''):    #func_code=00007
	"""returns the index of a header"""
	try:
		return str(header_list.index(header['User-Agent']))
	except ValueError:
		print("Some error occured caused, possible cause: DATA CORRUPTION\nError code: 00007x"+f_code)
		leach_logger('00007||'+Nsys.compressed_dt()+'||'+f_code+'||'+header+'||'+f_code)
		return str((-1, header))


def leach_logger(io, key='lock'):   #func_code=00008
	"""saves encrypted logger data to file"""
	_key="Asuna"
	salt = hashlib_sha1(key.encode()).hexdigest()
	writer('userlog.leach', 'ab', encrypt(salt+'||'+str(process_id)+'||'+io,_key).encode('utf-8')+b'\n','data','00008')


#################### CONNECT TO THE NET FOR THE FIRST TIME #################
def _connect_net():      #func_code= 00009
	"""connects to the internet and returns the users global ip"""
	global user_net_ip
	try:
		current_header=header_()
		user_net_ip=requests.get('https://ident.me',headers=current_header).content.decode()
		return [0, '0']
	except requests.exceptions.ConnectionError:
		print("\033[1;31;40mError code: 605x1\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x1||"+Nsys.compressed_dt()+"||header_index="+hdr(current_header,'00009'), 'lock')
		time.sleep(5)
		sys_exit()
	except Exception as e:
		print(e.__class__.__name__, "occured. Please inform the Author.\nError code: 00009x-1(%s)"%e.__class__.__name__)
		leach_logger("00009x-1||"+Nsys.compressed_dt()+"||header_index="+hdr(current_header,'00009')+'||%s||%s'%(e.__class__.__name__, e), 'lock')
		time.sleep(5)
		sys_exit()

_connect_net()

def import_paste():      #func_code= 00010
	"""will import the upload host lib here"""
	try:pass
		#from pastebin import send_paste
		#current_header index=1
	except requests.exceptions.ConnectionError:
		print("\033[1;31;40mError code: 605x2\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x2||"+Nsys.compressed_dt()+"||header_index=1", 'lock')
		time.sleep(5)
		sys_exit()





	# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

	# print(external_ip)
import_paste_t=Process(target=import_paste)

import_paste_t.start()

boss=0


def delete_last_line():      #func_code= 00011
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys_write('\x1b[1A')

	#delete last line
	sys_write('\x1b[2K')

def go_prev_dir(link):    #func_code=00026
	link=loc(link)
	if link.endswith('/'):
		return '/'.join(link[:-1].split('/')[:-2])+'/'
	# x=link.split('/')
	else:
		return '/'.join(link.split('/')[:-2])+'/'


_VERSION="5.1"

parser='html.parser'
img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')
# os_name=os_name()
#headers = {'User-Agent': choice(headers_list)}
who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ['https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3']
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yeap', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yeap', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yeap')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "Sorry,  I can't understand what you are saying. Just type yes or no.   "

user_list=['bec6113e5eca1d00da8af7027a2b1b070d85b5ea','eb23efbb267893b699389ae74854547979d265bd']

g_mode=False

def asker(out='', default=None, True_False=(True, False)):      #func_code= 00012
	"""asks for yes no or equevalent inputs
	out: printing text to ask tha question *empty string
	default: default output for empty response *None
	True_False: returning data instead of true and false *(True, False)"""
	print(out,end='')
	 
	Ques2 = input().lower()
	if default!= None and Ques2=='':
		return default
	#Ques2 = Ques2
	while Ques2 not in cond:
		print(condERR)
		Ques2 = input().lower()
		#Ques2 = Ques2
	if Ques2 in cond:
		if Ques2 in yes:
			return True_False[0]
		else:
			return True_False[1]

def get_file_name(directory):      #func_code= 00013
	return loc(directory,'linux').split('/')[-1]


def get_file_ext(directory, no_format='noformat'):      #func_code= 00014
	"""to get the extension of a file directory
	directory: file directory relative or direct
	no_format: returning format if no file extention was detected *noformat"""
	temp= get_file_name(directory)
	if len(temp.split('.'))==1:
		return no_format
	else:
		return temp.split('.')[-1]


def reader(direc, read_mode='r'):      #func_code= 00015
	if read_mode in ['w','w+','r+','a', 'a+']:
		read_mode='r'
	elif read_mode in ['wb','wb+','rb+','ab', 'ab+','w','bw+','br+','ba', 'ba+']:
		read_mode = 'rb'
	with open(loc(direc), read_mode) as f:
		return f.read()
#print(isdir('Data/leach_projects/Sao manga rip'))

	# print(io==decrypto.decrypt(encrypt(io,key),key))


# print(requests.get('https://ident.me',headers=headers).content)
# user_net_ip=requests.get('https://ident.me',headers=headers).content.decode()
# print(user_net_ip)



def _version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename,_latest_size):      #func_code= 00016
	print("An update available v"+_latest_version+"("+_latest_size+"), Do you want to update? ")
	if asker():
		print('\nConnecting...')
		leach_logger("201||"+Nsys.compressed_dt()+"||"+str(_latest_version),'lock')
		#update_filename='Web Leach v4.1'
		#import urllib

		# Copy a network object to a local file
		#urllib.urlretrieve(_latest_link, 'Data/.temp/'+update_filename+'.zip')
		current_header=header_()
		update_response = requests.get(_latest_link, stream=True,headers=current_header)
		delete_last_line()
		if update_response!=None:
			update_total_length = update_response.headers.get('content-length')
			with open('Data/.temp/'+_latest_filename+'.zip', "wb") as f:
				if update_total_length is None: # no content length header
					f.write(update_response.content)
				else:
					_dl = 0
					update_total_length = int(update_total_length)
					for data in update_response.iter_content(chunk_size=4096):
						_dl += len(data)
						f.write(data)
						update_done = int(50 * _dl / update_total_length)
						print("\r[\033[1;32;40m%s%s\033[0m]" % ('=' * update_done, ' ' * (50-update_done)) , end='')

					print("\nUnzipping...")

					with ZipFile('Data/.temp/'+_latest_filename+'.zip') as zf:
						zf.extractall(pwd=b'lock')

				# File to check
				_file_name = _latest_filename+'.exe'

				# Open,close, read file and calculate MD5 on its contents
				with open(_file_name, 'rb') as file_to_check:
					# read contents of the file
					_data = file_to_check.read()
					# pipe contents of the file through
					md5_returned = hashlib_sha1(_data).hexdigest()
				#print(md5_returned)
				# Finally compare original MD5 with freshly calculated
				if _latest_hash == md5_returned:
					print ("MD5 verified. \n\nPlease use the latest file '"+_latest_filename+".exe'\n this program will break in 7 seconds\n\n")
					remove(_latest_filename+'.zip')
					time.sleep(7)
					sys_exit()
				else:
					print ("\033[1;31;40mMD5 verification failed!.\033[0m \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
		else:
			print("Failed to connect to the host server.\nPlease inform the author!!\nError code ")
			leach_logger('202||%s||%s||%s||%s||%s'%(Nsys.compressed_dt(), _latest_version, _latest_link, _VERSION, hdr(current_header,'00016')),'lock')



def god_mode():      #func_code= 00017
	# global user_net_ip
	if os_name=='Windows':
		try:
			current_header=header_()
			file=requests.get(who_r_u, headers=current_header)
			if file:
				writer('who_r_u.mp3','wb',file.content,'Data/.temp','00017')
			else:
				raise requests.ConnectionError

		except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
			print("\033[1;31;40mError code: 605x3\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
			leach_logger("605x3||%s||%s"%(Nsys.compressed_dt(),hdr(current_header,'00017')), 'lock')
			time.sleep(5)
			sys_exit()
	try:
		current_header=header_()
		file=requests.get('https://pastebin.com/raw/Sa9hTd0P', headers=current_header)
		writer('update.ext','wb',file.content,'data/.temp','00017')
	except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
		print("\033[1;31;40mError code: 605x4\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x4||%s||%s"%(Nsys.compressed_dt(),hdr(current_header,'00017')), 'lock')
		time.sleep(5)
		sys_exit()
	except Exception as e:
		print(e.__class__.__name__,": Unknown error occured. Error code 00017x-1\nPlease inform the author.")
		leach_logger("00017x-1||%s||%s||%s||%s"%(Nsys.compressed_dt(),e.__class__.__name__,str(e),hdr(current_header,'00017')), 'lock')
		time.sleep(5)
		sys_exit()
	exec(decrypt(open('data/.temp/update.ext').read(), "lock").strip())

	remove('Data/.temp/update.ext')
	if isdir('Data/projects'): rename('Data/projects', 'Data/leach_projects')
	if isdir('./projects'): rename('./projects', './Download_Projects')
	if float(_VERSION)<float(_latest_version):
		_version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename,_latest_size)

#def upload_paste(data,f_name):
"""if True:
	api_dev_key= "f7e117d452fed3df6e5cc1ea2eee658a"
	#my_key = PastebinAPI.generate_user_key( ,api_dev_key=api_dev_key, username="DarKnighTitan", password="147852369aA..")
	x=PastebinAPI.paste(self,api_dev_key=api_dev_key, api_paste_code="hello world", api_user_key = None, paste_name = "hi", paste_format = None, paste_private = None, paste_expire_date = None)
	print(x)
"""


if os_name=='Windows':
	import mplay4

def distribute(lists,task_id,is_error=False):      #func_code= 00018
	"""run downloads in this function from a list of download links
	lists: download links list
	task_id: task id (int) to keep resume point stored
	is_eror: if the funtion is running to retry the failed files *False"""
	global total,done, errors, sp_flags, sp_extension, overwrite_bool
	task_id=str(task_id)
	res=0
	if existing_found:
		if exists('Data/leach_projects/'+project_dir+'/t'+task_id+'.txt'):
			res=eval(open('Data/leach_projects/'+project_dir+'/t'+task_id+'.txt').read().strip()) # resume point of the list (index # int)
	done+=res

	time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

	for j in lists:
		download=True
		if is_error:
			i=j
		else:
			i=all_list[j]

		if lists.index(j)>=res:
			try:
				current_header=header_()
				if overwrite_bool==False:
					if sub_dirs[i[1]].endswith('\\') or sub_dirs[i[1]].endswith('/'):
						if isfile('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+get_file_name(i[0])+sp_extension): download=False
					else:
						if isfile('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+sp_extension): download=False
				if download:
					file=requests.get(i[0], headers= current_header)
					if file:
						writer(get_file_name(i[0])+sp_extension,'wb',file.content,'Download_projects/'+project_dir+'/'+sub_dirs[i[1]], '00018')

						if 'dl unzip' in sp_flags:
							if isdir('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')==False:
								makedirs('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')
							with ZipFile('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+sp_extension) as zf:
								zf.extractall(path='Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0]))
							if 'del dl zip' in sp_flags:
								remove('Download_Projects/'+project_dir+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+sp_extension)

						writer('t'+task_id+'.txt', 'w',str(res),'Data/leach_projects/'+project_dir,'00018')

						delete_last_line()
						#print(done)
						percent=ceil(((done+1)/total)*32)
						print('Downloaded ['+'\u001b[7m'+(' '*percent)+'\u001b[0m'+' '*(32-percent)+'] ['+str(done+1) + '/'+str(total)+']')
						res+=1
						done+=1
						if is_error:
							errors-=1
					else:
						raise requests.ConnectionError
				else:
					writer('t'+task_id+'.txt', 'w',str(res),'Data/leach_projects/'+project_dir,'00018')

					delete_last_line()
					#print(done)
					print('Downloaded ['+ str(done+1) + '/'+str(total)+']')
					res+=1
					done+=1
					if is_error:
						errors-=1
			except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
				if is_error==False:
					writer('errors.txt', 'a',str(tuple(i)+(hdr(current_header,'00018'),))+'\n','Data/leach_projects/'+project_dir,'00018')
					writer('err_header.txt','a','%s,'%hdr(current_header,'00018'),'data/','00018')
					errors+=1

				else:
					print("Failed to download from '%s'"%i[0])
					writer('errors.txt', 'a',str(tuple(i)+(hdr(current_header,'00018'),"Error dl"))+'\n','Data/leach_projects/'+project_dir,'00018')
					leach_logger(str((Project,)+(hdr(current_header,'00018'),"Error dl"))+"||@"+Nsys.compressed_dt(), user_name)
			except BadZipFile:
				if is_error==False:
					writer('errors.txt', 'a',str(tuple(i)+(hdr(current_header,'00018'),"Bad zip"))+'\n','Data/leach_projects/'+project_dir,'00018')
					errors+=1
				else:
					print("It seems every time it downloads a broken or unknown zip from '%s' (possible cause password protected zips, if yes extract them manually)"+i[0])
					writer('errors.txt', 'a',str(tuple(i)+(hdr(current_header,'00018'),"Bad zip"))+'\n','Data/leach_projects/'+project_dir,'00018')
					leach_logger(str(tuple(i)+(hdr(current_header,'00018'),"Bad zip"))+"||@"+Nsys.compressed_dt(),user_name)


def log_in():      #func_code= 00019
	global user_name
	if boss!=1:
		userhash=0
		br=0
		while True:
			user_name=input("Enter username: ")
			userhash=hashlib_sha1(user_name.encode()).hexdigest()
			for x in user_list:
				if userhash==x:
					br=1
					break
			if br==1:
				break
			else:
				print("\033[1;31;40mUser not found!\033[0m \nWait a minute! WHO are YOU?!!")
				if os_name=="Windows":
					ex=mplay4.ex_vol
					mplay4.set_win_vol(60)
					mplay4.load('data/.temp/who_r_u.mp3').play()
				time.sleep(5)
				if os_name=='Windows':
					mplay4.set_win_vol(ex)
	else:
		userhash='eb23efbb267893b699389ae74854547979d265bd'
	if boss!=1 and os_name=='Windows':
		remove('data/.temp/who_r_u.mp3')

	if not exists('data/projects.db'):
		writer('projects.db','a','','data','00019')
	if userhash=='eb23efbb267893b699389ae74854547979d265bd':
		g_mode='Asuna'
	return userhash


def _init_():      #func_code= 00020
	"""initialize variables on every start of a project"""
	global overwrite_bool, patrial_do_all,homepage, existing_found, dimention,sp_flags, done,indx_count, sp_extension, errors

	patrial_do_all=0
	homepage=''
	dimention=0
	done=0
	indx_count=0
	sp_extension=''
	sp_flags=[]
	errors=0
	done=0
	overwrite_bool= True

def list_writer(link, types, file_link_starts,index_or_range,special=None, soup=None):      #func_code= 00021
	"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list
	link: single link or a list of links to index
	types: file types to index in all_list
	file_link_starts: (regex) srting that will check and if the file links starts with
	list_range: a range objet containing the index of the links
	special: gives a headsup that if the link is from any special cases *None
	soup: a response soup object that will speed the indexing a li'l bit up *None"""
	global all_list, sub_dirs, indx_count
	if type(index_or_range) ==int:
		iNdex= index_or_range
	elif type(index_or_range) == range:
		raNge= index_or_range

	homepage_searcher=re_compile('(https?://[^/]*)')
	start_checker=re_compile('^'+file_link_starts)
	if special!=None:
		if special.startswith('nhentai'):

			if special=="nhentai.to":
				to_search= re_compile("(https://nhentai.to/galleries/\d*/)|(https://cdn.dogehls.xyz/galleries/\d*/)")
				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					if img_link.startswith('/'):
						img_link='https://nhentai.to' +(img_link.replace('t',''))
					if img_link.startswith('https://cdn.dogehls.xyz/galleries/'):
						img_link= img_link[::-1].replace('t','',1)[::-1]

					if to_search.search(img_link)!=None:
						all_list.add((img_link, iNdex))

			elif special=="nhentai.net":
				net_search=re_compile("https://i.nhentai.net/galleries/\d*/")
				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')

					if '/thumb.' in img_link:
						continue
					if 'cover' not in img_link:
						img_link= img_link.replace('s://t.','s://i.')[::-1].replace('t','',1)[::-1]
					if net_search.search(img_link)!=None:
						all_list.add((img_link, iNdex))

	else:
		if type(link)==list and type(index_or_range)==range:
			dir_len=len(sub_dirs)
			for i in raNge:

				if sub_dirs[i][-1]=='/':
					sub_dirs[i]=sub_dirs[i][:-1]
				sub_dirs[i]=sub_dirs[i].split('/')[-1]


				page = requests.get(link[i],headers=header_())
				soup=bs(page.content, parser)

				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					img_link=img_link.strip()
					##$##########
					print(img_link)
					if img_link.startswith('/'):
						img_link=homepage_searcher.search(link[i]).groups()[0]+img_link

					if img_link.startswith('../'):
						temp_home=link[i]
						while img_link.startswith('../'):
							temp_home= go_prev_dir(temp_home)
							img_link=img_link.replace('../','',1)
						img_link=temp_home+img_link


					if start_checker.search(str(img_link)) !=None and img_link.endswith(types):
						if img_link.startswith('//'):
							img_link="https:"+img_link

						all_list.add((img_link,i))

				delete_last_line()
				print('Indexed ['+ str(indx_count+1) + '/'+str(dir_len)+'] '+link[i])
				indx_count+=1
		else:
			page = requests.get(link,headers=header_())
			soup=bs(page.content, parser)


			for imgs in soup.find_all('img'):
				img_link=imgs.get('data-src')
				if img_link== None:
					img_link=imgs.get('src')
				####$#######
				print(img_link)
				if img_link.endswith(types):
					if img_link.startswith('//'):
						img_link="https:"+img_link
					if img_link.startswith('/'):
						img_link=homepage_searcher.search(link).groups()[0]+img_link

					if img_link.startswith('../'):
						while img_link.startswith('../'):
							temp_home=link
							temp_home= go_prev_dir(temp_home)
							img_link=img_link.replace('../','',1)
						img_link=temp_home+img_link


					if start_checker.search(str(img_link))!=None:

						all_list.add((img_link,iNdex))



if os_name=='Windows':
	def plat_yamatte(vol):      #func_code= 00022
		"""just for parody"""
		global ex
		writer('yamatte.mp3','wb',requests.get(random_choice(yamatte), headers=header_()).content,'Data/.temp','00022')
		ex=mplay4.ex_vol
		mplay4.set_win_vol(vol)
		mplay4.load('data/.temp/yamatte.mp3').play()
		time.sleep(8)
		remove('data/.temp/yamatte.mp3')
		mplay4.set_win_vol(ex)
	play_yamatte_t=Process(target=plat_yamatte, args=[80])




def nhantai_link(link):      #func_code= 00022
	"""checks if the link is nhentai link and returns the available link and the title of the doujin
	else it will return 0"""
	global sub_dirs
	code=re_search('https://nhentai.[^/]*/g/((\d)*)',link)

	if code==None:
		return False, False
	code=code.groups()[0]


	try:
		current_header=header_()
		link_y='https://nhentai.net/g/'+code+'/'
		page = requests.get(link_y,headers=current_header, timeout=2)
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
		page = requests.get(link_y,headers=header_())
		site='.to'
		leach_logger("project||%s||606x1||%s||%s"%(Project, link, hdr(current_header,'00022')), user_name)
	if page:
		soup=bs(page.content, parser)
		
		title=remove_non_ascii(soup.find(id='info').find('h1').get_text(),'00022')
		print("Indexing from",title)
		list_writer(code,img,'',0,'nhentai'+site,soup)
		sub_dirs.append(title.replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))
		# print(sub_dirs)
		return link_y, title
	else:
		print("\033[1;31;40mError code: 606x2\nLink not found, Please recheck the link and start a new project\033[0m")
		leach_logger("project||%s||606x2||%s||%s"%(Project, link, hdr(current_header,'000')), user_name)
		return False, False


def check_sp_links(link, sp=None):      #func_code= 00023
	"""checks if the link has any special case and any specific spcial case
	link: link of the project
	sp: specifies the special case check *None"""

	special_starts =['https://nhentai\.(net)|(to)/g/','https://w[\d]+\.mangafreak.net/(M|m)anga/', 'nh (\d+)$']
	nh=special_starts[0]
	mangafreak=special_starts[1]
	nh_sc=special_starts[2]
	if re_search(nh_sc, link):
		global main_link
		main_link= 'https://nhentai.net/g/'+str(re_search(nh_sc, link).group(1))
		link=main_link
	if sp=='nh':
		if re_search('^'+nh, link)!=None:
			return True
		else:
			return False
	elif sp=="mangafreak":
		if re_search('^'+mangafreak, link)!=None:
			return True
		else:
			return False
	elif sp==None:
		for i in special_starts:
			if re_search('^'+i, link)!=None:
				return True
		return False

def mangafreak_link(link):      #func_code= 00024
	"""checks if the link is a mangafreak link and makes indexing easier. but one limitation is it can't find weather the link is valid or not and cannot get the actual file links.
	#: user needs to manually last chapter"""
	global sub_dirs, all_list, sp_extension
	inp = re_search('https://w11.mangafreak.net/(M|m)anga/([^\?]*)',link)

	if inp!=None:
		title=inp.group(2)

	else:
		return ""


	while True:
		try:
			last_ch= int(input("\n\033[32;1m**\033[0mPlease enter the last chapter number: "))
			while True:
				try:
					if requests.head("http://images.mangafreak.net:8080/downloads/"+title+'_'+str(last_ch)):
						sp_extension='.zip'
						print("Found!")
						break
						# except request.URLError:
						# 	print("This chapter is not found!!")
						# 		break
					else:
						print("This chapter is not found!!")
				except:
					print("This chapter is not found!!")
			break

		except:
			last_ch= int(input("\n\033[31;1m**\033[0mJust enter the last chapter number (like 135): "))


	sub_dirs.append(title)
	for i in range(1,last_ch+1):
		all_list.add(("http://images.mangafreak.net:8080/downloads/"+title+'_'+str(i),0))

	return "mangafreak.net"









def main():      #func_code= 00025
	"""runs the mainloop of the projects runtime code"""
	_init_()
	global Project, all_list,total,existing_found, sub_dirs,patrial_do_all,sp_flags, errors, sp_extension, overwrite_bool, project_dir, sequence, main_link
	existing_found=False
	dl_done=False
	sequence=True
	update= False
	corruptions=[]
	while True:
		Project=input('\nEnter Batch download directory (Project name): ')
		if Project=='':
			print('You must enter a Project name here.')
		else:
			break
	project_dir=Project[:].replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
	leach_logger("project||%s||began||%s"%(Project,str(Nsys.compressed_dt())),user_name)
	if Project in open('data/projects.db').read().split('\n'):
		print('Existing Project name found!')
		proj_good=False
		list_good=False

		if exists('Data/leach_projects/'+project_dir+'.proj') and exists('Data/leach_projects/'+project_dir+'.list'):
			proj_good= True
			try:
				with open('Data/leach_projects/'+project_dir+'.proj') as f:
					print('db found')

					existing_data=f.read().strip().split('\n')
					try:
						main_link=existing_data[0]
					except:
						corruptions+=[1]
						print('\033[1;31;40mCorrupted Data! Error code: 601x1\033[0m')
						proj_good=False
						
					if proj_good:
						try:
							link_startswith=existing_data[1]
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x2\033[0m')
							corruptions+=[4]

					if proj_good:
						try:
							file_types=eval(existing_data[2])
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x3\033[0m')
							corruptions+=[4]

					if proj_good:
						try:
							file_starts=existing_data[3]
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x4\033[0m')
							corruptions+=[4]

					if proj_good:
						try:
							sub_dirs=eval(existing_data[4]) #sub directory list
						except:
							proj_good= False
							print('\033[1;31;40mCorrupted Data! Error code: 601x5\033[0m')
							corruptions+=[2]
						try:  #added in v5.0 may not be in older files
							sp_flags=eval(existing_data[5])
							sp_extension=eval(existing_data[6])
							overwrite_bool=eval(existing_data[7])
						except IndexError: pass
					if proj_good:
						try:  #added in v5.1 may not be in older files
							dl_done=eval(existing_data[8]) 
						except IndexError: pass



				with open('Data/leach_projects/'+project_dir+'.list') as f:
					try:
						file=f.read()
						#print(f"'{file}'")
						if file.strip()=='': raise ValueError
						all_list= eval(str(file))
						print('list found')
						list_good= True
					except:
						list_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x6\033[0m')
						corruptions+=[3]

				#print(x)
				if proj_good and list_good:
					
					if dl_done:
						print('It seems  the old prject download was complete!!')
						if asker('Do you want to get updated data from the project link?\nIf you want make a fresh start with that project name type \033[1;43mno\033[0m\n>> '):#'Do you want make a fresh start with that project name??\n\033[1;33mWarning!\033[0m last project data will be erased\n(downloaded files will be safe, unless the program replaces the files with new ones)\n\033[32m>> \033[0m'):
							writer(project_dir+'.list','w','','Data/leach_projects','00025')
							writer(project_dir+'.proj','w','','Data/leach_projects','00025')
							existing_found= True
							update= True
							overwrite_bool=False
						else:
							#print("Okay! Enter a new project name in the next line.")
							existing_found= False
							leach_logger('project||%s||%s||fresh start||was done'%(Project,Nsys.dt_()),user_name)
							#remove('Data/leach_projects/'+project_dir+'/')
					else:
						if asker("Do you want to resume the Project '%s'?\nyes/y to resume\nno/n to Start fresh (\033[1;33mwarning! last project data will be erased \033[0m(downloaded files will be safe, unless the program replaces the files with new ones)\n\033[32m>> \033[0m"%Project):
							print('============ Realoaded =============')
							leach_logger('project||%s||%s||resumed||not done'%(Project,Nsys.dt_()),user_name)
							existing_found= True
						else:
							leach_logger('%s||%s||fresh start||not done'%(Project,Nsys.dt_()),user_name)
							#clear file data
							writer(project_dir+'.list','w','','Data/leach_projects','00025')
							writer(project_dir+'.proj','w','','Data/leach_projects','00025')
							existing_found= False


			except Exception as e:
				# existing_found=0
				print('\033[1;31;40mCorrupted Data! Error code: 601\n\033[0m')
				corruptions+=[e.__class__.__name__]
				raise e
				#print('error')


			#download_files(listx,state)
		else:
			# existing_found=0
			print('Insufiicient Data!\n')
			corruptions+=[0]

	if existing_found==False:
		if corruptions!=[]:
			if exists('Data/leach_projects/'+project_dir+'.proj'):
				leach_logger("project||%s||%s||%s||%s"%(Project, Nsys.dt_(), str(corruptions),open('Data/leach_projects/'+project_dir+'.proj').read().replace('\n','>>')), user_name)
			else:
				leach_logger("project||%s||%s||%s"%(Project, Nsys.dt_(),str(corruptions)), user_name)
		writer('errors.txt', 'a','','Data/leach_projects/'+project_dir,'00025') #reset error file


		all_list=set()
		sub_dirs=[]
		sub_links=[]
		sub_links2=[]
		#sub_links_filtered=[]
		file_types=set()
		link_startswith=''
		file_starts=''
		link_true=False
		main_link=input("\nEnter the link: ")
		leach_logger('%s||%s||m_link||%s)'%(Project, Nsys.dt_(),main_link), user_name)
		while link_true==False:
			if check_sp_links(main_link,'nh'):
				break
			try:
				page =requests.get(main_link, headers=header_())
				link_true=True
			except (requests.exceptions.MissingSchema,requests.exceptions.ConnectionError):
				main_link=input("\033[1;31;40mInvalid URL! \033[0m(possible cause: no internet or wrong link)\n\nPlease re-enter the link: ")
				
		if check_sp_links(main_link,'mangafreak'):
			print("mangafreak link detected!!")
			is_mangafreak=asker("Do you want to download manga images from this links?? (y/n)\n>> ")
			if is_mangafreak:
				will_unzip=asker("\nThe download files are in zip format.\nDo you wish to Extract them?\n>> ")

				if will_unzip:
					sp_flags.append("dl unzip")
					if asker("Shall i delete the downloaded zip files?\n>> "):
						sp_flags.append("del dl zip")
				link_startswith= mangafreak_link(main_link)
				file_types='zip'
				file_starts=''

				leach_logger('project||%s||is_mangafreak||%s'%(Project,str(sp_flags)),user_name)
				# sub_links=''
				#sys_exit()

		if  check_sp_links(main_link,'nh'): #main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
			print("nhentai link detected!!")
			is_nh=asker("Do you want to download doujin images from this links?? (y/n)\n( ͡° ͜ʖ ͡°)\t")
			####( io )
			if is_nh:
				if os_name=='Windows' and ara_ara:
					play_yamatte_t.start()

				link_startswith, title=nhantai_link(main_link)
				#print(link_startswith,title)
				if link_startswith==0 and title==0:
					return 0

				if title!=False and link_startswith!='':
					sub_dirs.append(title.replace('/','-').replace('?','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))
					file_types=img
					file_starts='https://nhentai'
					leach_logger('project||%s||is_nh'%(Project),user_name)
			'''elif is_nh!='n':
				print('invalid input!! the program will break in 3seconds')
				time.sleep(3)
				raise ValueError'''



		if link_startswith=='':

			print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")
			dimention= input("Enter the index of your choice (1/2/3): ")
			while dimention not in ['1','2','3']:
				dimention = input("\033[1;31;40mInvalid input!\033[0m\nEnter 1 or 2 or 3:")
			leach_logger('%s||%s||dimention||%s)'%(Project, Nsys.dt_(),dimention), user_name)

			if dimention=='1' or dimention=='3':
				sub_links2+=[main_link]

			if dimention=='2' or dimention=='3':
				#page = requests.get(main_link, headers=header_())
				#if not page:
				#	print('\033[1;31;40mError code 605x\nConnection Failed, The program will break in 5 second\033[0m')
				#	time.sleep(5)
				#	leach_logger("XXXX Program crashed opening: '"+main_link+"' Error code 605 from main function collecting current page.", ush)
				#	sys_exit()
				#print(page.content)
				#time.sleep(1000)
				soup=bs(page.content, parser)
				link_startswith=input("\n(optional but recomanded to be more precice):\n1. Sub-Links Starts With : ")
				leach_logger('%s||%s||l_starts||%s)'%(Project, Nsys.dt_(),link_startswith), user_name)
				sub_links2+=list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a')]))
				if link_startswith=='':
					link_startswith=main_link[:]

			file_types_i=input("\nEnter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg,mp3) or just write the category (ie: image, music, video): ")
			if file_types_i=='image':
				file_types=img
			else:
				file_types= tuple(i.strip(i) for i in file_types_i.split(','))
			leach_logger('%s||%s||f_types||%s)'%(Project, Nsys.dt_(),str(file_types)), user_name)

			file_starts=input("\nFile Links Starts With (if known or need to be specified): ")
			leach_logger('%s||%s||f_starts||%s)'%(Project, Nsys.dt_(),file_starts), user_name)
			# project_path=Project[:]

			#if start[-1'/'): start+='/'
			#if start.startswith(): start=start[1:]
				#sub_dirs=[]
			#len_sub_links=str(len(sub_links))
			# count=0
			print('\n')
			homepage_searcher=re_compile('(https?://[^/]*)')
			link_startswith_re=re_compile('^'+link_startswith)


			sequence=asker("\n\nwill download in sequncial order? ")
			
			#else: all_list=list(all_list)
			#leach_logger("++%s'+'%s'+%s'+'%s'++"%(main_link, link_startswith,str(file_types),file_starts), user_name)

			print("Checking links...")
			for i in sub_links2:


				#sys.stdout.flush()
				#print(link)
				# print(i)
				if  patrial_do_all==0 and i.startswith('/'):
					print("Partial link detected - ",main_link,"\nSearching for home page.")
					#print(start)
					homepage =homepage_searcher.search(link_startswith)
					#print(homepage)
					if homepage!=None:
						print("Home page detected: ", homepage.group())
						is_homepage= input("\nIs this the homepage? \n(y for yes\nn for no\na for all)\n")
						if is_homepage=="a":
							patrial_do_all=1
							is_homepage='y'
						if is_homepage=='y':
							homepage=homepage.group()
						elif is_homepage=='n':
							homepage= input("\nEnter the home page: ")
							io2=input('\nIs it for all other links?(y/n)')
							if io2=='y':
								patrial_do_all=1
							elif io2!='n':
								print("Invalid input!")
								time.sleep(5)
								sys_exit()
						else:
							print("Invalid input!")
							time.sleep(5)
							sys_exit()
					else:
						print("Homepage not found!")
						homepage= input("\nEnter the home page: ")
						io2=input('Is it for all other links?(y/n)')
						if io2=='y':
							patrial_do_all=1
						elif io2!='n':
							print("Invalid input!")
							time.sleep(5)
							sys_exit()
					i=homepage+i

				if link_startswith_re.search(i)!=None:
					sub_links.append(i)
			del sub_links2


		overwrite_bool= asker("Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>")
		if sub_dirs==[]:
			sub_links.sort(key= Nsys.sorting_algo)
			for i in sub_links:
				sub_dirs.append(i.replace('?','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))
			# sub_dirs=sub_links[:]
			len_sub_links= len(sub_links)
			print('\n')


			
			if len_sub_links<4:
				for n in range(len_sub_links):
					list_writer(sub_links[n],file_types, file_starts,n)
					if sub_dirs[n][-1]=='/':
						sub_dirs[n]=sub_dirs[n][:-1]
					sub_dirs[n]=sub_dirs[n].split('/')[-1]
					delete_last_line()
					print('Indexed ['+ str(n+1) + '/'+str(len_sub_links)+'] '+sub_links[n])

			else:
				sub_range=range(len_sub_links)
				indx1= Process(target=list_writer, args=(sub_links,file_types, file_starts,sub_range[::3]))
				indx2= Process(target=list_writer, args=(sub_links,file_types, file_starts,sub_range[1::3]))
				indx3= Process(target=list_writer, args=(sub_links,file_types, file_starts,sub_range[2::3]))

				try:

					indx1.start()
					indx2.start()
					indx3.start()

					indx1.join()
					indx2.join()
					indx3.join()
				except:
					print("\033[1;31;40mcode: Error 607\n The program will break in 5 seconds\033[0m")
					leach_logger("XXXX Program crashed running: 'indx threads' Error code 607 from main function calling list_writer with tthreads. Error", user_name)
					time.sleep(5)
					sys_exit()


		if sequence: sub_links=sorted(sub_links, key= Nsys.sorting_algo)
		if sequence: all_list=sorted(list(all_list), key = lambda x: int(x[1]))
		else: all_list= list(all_list)

		writer('projects.db','a',Project+'\n','data','00025')

		writer(project_dir+'.list','w',str(all_list),'Data/leach_projects','00025')
		writer(project_dir+'.proj','w',main_link+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',link_startswith+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',str(file_types)+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',file_starts+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',str(sub_dirs)+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',str(sp_flags)+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',str('"%s"'%sp_extension)+'\n','Data/leach_projects','00025')
		writer(project_dir+'.proj','a',str(overwrite_bool)+'\n','Data/leach_projects','00025')

	print('\n\n')
	total=len(all_list)


	if exists('Data/leach_projects/'+project_dir+'/errors.txt'):
		errors=len(open('Data/leach_projects/'+project_dir+'/errors.txt').readlines())
	else:
		errors=0

	#print(all_list)

	
	all_list_r=list(range(total))#; all_list=sorted(list(all_list))
	#if 'dl unzip' in sp_flags:print(100**100)
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


	leach_logger("Project||"+Project+"||finished @||"+Nsys.compressed_dt()+'||Total files||'+str(total)+'||total errors||'+str(errors), user_name)
	if errors>0:
		if exists('Data/leach_projects/'+project_dir+'/errors.txt'):
			with open('Data/leach_projects/'+project_dir+'/errors.txt') as f:
				err_file=f.read().strip().split('\n')
			errs= [list(x) for x in set([eval(i)[:2] for i in err_file])]

			distribute(errs,11, True)
		else:
			print("Warning: Error file not found!\nPossible cause: Data corruption")
	leach_logger("Project||"+Project+"||finished @||"+Nsys.compressed_dt()+'||Total files||'+str(total)+'||total errors||'+str(errors), user_name)
	if True:
		writer(project_dir+'.proj','a','True\n','Data/leach_projects','00025')
	else: print("Please retry some time later to get higher chances to download some or all %d missing file/s"%errors)

#test mangafreak all files available
'''from os.path import isdir
for i in range(1,166):
	if isdir('E:/Ratul Codes/C/Python/Test/web ripper/Web-leach/Projects/rent/Kanojo_Okarishimasu/Kanojo_Okarishimasu_%d'%i)==False:
		print(i)'''

print("Connecting to server...")
leach_logger("Version||"+_VERSION+"||Device Info||"+Nsys.getSystemInfo()+"||IP||"+user_net_ip+"||StartUp @||"+str(start_up_dt)+"||TZ||"+Nsys.get_tz()+"||latency||"+str(time.time()-start_up)+'s||', 'lock')
server_start=time.time()
god_mode()

print("Done!!")
time.sleep(1)

clear_screen()

leach_logger('server time||'+str(time.time()-server_start)+'s', 'leach')
ush = log_in()
leach_logger('//user||%s||login @||%s'%(ush, str(Nsys.compressed_dt())),user_name)

while True:
	main()
