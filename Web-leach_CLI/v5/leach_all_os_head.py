# pylint:disable=W0312
#: *****************************************************************************
#:                The code in this file was created by Ratul Hasan             *
#:                     So complete credit goes to creator(me)                  *
#:       requests, bs4, psutils and comtype Libraries are used in this code     *
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


'''
py -3.7 -m pip freeze > r.txt
py -3.7 -m pip uninstall -r r.txt -y
py -3.7 -m pip install pyinstaller-develop.zip requests  beautifulsoup4 natsort google pypiwin32 comtypes psutil lxml pywin32-ctypes rjsmin
py -3.7 -O -m PyInstaller "leach_win_setup.py" -F -n "Web leach 0.5.5.4" --version-file vtesty.py -i "EMO Angel.ico" --add-data "7z.exe;." --upx-dir=.
'''

requirements_all = ('requests',  'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pypiwin32', 'comtypes', 'psutil', 'lxml', 'pywin32-ctypes')
_VERSION ="5.50005"


							#>>>>>>update>>>>>
						#=========================
#>>>>>used re.compile to speed up (4.0)
#>>>>>added nhentai support with proxy (4.0)
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
#>>>>>download pausable (5.3_class)
#>>>>>backward compatible (5.3_class)
#>>>>>auto webpage generator (5.3_class)
#>>>>>auto localhost creation after login (5.3_class)
#>>>>>generate port based on user hash (5.3_class)
#>>>>>added nhentai.to proxy after nhentai.xxx proxy (5.500001_class)
#>>>>>added hash verification control in _version_update (5.500001_class)
#>>>>>switched backend server code link from raw.git... to https://cdn.jsdelivr.net/ (see https://stackoverflow.com/questions/17341122/link-and-execute-external-javascript-file-hosted-on-github) (5.500002)
#>>>>>(5.4) DEPRICATING https://github.com/Ratulhasan14789/Web-Leach_pub/blob/main/Backend_servers/_global(v5.5+).txt
#>>>>>(5.4) NEW GLOBAL SERVER https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global(v5.5+).txt
#>>>>>(5.4) NEW LOCAL SERVER https://gitcdn.xyz/repo/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update%20(server%20v5.500004).txt
#>>>>>(5.4) TRYING NEW LOCAL SERVER https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update (server v5.500004).txt
#>>>>>(5.4) Added Emojis (on title and runtime)

print("LOADING ASSETS...")

server_version = 'unreached'
import Number_sys_conv as Nsys           #f_code = 20000
# different number based functions I made
start_up_dt = Nsys.compressed_dt() #stores when the program was launched

import time

start_up = time.time()

from platform import system as os_name
os_name = os_name()

if os_name == 'Windows': 
	import console_mod
	console_mod.enable_color() 


from print_text import XprintClass

XprintEngine = XprintClass()
xprint = XprintEngine.slowtype

try:
	import ctypes
	def Ctitle(title):
		"""sets CLI winodw title
		*title: Window title"""

		try:
			ctypes.windll.kernel32.SetConsoleTitleW(title)
		except:
			#print('\33]0;%s\a'%title, end='', flush=True)
			pass

	Ctitle('Loading Assets \u26ef')

	true = True
	false = False



	img = ('jpeg', 'jpg', 'png', 'gif', 'webp', 'bmp', 'tif')


	who_r_u = 'https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
	yamatte = ('https://www.myinstants.com/media/sounds/yamatte.mp3', 'https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3')
	yes = ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yep', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yep', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yep')
	no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
	cond = yes + no
	condERR = "/y/Sorry,  I can't understand what you are saying./=/\n Just type yes or no.   "
	hard_cancel = '/y/Hand Cancel Command entered.\nExiting.../=/'


	__update__G = 'pass'
	__update__L = 'pass'
	user_list = ['bec6113e5eca1d00da8af7027a2b1b070d85b5ea', 'eb23efbb267893b699389ae74854547979d265bd']

	has_all_libs = True
	g_mode = False
	ara_ara = True #to control parody noise
	no_log = False #to stop logging
	death = False
	dying = False

	proxy_port = 0


	class server_code:
		"""creating fake class
		to bypass error"""

		def __init__(self=None):
			pass
		def server_close(self=None):
			pass
		def serve_forever(self=None):
			pass

	death_talk = 0

	sp_arg_flag = {'disable dl cancel' : False,
		      'disable dl get' : False,
		      'ara ara': False if ara_ara == None else ara_ara,
		      'no log': False if no_log == None else no_log,
              'no browser': False,
			  'max dlim': 0, # in kbps
			  'chunk_size': 8192, # in Bytes
			}

	mode_emoji = {
		'online': "🌐",
		'offline': "⚠"
	}

	ara_ara = False #to control parody noise

	# _server_version = "5.5"

	cloud_data_link_global = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global(v5.5+).txt'
	cloud_data_link = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update (server v5.500004).txt'
	user_net_ip = 'offline'


	#########################################################


	# SYS tools #######################
	from sys import exit as sys_exit, executable as sys_executable
	exit = sys_exit
	
	from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
	from os import devnull as os_devnull
	from sys import stdout as sys_stdout
	from importlib import reload
	# from functools import partial
	import atexit, traceback
	sys_write = sys_stdout.write
	del sys_stdout
	###################################

	# MATH tools ######################
	from math import floor
	from random import choice as random_choice, randint
	from hashlib import sha1 as hashlib_sha1, md5 as hashlib_md5
	from re import search as re_search, compile as re_compile, sub as re_sub

	from filesize import alternative as filesize_alt, size as filesize_size


	from rcrypto import encrypt, decrypt
	###################################



	# FILE system tools###############
	from os import makedirs, remove, rename, system as os_system, listdir as os_listdir, getcwd as os_getcwd
	from shutil import rmtree as rmdir, copyfile, move
	from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname, realpath as os_realpath
	from zipfile import ZipFile, BadZipFile
	###################################



	from threading import Thread as Process



	# HTML tools##############################
	from html import unescape as html_unescape, escape as html_escape
	from urllib import parse
	import webbrowser

	try:
		from bs4 import BeautifulSoup as bs
		parser = 'lxml'
		try:
			bs('<br>', parser)
		except:
			parser = 'html.parser'
		from googlesearch import search as g_search
		import requests, natsort, urllib3
		import _server001_
		if os_name == 'Windows': import mplay4

	except:
		has_all_libs = False


	from headers_file import header_list        # f_code = 30000
	##########################################

	#Other Libs###############################
	from collections import Counter
	import functools
	import operator


	import dig_info

	##########################################
