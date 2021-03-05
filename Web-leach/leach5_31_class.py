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

cloud_data_link='https://pastebin.com/raw/Sa9hTd0P'
import time
start_up=time.time()
no_psutil= True
try:
	import Number_sys_conv as Nsys
	start_up_dt = Nsys.dt_()
	no_psutil=False
except:
	pass

#########################################################

# MATH tools ######################
from math import floor
from random import choice as random_choice, randint
from hashlib import sha1 as hashlib_sha1
from re import search as re_search,compile as re_compile

from rcrypto import encrypt, decrypt
###################################


# SYS tools #######################
from platform import system as os_name
from subprocess import call as subprocess_call
from sys import exit as sys_exit,executable as sys_executable
from sys import stdout as sys_stdout
sys_write=sys_stdout.write
del sys_stdout
###################################

if no_psutil:
	subprocess_call([sys_executable, "-m", "pip", "install",'--disable-pip-version-check','--quiet', 'psutil'])
	import Number_sys_conv as Nsys
	start_up_dt = Nsys.dt_()
	no_psutil=False


# FILE system tools###############
from os import makedirs, remove, rename, system as os_system
from shutil import rmtree as rmdir
from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename
from zipfile import ZipFile, BadZipFile
###################################



from threading import Thread as Process, current_thread



# HTML tools##############################
from html import unescape as html_unescape, escape as html_escape
from urllib import parse
import webbrowser

from bs4 import BeautifulSoup as bs
import requests

from headers_file import header_list
##########################################

# Re Define to speed up###################
len = len
range = range
sorted = sorted
##########################################

process_id= randint(2003,9999)

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



import __main__ # used to load assets in global (idea from pydroid)



def clear_screen():    #func_code= 00000
	"""clears terminl output screen"""
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
		leach_logger('00001x-1||'+e.__class__.__name__+('||%s||'%e)+f_code+'||'+text)


os_name=os_name()

def header_():    #func_code=00002
	"""returns a random header from header_list for requests lib"""
	return( {'User-Agent':random_choice(header_list)})

def install(pack, alias=None):    #func_code=00003
	"""Just install package
	pack: the name the libraby (beautifulsoup4, requests)
	alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

	if alias == None:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install",'--disable-pip-version-check','--quiet', alias])


import pkg_resources
installed_pkgs=[pkg.key for pkg in pkg_resources.working_set]
del pkg_resources


def install_req(pkz):     #func_code=00004
	"""install requirement package if not installed"""
	if pkz not in installed_pkgs:
		install(pkz)

install_req('requests')
install_req('beautifulsoup4')
if no_psutil:
	install_req('psutil') #required to get win sys info
	import Number_sys_conv as Nsys
	start_up_dt = Nsys.dt_()
	no_psutil=False


exec(open('make_html.py').read(), globals())

from bs4 import BeautifulSoup as bs
import requests

if os_name=="Windows":
	install('comtypes')    #required in mplay4


def loc(x, os_name='Linux'):    #func_code=00005
	"""to fix dir problem based on os
	x: directory
	os_name: Os name *Linux"""
	if os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')


def writer(fname, mode, data, dir=None, f_code='', encoding='utf-8'):    #func_code=00006
	"""Writing on a file
		fname: filename,\n
		mode: write mode (w,wb,a,ab),\n
		data: data to write,\n
		dir: directory of the file, empty for current dir *None,\n
		func_code: (str) code of the running func *empty string,\n
		encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""
	#func_code='00006'
	if any(i in fname for i in ('\\|:*"><?')):
		leach_logger('00006||Invalid Fname||%s||replacing con char'%fname)
		fname=fname.replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
		
	try:
		if dir == None:
			if 'b' not in mode:
				with open(fname, mode, encoding=encoding) as file:
					file.write(data)
			else:
				with open(fname, mode) as file:
					file.write(data)
		else:
			locs=loc(dir, 'Linux')
			if any(i in locs for i in ('\\|:*"><?')):
				leach_logger('00006||Invalid dir||%s||replacing con char'%locs)
				locs=locs.replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
		
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
				writer(fname, mode, data, locs, f_code)
	except Exception as e:
		if e.__class__.__name__== "PermissionError":
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: 101x'+f_code)
			leach_logger('101||%s||%s||%s||%s'%(f_code, fname, mode, dir))
			raise LeachPermissionError
		else:
			leach_logger('00006x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s'%(f_code, fname, mode, dir,e))
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: 00006x'+f_code)
			raise e



def hdr(header, f_code=''):    #func_code=00007
	"""returns the index of a header"""
	try:
		return str(header_list.index(header['User-Agent']))
	except Exception as e:
		print("Some error occured caused, possible cause: DATA CORRUPTION\nError code: 00007x"+f_code)

		leach_logger('00007x-1||'+'||' +f_code+e.__class__.__name__+'||'+ e+'||'+header)
		return str((-1, header))


