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

requirements_all= ['requests',  'beautifulsoup4', 'natsort']
requirements_win= ['pypiwin32', 'comtypes', 'pyopenssl', 'psutil']

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
#>>>>>fixed main link not found errors(4.3)
#>>>>>multi-thread indexing for more than 3 files to index(5.1)
#>>>>>developed leach logger by removing text and adding error codes (5.1)
#>>>>>converted to class mode (5.3_class)
#>>>>>download puaseable (5.3_class)
#>>>>>backward compatitable (5.3_class)
#>>>>>auto webpage generator (5.3_class)
#>>>>>auto localhost creation after login (5.3_class)
#>>>>>generate port based on user hash (5.3_class)
#>>>>>added nhentai.to proxy after nhentai.xxx proxy (5.500001_class)


ara_ara= False #to control parody noise

print("LOADINS ASSETS...")

cloud_data_link_global='https://raw.githubusercontent.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global(v5.5%2B).txt'#'https://pastebin.com/raw/Sa9hTd0P' #backend server location
cloud_data_link='https://raw.githubusercontent.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update%20(server%20v5.500001).txt'
user_net_ip='offline'
import time


start_up=time.time()
no_psutil= True
'''`True` = psutil is not installed
	`False` = psutil is installed'''
try:
	import Number_sys_conv as Nsys           #f_code = 20000
	# different number based functions I made
	start_up_dt = Nsys.compressed_dt() #stores when the program was launched
	no_psutil=False # this means psutils is available
except:
	pass

#########################################################

# MATH tools ######################
from math import floor
from random import choice as random_choice, randint
from hashlib import sha1 as hashlib_sha1, md5 as hashlib_md5
from re import search as re_search,compile as re_compile, sub as re_sub

from rcrypto import encrypt, decrypt
###################################


# SYS tools #######################
from platform import system as os_name
os_name=os_name()
from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
from os import devnull as os_devnull
from sys import exit as sys_exit,executable as sys_executable
from sys import stdout as sys_stdout
from importlib import reload
from functools import partial
sys_write=sys_stdout.write
del sys_stdout
###################################



# FILE system tools###############
from os import makedirs, remove, rename, system as os_system, listdir as os_listdir
from shutil import rmtree as rmdir
from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname, realpath as os_realpath
from zipfile import ZipFile, BadZipFile
###################################



from threading import Thread as Process, current_thread



# HTML tools##############################
from html import unescape as html_unescape, escape as html_escape
from urllib import parse
import webbrowser

try:
	from bs4 import BeautifulSoup as bs
	import requests, natsort
except: pass

from headers_file import header_list        # f_code = 30000

##########################################

#Other Libs###############################
from collections import Counter

##########################################

# Re Define to speed up###################
len = len
range = range
##########################################

process_id= randint(2003,9999) # a process ID to identify use multiple windows in the same time from log

#==================================================#
#                ERROR CLASS                       #
#--------------------------------------------------#
class LeachUnknownError(Exception):                #
	pass                                           #
												   #
class LeachKnownError(Exception):                  #
	pass                                           #
												   #
class LeachICancelError(Exception):                #
	pass                                           #
												   #
class LeachPermissionError(Exception):             #
	pass                                           #
												   #
class LeachNetworkError(Exception):                #
	pass                                           #
												   #
class LeachCorruptionError(Exception):             #
	pass                                           #
#                                                  #
####################################################

death = False

# import __main__ # used to load assets in global (idea from pydroid)


def remove_duplicate(seq):	#func_code=00000
	"removes duplicates from a list or a tuple"
	return list(dict.fromkeys(seq))

def clear_screen():    #func_code=00001
	"""clears terminl output screen"""
	if os_name=="Windows":
		os_system('cls')
	else:
		os_system('clear')


def delete_last_line():      #func_code=0002
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys_write('\x1b[1A')

	#delete last line
	sys_write('\x1b[2K')


def remove_non_ascii(text, f_code):    #func_code=00003
	"""[DEPRICATED] [STILL WORKS] removes ascii charecters from a string 

	test: text to remove non ASCII

	f_code: The function Code called this funtion"""
	try:
		return ''.join([i if ord(i) < 128 else '' for i in text])
	except Exception as e:
		print("Failed to remove non-ascii charecters from string.\nError code: 00003x",f_code,'\nPlease inform the author.')
		leach_logger('00003x-1||'+e.__class__.__name__+('||%s||'%str(e))+f_code+'||'+text)

def remove_non_uni(text, f_code, types= 'str'):    #func_code=00018
	try:
		if type(text)==str:
			text =text.encode('utf-8', 'ignore')
			if types=='bin': return text
			return text.decode('utf-8')
		if types=='bin': return text.decode('utf-8','ignore').encode("utf-8")
		return text.decode('utf-8','ignore')
	except Exception as e:
		print("Failed to remove non-Unicode charecters from string.\nError code: 00018x",f_code,'\nPlease inform the author.')
		leach_logger('00018x-1||'+e.__class__.__name__+('||%s||'%str(e))+f_code+'||'+types+'||'+text)

def header_():    #func_code=00004
	"""returns a random header from header_list for requests lib"""
	return( {'User-Agent':random_choice(header_list)})