except KeyboardInterrupt:
	xprint(hard_cancel)
	import sys
	sys.exit(0)
except EOFError:
	xprint(hard_cancel)
	import sys
	sys.exit(0)


# Re Define to speed up###################
len = len
range = range
##########################################

process_id = randint(2003, 9999) # a process ID to identify use multiple windows in the same time from log

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



# import __main__ # used to load assets in global (idea from pydroid)

# ✓
# ✘

def remove_duplicate(seq, return_type = list):	#func_code= 00000  vvv
	"""removes duplicates from a list or a tuple
	also keeps the array in the same order

	args:
	-----
		seq: `tuple`|`list` to remove dups
		return_type: type of array to return"""

	return return_type(dict.fromkeys(seq))

def trans_str(txt, dicts): #func_code= 00019 vvv
	"""replaces all the matching charecters of a string for multuple times

	args:
	-----
		txt: string data
		dicts: dict of { find : replace }"""

	for i in dicts.keys():
		a = dicts[i]
		for j in i:
			txt = txt.replace(j, a)
	return txt

def clear_screen():    #func_code= 00001 vvv
	"""clears terminal output screen"""

	if os_name == "Windows":
		os_system('cls')
	else:
		os_system('clear')



def delete_last_line(lines=1):      #func_code=00002 vvv
	"""Use this function to delete the last line in the STDOUT

	args:
	-----
		lines: total number of lines *1"""

	for _ in range(lines):
		#cursor up one line
		sys_write('\x1b[1A')

		#delete last line
		sys_write('\x1b[2K')


def remove_non_ascii(text, f_code):    #func_code=00003 vvv
	"""[DEPRECATED] [STILL WORKS] removes ascii charecters from a string

	args:
	-----
		test: text to remove non ASCII
		f_code: The function Code called this function"""

	try:
		return ''.join([i if ord(i) < 128 else '' for i in text])
	except Exception as e:
		xprint("Failed to remove non-ascii charecters from string.\nError code: 00003x", f_code, '\nPlease inform the author.')
		leach_logger('00003||' + e.__class__.__name__ + ('||%s||'%str(e)) + f_code + '||' + text)

def remove_non_uni(text, f_code='?????', types= 'str', encoding= 'utf-8'):    #func_code=00018  vv
	"""Converts a string or binary to unicode string or binary by removing all non unicode char

	args:
	-----
		text: str to work on
		f_code: caller func code
		types: output type ('str' or 'bytes')
		encoding: output encoding *utf-8"""

	try:
		if type(text) == str:
			text = text.encode(encoding, 'ignore')
			if types == 'bin': return text
			return text.decode(encoding)
		if types == 'bin': return text.decode(encoding, 'ignore').encode(encoding)
		return text.decode(encoding, 'ignore')
	except Exception as e:
		xprint("/r/Failed to remove non-Unicode charecters from string.\nError code: 00018x", f_code, '/y/\nPlease inform the author./=/')
		leach_logger('00018||' + e.__class__.__name__ + ('||%s||'%str(e)) + f_code + '||' + types + '||' + text)
		return remove_non_ascii(text, f_code)

def header_():    #func_code=00004  v
	"""returns a random header from header_list for requests lib"""

	return( {'User-Agent':random_choice(header_list)})