def leach_logger(io, key='lock'):   #func_code=00008
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the begning)
	
	io: the log message\n
	key: salt text"""
	_key="Asuna"
	salt = hashlib_sha1(key.encode()).hexdigest()
	writer('userlog.leach', 'ab', encrypt(salt+('||%s||'%Nsys.dt_())+str(process_id)+'||'+io,_key).encode('utf-8')+b'\n','data','00008')


#################### CONNECT TO THE NET FOR THE FIRST TIME #################
def _connect_net():      #func_code= 00009
	"""connects to the internet and returns the users global ip"""
	global user_net_ip
	current_header=header_()
	try:
		user_net_ip=requests.get('https://ident.me',headers=current_header).content.decode()
		return [0, '0']
	except requests.exceptions.ConnectionError:
		print("\033[1;31;40mError code: 605x1\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x1||header_index="+hdr(current_header,'00009'), 'lock')
		time.sleep(5)
		exit(0)
	except Exception as e:
		print(e.__class__.__name__, "occured. Please inform the Author.\nError code: 00009x-1(%s)"%e.__class__.__name__)
		leach_logger("00009x-1||header_index="+hdr(current_header,'00009')+'||%s||%s'%(e.__class__.__name__, e), 'lock')
		time.sleep(5)
		exit(0)

_connect_net()

def import_paste():      #func_code= 00010
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


def delete_last_line():      #func_code= 00011
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys_write('\x1b[1A')

	#delete last line
	sys_write('\x1b[2K')

def go_prev_dir(link):    #func_code=00026
	"""returns the previous path str of web link or directory\n
	**warning: returns only in linux directory format"""
	link=loc(link,'Linux')
	if link.endswith('/'):
		return '/'.join(link[:-1].split('/')[:-2])+'/'
	# x=link.split('/')
	else:
		return '/'.join(link.split('/')[:-2])+'/'


_VERSION="5.31"

parser='html.parser'
img=('jpeg','jpg','png','gif', 'webp', 'bmp', 'tif')


who_r_u='https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
yamatte= ['https://www.myinstants.com/media/sounds/yamatte.mp3','https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3']
yes= ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yeap', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yeap', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yeap')
no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
cond=yes+no
condERR = "Sorry,  I can't understand what you are saying. Just type yes or no.   "

user_list=['bec6113e5eca1d00da8af7027a2b1b070d85b5ea','eb23efbb267893b699389ae74854547979d265bd']

g_mode=False

def safe_input(msg=''):
	sys_write(str(msg))
	try:
		try:
			try:
				box= input()
				return box
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
			except LeachICancelError:
				leach_logger('User Cancel command...')
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError
	except EOFError:
			raise LeachICancelError
	except KeyboardInterrupt:
		raise LeachICancelError

def asker(out='', default=None, True_False=(True, False)):      #func_code= 00012
	"""asks for yes no or equevalent inputs
	out: printing text to ask tha question *empty string
	default: default output for empty response *None
	True_False: returning data instead of true and false *(True, False)"""
	print(out,end='')

	Ques2 = safe_input().lower()
	if default!= None and Ques2=='':
		return default
	#Ques2 = Ques2
	while Ques2 not in cond:
		print(condERR)
		Ques2 = safe_input().lower()
		#Ques2 = Ques2
	if Ques2 in cond:
		if Ques2 in yes:
			return True_False[0]
		else:
			return True_False[1]


def get_file_name(directory, mode= 'dir'):      #func_code= 00013
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



def get_file_ext(directory, mode='dir', no_format='noformat'):      #func_code= 00014
	"""to get the extension of a file directory

	directory: file directory relative or direct\n
	no_format: returning format if no file extention was detected *noformat"""
	temp= get_file_name(directory, mode)
	if len(temp.split('.'))==1:
		return no_format
	else:
		return temp.split('.')[-1]



def reader(direc, read_mode='r'):      #func_code= 00015
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
#print(os_isdir('Data/leach_projects/Sao manga rip'))

	# print(io==decrypto.decrypt(encrypt(io,key),key))


# print(requests.get('https://ident.me',headers=headers).content)
# user_net_ip=requests.get('https://ident.me',headers=headers).content.decode()
# print(user_net_ip)



def _version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename,_latest_size):      #func_code= 00016
	print("An update available v"+_latest_version+"("+_latest_size+"), Do you want to update? ")
	try:
		reply= safe_input()
	except LeachICancelError:
		print('\n\u001b[33;1mCancellation command entered. Skipping uppdate!\u001b[0m\n')
		leach_logger("update-prompt||f-Exit-ask")
		return 0
	if reply:
		print('\nConnecting...')
		leach_logger("201||"+str(_latest_version),'lock')
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
					exit(0)
				else:
					print ("\033[1;31;40mMD5 verification failed!.\033[0m \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
		else:
			print("Failed to connect to the host server.\nPlease inform the author!!\nError code ")
			leach_logger('202||%s||%s||%s||%s'%(_latest_version, _latest_link, _VERSION, hdr(current_header,'00016')),'lock')



def god_mode():      #func_code= 00017
	# global user_net_ip
	if os_name=='Windows':
		current_header=header_()
		try:
			file=requests.get(who_r_u, headers=current_header)
			if file:
				writer('who_r_u.mp3','wb',file.content,'Data/.temp','00017')
			else:
				raise requests.ConnectionError

		except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
			print("\033[1;31;40mError code: 605x3\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
			leach_logger("605x3||%s"%(hdr(current_header,'00017')), 'lock')
			time.sleep(5)
			exit(0)
	current_header=header_()
	try:
		file=requests.get(cloud_data_link, headers=current_header)
		writer('update.ext','wb',file.content,'data/.temp','00017')
		exec(decrypt(open('data/.temp/update.ext').read(), "lock").strip())

		remove('Data/.temp/update.ext')
	except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
		print("\033[1;31;40mError code: 605x4\nNo internet connection!\nThe program will break in 5 seconds\033[0m")
		leach_logger("605x4||%s"%(hdr(current_header,'00017')), 'lock')
		time.sleep(5)
		exit(0)
	except Exception as e:
		print(e.__class__.__name__,": Unknown error occured. Error code 00017x-1\nPlease inform the author.")
		leach_logger("00017x-1||%s||%s||%s"%(e.__class__.__name__,str(e),hdr(current_header,'00017')), 'lock')
		time.sleep(5)
		exit(0)
	
	if os_isdir('Data/projects'): rename('Data/projects', 'Data/leach_projects')
	if os_isdir('./projects'): rename('./projects', './Download_Projects')
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


def log_in():      #func_code= 00019
	global user_name
	if boss!=1:
		userhash=0
		br=0
		while True:
			try:
				user_name=safe_input("Enter username: ")
			except LeachICancelError:
				print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
				leach_logger("Login exit||f-Stop")
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
					mplay4.set_win_vol(60)
					mplay4.load('data/.temp/who_r_u.mp3').play()
				time.sleep(5)
				if os_name=='Windows':
					mplay4.set_win_vol(ex)
	else:
		userhash='eb23efbb267893b699389ae74854547979d265bd'
	if boss!=1 and os_name=='Windows':
		remove('data/.temp/who_r_u.mp3')

	if not os_exists('data/projects.db'):
		writer('projects.db','a','','data','00019')
	if userhash=='eb23efbb267893b699389ae74854547979d265bd':
		g_mode='Asuna'
	return userhash


class web_leach:

	def __init__(self):      #func_code= 10001
		"""initialize variables on every start of a project"""
		#global overwrite_bool, partial_do_all, homepage, existing_found, dimention,sp_flags, done,indx_count, sp_extension, errors

		self.total=0
		self.break_all= False
		self.done=0
		self.errors=0	# number or errors
		self.sp_extension=''	# if custom file extension needed to be added with the downloaded file names
		self.sp_flags=[]	# list of flags for special downloads like mangafreaks
		self.overwrite_bool= True	# bool for wheather replace the duplicate file or not
		self.partial_do_all= False
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
		self.all_list = set()	# assigning a set so that duplication can be cancelled, will
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


	

	def distribute(self, lists,task_id,is_error=False):      #func_code= 10002
		"""run downloads in this function from a list of download links
		lists: download links list
		task_id: task id (int) to keep resume point stored
		is_eror: if the funtion is running to retry the failed files *False"""
		#global total,done, errors, sp_flags, sp_extension, overwrite_bool
		task_id=str(task_id)
		res=0
		if self.existing_found:
			if os_exists('Data/leach_projects/'+self.project_dir+'/t'+task_id+'.txt'):
				res=eval(open('Data/leach_projects/'+self.project_dir+'/t'+task_id+'.txt').read().strip()) # resume point of the list (index # int)
		self.done+=res

		time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:
			if self.break_all== True: return 0
			download=True	# switch for download it or not
			if is_error:
				i=list(j)
			else:
				i=list(self.all_list[j])

			if lists.index(j)>=res:
				current_header=header_()	# randomises header from list on every download to at least try to fool server
				try:
					if self.overwrite_bool==False:
						if self.sub_dirs[i[1]].endswith('\\') or self.sub_dirs[i[1]].endswith('/'):
							if os_isfile('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+get_file_name(i[0])+self.sp_extension): download=False
						else:
							if os_isfile('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension): download=False
					if download:
						file=requests.get(i[0], headers= current_header)
						if file:
							# clear the file
							writer(get_file_name(i[0])+self.sp_extension,'wb',b'','Download_projects/'+self.project_dir+'/'+self.sub_dirs[i[1]], '10001')
							with open('Download_projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension, 'wb') as loaded_file:
								for chunk in file.iter_content(chunk_size=8192): 
									if self.break_all: return 0
									loaded_file.write(chunk)
									self.dl_chunks+=1

									

							if 'dl unzip' in self.sp_flags:
								if os_isdir('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')==False:
									makedirs('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+'/')
								with ZipFile('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension) as zf:
									zf.extractall(path='Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0]))
								if 'del dl zip' in self.sp_flags:
									remove('Download_Projects/'+self.project_dir+'/'+self.sub_dirs[i[1]]+'/'+get_file_name(i[0])+self.sp_extension)

							writer('t'+task_id+'.txt', 'w',str(res),'Data/leach_projects/'+self.project_dir,'10002')

							delete_last_line()
							#print(done)
							percent=floor(((self.done+1)/self.total)*32)
							print('Downloaded ['+'\u001b[7m'+(' '*percent)+'\u001b[0m'+' '*(32-percent)+'] ['+str(self.done+1) + '/'+str(self.total)+']',task_id)
							res+=1
							self.done+=1
							if is_error:
								self.errors-=1
						else:
							raise requests.ConnectionError
					else:
						writer('t'+task_id+'.txt', 'w',str(res),'Data/leach_projects/'+self.project_dir,'10002')

						delete_last_line()
						#print(done)
						percent=floor(((self.done+1)/self.total)*32)
						print('Downloaded ['+'\u001b[7m'+(' '*percent)+'\u001b[0m'+' '*(32-percent)+'] ['+str(self.done+1) + '/'+str(self.total)+']')
						res+=1
						self.done+=1
						if is_error:
							self.errors-=1
				except (requests.ConnectionError,requests.exceptions.ChunkedEncodingError):
					if is_error==False:
						writer('errors.txt', 'a',str(i+[hdr(current_header,'10001')])+'\n','Data/leach_projects/'+self.project_dir,'10001')
						writer('err_header.txt','a','%s,'%hdr(current_header,'10001'),'data/','10001')
						self.errors+=1

					else:
						print("Failed to download from '%s'"%i[0])
						writer('errors.txt', 'a',str(i+[hdr(current_header,'10001'),"Error dl"])+'\n','Data/leach_projects/'+self.project_dir,'10001')
						leach_logger('project||'+self.Project+'||'+hdr(current_header,'10001')+'||Error dl||'+str(i), user_name)
				except BadZipFile:
					if is_error==False:
						writer('errors.txt', 'a',str(i+[hdr(current_header,'10001')]+["Bad zip"])+'\n','Data/leach_projects/'+self.project_dir,'10001')
						self.errors+=1
					else:
						print("It seems every time it downloads a broken or unknown zip from '%s' (possible cause password protected zips, if yes extract them manually)"+i[0])
						writer('errors.txt', 'a',str(tuple(i)+(hdr(current_header,'10001'),"Bad zip"))+'\n','Data/leach_projects/'+self.project_dir,'10001')
						
						leach_logger('project||'+self.Project+'||'+hdr(current_header,'10001')+'||Bad zip||'+str(i), user_name)
		
		self.error_triggers+=[int(task_id)]


	def list_writer(self, link, index_or_range,special=None, soup=None):      #func_code= 10003
		"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list
		link: single link or a list of links to index
		types: file types to index in all_list
		file_link_starts: (regex) srting that will check and if the file links starts with
		list_range: a range objet containing the index of the links
		special: gives a headsup that if the link is from any special cases *None
		soup: a response soup object that will speed the indexing a li'l bit up *None"""
		# global all_list, sub_dirs, indx_count
		if type(index_or_range) ==int:
			iNdex= index_or_range
		elif type(index_or_range) == range:
			raNge= index_or_range

		start_checker=re_compile('^'+self.file_starts)

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
							self.all_list.add((img_link, iNdex))

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
							self.all_list.add((img_link, iNdex))

		else:
			if type(link)==list and type(index_or_range)==range:
				dir_len=len(self.sub_dirs)
				for i in raNge:

					if self.sub_dirs[i][-1]=='/':
						self.sub_dirs[i]=self.sub_dirs[i][:-1]
					self.sub_dirs[i]=self.sub_dirs[i].split('/')[-1]


					page = requests.get(link[i],headers=header_())
					soup=bs(page.content, parser)

					for imgs in soup.find_all('img'):
						img_link=imgs.get('data-src')
						if img_link== None:
							img_link=imgs.get('src')
						else:
							print(img)
							continue
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



						if start_checker.search(str(img_link)) !=None and get_file_name(img_link, 'url').endswith(self.file_types):
							self.all_list.add((img_link.split("#")[0].split("?")[0],i))

					delete_last_line()
					print('Indexed ['+ str(self.indx_count+1) + '/'+str(dir_len)+'] '+link[i])
					self.indx_count+=1
			else:
				page = requests.get(link,headers=header_())
				soup=bs(page.content, parser)


				for imgs in soup.find_all('img'):
					temp_home=''
					img_link=imgs.get('data-src')
					if img_link== None:
						img_link=imgs.get('src')
					####$#######
					#print(img_link)
					if img_link.endswith(self.file_types):
						if img_link.startswith('//'):
							img_link="https:"+img_link
						if img_link.startswith('/'):
							img_link=self.homepage_searcher.search(link).groups()[0]+img_link

						if img_link.startswith('../'):
							while img_link.startswith('../'):
								temp_home=link
								temp_home= go_prev_dir(temp_home)
								img_link=img_link.replace('../','',1)
							img_link=temp_home+img_link
						
						if start_checker.search(str(img_link)) !=None and get_file_name(img_link, 'url').endswith(self.file_types):
							self.all_list.add((img_link.split("#")[0].split("?")[0],iNdex))



	if os_name=='Windows':
		def plat_yamatte(self, vol):      #func_code= 10004
			"""just for parody"""
			writer('yamatte.mp3','wb',requests.get(random_choice(yamatte), headers=header_()).content,'Data/.temp','10004')
			ex=mplay4.ex_vol
			mplay4.set_win_vol(vol)
			mplay4.load('data/.temp/yamatte.mp3').play()
			time.sleep(8)
			remove('data/.temp/yamatte.mp3')
			mplay4.set_win_vol(ex)
		play_yamatte_t=Process(target=plat_yamatte, args=[80])




	def nhantai_link(self,link):      #func_code= 10005
		"""checks if the link is nhentai link and returns the available link and the title of the doujin
		else it will return 0"""
		# global sub_dirs
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
			leach_logger("project||%s||606x1||%s||%s"%(self.Project, link, hdr(current_header,'10005')), user_name)
		self.file_types= img
		if page:
			soup=bs(page.content, parser)

			title=remove_non_ascii(soup.find(id='info').find('h1').get_text(),'10005')
			print("Indexing from",title)
			self.file_starts=''
			self.list_writer(code,0,'nhentai'+site,soup)
			self.sub_dirs.append(parse.unquote(html_unescape(title)).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))
			# print(self.sub_dirs)
			return link_y, title
		else:
			print("\033[1;31;40mError code: 606x2\nLink not found, Please recheck the link and start a new project\033[0m")
			leach_logger("project||%s||606x2||%s||%s"%(self.Project, link, hdr(current_header,'000')), user_name)
			return False, False


	def check_sp_links(self,link, sp=None):      #func_code= 10006
		"""checks if the link has any special case and any specific spcial case
		link: link of the project
		sp: specifies the special case check *None"""

		special_starts =['https://nhentai\.(net)|(to)/g/','https://w[\d]+\.mangafreak.net/(M|m)anga/', '^nh (\d+)$', 'https://www.pinterest.com/']
		nh=special_starts[0]
		mangafreak=special_starts[1]
		nh_sc=special_starts[2]
		pinterest=special_starts[3]
		if re_search(nh_sc, link):
			self.main_link= 'https://nhentai.net/g/'+str(re_search(nh_sc, link).group(1))
			link=self.main_link
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
		elif sp=="pinterest":
			if re_search('^'+pinterest, link)!=None:
				return True
			else:
				return False
		elif sp=="pinterest-pin":
			if re_search('^'+pinterest+'pin/\d+$', link)!=None:
				return True
			else:
				return False
		elif sp==None:
			for i in special_starts:
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
		inp = re_search('https://w11.mangafreak.net/(M|m)anga/([^\?]*)',link)

		if inp!=None:
			title=inp.group(2)

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
					leach_logger("%s||f-Stop||did not ans Mangafreak chapter no")
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
					leach_logger(self.Project+"||f-Stop||tried to ans Mangafreak chapter no||"+str(last_ch))
					return 0


		self.sub_dirs.append(parse.unquote(html_unescape(title)).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))
		for i in range(1,last_ch+1):
			self.all_list.add(("http://images.mangafreak.net:8080/downloads/"+title+'_'+str(i),0))

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

		leach_logger("Project||"+self.Project+"||finished||Total files||"+str(self.total)+'||total errors||'+str(self.errors), user_name)

		if self.errors>0:
			if os_exists('Data/leach_projects/'+self.project_dir+'/errors.txt'):
				with open('Data/leach_projects/'+self.project_dir+'/errors.txt') as f:
					err_file=f.read().strip().split('\n')
				if self.break_all:
					return 0
				errs= [eval(i)[:2] for i in err_file if i!='']

				self.distribute(errs,11, is_error= True)
			else:
				print("Warning: Error file not found!\nPossible cause: Data corruption")
		leach_logger("Project||"+self.Project+"||finished||Total files||"+str(self.total)+'||total errors||'+str(self.errors), user_name)
		if self.dl_done==False:
			writer(self.project_dir+'.proj','a','dl_done = True\n','Data/leach_projects','10008')
		else: print("\nPlease retry some time later to get higher chances to download some or all %d missing file/s"%self.errors)
		print('\n\nEnter "x" to open the first page\n or just press Enter to continue: ')
		self.dl_done=True
		
	def main(self):      #func_code= 10009
		"""runs the mainloop of the projects runtime code"""
		#self.__init__()


		while True:
			try:
				self.Project=safe_input('\nEnter Batch download directory (Project name): ')
			except LeachICancelError:
				print("\n\u001b[33;1mCancellation command entered.\nExiting peacefully\u001b[0m")
				leach_logger("User Exit-0")
				exit(0)
			if self.Project=='':
				print('You must enter a Project name here.')
			else:
				break
		self.project_dir=self.Project[:].replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
		leach_logger("project||%s||began"%(self.Project),user_name)
		if self.Project in open('data/projects.db').read().split('\n'):
			print('Existing Project name found!')
			proj_good=False
			list_good=False

			if os_exists('Data/leach_projects/'+self.project_dir+'.proj') and os_exists('Data/leach_projects/'+self.project_dir+'.list'):
				proj_good= True
				try:
					with open('Data/leach_projects/'+self.project_dir+'.proj') as f:
						print('db found')

						existing_data=f.read().strip().split('\n')
					try:
						global main_link, link_startswith, file_types, sub_dirs, sp_flags, sp_extension, overwrite_bool, dimention, dl_done
						dl_done=False
						for i in existing_data:
							exec(i, __main__.__dict__)
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

						del main_link, link_startswith, file_types, sub_dirs, sp_flags, sp_extension, overwrite_bool, dimention, dl_done
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
						except:
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
					with open('Data/leach_projects/'+self.project_dir+'.list') as f:
						try:
							file=f.read()

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

					if self.dl_done:
						print('It seems  the old prject download was complete!!')
						try:
							temp= asker('Do you want to get updated data from the project link?\nIf you want make a fresh start with that project name type \033[1;30;43mno\033[0m\n>> ') #'Do you want make a fresh start with that project name??\n\033[1;33mWarning!\033[0m last project data will be erased\n(downloaded files will be safe, unless the program replaces the files with new ones)\n\033[32m>> \033[0m'):
						except LeachICancelError:
							print("\n\u001b[33;1mCancellation command entered.\nReturning to main options\u001b[0m")
							leach_logger("%s||f-Stop||don't want to update proj or anything"%self.Project)
							return 0

						if temp:
							writer(self.project_dir+'.list','w','','Data/leach_projects','10009')
							writer(self.project_dir+'.proj','w','','Data/leach_projects','10009')
							self.existing_found= False
							self.update= True
							self.overwrite_bool=False
						else:
							#print("Okay! Enter a new project name in the next line.")
							self.existing_found= False
							leach_logger('project||%s||fresh start||was done'%self.Project,user_name)
							#remove('Data/leach_projects/'+self.project_dir+'/')
						del temp
					else:
						try:
							temp= asker("Do you want to resume the Project '%s'?\nyes/y to resume\nno/n to Start fresh (\033[1;33mwarning! last project data will be erased \033[0m(downloaded files will be safe, unless the program replaces the files with new ones)\n\033[32m>> \033[0m"%self.Project)
						except LeachICancelError:
							print("\n\u001b[33;1mCancellation command entered.\nReturning to main options\u001b[0m")
							leach_logger("%s||f-Stop||don't want to resume proj or anything"%self.Project)
							return 0

						if temp:
							print('============ Reloaded =============')
							leach_logger('project||%s||resumed||not done'%self.Project,user_name)
							self.existing_found= True
						else:
							leach_logger('project||%s||fresh start||not done'%self.Project,user_name)
							#clear file data
							writer(self.project_dir+'.list','w','','Data/leach_projects','10009')
							writer(self.project_dir+'.proj','w','','Data/leach_projects','10009')
							self.existing_found= False
						del temp


					#print('error')


				#download_files(listx,state)
			else:
				# self.existing_found=0
				print('Insufiicient Data!\n')
				self.corruptions+=[0]

		if self.existing_found==False:
			if self.update:
				rmdir('Data/leach_projects/'+self.project_dir)
				self.sub_dirs=[]
				sub_links=[]
				self.all_list=set()
				self.dl_done=False
				if not self.check_sp_links(self.main_link,'nh'):
					try:
						page =requests.get(self.main_link, headers=header_(), timeout=5)
						link_true=True
					except (requests.exceptions.MissingSchema,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
						print("\033[1;31;40mLink unreachable! \033[0m(possible cause: no internet or dead link)\n\nReturning to main page")

				if self.check_sp_links(self.main_link,'mangafreak'):
					print("Update isn't available for mangafreak")
					try:
						if asker('Do you want to re-download files from the same link?'):
							will_unzip=asker("\nThe download files are in zip format.\nDo you wish to Extract them?\n>> ")

							if will_unzip:
								self.sp_flags.append("dl unzip")
								if asker("Shall I delete the downloaded zip files?\n>> "):
									self.sp_flags.append("del dl zip")
							self.link_startswith= self.mangafreak_link(self.main_link)
							if self.link_startswith== 0: # cancel code
								return 0

							
							self.file_types=('zip',)
							self.file_starts=''

							leach_logger('project||%s||is_mangafreak||%s'%(self.Project,str(self.sp_flags)),user_name)
						
					except LeachICancelError:
						print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
						leach_logger("%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0

				elif self.check_sp_links(self.main_link,'nh'):
					self.link_startswith, title=self.nhantai_link(self.main_link)

					if self.link_startswith==0 and title==0:
						print("Failed to get data from %s\nReturning back to main page."%self.main_link)
						return 0

					if title!=False and self.link_startswith!='':
						#sub_dirs.append(title.replace('/','-').replace('?','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))

						leach_logger('project||%s||is_nh'%(self.Project),user_name)

				else:
					sub_links2=[]
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
						
							leach_logger('project||%s||dimention||%s)'%(self.Projec,self.dimention), user_name)

						if self.dimention==1 or self.dimention==3:
							sub_links2+=[self.main_link]
						if self.dimention==2 or self.dimention==3:
							soup=bs(page.content, parser)
							# link_startswith=input("\n(optional but recomanded to be more precice):\n1. Sub-Links Starts With : ")
							leach_logger('project||%s||l_starts||%s)'%(self.Project, self.link_startswith), user_name)
							sub_links2+=list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a')]))

						for i in sub_links2:
							if i.startswith('//'): i='https:'+i

							if  self.partial_do_all==0 and i.startswith('/'):
								print("Partial link detected - ",self.main_link,"\nSearching for home page.")
								#print(start)
								self.homepage =self.homepage_searcher.search(self.link_startswith)
								#print(homepage)
								
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
								i=self.homepage+i
							elif self.partial_do_all==1 and i.startswith('/'):
								i=self.homepage+i

							if link_startswith_re.search(i)!=None:
								sub_links.append(i)
							#print(sub_links)
						del sub_links2
								
					except LeachICancelError:
						print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
						leach_logger("%s||f-Stop||asking4home||user probably freaked out for too much Ques"%self.Project)
						return 0
					





			else:
				if self.corruptions!=[]:
					if os_exists('Data/leach_projects/'+self.project_dir+'.proj'):
						leach_logger("project||%s||%s||%s"%(self.Project,  str(self.corruptions),open('Data/leach_projects/'+self.project_dir+'.proj').read().replace('\n','>>')), user_name)
					else:
						leach_logger("project||%s||%s"%(self.Project, str(self.corruptions)), user_name)
				writer('errors.txt', 'a','','Data/leach_projects/'+self.project_dir,'10009') #reset error file


				self.all_list=set()
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
					leach_logger('%s||m_link||%s)'%(self.Project, self.main_link), user_name)
					while link_true==False:
						if self.check_sp_links(self.main_link,'nh'):
							break
						try:
							page =requests.get(self.main_link, headers=header_(), timeout=5)
							link_true=True
							writer(self.project_dir+'.html','wb',page.content,'Data/leach_projects/%s'%self.Project,'10009')
						except (requests.exceptions.MissingSchema,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
							self.main_link=safe_input("\033[1;31;40mInvalid URL! \033[0m(possible cause: no internet or wrong link)\n\nPlease re-enter the link: ")
				

					if self.check_sp_links(self.main_link,'mangafreak'):
						print("mangafreak link detected!!")
						is_mangafreak=asker("Do you want to download manga images from this links?? (y/n)\n>> ")
						if is_mangafreak:
							will_unzip=asker("\nThe download files are in zip format.\nDo you wish to Extract them?\n>> ")

							if will_unzip:
								self.sp_flags.append("dl unzip")
								if asker("Shall I delete the downloaded zip files?\n>> "):
									self.sp_flags.append("del dl zip")
							self.link_startswith= self.mangafreak_link(self.main_link)
							self.file_types=('zip',)
							self.file_starts=''

							leach_logger('project||%s||is_mangafreak||%s'%(self.Project,str(self.sp_flags)),user_name)
							# sub_links=''
							#exit(0)

					if  self.check_sp_links(self.main_link,'nh'): #main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
						print("nhentai link detected!!")
						is_nh=asker("Do you want to download doujin images from this links?? (y/n)\n( ͡° ͜ʖ ͡°)\t")
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
								leach_logger('project||%s||is_nh'%(self.Project),user_name)
						'''elif is_nh!='n':
							print('invalid input!! the program will break in 3seconds')
							time.sleep(3)
							raise ValueError'''
					if self.check_sp_links(self.main_link,'pinterest'):
						print("Pinterest link detected.\nDo you want to try the special features for pinterest images?\nWarning: All images may not be the same from the website as you see\n")
						if asker('>>'):

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
						leach_logger('project||%s||dimention||%s)'%(self.Project, self.dimention), user_name)

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
							leach_logger('project||%s||l_starts||%s)'%(self.Project, self.link_startswith), user_name)
							sub_links2+=list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a')]))
							

						file_types_i=safe_input("\nEnter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg,mp3) or just write the category (ie: image, music, video): ")
						if file_types_i=='image':
							self.file_types=img
						else:
							self.file_types= tuple(i.strip(i) for i in file_types_i.split(','))
						leach_logger('project||%s||f_types||%s)'%(self.Project, str(self.file_types)), user_name)

						self.file_starts=safe_input("\nFile Links Starts With (if known or need to be specified): ")
						leach_logger('project||%s||f_starts||%s)'%(self.Project, self.file_starts), user_name)
						# project_path=Project[:]

						#if start[-1'/'): start+='/'
						#if start.startswith(): start=start[1:]
							#sub_dirs=[]
						#len_sub_links=str(len(sub_links))
						# count=0
						print('\n')



						self.sequence=asker("\n\nwill download in sequncial order? ")
						self.overwrite_bool= asker("Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>")

				except LeachICancelError:
					print('\n\u001b[33;1mCancellation command entered, returning to main menu...\u001b[0m\n\n')
					leach_logger("%s||f-Stop||discontinued||user probably freaked out for too much Ques"%self.Project)
					return 0
				#else: all_list=list(all_list)
				#leach_logger("++%s'+'%s'+%s'+'%s'++"%(main_link, link_startswith,str(file_types),file_starts), user_name)

				print("Checking links...")

				link_startswith_re=re_compile('^'+self.link_startswith)

				for i in sub_links2:


					#sys.stdout.flush()
					#print(link)
					# print(i)
					if i.startswith('//'): i='https:'+i
					if self.partial_do_all==0 and i.startswith('/'):
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
							leach_logger("%s||f-Stop||discontinued||user probably freaked out for too much Ques"%self.Project)
							return 0
					elif self.partial_do_all==1 and i.startswith('/'):
						i=self.homepage+i

					if link_startswith_re.search(i)!=None:
						sub_links.append(i)
				#print(sub_links)
				del sub_links2


			if self.sub_dirs==[]:
				if self.sequence: sub_links=sorted(sub_links, key= Nsys.sorting_algo)
				for i in sub_links:
					self.sub_dirs.append(parse.unquote(html_unescape(i)).replace('?','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-'))
				# sub_dirs=sub_links[:]


				len_sub_links= len(sub_links)



				if len_sub_links<4:
					for n in range(len_sub_links):
						self.list_writer(sub_links[n], n)
						if self.sub_dirs[n][-1]=='/':
							self.sub_dirs[n]=self.sub_dirs[n][:-1]
						self.sub_dirs[n]=self.sub_dirs[n].split('/')[-1]
						print('\n')
						delete_last_line()
						print('Indexed ['+ str(n+1) + '/'+str(len_sub_links)+'] '+sub_links[n])

				else:
					sub_range=range(len_sub_links)
					indx1= Process(target=self.list_writer, args=(sub_links, sub_range[::3]))
					indx2= Process(target=self.list_writer, args=(sub_links, sub_range[1::3]))
					indx3= Process(target=self.list_writer, args=(sub_links, sub_range[2::3]))

					try:

						indx1.start()
						indx2.start()
						indx3.start()

						indx1.join()
						indx2.join()
						indx3.join()
					except:
						print("\033[1;31;40mcode: Error 607\n The program will break in 5 seconds\033[0m")
						leach_logger("XXXX Program crashed running: 'indx threads' Error code 607 from main function calling list_writer with threads. Error", user_name)
						time.sleep(5)
						exit(0)



			if self.sequence: self.all_list=sorted(list(self.all_list), key = lambda x: Nsys.sorting_algo(x[0]))
			else: self.all_list= list(self.all_list)

			writer('projects.db','a',self.Project+'\n','data','10009')

			writer(self.project_dir+'.list','w',str(self.all_list),'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','w','main_link= "%s"\n'%self.main_link,'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','link_startswith= "%s"\n'%self.link_startswith,'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','file_types = %s\n'%str(self.file_types),'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','file_starts= "%s"\n'%self.file_starts,'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','sub_dirs = %s\n'%str(self.sub_dirs),'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','sp_flags = %s\n'%str(self.sp_flags),'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','sp_extension = "%s"\n'%self.sp_extension ,'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','overwrite_bool = %s\n'%str(self.overwrite_bool),'Data/leach_projects','10009')
			writer(self.project_dir+'.proj','a','dimention = %s\n'%str(self.dimention),'Data/leach_projects','10009')

		print('\n')
		self.total=len(self.all_list)


		if os_exists('Data/leach_projects/'+self.project_dir+'/errors.txt'):
			self.errors=len(open('Data/leach_projects/'+self.project_dir+'/errors.txt').readlines())
		else:
			self.errors=0

		#print(all_list)


		all_list_r=list(range(self.total))

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


		while any([t11.is_alive(),t2.is_alive(),t3.is_alive(),t4.is_alive(),t5.is_alive(),t6.is_alive(),t7.is_alive(),t8.is_alive(),t9.is_alive(),t10.is_alive(), t99.is_alive()]):
			try:
				will_open= safe_input()
				# print([t11.is_alive(),t2.is_alive(),t3.is_alive(),t4.is_alive(),t5.is_alive(),t6.is_alive(),t7.is_alive(),t8.is_alive(),t9.is_alive(),t10.is_alive(), t99.is_alive()])
			except LeachICancelError:
				self.break_all= True
				leach_logger("%s||f-Break||%i||%i"%(self.Project))
				break
		
		if self.break_all:
			print("\u001b[33;1mProject continuation cancelled by Keyboard\u001b[0m")
			leach_logger("%s||f-Stop||%i||%i"%(self.Project, self.done, self.errors))
		else:
			first_page=make_pages(self.all_list,self.sub_dirs, self.Project)
			if will_open=='x':
				webbrowser.open('file://'+first_page)
		
		
#test mangafreak all files available
'''from os.path import os_isdir
for i in range(1,166):
	if os_isdir('E:/Ratul Codes/C/Python/Test/web ripper/Web-leach/Projects/rent/Kanojo_Okarishimasu/Kanojo_Okarishimasu_%d'%i)==False:
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
leach_logger('//user||%s||login @||%s'%(ush, str(Nsys.dt_())),user_name)


while True:
	program_class = web_leach()
	program_class.main()