def install(pack, alias=None):    #func_code=00005
	"""Just install package

	pack: the name the libraby (beautifulsoup4, requests)\n
	alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

	if alias == None:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install",'--disable-pip-version-check','--quiet', alias])


import pkg_resources as pkg_r
# installed_pkgs=[pkg.key for pkg in pkg_resources.working_set] # list of installed packages

# print(pkg_resources)

def install_req(pkz):     #func_code=00006
	"""install requirement package if not installed"""
	if pkz not in (pkg.key for pkg in pkg_r.working_set):
		print("Installing missing libraries")
		install(pkz)
		delete_last_line()
	reload(pkg_r)
	if pkz not in (pkg.key for pkg in pkg_r.working_set):
		print('Failed to install and load required Library: "%s"\nThe app will close in 5 seconds'%pkz)
		try: leach_logger('00006||%s||%s'%(pkz, str(check_internet("https://pypi.org", '00006'))))
		except NameError: pass


if no_psutil:
	install_req('psutil') #required to get win sys info
	import Number_sys_conv as Nsys

	start_up_dt = Nsys.compressed_dt()
	no_psutil=False

for i in requirements_all: install_req(i)
#install_req('requests')
#install_req('beautifulsoup4')
#install_req('natsort')


from bs4 import BeautifulSoup as bs
import requests, natsort

if os_name=="Windows":
	for i in requirements_win: install_req(i)    #required in mplay4


def loc(x, os_name='Linux'):    #func_code=00007
	"""to fix dir problem based on os

	x: directory

	os_name: Os name *Linux"""
	if os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')


def writer(fname, mode, data, direc=None, f_code='None', encoding='utf-8'):    #func_code=00008
	"""Writing on a file

		fname: filename,\n
		mode: write mode (w,wb,a,ab),\n
		data: data to write,\n
		dir: directory of the file, empty for current dir *None,\n
		func_code: (str) code of the running func *empty string,\n
		encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""
	#func_code='00008'

	# err_logged = False
	if any(i in fname for i in ('\\|:*"><?')):
		leach_logger('00008x1||%s'%fname)
		fname=fname.replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')

	try:
		if direc == None:
			if 'b' not in mode:
				with open(fname, mode, encoding=encoding) as file:
					file.write(data)
			else:
				with open(fname, mode) as file:
					file.write(data)
		else:
			locs=loc(direc, 'Linux')
			if any(i in locs for i in ('\\|:*"><?')):
				leach_logger('00008x2||%s'%locs)
				locs=locs.replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-').replace('\\','-')

			if os_isdir(locs):
				if locs.endswith('/'):
					if 'b' not in mode:
						with open(loc(locs + fname), mode, encoding=encoding) as f:
							f.write(data)
					else:
						with open(loc(locs + fname), mode) as f:
							f.write(data)
				else:
					if 'b' not in mode:
						with open(loc(locs + '/' + fname), mode, encoding=encoding) as f:
							f.write(data)
					else:
						with open(loc(locs + '/' + fname), mode) as f:
							f.write(data)
			else:
				try:
					makedirs(locs)
				except FileExistsError: pass
				except Exception as e:
					if e.__class__.__name__== "PermissionError":
						_temp= ''
						_temp2= locs.split('/')
						_temp3= 0
						while True:
							_temp+= _temp2[_temp3]+'/'
							if not os_isdir(_temp): break
						leach_logger('00008x101||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, _temp))
						del _temp, _temp2, _temp3
						# err_logged = True
					raise e
				writer(fname, mode, data, locs, f_code)
	except Exception as e:
		if e.__class__.__name__== "PermissionError":
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: %sx101'%f_code)
			leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
			raise LeachPermissionError
		else:
			leach_logger('00008x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc,str(e)))
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: 00008x'+f_code)
			raise e



def hdr(header, f_code=''):    #func_code=00009
	"""returns the index of a header"""
	try:
		return str(header_list.index(header['User-Agent']))
	except ValueError:
		print("DATA CORRUPTION found\nError code: 00009x"+f_code)

		leach_logger('00009x'+f_code+'||'+ str(e)+'||'+header)
		return str((-1, header))

	except Exception as e:
		print("Some error occured caused, possible cause: DATA CORRUPTION\nError code: 00009x"+f_code)

		leach_logger('00009x-1||'+'||' +f_code+e.__class__.__name__+'||'+ str(e)+'||'+header)
		return str((-1, header))


def leach_logger(io, key='lock'):   #func_code=0000A
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the begning)

	io: the log message\n
	key: salt text"""
	try:
		while True:
			try:
				try:
					_key="Asuna"
					salt = hashlib_sha1(key.encode()).hexdigest()
					writer('userlog.leach', 'ab', encrypt(salt+('%s||'%Nsys.compressed_dt())+str(process_id)+'||'+io+'||',_key).encode('utf-8')+b'\n','data','00008')
					break
				except EOFError: pass
				except KeyboardInterrupt: pass
			except EOFError: pass
			except KeyboardInterrupt: pass

	except EOFError: leach_logger(io, key='lock')
	except KeyboardInterrupt: leach_logger(io, key='lock')


#################### CONNECT TO THE NET FOR THE FIRST TIME #################

def run_server(port, cd=None, f_code= 'None'):      #func_code=0000B
	"""Runs localhost server using python.\n
	the I/O is suppressed

	port : PORT number\n
	cd : the directory to host"""
	
	if cd!=None and type(cd)!=str:
		temp= type(cd)
		try:
			cd= str(cd)
		except:
			cd= '?'
		print("Invalid localhost directory. Please inform the author.\nError code: 0000Bx1")
		leach_logger("0000Bx1||%s||%s||%s"%(temp, cd, f_code))
		time.sleep(5)
		sys_exit()

	elif cd!= None and any(i in cd for i in '\\|:*"><?'):
		print("Invalid localhost directory. Please inform the author.\nError code: 0000Bx2")
		leach_logger("0000Bx2||%s||%s"%(cd, f_code))
		time.sleep(5)
		sys_exit()
	
	elif cd!=None and not os_isdir(cd):
		print(cd,"not found!\nPlease inform the author\nError code: 0000Bx3")
		leach_logger("0000Bx3||"+cd+'||'+f_code)
		time.sleep(5)
		sys_exit()

	try:
		if check_internet("http://localhost:%i"%port, '1000B', timeout=2)==False:
			if cd!=None:
				server_code = subprocess_Popen(['python', '_server000_.py', str(port), '-d', cd], 
				stdin=open(os_devnull), start_new_session=True, stdout=subprocess_DEVNULL, stderr=subprocess_DEVNULL)
				
			else:
				server_code = subprocess_Popen(['python', '_server000_.py', str(port)], 
				stdin=open(os_devnull), start_new_session=True, stdout=subprocess_DEVNULL, stderr=subprocess_DEVNULL)
			
			return server_code
		else: return 0
	except EOFError:
		pass
	except KeyboardInterrupt:
		pass



def _connect_net():      #func_code=0000C
	"""connects to the internet and returns the users global ip"""
	global user_net_ip
	current_header=header_()
	try:
		# gfh= time.time()
		user_net_ip=requests.get('https://api.myip.com/',headers=current_header, timeout=3).content.decode()
		# print(time.time()-gfh)#return [True, '0']
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
		print("\033[1;31;40mError code: 605x1\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x1||%s||%s"%(hdr(current_header,'0000C'), e.__class__.__name__), 'lock')
		time.sleep(5)
		exit(0)
	except Exception as e:
		print(e.__class__.__name__, "occured. Please inform the Author.\nError code: 0000Cx-1(%s)"%e.__class__.__name__)
		leach_logger("0000Cx-1||"+hdr(current_header,'0000C')+'||%s||%s'%(e.__class__.__name__, str(e)), 'lock')
		time.sleep(5)
		exit(0)


def run_in_local_server(port, host_dir=''):     #func_code=0000D
	"""opens a directory or a file in localhost server using browser

	port : port number\n
	host_dir : desired file or folder directory"""

	webbrowser.open_new_tab('http://localhost:%i/%s'%(port, host_dir))


def import_paste():      #func_code=0000E
	"""will import the upload host lib here"""
	try:pass
		#from pastebin import send_paste
		#current_header index=1
	except requests.exceptions.ConnectionError:
		print("\033[1;31;40mError code: 605x2\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x2||header_index=1", 'lock')
		time.sleep(5)
		exit(0)





	# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

	# print(external_ip)
import_paste_t=Process(target=import_paste)

import_paste_t.start()

boss=0


'''def go_prev_dir(link):    #func_code=0000E
	"""returns the previous path str of web link or directory\n
	**warning: returns only in linux directory format"""
	link=loc(link,'Linux')
	if link.endswith('/'):
		return '/'.join(link[:-1].split('/')[:-2])+'/'
	# x=link.split('/')
	else:
		return '/'.join(link.split('/')[:-2])+'/'
'''


_VERSION="5.50001"

parser='html.parser'
img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')


who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ['https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3']
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yeap', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yeap', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yeap')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "Sorry,  I can't understand what you are saying. Just type yes or no.   "

user_list=['bec6113e5eca1d00da8af7027a2b1b070d85b5ea','eb23efbb267893b699389ae74854547979d265bd']

sp_arg_flag={'disable dl cancel' : False,
			 'disable dl get' : False}

g_mode=False
# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
def safe_input(msg='', input_func=input):     #func_code=0000F
	sys_write(str(msg))
	try:
		try:
			try:
				box= input_func('')
				return box
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
			except LeachICancelError:
				leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError
	except EOFError:
			raise LeachICancelError
	except KeyboardInterrupt:
		raise LeachICancelError

def asker(out='', default=None, True_False=(True, False), extra_opt=tuple(), extra_return=tuple()):      #func_code=00010
	"""asks for yes no or equevalent inputs
	out: printing text to ask tha question *empty string
	default: default output for empty response *None
	True_False: returning data instead of true and false *(True, False)"""
	print(out,end='')

	if len(extra_opt)!=len(extra_return):
		print('Additional options and Additional return data don\'t have equal length')
		raise IndexError

	Ques2 = safe_input().lower()
	if default!= None and Ques2=='':
		return default
	#Ques2 = Ques2
	while Ques2 not in cond+extra_opt:
		print(condERR)
		Ques2 = safe_input().lower()
		#Ques2 = Ques2
	if Ques2 in cond:
		if Ques2 in yes:
			return True_False[0]
		else:
			return True_False[1]
	else:
		return extra_return[extra_opt.index(Ques2)]



def get_file_name(directory, mode= 'dir'):      #func_code=00011
	"""[takes a file directory and returns the last last part of the dir (can be file or folder)

	directory: the file directory, only absolute path to support multiple os
	mode: url or file directory
	"""
	if mode=='url':
		fragment_removed = directory.split("#")[0]  # keep to left of first #
		query_string_removed = fragment_removed.split("?")[0]
		scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
		if scheme_removed.find("/") == -1:
			return ""
		return os_basename(scheme_removed)
	elif mode=='dir':
		return os_basename(directory)
	else:
		raise ValueError



def get_file_ext(directory, mode='dir', no_format='noformat'):      #func_code=00012
	"""to get the extension of a file directory

	directory: file directory relative or direct\n
	no_format: returning format if no file extention was detected *noformat"""
	temp= get_file_name(directory, mode)
	if len(temp.split('.'))==1:
		return no_format
	else:
		return temp.split('.')[-1]



def reader(direc, read_mode='r'):      #func_code=00013
	if type(read_mode)!=str:
		print("Invalid read type. Mode must be a string data")
		raise TypeError
	if read_mode in ['w', 'wb', 'a', 'ab', 'x', 'xb']:
		print("\033[1;31;40mInvaid read mode:\033[0m\033[1m %s is not a valid read mode.\nTry using 'r' or 'rb' based on your need\033[0m")
		raise LeachKnownError
	if 'b' in read_mode:
		read_mode='rb'
	else:
		read_mode = 'r'
	with open(loc(direc), read_mode) as f:
		return f.read()
#print(os_isdir('data/leach_projects/Sao manga rip'))

	# print(io==decrypto.decrypt(encrypt(io,key),key))


# print(requests.get('https://ident.me',headers=headers).content)
# user_net_ip=requests.get('https://ident.me',headers=headers).content.decode()
# print(user_net_ip)



def _version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename,_latest_size, server_link):      #func_code=00014
	print("An update available v"+_latest_version+"("+_latest_size+"), Do you want to update? ")
	try:
		reply= safe_input()
	except LeachICancelError:
		print('\n\u001b[33;1mCancellation command entered. Skipping uppdate!\u001b[0m\n')
		leach_logger("update-prompt||f-Exit-ask")
		return 0
	if reply:
		print('\nConnecting...')
		leach_logger("201||"+str(_latest_version)+'||'+_latest_link+'||'+server_version,'lock')
		update_x= time.time()
		
		#update_filename='Web Leach v4.1'
		#import urllib

		# Copy a network object to a local file
		#urllib.urlretrieve(_latest_link, 'data/.temp/'+update_filename+'.zip')
		current_header=header_()

		try:
			update_response = requests.get(_latest_link, stream=True,headers=current_header)
		except Exception as e:
			update_response= False
			leach_logger('202||%s||%s||err:%s'%(_latest_link, hdr(current_header,'00014'), str(e.__class__.__name__)),'lock')

		delete_last_line()
		if update_response!=None:
			update_total_length = update_response.headers.get('content-length')
			with open('data/.temp/'+_latest_filename+'.zip', "wb") as f:
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
			leach_logger("203||"+str(_latest_version))
			print("\nUnzipping...")
			server_fucked = False
			with ZipFile('data/.temp/'+_latest_filename+'.zip') as zf:
				if list(zf.namelist()) != [_latest_filename+'.exe']:
					server_fucked = True
					fucked_list=list(zf.namelist())

				else:
					zf.extractall(pwd=b'lock')
			
			if server_fucked:
				leach_logger("204||"+_latest_link+'||'+_latest_version+'||'+server_link+'||'+str(fucked_list))
				remove(_latest_filename+'.zip')
				raise LeachCorruptionError

			leach_logger("205||"+str(_latest_version))

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
				leach_logger("206")
				remove(_latest_filename+'.zip')
				leach_logger('207')

				time.sleep(7)
				exit(0)
			else:
				print ("\033[1;31;40mMD5 verification failed!.\033[0m \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
				leach_logger('208||%s'%md5_returned+"||"+_latest_link+'||'+_latest_version+'||'+server_link)
				remove(_latest_filename+'.zip')
				remove(_latest_filename+'.exe')
				raise LeachCorruptionError
				# remove('')
		elif update_response!=False:
			print("Failed to connect to the host server.\nPlease inform the author!!\nError code 202")
			leach_logger('202||%s||%s||code:%s'%(_latest_link, hdr(current_header,'00014'), str(update_response.status_code)),'lock')



_server_version = "5.4"

def god_mode():      #func_code=00015
	global _server_version
	if os_isdir('data/projects'): rename('data/projects', 'data/leach_projects')
	if os_isdir('./projects'): rename('./projects', './Download_Projects')

	if os_name=='Windows':
		current_header=header_()
		try:
			if not os_isfile('data/.temp/who_r_u.mp3'):
				file=requests.get(who_r_u, headers=current_header)
				if file:
					writer('who_r_u.mp3','wb',file.content,'data/.temp','00015')
				else:
					raise requests.exceptions.ConnectionError

		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
			print("\033[1;31;40mError code: 605x3\nNo internet connection!\033[0m\nRunning offline mode")
			leach_logger("605x3||%s||%s||%s"%(hdr(current_header,'00015'),who_r_u, e.__class__.__name__), 'lock')
			return 'offline'
	current_header=header_()
	# cloud_data_link = 'htt://jhhgj.com'
	try:
		file=requests.get(cloud_data_link, headers=current_header)
		if file:
			writer('updateL.ext','wb',file.content,'data/.temp','00015')
			exec(decrypt(open('data/.temp/updateL.ext').read(), "lock").strip())

			# _server_version = server_version
			#print(decrypt(open('data/.temp/update.ext').read().strip(), "lock").strip())
			#AssertionErrorprint(server_version)
			# time.sleep(500)
		else:
			print("\033[1;31;40mError code: 605x4\nNo internet connection!\033[0m\nRunning offline mode in 3 seconds")
			leach_logger("605x4||%s||%s||%s"%(hdr(current_header,'00015'), cloud_data_link, str(file.status_code)), 'lock')
			time.sleep(3)
			return 'offline'

		#remove('data/.temp/update.ext')
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
		print("\033[1;31;40mError code: 605x4\nNo internet connection!\033[0m\nRunning offline mode in 3 seconds")
		leach_logger("605x4||%s||%s||%s"%(hdr(current_header,'00015'), cloud_data_link, e.__class__.__name__), 'lock')
		time.sleep(3)
		return 'offline'
	except Exception as e:
		print(e.__class__.__name__,": Unknown error occured. Error code 00015x-1\nPlease inform the author.")
		leach_logger("00015x-1||%s||%s||%s"%(e.__class__.__name__,str(e),hdr(current_header,'00015')), 'lock')
		time.sleep(5)
		exit(0)


	try:
		file=requests.get(cloud_data_link_global, headers=current_header)
		if file:
			writer('updateG.ext','wb',file.content,'data/.temp','00015')
			exec(decrypt(open('data/.temp/updateG.ext').read(), "lock").strip())

			# _server_version = server_version
			#print(decrypt(open('data/.temp/update.ext').read().strip(), "lock").strip())
			#AssertionErrorprint(server_version)
			# time.sleep(500)
		else:
			print("\033[1;31;40mError code: 605x4\nNo internet connection!\033[0m\nRunning offline mode in 3 seconds...")
			leach_logger("605x4||%s||%s||%s"%(hdr(current_header,'00015'), cloud_data_link_global, str(file.status_code)), 'lock')
			time.sleep(3)
			return 'offline'

		#remove('data/.temp/update.ext')
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
		print("\033[1;31;40mError code: 605x4\nNo internet connection!\033[0m\nRunning offline mode in 3 seconds...")
		leach_logger("605x4||%s||%s||%s"%(hdr(current_header,'00015'), cloud_data_link, e.__class__.__name__), 'lock')
		time.sleep(3)
		return 'offline'
	except Exception as e:
		print(e.__class__.__name__,": Unknown error occured. Error code 00015x-1\nPlease inform the author.")
		leach_logger("00015x-1||%s||%s||%s"%(e.__class__.__name__,str(e),hdr(current_header,'00015')), 'lock')
		time.sleep(5)
		exit(0)

	if float(_VERSION)<float(_latest_version):
		_version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename,_latest_size, cloud_data_link)
	return 'online'

#def upload_paste(data,f_name):
"""if True:
	api_dev_key= "f7e117d452fed3df6e5cc1ea2eee658a"
	#my_key = PastebinAPI.generate_user_key( ,api_dev_key=api_dev_key, username="DarKnighTitan", password="147852369aA..")
	x=PastebinAPI.paste(self,api_dev_key=api_dev_key, api_paste_code="hello world", api_user_key = None, paste_name = "hi", paste_format = None, paste_private = None, paste_expire_date = None)
	print(x)
"""


if os_name=='Windows':
	import mplay4


def log_in():      #func_code=00016
	global user_name
	if boss!=1:
		userhash=0
		br=0
		while True:
			try:
				user_name=safe_input("Enter username: ")
			except LeachICancelError:
				print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
				leach_logger("0x1||00016||Login exit")
				exit(0)
			# print(user_list)
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
					# mplay4.set_win_vol(60)
					mplay4.load('data/.temp/who_r_u.mp3').play()
				time.sleep(5)
				if os_name=='Windows':
					mplay4.set_win_vol(ex)
	else:
		userhash='eb23efbb267893b699389ae74854547979d265bd'


	if not os_exists('data/projects.db'):
		writer('projects.db','a','','data','00016')
	if userhash=='eb23efbb267893b699389ae74854547979d265bd':
		g_mode='Asuna'
	return userhash


try:
	exec(open('make_html.py').read(), globals())      # f_code= 40000
except Exception as e:
	print("Some error occured while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
	leach_logger('40000x-1||' +str(e.__class__.__name__)+'||'+ str(e))
	time.sleep(5)
	exit()


def check_internet(link, f_code, timeout=None):       #f_code=00017
	"""Check if the connection is available or not

	link: link to check for connection status"""
	current_header=header_()
	try:
		if timeout==None: r=requests.head(link, headers=current_header)
		else: r=requests.head(link, headers=current_header, timeout= timeout)
		
		if r:
			return True
		else:
			leach_logger('00017||%s||%s||%s||%s'%(link, hdr(current_header, '00017'), f_code, str(r.status_code)))
	except (requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout) as e:
		leach_logger('00017||%s||%s||%s'%(link, hdr(current_header, '00017'), f_code))
		return False


class web_leach:

	def __init__(self):      #func_code= 10001
		"""initialize variables on every start of a project"""
		#global overwrite_bool, partial_do_all, homepage, existing_found, dimention,sp_flags, done,indx_count, sp_extension, errors

		self.total=0	  # number of total files
		self.break_all= False	  # trigger to stop the download
		self.done=0	  # total downloaded files
		self.errors=0	# number or errors
		self.sp_extension=''	# if custom file extension needed to be added with the downloaded file names
		self.sp_flags=[]	# list of flags for special downloads like mangafreaks
		self.overwrite_bool= True	# bool for wheather replace the duplicate file or not
		self.partial_do_all= False	# will use the same detected homepage for every other pages with no home
		"""if partial link found while indexing, then the program will find the
		homepage and ask if it will be used for all other partial links or not"""

		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""

		self.homepage= ''	# just assigning the homepage variable
		self.indx_count= 0	# counts the number of indexed links
		self.all_list = []	# assigning a set so that duplication can be cancelled, will
		self.existing_found=False	# indicates if valid existing project is found
		self.dl_done=False	# indicates if the project scrapping was done or not
		self.sequence=True	# indicates if the files will be sorted or not
		self.update= False	# indicates if the project is getting an update or not
		self.corruptions=[]	# list of corruptions in project data if there's any or empty
		self.sub_dirs=[]	# list of sub directories on the project folder
		self.homepage_searcher=re_compile('(https?://[^/]*)')	# compiled regex tool for getting homepage
		self.Project=''	# project name (case insensitive *need to work on it)
		self.main_link=''	# the main link
		self.file_types= set()	# set of file extensions to be downloaded
		self.file_starts=''	# (str) each files must start with (used regex)
		self.link_startswith=''	# (str) each sublink must start with
		self.error_triggers=[]	# 0 to 9 the number of tasks
		self.open_file = False
		self.dl_chunks=0
		self.from_file= False
		self.page_error = 0
		self.re_error = 0   # number of errors after retrying errors

		self.special_starts ={'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://w[\d]+\.mangafreak.net/(M|m)anga/',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https://w[\d]+\.mangafreak.net/Read1_(.+)'}


		self.port= (int(ush, 16) % (6000 - 4000 + 1)) + 4000
		self.run_server_t('Download_projects')

	def catch_KeyboardInterrupt(self, func, *args):       #func_code= 11001
		try:
			try:
				try:
					box= func(*args)
					return box
				except EOFError:
					raise LeachICancelError
				except KeyboardInterrupt:
					raise LeachICancelError
				except LeachICancelError:
					leach_logger('0x0||11001||input exit code L&infin;ping for unknown reason')
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError



	def run_server(self, cd=None):      #func_code= 10010
		if not death:
			self.server_code = run_server(self.port, cd)

	def run_server_t(self, cd = None):
		self.server_code= None
		Process(target= self.run_server, args = (cd,)).start()

	def distribute(self, lists,task_id,is_error=False):      #func_code= 10002
		"""run downloads in this function from a list of download links
		lists: download links list
		task_id: task id (int) to keep resume point stored
		is_eror: if the funtion is running to retry the failed files *False"""
		#global total,done, errors, sp_flags, sp_extension, overwrite_bool
		global err_hdr_list
		task_id=str(task_id)
		res=0
		if self.existing_found:
			if os_exists('data/leach_projects/'+self.Project+'/t'+task_id+'.txt'):
				res=eval(open('data/leach_projects/'+self.Project+'/t'+task_id+'.txt').read().strip()) # resume point of the list (index # int)
		self.done+=res

		

		time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:
			if self.break_all== True: return 0
			download=True	# switch for download it or not
			if is_error:
				i=list(j)
			else:
				i=list(self.all_list2[j])

			if lists.index(j)>=res:
				current_header=header_()	# randomises header from list on every download to at least try to fool server
				try:
					if self.overwrite_bool==False:
						if self.sub_dirs[i[1]].endswith('\\') or self.sub_dirs[i[1]].endswith('/'):
							if os_isfile('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+get_file_name(i[0])+self.sp_extension): download=False
						else:
							if os_isfile('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension): download=False
					if download:
						if sp_arg_flag['disable dl get']==True:
							file=requests.head(i[0], headers= current_header, timeout=2)
						else:
							file=requests.get(i[0], headers= current_header, timeout=2, stream= (not is_error))
						if file:
							if sp_arg_flag['disable dl get']!=True:
								# clear the file
								writer(get_file_name(i[0])+self.sp_extension,'wb',b'','Download_projects/'+self.Project+'/'+self.sub_dirs[i[1]], '10002')
								loaded_file = open('Download_projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension, 'wb')
								for chunk in file.iter_content(chunk_size=8192):
									if not self.break_all:
										loaded_file.write(chunk)
										self.dl_chunks+=1
									
									else:
										loaded_file.close()
										if os_exists('Download_projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension):
											remove('Download_projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension)

										return 0
								loaded_file.close()
								


								if 'dl unzip' in self.sp_flags:
									if os_isdir('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')==False:
										makedirs('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')
									with ZipFile('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension) as zf:
										zf.extractall(path='Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0]))
									if 'del dl zip' in self.sp_flags:
										remove('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension)

							writer('t'+task_id+'.txt', 'w',str(res),'data/leach_projects/'+self.Project,'10002')

							delete_last_line()
							#print(done)
							percent=floor(((self.done+1)/self.total)*32)
							
							print('Downloaded ['+'\u001b[7m'+(' '*percent)+'\u001b[0m'+' '*(32-percent)+'] ['+str(self.done+1) + '/'+str(self.total)+']',task_id)
							res+=1
							self.done+=1
							if is_error:
								self.errors-=1
						else:
							if is_error==False:
								writer('errors.txt', 'a',str(i+[hdr(current_header,'10002')])+'\n','data/leach_projects/'+self.Project,'10002')
								err_hdr_list += Counter([hdr(current_header,'10002')])
								writer('err_header.txt', 'w', str(err_hdr_list),'data/','10002')
								self.errors+=1
								

							else:
								self.re_error +=1
								if self.re_error<4: 
									print("Failed to download from '%s'"%i[0])
								else:
									if self.re_error!=4:delete_last_line()
									print("And %i others"%(self.re_error-3))
								writer('left_errors.txt', 'a',str(i+[hdr(current_header,'10002'),"Error dl"])+'\n','data/leach_projects/'+self.Project,'10002')
								leach_logger('10002x1||'+self.Project+'||'+hdr(current_header,'10002')+'||'+str(i)+'||'+str(file.status_code), user_name)
							continue
					else:
						writer('t'+task_id+'.txt', 'w',str(res),'data/leach_projects/'+self.Project,'10002')

						delete_last_line()
						#print(done)
						percent=floor(((self.done+1)/self.total)*32)

						print('Downloaded ['+'\u001b[7m'+(' '*percent)+'\u001b[0m'+' '*(32-percent)+'] ['+str(self.done+1) + '/'+str(self.total)+']',task_id)
						res+=1
						self.done+=1
						if is_error:
							self.errors-=1
				except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout) as e:
					if is_error==False:
						writer('errors.txt', 'a',str(i+[hdr(current_header,'10002')])+'\n','data/leach_projects/'+self.Project,'10002')

						err_hdr_list += Counter([hdr(current_header,'10002')])
						writer('err_header.txt','w', str(err_hdr_list),'data/','10002')
						self.errors+=1


					else:
						self.re_error +=1
						if self.re_error<4: 
							print("Failed to download from '%s'"%i[0])
						else:
							if self.re_error!=4:delete_last_line()
							print("And %i others"%(self.re_error-3))
						writer('left_errors.txt', 'a',str(i+[hdr(current_header,'10002'),"Error dl"])+'\n','data/leach_projects/'+self.Project,'10002')
						leach_logger('10002x1||'+self.Project+'||'+hdr(current_header,'10002')+'||'+str(i)+'||'+str(e.__class__.__name__), user_name)
				except BadZipFile:
					if os_isfile('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension):
						remove('Download_Projects/'+self.Project+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension)


					if is_error==False:
						writer('errors.txt', 'a',str(i+[hdr(current_header,'10002')]+["Bad zip"])+'\n','data/leach_projects/'+self.Project,'10002')
						self.errors+=1
					else:
						self.re_error +=1
						if self.re_error<4: 
							print("Failed to download from '%s'"%i[0])
						else:
							if self.re_error!=4:delete_last_line()
							print("And %i others"%(self.re_error-3))
						print("It seems every time it downloads a broken or unknown zip from '%s' (possible cause password protected zips, if yes extract them manually)"+i[0])
						writer('left_errors.txt', 'a',str(tuple(i)+(hdr(current_header,'10002'),"Bad zip"))+'\n','data/leach_projects/'+self.Project,'10002')

						leach_logger('10002x2||'+self.Project+'||'+hdr(current_header,'10002')+'||'+str(i), user_name)

		self.error_triggers+=[int(task_id)]


	def list_writer(self, link, list_range,special=None, soup=None):      #func_code= 10003
		"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list
		link: single link or a list of links to index
		#types: file types to index in all_list
		file_link_starts: (regex) srting that will check and if the file links starts with
		list_range: a range objet containing the index of the links
		special: gives a headsup that if the link is from any special cases *None
		soup: a response soup object that will speed the indexing a li'l bit up *None"""
		# global all_list, sub_dirs, indx_count

		start_checker=re_compile('^'+self.file_starts)

		if special!=None:
			if special.startswith('nhentai'):
				if special=="nhentai.xxx":
					xxx_search= re_compile("https://cdn.nhentai.xxx/g/\d+/\d*t..*")
					for imgs in soup.find_all('img'):
						img_link=imgs.get('data-src')
						if img_link== None:
							img_link=imgs.get('src')
						if xxx_search.search(img_link)!=None:
							self.all_list.append((''.join([img_link.rpartition('t')[0], img_link.rpartition('t')[2]]), 0))
							img_link.rpartition('t')[1]
				elif special=="nhentai.to":
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
							self.all_list.append((img_link, 0))


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
							self.all_list.append((img_link, 0))

		else:
			dir_len=len(self.sub_dirs)
			for i in list_range:
				if self.break_all:
					return 0

				if self.sub_dirs[i][-1]=='/':
					self.sub_dirs[i]=self.sub_dirs[i][:-1]
				self.sub_dirs[i]=self.sub_dirs[i].split('/')[-1]

				try:
					current_header=header_()
					page = requests.get(link[i],headers= current_header)
					if not page:
						print('\nFailed to connect "%s"\nPlease try the update option after downloading\n\n'%link[i])
						leach_logger("10003x1||"+self.Project+'||'+hdr(current_header, '10003')+'||'+link[i]+'||'+str(page.status_code)+'||'+'None')
						continue
					soup=bs(page.content, parser)
				except (requests.exceptions.ChunkedEncodingError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
					print('\nFailed to connect "%s"\nPlease try the update option after downloading\n\n'%link[i])
					leach_logger("10003x1||"+self.Project+'||'+hdr(current_header, '10003')+'||'+link[i]+'||'+e.__class__.__name__+'||'+str(e))
					continue

				for imgs in soup.find_all('img'):
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					img_link=img_link.strip()
					# ##$##########
					# print(img_link)
					if img_link.startswith('//'): img_link='https:'+img_link
					if img_link.startswith('/'):
						img_link=self.homepage_searcher.search(link[i]).groups()[0]+img_link

					if img_link.startswith('../'):
						temp_home=link[i]
						while img_link.startswith('../'):
							temp_home= go_prev_dir(temp_home)
							img_link=img_link.replace('../','',1)
						img_link=temp_home+img_link
					
					if '//' not in img_link:
						temp=self.homepage_searcher.search(link[i]).group()
						if temp.endswith('/'):
							if img_link.startswith('/'): img_link=temp+img_link[1:]
							else: img_link=temp+img_link
						else:
							if img_link.startswith('/'): img_link=temp+img_link
							else: img_link=temp+'/'+img_link

					if start_checker.search(str(img_link)) !=None and get_file_name(img_link, 'url').endswith(self.file_types):
						self.all_list.append((img_link.split("#")[0].split("?")[0],i))
				delete_last_line()
				print('Indexed ['+ str(self.indx_count+1) + '/'+str(dir_len)+'] '+link[i])
				self.indx_count+=1
	


	if os_name=='Windows':
		def play_yamatte(self, vol):      #func_code= 10004
			"""just for parody"""
			writer('yamatte.mp3','wb',requests.get(random_choice(yamatte), headers=header_()).content,'data/.temp','10004')
			ex=mplay4.ex_vol
			mplay4.set_win_vol(vol)
			mplay4.load('data/.temp/yamatte.mp3').play()
			time.sleep(8)
			remove('data/.temp/yamatte.mp3')
			mplay4.set_win_vol(ex)
		play_yamatte_t=Process(target=play_yamatte, args=[80])




	def nhantai_link(self,link):      #func_code= 10005
		"""checks if the link is nhentai link and returns the available link and the title of the doujin
		else it will return 0"""
		# global sub_dirs
		if re_search(self.special_starts['nh_sc'], link):
			self.main_link= 'https://nhentai.net/g/'+str(re_search(self.special_starts['nh_sc'], link).group(1))
		link=self.main_link
		code=re_search('https://nhentai.[^/]*/g/((\d)*)',link)

		if code==None:
			return False, False
		code=code.groups()[0]

		current_header=header_()
		try:
			link_y='https://nhentai.net/g/'+code+'/'
			page = requests.get(link_y,headers=current_header, timeout=2)
			if page:
				site=".net"
			else:
				raise requests.exceptions.ConnectionError
				#link_y='https://nhentai.to/g/'+code+'/'
				#page = requests.get(link_y,headers=headers)
				#site='.to'
				# site="https://nhentai.net/"
				# thumb_pattern="https://t.nhentai.net/galleries/\d/\dt."

		except (requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema):
			leach_logger("606x1||%s||%s||%s"%(self.Project, link, hdr(current_header,'10005')), user_name)
			print('nhentai.net server is not reachable, trying proxy server...')
			link_y='https://nhentai.xxx/g/'+code+'/'
			# link_y='https://nhentai.to/g/'+code+'/'
			try:
				page = requests.get(link_y,headers=header_())
				if page:
					site=".xxx"
				else:
					raise requests.exceptions.ConnectionError
			except (requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema):
				delete_last_line()
				print("\033[1;31;40mError code: 606x2\nLink not found, Please recheck the link and start a new project\033[0m")
				leach_logger("606x2||%s||%s||%s"%(self.Project, link, hdr(current_header,'10005')), user_name)
				delete_last_line()
				print('nhentai.net server is not reachable, trying proxy server...(2)')
				link_y='https://nhentai.to/g/'+code+'/'
				# link_y='https://nhentai.to/g/'+code+'/'
				try:
					page = requests.get(link_y,headers=header_())
					if page:
						site=".to"
					else:
						raise requests.exceptions.ConnectionError
				except (requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema):
					# delete_last_line()
					print("\033[1;31;40mError code: 606x3\nLink not found, Please recheck the link and start a new project\033[0m")
					leach_logger("606x3||%s||%s||%s"%(self.Project, link, hdr(current_header,'10005')), user_name)
					return False, False

			
		self.file_types= img
		if page:
			soup=bs(page.content, parser)

			title=remove_non_uni(soup.find(id='info').find('h1').get_text(),'10005')
			print("Indexing from",title)
			self.file_starts=''
			self.list_writer(code,0,'nhentai'+site,soup)
			self.sub_dirs.append(parse.unquote(html_unescape(title)).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))
			# print(self.sub_dirs)
			return link_y, title
		else:
			print("\033[1;31;40mError code: 606x2\nLink not found, Please recheck the link and start a new project\033[0m")
			leach_logger("606x2||%s||%s||%s"%(self.Project, link, hdr(current_header,'10005')), user_name)
			return False, False


	def check_sp_links(self,link, sp=None):      #func_code= 10006
		"""checks if the link has any special case and any specific spcial case
		link: link of the project
		sp: specifies the special case check *None"""


		'''
		self.special_starts ={'nh':'https://nhentai\.(net)|(to)/g/',
		'mangafreak':'https://w[\d]+\.mangafreak.net/(M|m)anga/',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https://w[\d]+\.mangafreak.net/Read1_(.+)'}
		'''

		if re_search(self.special_starts['nh_sc'], link):
			link= 'https://nhentai.net/g/'+str(re_search(self.special_starts['nh_sc'], link).group(1))
		if re_search(self.special_starts['mf_read'], link):
			link= 'https://w11.mangafreak.net/Manga/'+str(re_search(self.special_starts['mf_read'], link).group(1))
		if re_search(self.special_starts['mf_sc'], link):
			link= 'https://w11.mangafreak.net/Manga/'+str(re_search(self.special_starts['mf_sc'], link).group(1).replace(' ', '_'))

		if type(sp)== list:
			return any([self.check_sp_links(link, sp=i) for i in sp])
		if sp=='nh':
			if re_search('^'+self.special_starts['nh'], link)!=None:
				return True
			else:
				return False
		elif sp=="mangafreak":
			if re_search('^'+self.special_starts['mangafreak'], link)!=None:
				return True
			else:
				return False
		elif sp=="pinterest":
			if re_search('^'+self.special_starts['pinterest'], link)!=None:
				return True
			else:
				return False
		elif sp=="pinterest-pin":
			if re_search('^'+self.special_starts['pinterest']+'pin/\d+$', link)!=None:
				return True
			else:
				return False
		elif sp==None:
			for i in self.special_starts.values():
				if re_search('^'+i, link)!=None:
					return True
			return False
		else:
			print("INvalid arg!\n    pLEaSe REcHECK\n=======> %s <=======\n WITH\n-------> %s <-------"%(self.main_link, str(sp)))
			raise ValueError

	def mangafreak_link(self,link):      #func_code= 10007
		"""checks if the link is a mangafreak link and makes indexing easier. but one limitation is it can't find weather the link is valid or not and cannot get the actual file links.
		#: user needs to manually last chapter"""
		#global sub_dirs, all_list, sp_extension


		if re_search(self.special_starts['mf_sc'], link):
			link= 'https://w11.mangafreak.net/Manga/'+str(re_search(self.special_starts['mf_sc'], link).group(1))
			self.main_link= link
		inp = re_search('https://w11.mangafreak.net/(M|m)anga/([^\?]*)',link)

		if inp!=None:
			title=inp.group(2)
			self.sp_flags.append('mangafreak')

		else:
			return ""

		last_ch=-1
		while True:
			try:
				try:
					if last_ch<1:
						last_ch= int(safe_input("\n\033[32;1m**\033[0mPlease enter the last chapter number: "))
				except LeachICancelError:
					print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
					leach_logger("000||10007||%s||f-Stop||is_mangafreak||did not ans Mangafreak chapter no"%self.Project)
					return 0
				while True:
					try:
						if requests.head("http://images.mangafreak.net:8080/downloads/"+title+'_'+str(last_ch)):
							self.sp_extension='.zip'
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
				try:
					last_ch= int(safe_input("\n\033[31;1m**\033[0mJust enter the last chapter number (like 135): "))
					break
				except LeachICancelError:
					print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
					leach_logger('000||10007||'+self.Project+"||f-Stop||is_mangafreak||tried to ans Mangafreak chapter no||"+str(last_ch))
					return 0


		self.sub_dirs.append('.')
		for i in range(1,last_ch+1):
			self.all_list.append(("http://images.mangafreak.net:8080/downloads/"+title+'_'+str(i),0))

		return "mangafreak.net"

	def pint_link(self):      #func_code= 10005
		"""checks if the link is pinteresst link and indexes the files
		else it will return 0"""

		if self.check_sp_links(self.main_link, 'pinterest'):
			temp= input()
	def retry_errors(self):      #func_code= 10008
		while sorted(self.error_triggers)!=[1,2,3,4,5,6,7,8,9, 10]:
			if self.break_all:
				return 0
			time.sleep(2)

		leach_logger("10008x0||"+self.Project+"||"+str(self.total)+'||'+str(self.errors), user_name)

		if self.errors>0:
			if os_exists('data/leach_projects/'+self.Project+'/errors.txt'):
				with open('data/leach_projects/'+self.Project+'/errors.txt', 'rb') as f:
					err_file=f.readlines()
				if self.break_all:
					return 0
				errs =[]
				for i in err_file:
					if i.strip()!=b'':
						try: errs.append(eval(i.decode())[:2])
						except TypeError: print(i)
                                                        
				#errs= [eval(i)[:2] for i in err_file if i!='']

				self.distribute(errs,11, is_error= True)
			else:
				print("Warning: Error file not found!\nPossible cause: data corruption")
				leach_logger("10008x1||"+self.Project, user_name)
		leach_logger("10008x2||"+self.Project+'||'+str(self.errors), user_name)


		if self.dl_done==False:
			writer(self.Project+'.proj','a','dl_done = True\n','data/leach_projects','10008')
		else: print("\nPlease retry some time later to get higher chances to download some or all %d missing file/s"%self.errors)
		print('\n\nEnter \u001b[1m\u001b[4m\u001b[7m x \033[0m to open the first page\n or just press Enter to continue: ')
		self.dl_done=True
	def data_checkup(self, path = None, proj_name = None):     # f_code = 11000
		if path!=None:
			proj_path=path
			list_path=path[:-5]+'.list'
		else:
			proj_path='data/leach_projects/'+self.Project+'.proj'
			list_path='data/leach_projects/'+self.Project+'.list'
		if os_exists(proj_path) and os_exists(list_path):
			proj_good= True
			try:
				with open(proj_path, 'rb') as f:
					print('db found')
					existing_data=f.read().decode().strip().split('\n')
				try:
					global Project, main_link, link_startswith, file_types, sub_dirs, sp_flags, sp_extension, overwrite_bool, dimention, dl_done, sequence
					dl_done=False
					Project = self.Project
					for i in existing_data:
						exec(i, globals())
					self.main_link= main_link
					self.link_startswith= link_startswith
					self.file_types = file_types
					self.file_starts= file_starts
					self.sub_dirs = sub_dirs
					self.sp_flags = sp_flags
					self.sp_extension = sp_extension
					self.overwrite_bool = overwrite_bool
					self.dimention = dimention
					try:
						self.dl_done = dl_done
					except: pass
					try:
						self.Project = Project
					except:
						if path!=None:
							self.Project=get_file_name(path)[:-5]
					try:
						self.sequence = sequence
					except: sequence= None

					del Project, main_link, link_startswith, file_types, sub_dirs, sp_flags, sp_extension, overwrite_bool, dimention, dl_done, sequence
					proj_good= True
				except Exception as e:
					raise LeachKnownError
			except LeachKnownError:
				#print(existing_data)
				try:
					self.main_link=existing_data[0]
				except:
					self.corruptions+=[1]
					print('\033[1;31;40mCorrupted Data! Error code: 601x1\033[0m')
					proj_good=False
				if proj_good:
					try:
						self.link_startswith=existing_data[1]
					except:
						proj_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x2\033[0m')
						self.corruptions+=[4]

				if proj_good:
					try:
						self.file_types=eval(existing_data[2])
					except Exception as e:
						proj_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x3\033[0m')
						self.corruptions+=[4]

				if proj_good:
					try:
						self.file_starts=existing_data[3]
					except:
						proj_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x4\033[0m')
						self.corruptions+=[4]

				if proj_good:
					try:
						self.sub_dirs=eval(existing_data[4]) #sub directory list
					except:
						proj_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x5\033[0m')
						self.corruptions+=[2]
					try:  #added in v5.0 may not be in older files
						self.sp_flags=eval(existing_data[5])
						self.sp_extension=eval(existing_data[6])
						self.overwrite_bool=eval(existing_data[7])
					except IndexError: pass
				if proj_good:
					try:  #added in v5.1 may not be in older files
						self.dl_done=eval(existing_data[8])
					except IndexError:
						pass


			if proj_good:
				with open(list_path, 'rb') as f:
					try:
						file=f.read().decode()

						if file.strip()=='': raise ValueError
						self.all_list= eval(str(file))
						print('list found')
						list_good= True
					except:
						list_good= False
						print('\033[1;31;40mCorrupted Data! Error code: 601x6\033[0m')
						self.corruptions+=[3]

				#print(x)
			if proj_good and list_good:
				if path!=None:
					self.Project=get_file_name(path)[:-5]
				if self.dl_done:
					print('It seems  the old prject download was complete!!')
					try:
						temp= asker(out='\u29bf Do you want to get updated data from the project link?\n\u29bf If you want make a fresh start with that project name type \u001b[1m\u001b[4m\u001b[7m fresh \033[0m/\u001b[1m\u001b[4m\u001b[7m f \033[0m\n\u29bf To open the project in Browser enter \u001b[1m\u001b[4m\u001b[7m x \033[0m\n\u001b[33;1m  >> \033[0m',extra_opt=('x','fresh', 'f'), extra_return=('run','fresh', 'fresh')) #Do you want make a fresh start with that project name??\n\033[1;33mWarning!\033[0m last project data will be erased\n(downloaded files will be safe, unless the program replaces the files with new ones)\n\033[32m>> \033[0m'):
						if temp=='run':
							if 'mangafreak' in self.sp_flags:
								self.all_list=[]
								self.sub_dirs= [i for i in os_listdir('Download_projects/'+self.Project) if os_isdir('Download_projects/'+self.Project+'/'+i)]
								for i in range(len(self.sub_dirs)):
									for j in os_listdir('Download_projects/'+self.Project+'/'+self.sub_dirs[i]):
										# print(j)
										if os_isfile('Download_projects/'+self.Project+'/'+self.sub_dirs[i]+'/'+j):
											self.all_list.append([j,i])
								# print(self.all_list, self.sub_dirs)
							first_page=make_pages(self.all_list,self.sub_dirs, self.Project, True)
							run_in_local_server(self.port, host_dir='%s/%s.html'%(self.Project, self.Project))
							return 0
					except LeachICancelError:
						print("\n\u001b[33;1mCancellation command entered.\nReturning to main options\u001b[0m")
						leach_logger("000||11000||%s||f-Stop||was_done||don't want to update proj or anything"%(self.Project))
						return 0
					if temp==True:
						self.existing_found= False
						self.update= True
						self.overwrite_bool=False
						leach_logger('11000x2||%s'%self.Project,user_name)
					elif temp=='fresh':
						#print("Okay! Enter a new project name in the next line.")
						
						Project = self.Project
						self.__init__()
						self.Project= Project
						self.existing_found= False
						leach_logger('11000x1||%s'%self.Project,user_name)

					elif temp== False: return 0

						#remove('data/leach_projects/'+self.Project+'/')
					del temp
				else:
					try:
						temp= asker("\u29bf Do you want to resume the Project '%s'?\nyes/y to resume\n\u29bf \u001b[1m\u001b[4m\u001b[7m fresh \033[0m/\u001b[1m\u001b[4m\u001b[7m f \033[0m to Start fresh\n (\033[1;33mwarning! last project data will be erased \033[0m(downloaded files will be safe, unless the program replaces the files with new ones)\n\u001b[33;1m  >> \033[0m"%self.Project, extra_opt=('f','fresh'), extra_return=('fresh','fresh'))
					except LeachICancelError:
						print("\n\u001b[33;1mCancellation command entered.\nReturning to main options\u001b[0m")
						leach_logger("000||11000||%s||f-Stop||was_paused||don't want to resume proj or anything"%self.Project)
						return 0
					if temp==True:
						print('============ Reloaded =============')
						leach_logger('11000x3||%s'%self.Project,user_name)
						self.existing_found= True
					elif temp=='fresh':
						leach_logger('11000x4||%s'%self.Project,user_name)
						#clear file data
						#writer(self.Project+'.list','w','','data/leach_projects','10009')
						#writer(self.Project+'.proj','w','','data/leach_projects','10009')
						
						Project = self.Project
						self.__init__()
						self.Project= Project
						self.existing_found= False
					elif temp== False: return 0
					del temp
			else:
				print("Could not load data from file. Please start over.")
				self.existing_found=False


				#print('error')

			#download_files(listx,state)
		else:
			# self.existing_found=0
			print('Insufiicient data!\n')
			self.corruptions+=[0]
	def main(self):      #func_code= 10009
		global death, sp_arg_flag
		"""runs the mainloop of the projects runtime code"""
		self.__init__()

		try:
			while True:
				try:
					self.Project=safe_input('\nEnter Batch download directory (Project name): ')

				except LeachICancelError:
					death = True
					print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
					leach_logger("0x1||10009||User Exit-0")
					try:
						self.server_code.kill()
					except: pass

					

					exit(0)
					# sys_exit(0)
				if self.Project=='':
					print('You must enter a Project name here.')
				elif self.Project == '?enable-dl-thread':
					sp_arg_flag['disable dl cancel'] = True
					print('Disabled download cancellation by adding join thread option')
					return 0

				elif self.Project == '?disable-dl-thread':
					sp_arg_flag['disable dl cancel'] = False
					print('Enabled download cancellation by adding removing thread option [DEFAULT]')
					return 0
				elif self.Project in ['?disable-dl-get', '?D-dl']:
					sp_arg_flag['disable dl get'] = True
					print('Disabled download save by using requests.head')
					return 0

				elif self.Project in ['?enable-dl-get', '?E-dl'] :
					sp_arg_flag['disable dl get'] = False
					print('Enabled download save by using requests.get [DEFAULT]')
					return 0

				else:
					self.Project= self.Project
					break
		except EOFError:
			exit(0)
		except KeyboardInterrupt:
			exit(0)
		temp = self.Project
		temp1= temp.replace('"','')
		if temp1[0]=="'" and temp1[1]=="'": temp[1:-1]
		try:
			from_file= True
			if temp1.endswith('.proj') and os_isfile(temp1):
				if asker("Project file detected.\n\u29bf Do you want re-open project from that file?\n >> "):
					leach_logger("10009x0||%s||fileOpen"%(self.Project),user_name)
					if self.data_checkup(path = temp1, proj_name= temp)==0:
						return 0
				else: from_file = False
			else: from_file= False

			if from_file == False:
				if any([i in self.Project for i in '/\<>?"*|:']):
					print('Project name can\'t have these charecters : /\<>?"*|:\n\n')
					return 0
					
				# self.project_dir=self.Project[:].replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
				leach_logger("10009x0||%s||Checking Project Database"%(self.Project),user_name)
				if self.Project in open('data/projects.db').read().split('\n'):
					print('Existing Project name found!')
					proj_good=False
					list_good=False
					if self.data_checkup()==0:
						return 0
			del from_file
		except LeachICancelError:
			print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
			leach_logger("000||10009||%s||f-Stop||is_proj_file||user probably freaked out for too much Ques"%self.Project)
			return 0

		

		del temp, temp1

		if any(i in self.Project for i in '\\/|:*"><?'):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0

		if self.existing_found==False:
			if self.update:
				if os_exists('data/leach_projects/'+self.Project): rmdir('data/leach_projects/'+self.Project)
				self.sub_dirs=[]
				sub_links=[]
				self.all_list=[]
				self.dl_done=False

				if not self.check_sp_links(self.main_link,['nh', 'mangafreak']):
					page = self.dl_page()
					if page:
						link_true= True

				if self.check_sp_links(self.main_link,'mangafreak'):
					print("Update isn't available for mangafreak")
					try:
						if asker('\u29bf Do you want to re-download files from the same link?'):
							will_unzip=asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

							if will_unzip:
								self.sp_flags.append("dl unzip")
								if asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
									self.sp_flags.append("del dl zip")
							try:
								self.link_startswith= self.mangafreak_link(self.main_link)
	
							except EOFError:
								print("Cancel command entered! stopping")
								return 0
							except KeyboardInterrupt:
								print("cancel command entered! stopping")
								return 0
							if self.link_startswith== 0: # cancel code
								return 0


							self.file_types=('zip',)
							self.file_starts=''

							leach_logger('10009x1||%s||is_mangafreak||%s'%(self.Project,str(self.sp_flags)),user_name)

					except LeachICancelError:
						print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
						leach_logger("000||10009||%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0

				elif self.check_sp_links(self.main_link,'nh'):
					try:
						self.link_startswith, title=self.nhantai_link(self.main_link)

					except EOFError:
						print("Cancel command entered! stopping")
						return 0
					except KeyboardInterrupt:
						print("cancel command entered! stopping")
						return 0

					if self.link_startswith==False and title==False:
						print("Failed to get data from %s\nReturning back to main page."%self.main_link)
						return 0

					if title!=False and self.link_startswith!='':
						#sub_dirs.append(title.replace('/','-').replace('?','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))

						leach_logger('10009x0||%s||is_nh'%(self.Project),user_name)

				else:
					sub_links2=[]
					try:
						self.sequence=asker("\n\n\u29bf Will download in sequncial order? ")
					except LeachICancelError:
						print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
						leach_logger("000||10009||%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0

					link_startswith_re=re_compile('^'+self.link_startswith)
					try:
						if self.dimention==0:
							print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")
							try:
								self.dimention= int(safe_input("Enter the index of your choice (1/2/3): "))
							except ValueError:
								self.dimention= -1
							while self.dimention not in [1,2,3]:
								try:
									self.dimention = int(safe_input("\033[1;31;40mInvalid input!\033[0m\nEnter 1 or 2 or 3:  "))
								except ValueError:
									self.dimention= -1

							leach_logger('10009x1||%s||dimention||%s'%(self.Project,self.dimention), user_name)

						if self.dimention==1 or self.dimention==3:
							sub_links2+=[self.main_link]
						if self.dimention==2 or self.dimention==3:
							soup=bs(page.content, parser)
							# link_startswith=input("\n(optional but recomanded to be more precice):\n1. Sub-Links Starts With : ")
							leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), user_name)
							sub_links2+=list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href')!=None]))

						for i in sub_links2:


							#sys.stdout.flush()
							#print(link)
							# print(i)
							if i.startswith('#'): continue
							elif i.startswith('//'): i='https:'+i

							elif i.startswith('../'):
								_temp= self.main_link
								while i.startswith('../'):
									_temp= go_prev_dir(_temp)
									i= i.replace('../', '', 1)
								i= _temp+i
								del _temp

							elif self.partial_do_all==0 and i.startswith('/'):
								print("Partial link detected - ",i,"\nSearching for home page.")
								#print(start)
								self.homepage =self.homepage_searcher.search(self.main_link)
								#print(homepage)
								try:
									if self.homepage!=None:
										print("Home page detected: ", self.homepage.group())
										is_homepage= safe_input("\nIs this the homepage? \n(y for yes\nn for no\na for all)\n")
										if is_homepage=="a":
											self.partial_do_all=1
											is_homepage='y'
										if is_homepage=='y':
											self.homepage=self.homepage.group()
										elif is_homepage=='n':
											self.homepage= safe_input("\nEnter the home page: ")
											io2=safe_input('\nIs it for all other links?(y/n)')
											if io2=='y':
												self.partial_do_all=1
											elif io2!='n':
												print("Invalid input!")
												time.sleep(5)
												exit(0)
										else:
											print("Invalid input!")
											time.sleep(5)
											exit(0)
									else:
										print("Homepage not found!")
										self.homepage= safe_input("\nEnter the home page: ")
										io2=safe_input('Is it for all other links?(y/n)')
										if io2=='y':
											self.partial_do_all=1
										elif io2!='n':
											print("Invalid input!")
											time.sleep(5)
											exit(0)
									i= self.homepage+i
								except LeachICancelError:
									print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
									leach_logger("000||10009||%s||f-Stop||discontinued||user probably freaked out for too much Ques"%self.Project)
									return 0
							elif self.partial_do_all==1 and i.startswith('/'):
								i=self.homepage+i
							if '//' not in i:
								temp=self.homepage_searcher.search(self.main_link).group()
								if temp.endswith('/'):
									if i.startswith('/'): i=temp+i[1:]
									else: i=temp+i
								else:
									if i.startswith('/'): i=temp+i
									else: i=temp+'/'+i
								

							if link_startswith_re.search(i)!=None:
								sub_links.append(i)
						#print(sub_links)
						del sub_links2

						sub_links=natsort.natsorted(remove_duplicate(sub_links), key= lambda x: x.lower())

						
					except LeachICancelError:
						print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
						leach_logger("000||10009||%s||f-Stop||asking4home||user probably freaked out for too much Ques"%self.Project)
						return 0






			else:
				if os_exists('data/leach_projects/'+self.Project): rmdir('data/leach_projects/'+self.Project)
				if self.corruptions!=[] and self.corruptions != [0]:
					leach_logger("10009x1||%s||Corruptions||%s"%(self.Project,  str(self.corruptions,open('data/leach_projects/'+self.Project+'.proj').readlines())), user_name)

				writer('errors.txt', 'a','','data/leach_projects/'+self.Project,'10009') #reset error file


				self.all_list=[]
				self.sub_dirs=[]
				sub_links=[]
				sub_links2=[]
				#sub_links_filtered=[]
				self.file_types=set()
				self.link_startswith=''
				self.file_starts=''
				link_true=False
				try:
					self.main_link=safe_input("\nEnter the link: ")
					leach_logger('10009x1||%s||m_link||%s'%(self.Project, self.main_link), user_name)
					while link_true==False:
						if self.check_sp_links(self.main_link,['nh', 'mangafreak']):
							break
						page = self.dl_page()
						if page:
							link_true= True


					if self.check_sp_links(self.main_link,'mangafreak'):
						print("mangafreak link detected!!")
						is_mangafreak=asker("\u29bf Do you want to download manga images from this links?? (\u001b[1m\u001b[4m\u001b[7m y \033[0m/\u001b[1m\u001b[4m\u001b[7m n \033[0m)\n>> ")
						if is_mangafreak:
							will_unzip=asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

							if will_unzip:
								self.sp_flags.append("dl unzip")
								if asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
									self.sp_flags.append("del dl zip")
							self.link_startswith= self.mangafreak_link(self.main_link)
							self.file_types=('zip',)
							self.file_starts=''

							leach_logger('10009x1||%s||is_mangafreak.sp_flags||%s'%(self.Project,str(self.sp_flags)),user_name)
							# sub_links=''
							#exit(0)
						
						else:
							page = self.dl_done()
							if page:
								link_true= True

					if  self.check_sp_links(self.main_link,'nh'): #main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
						print("nhentai link detected!!")
						is_nh=asker("\u29bf Do you want to download doujin images from this links?? (\u001b[1m\u001b[4m\u001b[7m y \033[0m/\u001b[1m\u001b[4m\u001b[7m n \033[0m)\n>> \n( ͡° ͜ʖ ͡°)\t")
						####( io )
						if is_nh:
							if os_name=='Windows' and ara_ara:
								self.play_yamatte_t.start()

							self.link_startswith, title=self.nhantai_link(self.main_link)
							#print(link_startswith,title)
							if self.link_startswith==0 and title==0:
								return 0

							if title!=False and self.link_startswith!='':
								#sub_dirs.append(title.replace('/','-').replace('?','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))
								self.file_types=img
								self.file_starts='https://nhentai'
								leach_logger('10009x1||%s||is_nh||True||Assigned after testing the link'%(self.Project),user_name)
						
						else:
							page = self.dl_done()
							if page:
								link_true= True
					if self.check_sp_links(self.main_link,'pinterest'):
						print("Pinterest link detected.\nDo you want to try the special features for pinterest images?\nWarning: All images may not be the same from the website as you see\n")
						if asker('>> '):

							if self.check_sp_links(self.main_link, 'pinterest-pin'):
								try:
									self.dimention= int(safe_input("Enter the index of your choice (1/2/3): "))
								except ValueError:
									self.dimention= -1
								while self.dimention not in [1,2,3]:
									try:
										self.dimention = int(safe_input("\033[1;31;40mInvalid input!\033[0m\nEnter 1 or 2 or 3:  "))
									except ValueError:
										self.dimention= -1



							self.link_startswith='https://www.pinterest.com'


					if self.link_startswith=='':

						print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")

						try:
							self.dimention= int(safe_input("Enter the index of your choice (1/2/3): "))
						except ValueError:
							self.dimention= -1
						while self.dimention not in [1,2,3]:
							try:
								self.dimention = int(safe_input("\033[1;31;40mInvalid input!\033[0m\nEnter 1 or 2 or 3:  "))
							except ValueError:
								self.dimention= -1
						leach_logger('10009x1||%s||dimention||%s'%(self.Project, self.dimention), user_name)

						if self.dimention==1 or self.dimention==3:
							sub_links2+=[self.main_link]

						if self.dimention==2 or self.dimention==3:
							#page = requests.get(main_link, headers=header_())
							#if not page:
							#	print('\033[1;31;40mError code 605x\nConnection Failed, The program will break in 5 second\033[0m')
							#	time.sleep(5)
							#	leach_logger("XXXX Program crashed opening: '"+main_link+"' Error code 605 from main function collecting current page.", ush)
							#	exit(0)
							#print(page.content)
							#time.sleep(1000)
							soup=bs(page.content, parser)
							self.link_startswith=safe_input("\n(optional but recomanded to be more precice):\n1. Sub-Links Starts With : ")
							leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), user_name)
							sub_links2+=list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href')!=None]))


						file_types_i=safe_input("\nEnter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg,mp3) or just write the category (ie: image, music, video): ")
						if file_types_i=='image':
							self.file_types=img
						else:
							self.file_types= tuple(i.strip(i) for i in file_types_i.split(','))
						leach_logger('10009x1||%s||f_types||%s'%(self.Project, str(self.file_types)), user_name)

						self.file_starts=safe_input("\nFile Links Starts With (if known or need to be specified): ")
						leach_logger('10009x1||%s||f_starts||%s'%(self.Project, self.file_starts), user_name)
						# project_path=Project[:]

						#if start[-1'/'): start+='/'
						#if start.startswith(): start=start[1:]
							#sub_dirs=[]
						#len_sub_links=str(len(sub_links))
						# count=0
						print('\n')



						self.sequence=asker("\n\n\u29bf Will download in sequncial order? ")
						self.overwrite_bool= asker("\u29bf Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>")

				except LeachICancelError:
					print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
					leach_logger("000||10009||%s||f-Stop||discontinued||user probably freaked out for too much Ques"%self.Project)
					return 0
				#else: all_list=list(all_list)
				#leach_logger("++%s'+'%s'+%s'+'%s'++"%(main_link, link_startswith,str(file_types),file_starts), user_name)

				print("Checking links...")

				link_startswith_re=re_compile('^'+self.link_startswith)

				for i in sub_links2:


					#sys.stdout.flush()
					#print(link)
					# print(i)
					if i.startswith('#'): continue
					elif i.startswith('//'): i='https:'+i

					elif i.startswith('../'):
						_temp= self.main_link
						while i.startswith('../'):
							_temp= go_prev_dir(_temp)
							i=i.replace('../', '', 1)
						i= _temp+i
						del _temp

					elif self.partial_do_all==0 and i.startswith('/'):
						print("Partial link detected - ",i,"\nSearching for home page.")
						#print(start)
						self.homepage =self.homepage_searcher.search(self.main_link)
						#print(homepage)
						try:
							if self.homepage!=None:
								print("Home page detected: ", self.homepage.group())
								is_homepage= safe_input("\nIs this the homepage? \n(y for yes\nn for no\na for all)\n")
								if is_homepage=="a":
									self.partial_do_all=1
									is_homepage='y'
								if is_homepage=='y':
									self.homepage=self.homepage.group()
								elif is_homepage=='n':
									self.homepage= safe_input("\nEnter the home page: ")
									io2=safe_input('\nIs it for all other links?(y/n)')
									if io2=='y':
										self.partial_do_all=1
									elif io2!='n':
										print("Invalid input!")
										time.sleep(5)
										exit(0)
								else:
									print("Invalid input!")
									time.sleep(5)
									exit(0)
							else:
								print("Homepage not found!")
								self.homepage= safe_input("\nEnter the home page: ")
								io2=safe_input('Is it for all other links?(y/n)')
								if io2=='y':
									self.partial_do_all=1
								elif io2!='n':
									print("Invalid input!")
									time.sleep(5)
									exit(0)
							i= self.homepage+i
						except LeachICancelError:
							print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
							leach_logger("000||10009||%s||f-Stop||discontinued||user probably freaked out for too much Ques"%self.Project)
							return 0
					elif self.partial_do_all==1 and i.startswith('/'):
						i=self.homepage+i
					if '//' not in i:
						temp=self.homepage_searcher.search(self.main_link).group()
						if temp.endswith('/'):
							if i.startswith('/'): i=temp+i[1:]
							else: i=temp+i
						else:
							if i.startswith('/'): i=temp+i
							else: i=temp+'/'+i
						

					if link_startswith_re.search(i)!=None:
						sub_links.append(i)
				#print(sub_links)
				del sub_links2


				sub_links=natsort.natsorted(remove_duplicate(sub_links), key= lambda x: x.lower())



			if self.sub_dirs==[]:
				leach_logger("10009x2||%s||%i"%(self.Project, len(sub_links)), user_name)
				for i in sub_links:
					self.sub_dirs.append(parse.unquote(html_unescape(i)).replace('?','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))
				# sub_dirs=sub_links[:]

				len_sub_links= len(sub_links)




				sub_range=range(len_sub_links)
				indx1= Process(target=self.list_writer, args=(sub_links, sub_range[::3]))
				indx2= Process(target=self.list_writer, args=(sub_links, sub_range[1::3]))
				indx3= Process(target=self.list_writer, args=(sub_links, sub_range[2::3]))

				try:

					indx1.start()
					indx2.start()
					indx3.start()
					try:
						indx1.join()
						indx2.join()
						indx3.join()

					except EOFError:
						leach_logger("000||10009||%s||f-Stop||is_indexing||user probably freaked out for any link being indexed")
						print("\u001b[33;1mProject indexing cancelled by Keyboard\u001b[0m")
						self.break_all= True
						return 0
					except KeyboardInterrupt:
						leach_logger("000||10009||%s||f-Stop||is_indexing||user probably freaked out for any link being indexed")
						print("\u001b[33;1mProject indexing cancelled by Keyboard\u001b[0m")
						self.break_all= True
						return 0
					
				except Exception as e:
					print("\033[1;31;40mcode: Error 607\n The program will break in 5 seconds\033[0m")
					leach_logger("10009x-1||%s||%s||%s"%(self.Project, e.__class__.__name__, str(e)), user_name)
					time.sleep(5)
					exit(0)

			

			if self.sequence: self.all_list=natsort.natsorted(self.all_list, key = lambda x: x[0].lower())


			writer('projects.db','a',self.Project+'\n','data','10009')

		self.all_list2 = remove_duplicate(self.all_list)

		leach_logger("10009x3||%s||%i||%i"%(self.Project, len(self.sub_dirs), len(self.all_list)), user_name)

		# clean the files if exist
		writer(self.Project+'.list','w','','data/leach_projects','10009')
		writer(self.Project+'.proj','w','','data/leach_projects','10009')

		# write new data
		writer(self.Project+'.list','w',str(self.all_list),'data/leach_projects','10009')
		writer(self.Project+'.proj','w','main_link= "%s"\n'%self.main_link,'data/leach_projects','10009')
		writer(self.Project+'.proj','a','link_startswith= "%s"\n'%self.link_startswith,'data/leach_projects','10009')
		writer(self.Project+'.proj','a','file_types = %s\n'%str(self.file_types),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','file_starts= "%s"\n'%self.file_starts,'data/leach_projects','10009')
		writer(self.Project+'.proj','a','sub_dirs = %s\n'%str(self.sub_dirs),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','sp_flags = %s\n'%str(self.sp_flags),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','sp_extension = "%s"\n'%self.sp_extension ,'data/leach_projects','10009')
		writer(self.Project+'.proj','a','overwrite_bool = %s\n'%str(self.overwrite_bool),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','dimention = %s\n'%str(self.dimention),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','sequence = %s\n'%str(self.sequence),'data/leach_projects','10009')
		writer(self.Project+'.proj','a','Project = "%s"\n'%str(self.Project),'data/leach_projects','10009')

		print('\n')
		self.total=len(self.all_list2)


		if os_exists('data/leach_projects/'+self.Project+'/errors.txt'):
			self.errors=len(open('data/leach_projects/'+self.Project+'/errors.txt').readlines())
		else:
			self.errors=0

		#print(all_list)


		all_list_r=list(range(self.total))

		print('Downloaded ['+'\u001b[7m'+(' '*0)+'\u001b[0m'+' '*(32-0)+'] ['+str(0) + '/'+str(self.total)+']')

		t11= Process(target=self.distribute, args=(all_list_r[::10],1))
		t2= Process(target=self.distribute, args=(all_list_r[1::10],2))
		t3= Process(target=self.distribute, args=(all_list_r[2::10],3))
		t4= Process(target=self.distribute, args=(all_list_r[3::10],4))
		t5= Process(target=self.distribute, args=(all_list_r[4::10],5))
		t6= Process(target=self.distribute, args=(all_list_r[5::10],6))
		t7= Process(target=self.distribute, args=(all_list_r[6::10],7))
		t8= Process(target=self.distribute, args=(all_list_r[7::10],8))
		t9= Process(target=self.distribute, args=(all_list_r[8::10],9))
		t10= Process(target=self.distribute, args=(all_list_r[9::10],10))
		t99= Process(target=self.retry_errors)
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
		t99.start()

		if sp_arg_flag['disable dl cancel']== True:
			try:
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
				t99.join()
			
			except EOFError:
				print("Hard cancel command entered! stopping")
				self.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.break_all = True

		will_open = None

		exec(open('make_html.py').read(), globals())

		if not 'mangafreak' in self.sp_flags:
			#print(True)
			first_page=make_pages(self.all_list,self.sub_dirs, self.Project, self.sequence)

		while self.break_all==False and any([t11.is_alive(),t2.is_alive(),t3.is_alive(),t4.is_alive(),t5.is_alive(),t6.is_alive(),t7.is_alive(),t8.is_alive(),t9.is_alive(),t10.is_alive(), t99.is_alive()]):
			try:
				will_open= safe_input()
				# print([t11.is_alive(),t2.is_alive(),t3.is_alive(),t4.is_alive(),t5.is_alive(),t6.is_alive(),t7.is_alive(),t8.is_alive(),t9.is_alive(),t10.is_alive(), t99.is_alive()])
			except LeachICancelError:
				self.break_all= True
				leach_logger("000||10009||%s||D-Break||Download stopped"%(self.Project))
				break

		if self.break_all:
			print("\u001b[33;1mProject continuation cancelled by Keyboard\u001b[0m")
			leach_logger("000||10009||%s||D-Stop||Downloaded-%i | Error-%i"%(self.Project, self.done, self.errors))
		else:
			if 'mangafreak' in self.sp_flags:
				if not os_exists('Download_projects/'+Project+'/'):\
					print("\n  \u001b[1m\u001b[4m\u001b[7mProject folder not found.\033[0m\nPlease recheck or update the donwload project\n*its required for Manga Freak Projects")						
				sub_dirs = natsort.natsorted([get_file_name(i[0], 'url').split('.')[0] for i in self.all_list], key= lambda x: x.lower())
				all_list =[]
				for i in range(len(sub_dirs)):
					try:
						for j in os_listdir('Download_projects/'+self.Project+'/'+sub_dirs[i]):
							#print(j)
							if os_isfile('Download_projects/'+self.Project+'/'+sub_dirs[i]+'/'+j) and not j.endswith('.html'):
								all_list.append([j,i])
					except OSError: continue
				first_page = make_pages(all_list,sub_dirs, self.Project, True)

			if will_open=='x':
				run_in_local_server(self.port, host_dir='%s/%s.html'%(self.Project, self.Project))


	def dl_page(self):
		try:
			page =requests.get(self.main_link, headers=header_(), timeout=5)
			writer(self.Project+'.html','wb',page.content,'data/leach_projects/%s'%self.Project,'10009')
			
		except (requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema):
			self.main_link=safe_input("\033[1;31;40mInvalid URL! \033[0m(possible cause: no internet or wrong link)\n\nPlease re-enter the link: ")
		

		return page
	


#test mangafreak all files available
'''from os.path import os_isdir
for i in range(1,166):
	if os_isdir('E:/Ratul Codes/C/Python/Test/web ripper/Web-leach/Projects/rent/Kanojo_Okarishimasu/Kanojo_Okarishimasu_%d'%i)==False:
		print(i)'''


#Update err_header.txt#######################################
with open('data/err_header.txt', 'r') as error_hdr_file:
	temp_ = re_sub('\,{2,}', ',', error_hdr_file.read())

if temp_[-1]==',': temp_= temp_[:-1]

err_hdr_list = eval(temp_)
#print(type(err_hdr_list))
if type(err_hdr_list)== tuple:
	err_hdr_list = Counter(err_hdr_list)

	writer('err_header.txt','w',str(err_hdr_list),'data/','00000')

elif type(err_hdr_list)== list:
	_t = Counter()
	for i, j in err_hdr_list:
		_t[i]=j

	err_hdr_list =_t

	writer('err_header.txt','w',str(err_hdr_list),'data/','00000')

	
elif type(err_hdr_list)== dict:
	err_hdr_list = Counter(err_hdr_list)
	

#############################################################



try:
	init_upto = 'Importing Assets'
	print("Connecting to server...")
	_connect_net()
	init_upto = 'Getting IP'
	leach_logger("001||"+_VERSION+"||"+Nsys.getSystemInfo()+"||"+user_net_ip+"||"+str(start_up_dt)+"||"+Nsys.get_tz()+"||"+str(time.time()-start_up)+'s', 'lock')
	server_start=time.time()


	run_mod= god_mode()

	init_upto = 'God mode'

	import getpass


	if run_mod=='offline' :
		if os_exists('data/.temp/updateG.ext') and os_exists('data/.temp/updateL.ext'):
			exec(decrypt(open('data/.temp/updateG.ext').read(), "lock").strip())
			exec(decrypt(open('data/.temp/updateL.ext').read(), "lock").strip())
		else:
			print("Failed to startup. Please connet to the internet for the first initialization")
			leach_logger('0x0')

			try:
				IloveAsuna=safe_input('Press enter to exit...', getpass.getpass)
				backdoor=IloveAsuna
				if hashlib_md5('RandomteXtZYIQrgYlb0sHdFLaIW'+backdoor[2]+'#testTubeAlabam@ToGBNr3SfYrIIfHQSY'+backdoor[0]+'2Jpx4Piks84XCvN8El'+backdoor[:-2:-1]+'xf4wXXygZPILxsOUAP'+backdoor[::-2]+'#testTubeAlabam@%sToGBNr3SfYrIIfHQSY'%backdoor[::-1]+backdoor[0]+'2Jpx4Piks84XCvN8El'+backdoor[1::-2]+'KgCaIWjP6X4W5h4P2G').hexdigest()=='751fa7e19763b50a399806fdcc5dee34':
					pass
				else:
					exit(0)
			except LeachICancelError:
				print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
				exit(0)


	'751fa7e19763b50a399806fdcc5dee34'

	try:
		if not os_isdir("Download_projects"): makedirs("Download_projects")
	except PermissionError:
		print("Can't write in this directory, either change the write permission or move this program to somewhere with write permission.\nError code: 00000x101")
		leach_logger("00000x101||Download_projects||1")
		sys_exit()

	init_upto = 'Dl folder making'


	print("Done!!")
	time.sleep(1)

	clear_screen()

	leach_logger('002||'+str(time.time()-server_start)+'s||'+server_version, 'leach')
	ush = log_in()
	leach_logger('003||%s||%s'%(ush, Nsys.compressed_dt()),user_name)

	init_upto = 'user login'

except EOFError:
	print("Hard cancel command entered! stopping")
	leach_logger('0x1||00000||Hard Exit by User on Start up. Init upto - "%s"')
	exit(0)
	
except KeyboardInterrupt:
	print("Hard cancel command entered! stopping")
	leach_logger('0x1||00000||Hard Exit by User on Start up. Init upto - "%s"'%init_upto)
	exit(0)







program_class= None
if __name__ != "__main__":
	port= (int(ush, 16) % (6000 - 4000 + 1)) + 4000

while __name__=='__main__' and run_mod=='online':
	program_class = web_leach()
	program_class.main()