def install(pack, alias=None):    #func_code=00005  v
	"""Just install package

	args:
	-----
		pack: the name the library (beautifulsoup4, requests)
		alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

	if alias == None:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install", '--disable-pip-version-check', '--quiet', alias])


import pkg_resources as pkg_r
# installed_pkgs=[pkg.key for pkg in pkg_resources.working_set] # list of installed packages

# print(pkg_resources)

def install_req(pkg_name, alias=None):     #func_code=00006  vv
	"""install requirement package if not installed

	args:
	-----
		pkg_name: Package name to search if installed
		alias: if the pip package name is different from lib name,
			then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """


	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
		xprint("/y/Installing missing libraries/=/")
		install(pkg_name, alias)
		delete_last_line()
	reload(pkg_r)
	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
		xprint('/r/Failed to install and load required Library: "%s"/y/\nThe app will close in 5 seconds/=/'%pkg_name)
		try: leach_logger('00006||%s||%s'%(pkg_name, str(check_internet("https://pypi.org", '00006'))))
		except NameError: pass
		return False
	return True

##############################################
				# Checks and Installing missing libraries
##############################################
if os_name == 'Windows':
	if not 'psutils' in (pkg.key for pkg in pkg_r.working_set):
		has_all_libs = False

if has_all_libs == False:
	for i in requirements_all:
		if not install_req(i):
			time.sleep(5)
			exit()

	if os_name == "Windows":
		for i in requirements_win:
			if not install_req(i):
				time.sleep(5)
				exit()    #required in mplay4

	from bs4 import BeautifulSoup as bs
	parser = 'lxml'
	try:
		bs('<br>', parser)
	except:
		parser = 'html.parser'
	from googlesearch import search as g_search
	import requests, natsort
	import _server001_
	if os_name == "Windows": import mplay4


def loc(x, _os_name='Linux'):    #func_code=00007  v
	"""to fix dir problem based on os

	args:
	-----
		x: directory
		os_name: Os name *Linux"""

	if _os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')


def writer(fname, mode, data, direc=None, f_code='None',
			encoding='utf-8'):    #func_code=00008  v
	"""Writing on a file

	args:
	-----
		fname: filename
		mode: write mode (w, wb, a, ab)
		data: data to write
		direc: directory of the file, empty for current dir *None
		func_code: (str) code of the running func *empty string
		encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""

	if mode in ('r', 'rb'):
		# can't write with just read modes
		xprint('/r/Invalid mode\nMust be a Writable Mode/=/')

	if any(i in fname for i in ('\\|:*"><?')):
		# these charecters are forbidden to use in file or folder Names
		leach_logger('00008x1||%s'%fname)
		fname = trans_str(fname, {'/\\|:*><?': '-', '"':"'"})


	if direc == None:
		direc = './'
	# directory and file names are auto stripped by OS
	direc = direc.strip()
	fname = fname.strip()

	try:
		if direc == None:
			if 'b' not in mode:
				with open(fname, mode, encoding=encoding) as file:
					file.write(data)
			else:
				with open(fname, mode) as file:
					file.write(data)
		else:
			locs = loc(direc, 'Linux')
			if any(i in locs for i in ('\\|:*"><?')):
				leach_logger('00008x2||%s'%locs)
				locs = trans_str(locs, {'\\|:*><?': '-', '"':"'"})

			if not os_isdir(locs):
				# creates the directory, then write the file
				try:
					makedirs(locs)
				except FileExistsError: pass
				except Exception as e:
					if e.__class__.__name__ == "PermissionError":
						_temp = ''
						_temp2 = locs.split('/')
						_temp3 = 0
						while True:
							_temp += _temp2[_temp3] + '/'
							if not os_isdir(_temp): break
						leach_logger('00008x101||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, _temp))
						del _temp, _temp2, _temp3
					raise e
			if locs.endswith('/'): direc = loc(locs + fname)
			else: direc = loc(locs + '/' + fname)

			if 'b' not in mode:
				with open(direc, mode, encoding=encoding) as f:
					f.write(data)
			else:
				with open(direc, mode) as f:
					f.write(data)

	except Exception as e:
		if e.__class__.__name__ == "PermissionError":
			xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc == None else direc, '/y/\nPlease inform the author. Error code: %sx101/=/'%f_code)
			leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
			raise LeachPermissionError
		else:
			leach_logger('00008x-1||' + e.__class__.__name__ + '||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, str(e)))
			xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc == None else direc, '/y/\nPlease inform the author. Error code: 00008x' + f_code, '/=/')
			raise e



def hdr(header, f_code=''):    #func_code=00009  v
	"""returns the index of a header

	args:
	-----
		header: header dict
		f_code: function caller code"""

	try:
		return str(header_list.index(header['User-Agent']))
	except ValueError as e:
		xprint("/y/DATA CORRUPTION found\nError code: 00009x" + f_code, '/=/')

		leach_logger('00009x' + f_code + '||' + str(e) + '||' + header)
		return str((-1, header))

	except Exception as e:
		xprint("/y/Some error occurred caused, possible cause: DATA CORRUPTION\nError code: 00009x" + f_code, '/=/')

		leach_logger('00009x-1||' + '||' + f_code + e.__class__.__name__ + '||' + str(e) + '||' + header)
		return str((-1, header))


def leach_logger(io, key='lock'):   #func_code=0000A  v
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the begining)

	args:
	-----
		io: the log message\n
		key: salt text"""

	if sp_arg_flag['no log']:
		return None
	try:
		while True:
			try:
				try:
					_key = "Asuna"
					salt = hashlib_sha1(key.encode()).hexdigest()
					writer('userlog.leach', 'ab', encrypt(salt + ('%s||'%Nsys.compressed_dt()) + str(process_id) + '||' + io + '||', _key).encode('utf-8') + b'\n', 'data', '00008')
					break
				except EOFError: pass
				except KeyboardInterrupt: pass
			except EOFError: pass
			except KeyboardInterrupt: pass

	except EOFError: leach_logger(io, key='lock')
	except KeyboardInterrupt: leach_logger(io, key='lock')


#################### CONNECT TO THE NET FOR THE FIRST TIME #################

def run_server(port, cd=None, f_code= '00000'):      #func_code=0000B  v
	"""Runs localhost server using python.\n
	the I/O is suppressed

	args:
	-----
		port : PORT number\n
		cd : the directory to host
		f_code: caller id"""

	if cd!=None and type(cd)!=str:
		temp = type(cd)
		try:
			cd = str(cd)
		except:
			cd = '?'
		xprint("/=/Invalid localhost directory. Please inform the author.\nError code: 0000Bx1/=/")
		leach_logger("0000Bx1||%s||%s||%s"%(temp, cd, f_code))
		time.sleep(5)
		sys_exit()

	elif cd!= None and any(i in cd for i in '\\|:*"><?'): # there characters are forbidden
		xprint("/y/Invalid localhost directory. Please inform the author.\nError code: 0000Bx2/=/")
		leach_logger("0000Bx2||%s||%s"%(cd, f_code))
		time.sleep(5)
		sys_exit()

	elif cd!=None and not os_isdir(cd): # invalid missing directory
		xprint('/y/' + cd, "not found!\nPlease inform the author\nError code: 0000Bx3/=/")
		leach_logger("0000Bx3||" + cd + '||' + f_code)
		time.sleep(5)
		sys_exit()

	try:
		if server_status in (False, None):
			if cd!=None:
				return _server001_.run_server(port, cd)
			else:
				return _server001_.run_server(port)
		else:
			return 0
	except EOFError:
		pass
	except KeyboardInterrupt:
		pass

server_running = False
def run_server_t(server_status, cd='./'):      #func_code=0001B  v
	"""Runs server in a thread and returns the thread to server_code

	args:
	-----
		server_status: if its used by web leach or other program:
			`True` -> `web_leach`
			`None` -> none
			`False`-> someone
		cd: Directory to run the server. *`current dir`
	"""

	global server_code, server_running

	if server_status == True:
		return

	port = running_port # user specified port or proxy port

	_t = run_server(port= port, cd= cd)
	if _t!=0:
		server_code = None
		server_code = _t
	else:
		return 0
	try:
		server_running = True
		server_code.serve_forever()

	except OSError:
		exit()
	except:
		pass


def _connect_net():      #func_code=0000C  v
	"""connects to the internet and returns the users global ip

    return: void, but sets global variable `user_net_ip`"""

	global user_net_ip
	current_header = header_()
	try:
		user_net_ip = requests.get('https://api.myip.com/', headers = current_header, timeout=3).content.decode()

	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
		xprint("/r/Error code: 605x1\nNo internet connection!/=/\nChecking Offline mode...")
		leach_logger("605x1||%s||%s"%(hdr(current_header, '0000C'), e.__class__.__name__), 'lock')


	except Exception as e:
		xprint('/r/', e.__class__.__name__, "occurred. Please inform the Author.\nError code: 0000Cx-1(%s)/=/"%e.__class__.__name__)
		leach_logger("0000Cx-1||" + hdr(current_header, '0000C') + '||%s||%s'%(e.__class__.__name__, str(e)), 'lock')
		time.sleep(5)
		exit(0)


def run_in_local_server(port, host_dir=''):     #func_code=0000D  v
	"""opens a directory or a file in localhost server using browser

	args:
	-----
		port : port number
		host_dir : desired file or folder directory"""

	if sp_arg_flag['no browser']: return 0

	webbrowser.open_new_tab('http://localhost:%i/%s'%(port, host_dir))

def import_paste():      #func_code=0001C  v
	"""TODO: will import the upload host lib here"""

	try:pass
		#from pastebin import send_paste
		#current_header index=1
	except requests.exceptions.ConnectionError:
		xprint("/r/40mError code: 605x2\nNo internet connection!\nThe program will break in 5 seconds/=/")
		leach_logger("605x2||header_index=1", 'lock')
		time.sleep(5)
		exit(0)


	# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

	# print(external_ip)
import_paste_t = Process(target=import_paste)

import_paste_t.start()

boss = 0


def go_prev_dir(link):    #func_code=0000E  v
	"""returns the previous path str of web link or directory
	warning: returns only in linux directory format
	-------"""

	link = loc(link, 'Linux')
	if link.endswith('/'):
		return '/'.join(link[:-1].split('/')[:-2]) + '/'
	else:
		return '/'.join(link.split('/')[:-2]) + '/'



# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
def safe_input(msg='', i_func=input, o_func=xprint,
				on_error= LeachICancelError):     #func_code=0000F  v
	"""gets user input and returns str

	args:
	-----
		msg: the message to show for asking input *`empty string`
		i_func: the function used for input *`input()`
		o_func: the function used for msg print *`xprint()`
		on_error: What to do when `^C` pressed *`raise LeachICancelError` or `return None`"""

	o_func(msg, end='')
	try:
		try:
			try:
				box = i_func()
				return box
			except EOFError:
				if on_error == LeachICancelError:
					raise LeachICancelError
				else:
					return on_error
			except KeyboardInterrupt:
				raise LeachICancelError
			except LeachICancelError:
				leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
				exit(0)
		except EOFError:
			if on_error == LeachICancelError:
				raise LeachICancelError
			else:
				return on_error
		except KeyboardInterrupt:
			if on_error == LeachICancelError:
				raise LeachICancelError
			else:
				return on_error
	except EOFError:
		if on_error == LeachICancelError:
			raise LeachICancelError
		else:
			return on_error
	except KeyboardInterrupt:
		if on_error == LeachICancelError:
			raise LeachICancelError
		else:
			return on_error
safe_input
def asker(out='', default=None, True_False=(True, False),
		  extra_opt=tuple(), extra_return=tuple(),
		  i_func=input, o_func=xprint, on_error= LeachICancelError,
		  condERR= condERR, no_bool = False):      #func_code=00010  v
	"""asks for yes no or equivalent inputs

	args:
	-----
		out: `xprint` text to ask tha question *`empty string`
		default: default output for empty response *`None`
		True_False: returning data instead of true and false *`(True, False)`
		extra_opt: Add additional options with Yeses and Nos *must be array of single options*
		extra_return: Returns output according to `extra_ops`
		i_func: the function used for input *`input()`
		o_func: the function used for msg print *`xprint()`
		on_error: What to do when `^C` pressed *`raise LeachICancelError` or `return None`
		no_bool: won't take yes no as input [extras required] *`False`"""

	if len(extra_opt)!=len(extra_return):
		xprint('/r/Additional options and Additional return data don\'t have equal length/=/')
		raise LeachKnownError


	if no_bool:
		if len(extra_opt)<1:
			xprint('/r/With no_bool arg, you must give at least 1 extra option [extra_arg & extra_return]/=/')
			raise LeachKnownError

	Ques2 = safe_input(out, i_func, o_func, on_error).lower()
	if default!= None and Ques2 == '':
		return default
	#Ques2 = Ques2
	while Ques2 not in (tuple() if no_bool else cond) + Nsys.flatten_array(extra_opt, tuple):
		Ques2 = safe_input(condERR, i_func, o_func, on_error).lower()
		#Ques2 = Ques2

	if not no_bool and Ques2 in cond:
		if Ques2 in yes:
			return True_False[0]
		else:
			return True_False[1]
	else:
		return extra_return[extra_opt.index(Ques2)]



def get_file_name(directory, mode= 'dir'):      #func_code=00011  v
	"""takes a file directory and returns the last last part of the dir (can be file or folder)

	args:
	-----
		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory
	"""

	if isinstance(directory, bytes): directory = directory.decode()
	if mode == 'url':
		fragment_removed = directory.split("#")[0]  # keep to left of first #
		query_string_removed = fragment_removed.split("?")[0]
		scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
		if scheme_removed.find("/") == -1:
			return ""
		return os_basename(scheme_removed)
	elif mode == 'dir':
		return os_basename(directory)
	else:
		raise ValueError



def get_file_ext(directory, mode='dir', no_format='noformat'):      #func_code=00012  v
	"""to get the extension of a file directory

	args:
	-----
		directory: file directory relative or direct
		no_format: returning format if no file extention was detected *noformat"""

	temp = get_file_name(directory, mode)
	if len(temp.split('.')) == 1:
		return no_format
	else:
		return temp.split('.')[-1]

def get_dir(directory, mode='dir'):      #func_code=0001D  v
	"""takes a file directory and returns the last last part of the dir (can be file or folder)

	args:
	-----
		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory (os based)
	"""

	if mode == 'url':
		fragment_removed = directory.split("#")[0]  # keep to left of first #
		query_string_removed = fragment_removed.split("?")[0]
		scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]

		dirs = scheme_removed.split('/')
		if dirs[-1] == '':
			dirs.pop()
		if dirs == []:
			return '__HomePage__'
		else:
			return dirs[-1]
	elif mode == 'dir':
		if os_basename(directory) == '':
			return os_basename(os_dirname(directory))
		else:
			return os_basename(directory)
	else:
		raise ValueError

def get_link(i, current_link, homepage):		#func_code= 0001E  v
	"""Gets permanent link from relative link.

	Args:
	-----
		i : relative link
		current_link : the link used for getting links inside the page
		homepage : the homepage of the current_link

	Returns:
	--------
		str: permanent link
	"""
	if i.startswith('#'): i = current_link
	elif i.startswith('//'): i = 'https:' + i

	elif i.startswith('../'):
		_temp = current_link
		while i.startswith('../'):
			_temp = go_prev_dir(_temp)
			i = i.replace('../', '', 1)
		i = _temp + i
		del _temp

	elif i.startswith('/'):
		i = homepage + i
	if '//' not in i:
		temp = homepage
		if temp.endswith('/'):
			if i.startswith('/'): i = temp + i[1:]
			else: i = temp + i
		else:
			if i.startswith('/'): i = temp + i
			else: i = temp + '/' + i

	return i


def reader(direc, read_mode='r', ignore_error= False, output = None,
			encoding = 'utf-8', f_code= '?????', on_missing= None,
			ignore_missing_log = False):      #func_code=00013  v
	"""reads file from given directory. If NOT found, returns `None`

	args:
	-----
		direc: file directory
		read_mode: `r` or `rb` *`r`
		ignore_error: ignores charecter encoding errors *`False`
		output: output type `bin`/`str`/`None` to auto detect *`None`
		encoding: read encoding charset *`utf-8`
		func_code: calling function *`?????`
	"""

	if type(read_mode)!=str:
		print("Invalid read type. Mode must be a string data")
		raise TypeError
	if read_mode in ('w', 'wb', 'a', 'ab', 'x', 'xb'):
		xprint("/r/Invaid read mode:/=/ %s is not a valid read mode.\nTry using 'r' or 'rb' based on your need/=/")
		raise LeachKnownError
	if 'b' in read_mode:
		read_mode ='rb'

	else:
		read_mode = 'r'

	if (not os_isfile(loc(direc))):
		if (not ignore_missing_log):
			print(loc(direc), 'NOT found to read. Error code: 00013')
			leach_logger('00013||' + f_code + '||' + direc)
		return on_missing

	with open(loc(direc), read_mode) as f:
		out = f.read()
	if output == None:
		if read_mode == 'r':
			output = 'str'
		else:
			output = 'bin'
	if ignore_error:
		out = remove_non_uni(out, '00013', output)

	else:
		if output == 'str' and read_mode == 'rb':
			out = out.decode()
		elif output == 'bin' and read_mode == 'r':
			out = out.encode(encoding)

	return out
#print(os_isdir('data/leach_projects/Sao manga rip'))

	# print(io == decrypto.decrypt(encrypt(io, key), key))


# print(requests.get('https://ident.me', headers=headers).content)
# user_net_ip = requests.get('https://ident.me', headers = headers).content.decode()
# print(user_net_ip)


def _version_updater(_latest_version, _latest_link, _latest_hash,
					_latest_filename, _latest_size, server_link):      #func_code=00014  v
	"""Downloads and installs latest version of app
    also verifies zip and exe file"""
	print("An update available v" + _latest_version + "(" + _latest_size + "), Do you want to update? ")
	try:
		reply = asker()
	except LeachICancelError:
		xprint('\n/yh/Cancellation command entered. Skipping update!/=/\n')
		leach_logger("update-prompt||f-Exit-ask")
		return 0
	if reply:
		print('\nConnecting...')
		leach_logger("201||" + str(_latest_version) + '||' + _latest_link + '||' + _VERSION + '||' + server_version, 'lock')
		update_x = time.time()

		#update_filename = 'Web Leach v4.1'
		#import urllib

		# Copy a network object to a local file
		#urllib.urlretrieve(_latest_link, 'data/.temp/' + update_filename + '.zip')
		current_header = header_()

		try:
			update_response = requests.get(_latest_link, stream=True, headers=current_header)
		except Exception as e:
			update_response = False
			leach_logger('202||%s||%s||err:%s'%(_latest_link, hdr(current_header, '00014'), str(e.__class__.__name__)), 'lock')

		delete_last_line()
		if update_response!=None:
			update_total_length = update_response.headers.get('content-length')
			with open('data/.temp/' + _latest_filename + '.zip', "wb") as f:
				if update_total_length is None: # no content length header
					f.write(update_response.content)
				else:
					_dl = 0
					update_total_length = int(update_total_length)
					for data in update_response.iter_content(chunk_size=4096):
						_dl += len(data)
						f.write(data)
						update_done = int(50 * _dl / update_total_length)
						print("\r[\u001b[1;32m%s%s\u001b[0m]" % ('=' * update_done, ' ' * (50-update_done)), end='')
			leach_logger("203||" + str(_latest_version))

			print()
			# Open, close, read file and calculate MD5 on its contents

			if '_latest_check_zip_hash' in globals() and _latest_check_zip_hash:
				try:
					_file_name = 'data/.temp/' + _latest_filename + '.zip'
					file_ = reader(_file_name, 'rb')
					md5_returned = hashlib_md5(file_).hexdigest()
					del file_

					if _latest_zip_hash == md5_returned:
						print ("ZIP verified.")

					else:
						leach_logger('209||%s'%md5_returned + "||" + _latest_link + '||' + _latest_version + '||' + server_link)
						remove('data/.temp/' + _latest_filename + '.zip')

				except Exception as e:
					xprint ("/rh/HASH verification failed!./=/ \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
					leach_logger('2FF||' + _latest_link + '||' + _latest_version + '||' + server_link + '||Hashing update ZIP||%s||%s'%(e, e.__class__.__name__))
					remove('data/.temp/' + _latest_filename + '.zip')
					raise LeachCorruptionError


			print("\nUnzipping...")
			server_fucked = False
			with ZipFile('data/.temp/' + _latest_filename + '.zip') as zf:
				if list(zf.namelist()) != [_latest_filename + '.exe']:
					server_fucked = True
					fucked_list = list(zf.namelist())
					raise LeachCorruptionError

				else:
					subprocess_call(['7z.exe', 'e', '-odata/.temp/', '-y', '-plock', './data/.temp/' + _latest_filename + '.zip'], stdin=open(os_devnull), start_new_session=True, stdout=subprocess_DEVNULL, stderr=subprocess_DEVNULL)


			if server_fucked:
				leach_logger("204||" + _latest_link + '||' + _latest_version + '||' + server_link + '||' + str(fucked_list))
				remove('data/.temp/' + _latest_filename + '.zip')
				raise LeachCorruptionError

			leach_logger("205||" + str(_latest_version))

			if '_latest_check_exe_hash' in globals() and _latest_check_zip_hash:
				try:
					_file_name = _latest_filename + '.exe'

					_file_name = 'data/.temp/' + _latest_filename + '.exe'
					file_ = reader(_file_name, 'rb')
					md5_returned = hashlib_md5(file_).hexdigest()
					del file_

					if _latest_hash == md5_returned:
						print ("EXE verified. \n\nPlease use the latest file '" + _latest_filename + ".exe'\n this program will break in 7 seconds\n\n")
						leach_logger("206")
						move('data/.temp/' + _latest_filename + '.exe', './' + _latest_filename + '.exe')

						leach_logger('207')

						time.sleep(7)
						exit(0)
					else:
						leach_logger('208||%s'%md5_returned + "||" + _latest_link + '||' + _latest_version + '||' + server_link)
						remove('data/.temp/' + _latest_filename + '.zip')
						remove('data/.temp/' + _latest_filename + '.exe')
						raise LeachCorruptionError
				except Exception as e:
					xprint ("/rh/HASH verification failed!./=/ \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
					leach_logger('2FF||' + _latest_link + '||' + _latest_version + '||' + server_link + 'Hashing update EXE||%s||%s'%(e, e.__class__.__name__))
					remove('data/.temp/' + _latest_filename + '.zip')
					remove('data/.temp/' + _latest_filename + '.exe')
					raise LeachCorruptionError
		elif update_response!=False:
			print("Failed to connect to the host server.\nPlease inform the author!!\nError code 202")
			leach_logger('202||%s||%s||code:%s'%(_latest_link, hdr(current_header, '00014'), str(update_response.status_code)), 'lock')


def god_mode():      #func_code=00015  v
	global __update__G, __update__L
	if os_isdir('data/projects'): rename('data/projects', 'data/leach_projects')
	if os_isdir('./projects'): rename('./projects', './Download_Projects')

	if os_name == 'Windows':
		current_header = header_()
		try:
			if not os_isfile('data/.temp/who_r_u.mp3'):
				file = requests.get(who_r_u, headers = current_header)
				if file:
					writer('who_r_u.mp3', 'wb', file.content, 'data/.temp', '00015')
				else:
					raise requests.exceptions.ConnectionError

		except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
			xprint("/rh/Error code: 605x3\nNo internet connection!/=/\nRunning offline mode")
			leach_logger("605x3||%s||%s||%s"%(hdr(current_header, '00015'), who_r_u, e.__class__.__name__), 'lock')
			return 'offline'
	current_header = header_()

	try:
		file = requests.get(cloud_data_link, headers=current_header)
		if file:
			writer('updateL.ext', 'wb', file.content, 'data/.temp', '00015')
			exec(decrypt(reader('data/.temp/updateL.ext'), "lock").strip(), globals())
			# time.sleep(500)
		else:
			xprint("/rh/Error code: 605x4\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
			leach_logger("605x4||%s||%s||%s"%(hdr(current_header, '00015'), cloud_data_link, str(file.status_code)), 'lock')
			time.sleep(3)
			return 'offline'

		#remove('data/.temp/update.ext')
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
		xprint("/rh/Error code: 605x4\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
		leach_logger("605x4||%s||%s||%s"%(hdr(current_header, '00015'), cloud_data_link, e.__class__.__name__), 'lock')
		time.sleep(3)
		return 'offline'
	except Exception as e:
		print(e.__class__.__name__, ": Unknown error occurred. Error code 00015x-1\nPlease inform the author.")
		leach_logger("00015x-1||%s||%s||%s"%(e.__class__.__name__, str(e), hdr(current_header, '00015')), 'lock')
		time.sleep(5)
		exit(0)


	try:
		file = requests.get(cloud_data_link_global, headers=current_header)
		if file:
			writer('updateG.ext', 'wb', file.content, 'data/.temp', '00015')
			exec(decrypt(reader('data/.temp/updateG.ext'), "lock").strip(), globals())

		else:
			xprint("/rh/Error code: 605x4\nNo internet connection!/=/\nRunning offline mode in 3 seconds...")
			leach_logger("605x4||%s||%s||%s"%(hdr(current_header, '00015'), cloud_data_link_global, str(file.status_code)), 'lock')
			time.sleep(3)
			return 'offline'

	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
		xprint("/rh/Error code: 605x4\nNo internet connection!/=/\nRunning offline mode in 3 seconds...")
		leach_logger("605x4||%s||%s||%s"%(hdr(current_header, '00015'), cloud_data_link, e.__class__.__name__), 'lock')
		time.sleep(3)
		return 'offline'
	except Exception as e:
		print(e.__class__.__name__, ": Unknown error occurred. Error code 00015x-1\nPlease inform the author.")
		leach_logger("00015x-1||%s||%s||%s"%(e.__class__.__name__, str(e), hdr(current_header, '00015')), 'lock')
		time.sleep(5)
		exit(0)


	return 'online'

#def upload_paste(data, f_name):
"""if True:
	api_dev_key= "f7e117d452fed3df6e5cc1ea2eee658a"
	#my_key = PastebinAPI.generate_user_key( ,api_dev_key=api_dev_key, username = "DarKnighTitan", password="147852369aA..")
	x=PastebinAPI.paste(self, api_dev_key=api_dev_key, api_paste_code="hello world", api_user_key = None, paste_name = "hi", paste_format = None, paste_private = None, paste_expire_date = None)
	print(x)
"""




def log_in():      #func_code=00016  v
	global user_name
	if boss!=1:
		userhash = 0
		br = 0
		while True:
			try:
				user_name = safe_input("Enter username: ")
			except LeachICancelError:
				xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
				leach_logger("0x1||00016||Login exit")
				exit(0)
			# print(user_list)
			userhash = hashlib_sha1(user_name.encode()).hexdigest()
			for x in user_list:
				if userhash == x:
					br = 1
					break
			if br == 1:
				break
			else:
				xprint("/rh/User not found!/=/ \nWait a minute! WHO are YOU?!!")
				if os_name == "Windows":
					ex = mplay4.ex_vol
					# mplay4.set_win_vol(60)
					mplay4.load('data/.temp/who_r_u.mp3').play()
				time.sleep(5)
				if os_name == 'Windows':
					mplay4.set_win_vol(ex)
	else:
		userhash = 'eb23efbb267893b699389ae74854547979d265bd'


	if not os_exists('data/projects.db'):
		writer('projects.db', 'a', '', 'data', '00016')
	if userhash == 'eb23efbb267893b699389ae74854547979d265bd':
		g_mode = 'Asuna'
	return userhash

def import_make():      #func_code= 0001F  v
	""" reads and exec() necessary files to create different formats of
	output [ie: html, cbz]
	"""
	try:
		exec(reader('make_html.py'), globals())      # f_code= 40000
	except Exception as e:
		print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
		leach_logger('40000x-1||' + str(e.__class__.__name__) + '||' + str(e))
		time.sleep(5)
		exit()

	try:
		exec(reader('make_cbz.py'), globals())      # f_code= 50000
	except Exception as e:
		print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
		leach_logger('50000x-1||' + str(e.__class__.__name__) + '||' + str(e))
		time.sleep(5)
		exit()

import_make()


def check_internet(link, f_code, timeout=None):       #f_code=00017  v
	"""Check if the connection is available or not

	args:
	-----
		link: link to check for connection status"""
	current_header = header_()
	try:
		if timeout == None: 
			r = requests.head(link, headers=current_header)
		else: 
			r = requests.head(link, headers=current_header, timeout= timeout)

		if r:
			return True
		else:
			leach_logger('00017||%s||%s||%s||%s'%(link, hdr(current_header, '00017'), f_code, str(r.status_code)))
	except (requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
		leach_logger('00017||%s||%s||%s'%(link, hdr(current_header, '00017'), f_code))
		return False
	except KeyboardInterrupt:
		return False
	except EOFError:
		return False

def check_server(link, f_code, timeout=None):       #f_code=0001A  v
	"""Checks if localhost server is running perfectly or the port is occupied

	link: site link with port [adds /?response on request]
	f_code: caller id
	timeout: request timeout
	"""

	try:
		response = requests.get(link + '/root?response')
		if response:
			if response.content.startswith(b'Web-leach'):
				return True
			else:
				return False
		else:
			leach_logger('0001Ax0||%s||%s||%s'%(link, f_code, str(response.status_code)))
			return False
	except (requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
		leach_logger('0001Ax1||%s||%s||%s'%(link, f_code, str(e.__class__.__name__)))
		return 2

	except requests.exceptions.ConnectionError:
		return None # if the port is open

	except KeyboardInterrupt:
		return 2
	except EOFError:
		return 2

def flatten2D(arr):     # f_code=00020
	functools.reduce(operator.iconcat, arr, [])


def remove_noscript(content): # f_code=00021
	"""Removes <noscript> contents from html to fool my app
	
	content: HTML content returned by requests.get().content"""
	return re_sub(b"(?i)(?:<noscript>)(?:.|\n)*?(?:<\/noscript>)", b'', content)
