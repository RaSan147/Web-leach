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
py -3.8 -m pip freeze > r.txt
py -3.8 -m pip uninstall -r r.txt -y
py -3.8 -m pip install pyinstaller requests  beautifulsoup4 natsort google pypiwin32 comtypes psutil lxml pywin32-ctypes rjsmin
py -3.8 -O -m PyInstaller "leach_win_setup.py" -F -n "Web leach 0.5.5.4" --version-file vtesty.py -i "EMO Angel.ico" --add-data "7z.exe;." --upx-dir=.
'''

requirements_all = ('requests',  'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pypiwin32', 'comtypes', 'psutil', 'lxml', 'pywin32-ctypes')
_VERSION ="5.50004"


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
			pass  #print('\33]0;%s\a'%title, end='', flush=True)

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

# def install(pack, alias=None):    #func_code=00005  v
# 	"""Just install package
#
# 	args:
# 	-----
# 		pack: the name the library (beautifulsoup4, requests)
# 		alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """
#
# 	if alias == None:
# 		alias = pack
#
# 	subprocess_call([sys_executable, "-m", "pip", "install", '--disable-pip-version-check', '--quiet', alias])
#
#
# import pkg_resources as pkg_r
# # installed_pkgs=[pkg.key for pkg in pkg_resources.working_set] # list of installed packages
#
# # print(pkg_resources)
#
# def install_req(pkg_name, alias=None):     #func_code=00006  vv
# 	"""install requirement package if not installed
#
# 	args:
# 	-----
# 		pkg_name: Package name to search if installed
# 		alias: if the pip package name is different from lib name,
# 			then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """
#
#
# 	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
# 		xprint("/y/Installing missing libraries/=/")
# 		install(pkg_name, alias)
# 		delete_last_line()
# 	reload(pkg_r)
# 	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
# 		xprint('/r/Failed to install and load required Library: "%s"/y/\nThe app will close in 5 seconds/=/'%pkg_name)
# 		try: leach_logger('00006||%s||%s'%(pkg_name, str(check_internet("https://pypi.org", '00006'))))
# 		except NameError: pass
# 		return False
# 	return True
#
# ##############################################
# 				# Checks and Installing missing libraries
# ##############################################
# if os_name == 'Windows':
# 	if not 'psutils' in (pkg.key for pkg in pkg_r.working_set):
# 		has_all_libs = False
#
# if has_all_libs == False:
# 	for i in requirements_all:
# 		if not install_req(i):
# 			time.sleep(5)
# 			exit()
#
# 	if os_name == "Windows":
# 		for i in requirements_win:
# 			if not install_req(i):
# 				time.sleep(5)
# 				exit()    #required in mplay4
#
# 	from bs4 import BeautifulSoup as bs
# 	parser = 'lxml'
# 	try:
# 		bs('<br>', parser)
# 	except:
# 		parser = 'html.parser'
# 	from googlesearch import search as g_search
# 	import requests, natsort
# 	import _server001_
# 	if os_name == "Windows": import mplay4


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
	global make_pages, make_cbz
	try:
		import rjsmin


		class css_minify():
			def __init__(self):
				# remove comments - this will break a lot of hacks :-P
				self.css1 = re_compile( r'\s*/\*\s*\*/') # preserve IE<6 comment hack .sub( r'\s*/\*\s*\*/', "$$HACK1$$", css )
				self.css2 = re_compile( r'/\*[\s\S]*?\*/') # .sub( r'/\*[\s\S]*?\*/', "", css )
				#css = css.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

				# url() doesn't need quotes
				self.css3 = re_compile( r'url\((["\'])([^\)]*)\1\)') # .sub( r'url\((["\'])([^)]*)\1\)', r'url(\2)', css )

				# spaces may be safely collapsed as generated content will collapse them anyway
				self.css4 = re_compile( r'\s+') # .sub( r'\s+', ' ', css )

				# shorten collapsable colors: #aabbcc to #abc
				self.css5 = re_compile( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)')
				# .sub( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)', r'#\1\2\3\4', css )
				# fragment values can loose zeros
				self.css6 = re_compile( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;')
				# .sub( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;', r':\1;', css )

				self.css7 = re_compile( r'([^{]+){([^}]*)}')
				self.css8 = re_compile( r'(?<=[\[\(>+=])\s+|\s+(?=[=~^$*|>+\]\)])')
				self.css9 = re_compile( r'(.*?):(.*?)(;|$)')


			def css_min(self, css_txt):
				# remove comments - this will break a lot of hacks :-P
				css = self.css1.sub( "$$HACK1$$", css_txt ) # preserve IE<6 comment hack
				css = self.css2.sub( "", css )
				css = css.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

				# url() doesn't need quotes
				css = self.css3.sub( r'url(\2)', css )

				# spaces may be safely collapsed as generated content will collapse them anyway
				css = self.css4.sub( ' ', css )

				# shorten collapsable colors: #aabbcc to #abc
				css = self.css5.sub( r'#\1\2\3\4', css )

				# fragment values can loose zeros
				css = self.css6.sub( r':\1;', css )
				box = []
				for rule in self.css7.findall( css ):

					# we don't need spaces around operators
					selectors = [self.css8.sub( r'', selector.strip() ) for selector in rule[0].split( ',' )]

					# order is important, but we still want to discard repetitions
					properties = {}
					porder = []
					for prop in self.css9.findall( rule[1] ):
						key = prop[0].strip().lower()
						if key not in porder: porder.append( key )
						properties[ key ] = prop[1].strip()

					# output rule if it contains any declarations
					if properties:
						box.append("%s{%s}" % ( ','.join( selectors ), ''.join(['%s:%s;' % (key, properties[key]) for key in porder])[:-1] ))
				return '\n'.join(box)
		cssmin = css_minify()
		css_min = cssmin.css_min


		def return_sub_page(all_list, sub_dirs, page_index, title):
			sub_page_template="""<!DOCTYPE html>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta charset="UTF-8">
		
		<head>
			<title></title>
		
		
			<style type="text/css">
			""" + css_min("""
		
			.container {
				margin: 80px auto;
				width: 400px;
				text-align: center;
			}
		
			#page_title{
				align: center;
				color: #00b7ff;
			}
		
			.paginationA {
				font: bold 20px Arial;
				text-decoration: none;
				background-color: #8a8b8d6b;
				color: #00b7ff;
				padding: 2px 6px 2px 6px;
				border-top: 1px solid #828d94;
				box-shadow: 4px 4px #5050506b;
				border-left: 1px solid #828D94;
			}
		
			#lastleft{
				font-size: 20px;
				font-weight: 600;
				font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
				text-decoration: none;
				color: #06A5EE;
			}
		
			body {
				font-family: Arial, Helvetica, sans-serif;
				position: relative;
				min-height: 100vh;
				background-color: #222;
			}
		
			#pageFormats{
				background-color: rgba(117, 117, 119, 0.507);
				height: 35px;
				width: 140px;
				color:  #3ab7ff;
				font-size: 17px;
				font-family: sans-serif;
				font-weight: 700;
			}
		
			
			#spacer{
				background-color: #222;
				color: #3094BE;
				font-weight: 500;
			}
		
			.containerR {
				display: block;
				position: relative;
				padding-left: 35px;
				margin-bottom: 12px;
				cursor: pointer;
				font-size: 22px;
				-webkit-user-select: none;
				-moz-user-select: none;
				-ms-user-select: none;
				user-select: none;
			}
		
			/* Hide the browser's default radio button */
			.containerR input {
				position: absolute;
				opacity: 0;
				cursor: pointer;
			}
		
			#LARROW:not(.disabled), #RARROW:not(.disabled){
				cursor: pointer;
				color: #C8C3BC;
				background-color: #103c8b;
			}
		
			.disabled{
				cursor: default;
				color: #C8C3BC;
				background-color: #999;
			}
		
		
			#LARROW:not(.disabled):hover, #RARROW:not(.disabled):hover{
				background-color: #6495ED;
				color: #EEE;
			}
		
			/* Create a custom radio button */
			.checkmark {
				position: absolute;
				top: 0;
				left: 0;
				height: 18px;
				width: 18px;
				background-color: #eee;
				border-radius: 60%;
			}
		
			/* On mouse-over, add a grey background color */
			.containerR:hover input ~ .checkmark {
				background-color: #ccc;
			}
		
			/* When the radio button is checked, add a blue background */
			.containerR input:checked ~ .checkmark {
				background-color: #3ab7ff;
			}
		
			/* Create the indicator (the dot/circle - hidden when not checked) */
			.checkmark:after {
				content: "";
				position: absolute;
				display: none;
			}
		
			/* Show the indicator (dot/circle) when checked */
			.containerR input:checked ~ .checkmark:after {
				display: block;
			}
		
			/* Style the indicator (dot/circle) */
			.container .checkmark:after {
				top: 9px;
				left: 9px;
				width: 8px;
				height: 8px;
				border-radius: 50%;
				background: white;
			}
		
			#myImg {
				cursor: pointer;
				transition: 0.3s;
				max-width: 95vw;
			}
		
			/* #myImg:hover {opacity: 0.7;} */
		
			/* The Modal (background) */
			.modal {
				display: none; /* Hidden by default */
				position: fixed; /* Stay in place */
				z-index: 1; /* Sit on top */
				padding-top: 100px; /* Location of the box */
				left: 0;
				top: 0;
				width: 100%; /* Full width */
				height: 100%; /* Full height */
				overflow: auto; /* Enable scroll if needed */
				background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
			}
		
			/* Modal Content (image) */
			.modal-content {
				margin: auto;
				display: none;
				width: 80%;
			}
		
			/* Caption of Modal Image */
			#caption {
				margin: auto;
				display: block;
				width: 80%;
				max-width: 700px;
				text-align: center;
				color: #ccc;
				padding: 10px 0;
				height: 150px;
				overflow-wrap: break-word;
			}
		
			/* Add Animation */
			.modal-content, #caption {
				-webkit-animation-name: zoom;
				-webkit-animation-duration: 0.6s;
				animation-name: zoom;
				animation-duration: 0.6s;
			}
		
			@-webkit-keyframes zoom {
				from {-webkit-transform:scale(0)} 
				to {-webkit-transform:scale(1)}
			}
		
			@keyframes zoom {
				from {transform:scale(0)} 
				to {transform:scale(1)}
			}
		
			/* The Close Button */
			.close {
				position: absolute;
				top: 40px;
				right: 40px;
				color: #f1f1f1;
				font-size: 40px;
				font-weight: bold;
				transition: 0.3s;
			}
		
			.close:hover,
			.close:focus {
				color: #bbb;
				text-decoration: none;
				cursor: pointer;
			}
		
			/* 100% Image Width on Smaller Screens */
			@media only screen and (max-width: 700px){
				.modal-content {
				width: 100%;
				}
			}
		
			.popup .overlay {
				position:fixed;
				top:0px;
				left:0px;
				width:100vw;
				height:100vh;
				background:rgba(0,0,0,0.7);
				z-index:1;
				display:none;
			}
		
			.popup .content {
				position:fixed;
				top:50%;
				left:50%;
				color: #AAA;
				transform:translate(-50%,-50%) scale(0);
				background:#222;
				width:500px;
				height:250px;
				z-index:2;
				text-align:center;
				padding:20px;
				box-sizing:border-box;
				font-family:"Open Sans",sans-serif;
			}
		
			.popup .close-btn {
				cursor:pointer;
				position:absolute;
				right:20px;
				top:20px;
				width:30px;
				height:30px;
				background:#222;
				color:#fff;
				font-size:25px;
				font-weight:600;
				line-height:30px;
				text-align:center;
				border-radius:50%;
			}
		
			.popup.active .overlay {
				display:block;
			}
		
			.popup.active .content {
				transition:all 300ms ease-in-out;
				transform:translate(-50%,-50%) scale(1);
			}
		
			#button {
				position:absolute;
				top:50%;
				left:50%;
				transform:translate(-50%,-50%);
				padding:15px;
				font-size:18px;
				border:2px solid #222;
				color:#222;
				text-transform:uppercase;
				font-weight:600;
				background:#fff;
			}
		
			#go2main{
				font-size: 20px;
				font-weight: 600;
				font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
				text-decoration: none;
				color: #06A5EE;
			}
		
			#footer {
				position: absolute;
				bottom: 0;
				width: 100%;
				height: 2.5rem;            /* Footer height */
			}
			""") + """
			</style>
			</head>
			
			<body>
			<div id="contents">
		
			<div align="center"><h2 id="page_title"></h2></div>
		
		
			<div id='customize_tools' style="margin: 4%%;">
			<a id='go2main'>Go to Page list</a>
			<h4 style="color: #dbdee0d5;">Customize Your Page For Your Desired Manga</h4>
			<br>
			<select id="pageFormats">
			<option value="shortS" id ='spacer'>Short space</option>
			<option value="noS" id='spacer'>No space</option>
			</select>
			<br><br><br><br>
			<label class="containerR" style="color: #bbb;">Border Enabled
			<input type="radio" name="borderSelection" value="be">
			<span class="checkmark"></span>
			</label>
			<label class="containerR" style="color: #bbb;">Border Disabled
			<input type="radio" name="borderSelection" value="bd" checked="checked">
			<span class="checkmark"></span>
			</label>
			</div>
		<br>
			<center>
			<button id="submit" onclick="displayValue()" style= 'width: 140px; height: 40px; font-size:16px;'>Apply Style</button> <hr><br>
			<div class="popup" id="popup-1">
				<div class="overlay"></div>
				<div class="content">
				<div class="close-btn" onclick="togglePopup(0)">&times;</div>
				<h1>Psst..</h1>
				<p id='last'></p>
				</div>
			</div>
		
			<div id="myModal" class="modal" onkeydown="nav_n_zoom(event)">
				<span class="close">&times;</span>
				<img class="modal-content" id="img01">
				<div id="caption"></div>
			</div>
			<div id="images" style="position: relative"></div>
			</center>
		</div>
		
		<br>
		<br>
		
		</body>
		
		<footer id ='footer' style= "align-self: center;">
			<pre>
		
			<pre>
			<p id="pagination" style="text-align: center;" ></p>
			<pre>
		
		
		
		
			<pre>
		</footer>
		
		<script type="text/javascript">
		""" + rjsmin.jsmin("""
			
			
			const page_style = ['bd', "shortS"];
		
			var images_loc = %s;
			var pages_list = %s;
			var current_page_index = %i;
			var proj_name= '%s';
			document.title = pages_list[current_page_index];
		
			document.getElementById("page_title").innerHTML = document.title;
		
		
			document.getElementById('go2main').href= '../'+proj_name+'.html';
		
			var style_= JSON.parse(localStorage.getItem('style?'+proj_name));
			
			function stylish(style){
			style_temp = style;
			
			localStorage.setItem('style?'+proj_name, JSON.stringify(style_temp));
			var ele = document.getElementsByTagName('input');
			for (i = 0; i < ele.length; i++) {
				if (ele[i].type = "radio") {
				if (ele[i].value==style_temp[0]){
					ele[i].checked = true;
				}
				else{
					ele[i].checked = false;
				}
				}
			}
		
			document.getElementById("pageFormats").value = style_temp[1];
			
			
			}
			
		
			function display_imgs() {
			for (i = 0; i < images_loc.length; i++) {
				var imgx = document.createElement("IMG");
				imgx.src = images_loc[i];
				imgx.className = 'per_img';
				imgx.alt = 'It seems image is not found ('+images_loc[i]+')';
				imgx.style.display= 'block';
				imgx.style.margin= 'auto';
				imgx.id = 'myImg';
		
				
				var images_const = document.getElementById("images");
				images_const.appendChild(imgx);
				if (i < (images_loc.length)-1) {
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
				}
			}
			}
		
			display_imgs();
		
			function getValue() {
			var ele = document.getElementsByTagName('input');
			var arr = [];
			for (i = 0; i < ele.length; i++) {
				if (ele[i].type = "radio") {
				if (ele[i].checked)
				arr.push(ele[i].value);
				}
			}
			arr.push(document.getElementById("pageFormats").value);
			return arr;
			}
		
			function pagination () {
			var page_direction=document.getElementById("pagination");
			if (page_direction==null){page_direction.innerHTML = '<span/>'}
			
			if (current_page_index != 0) {
				var prev_a= document.createElement("A");
				prev_a.href= "../"+pages_list[current_page_index-1]+"/"+pages_list[current_page_index-1]+".html";
				prev_a.innerHTML= '<< Previous page  ';
				prev_a.className='paginationA';
				prev_a.onclick= function(){
				localStorage.setItem(proj_name, current_page_index-1);
				};
				page_direction.appendChild(prev_a);
				
			}
			
			page_direction.innerHTML+='<span style="padding : 15%%;"></span>'
		
			if (current_page_index != pages_list.length-1){
				var next_a= document.createElement('A');
				next_a.href= "../"+pages_list[current_page_index+1]+"/"+pages_list[current_page_index+1]+".html";
				next_a.innerHTML= '  Next page >>';
				next_a.className='paginationA';
				next_a.onclick= function(){
				localStorage.setItem(proj_name, current_page_index+1);
				};
				page_direction.appendChild(next_a);
			} 
		
			
			}
			
			pagination();
			function displayValue(values=false) {
			
			if(values==false){var values = getValue();}
			
			stylish(values);
			
			var str = "Page Status: "+values[1]+"<br>Border Status: "+ values[0];
			var img_div1 = document.getElementById('images');
			var eleIMG = document.getElementsByClassName('per_img');
			var breaks = img_div1.getElementsByTagName("BR");
			
			if (values[0] == "be") {
				for (i = 0; i < eleIMG.length; i++) {
				eleIMG[i].border = "4px";
				}
			}
			if (values[0] == "bd") {
				for (i = 0; i < eleIMG.length; i++) {
				eleIMG[i].border = "0px";
				}
			}
			
			if (values[1] == "noS") {
				for (i = breaks.length-1; i >= 0; i--) {
				breaks[i].style.display = 'none'
				}
			}
			
			
			if (values[1] == "shortS") {
				var y = img_div1.childElementCount;
				for (i = breaks.length-1; i >= 0; i--) {
				breaks[i].style.display = 'initial';
				}
			}
			}
		
			if(style_==null){displayValue(page_style);}
			else{displayValue(style_);}
		
		
			//###  modal (floating image script)    #####
		
			// create references to the modal...
			var modal = document.getElementById('myModal');
			// to all images -- note I'm using a class!
			var images = document.getElementsByClassName('per_img');
			// the image in the modal
			var modalImg = document.getElementById("img01");
			// and the caption in the modal
			var captionText = document.getElementById("caption");
			var js_img_src = [];
			var no_arrow= true;
			modalImg.width =100;
		
			var modal_img_indx= -1;
			// Go through all of the images with our custom class
			for (var i = 0; i < images.length; i++) {
			var img = images[i];
			js_img_src.push(img.src);
			// and attach our click listener for this image.
			img.onclick = function() {
				modal.style.display = "initial";
				modalImg.style.display = "initial";
		
				modalImg.src = this.src;
				modal_img_indx = js_img_src.indexOf(modalImg.src);
		
				if(no_arrow){
				const LAdiv = document.createElement("DIV");
				LAdiv.style.display = 'inline-block';
				var LArrow= document.createElement('SPAN');
				LArrow.id= 'LARROW';
				LAdiv.appendChild(LArrow);
				captionText.appendChild(LAdiv);
				
				var captionText_ = document.createElement("SPAN");
				captionText_.id = 'capt_name';
				captionText.appendChild(captionText_);
				
				const RAdiv = document.createElement("DIV");
				RAdiv.style.display = 'inline-block';
				var RArrow= document.createElement('SPAN');
				RArrow.id= 'RARROW';
				RAdiv.appendChild(RArrow);
				captionText.appendChild(RAdiv);
				
				
				no_arrow=false;}
		
		
				var LArrow = document.getElementById('LARROW');
				
				LArrow.style.padding='7px';
				if (modal_img_indx == 0){LArrow.classList.add('disabled');}
				
				LArrow.innerText='\\u00A0\\u00A0\\u00A0< Prev\\u00A0\\u00A0\\u00A0';
				LArrow.onclick = function(){ 
				if (modal_img_indx != 0){
					modal_img_indx-=1;
					modalImg.src = js_img_src[modal_img_indx];
					document.getElementsByClassName( 'close' )[0].scrollIntoView(); 
					if (modal_img_indx+1 == js_img_src.length){RArrow.classList.add('disabled');}
					else{RArrow.classList.remove('disabled');}
		
					if (modal_img_indx == 0){LArrow.classList.add('disabled');}
					else{LArrow.classList.remove('disabled');}
		
				}
				document.getElementById('capt_name').innerText = "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0"+ modalImg.src.replace(/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
				}
		
		
				
		
				document.getElementById('capt_name').innerText= "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0"+modalImg.src.replace(/^.*[\\/]/, '') +"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
				
		
		
				
		
				var RArrow = document.getElementById('RARROW');
				
				RArrow.style.padding='7px';
		
				if (modal_img_indx+1 == js_img_src.length){RArrow.classList.add('disabled');}
				RArrow.innerText='\\u00A0\\u00A0\\u00A0Next >\\u00A0\\u00A0\\u00A0'
				RArrow.onclick = function(){
					if (modal_img_indx+1 != js_img_src.length){
					modal_img_indx+=1;
					modalImg.src = js_img_src[modal_img_indx];
					document.getElementsByClassName( 'close' )[0].scrollIntoView(); 
					if (modal_img_indx+1 == js_img_src.length){RArrow.classList.add('disabled');}
					else{RArrow.classList.remove('disabled');}
					if (modal_img_indx == 0){LArrow.classList.add('disabled');}
					else{LArrow.classList.remove('disabled');}
					}
					document.getElementById('capt_name').innerHTML = "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0"+ modalImg.src.replace(/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";}
		
				
				modal.onkeydown =document.addEventListener('keydown',key_control);
		}}
		
		var span = document.getElementsByClassName( 'close' )[0];
		
			span.onclick = function() {
			modal.style.display = "none";
			modalImg.removeEventListener('keydown',key_control);
			}
		
			function key_control(event){
		
			var RArrow = document.getElementById('RARROW');
			var LArrow = document.getElementById('LARROW');
		
			if(event.keyCode==40){modalImg.style.transition='width .6s, height .6s'; modalImg.style.width = modalImg.width*0.9+'px';}
		
			if(event.keyCode==38){modalImg.style.transition='width .6s, height .6s'; modalImg.style.width = modalImg.width*1.1+'px';}
		
			if(event.keyCode==37){ 
				if (modal_img_indx != 0){
				modal_img_indx-=1;
				modalImg.src = js_img_src[modal_img_indx];
				document.getElementsByClassName( 'close' )[0].scrollIntoView(); 
				} 
				if (modal_img_indx+1 == js_img_src.length){RArrow.classList.add('disabled');}
					else{RArrow.classList.remove('disabled');}
				if (modal_img_indx == 0){LArrow.classList.add('disabled');}
					else{LArrow.classList.remove('disabled');}
				document.getElementById('capt_name').innerText = "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0"+ modalImg.src.replace(/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
			} 
		
			if(event.keyCode==39){
				if (modal_img_indx+1 != js_img_src.length){
				modal_img_indx+=1;
				modalImg.src = js_img_src[modal_img_indx];
				document.getElementsByClassName( 'close' )[0].scrollIntoView();  
				}
				if (modal_img_indx+1 == js_img_src.length){RArrow.classList.add('disabled');}
					else{RArrow.classList.remove('disabled');}
				if (modal_img_indx == 0){LArrow.classList.add('disabled');}
					else{LArrow.classList.remove('disabled');}
				document.getElementById('capt_name').innerHTML = "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0"+ modalImg.src.replace(/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";}
		
			if(event.keyCode==27){
				modal.style.display = "none";
				modalImg.removeEventListener('keydown',key_control);
			}
			}
		
			
			//################################################
		
			//############ Pop up ###########################
			var last_opened = localStorage.getItem(proj_name);
			function togglePopup(on_or_off){
			document.getElementById("popup-1").classList.toggle("active");
			if(on_or_off==0){
				localStorage.setItem(proj_name, current_page_index);
			}
		
			}
			
		
			if(last_opened === undefined || last_opened === null) {
			localStorage.setItem(proj_name, current_page_index);
			last_opened = current_page_index;
		}
		
			if(last_opened!=current_page_index){
				if(last_opened!=-1){
				document.getElementById('last').innerHTML= "You left the page on <a id= 'lastleft' href='../"+ pages_list[localStorage.getItem(proj_name)]+ '/'+pages_list[localStorage.getItem(proj_name)]+".html'>"+ pages_list[localStorage.getItem(proj_name)]+ '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
				togglePopup(1);}
			}
			"""%(all_list, sub_dirs, page_index, title)) +"""
		</script>
		
		
		"""

			return sub_page_template

		# print(return_sub_page('aaa','sss', 6, 'ttt'))
		main_page_template="""
		<!DOCTYPE html>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta charset="UTF-8">
		
		<head>
			<title></title>
			<script type="text/javascript">
			var pages_list = %s;
			var current_page_index = -1;
			var proj_name= "%s";
			document.title = proj_name;
		
		</script>
		
		<style>
			.popup .overlay {
			position:fixed;
			top:0px;
			left:0px;
			width:100vw;
			height:100vh;
			background:rgba(0,0,0,0.7);
			z-index:1;
			display:none;
			}
		
			.popup .content {
			position:fixed;
			top:50%%;
			left:50%%;
			color: #AAA;
			transform:translate(-50%%,-50%%) scale(0);
			background:#222;
			width:500px;
			height:250px;
			z-index:2;
			text-align:center;
			padding:20px;
			box-sizing:border-box;
			font-family:"Open Sans",sans-serif;
			}
		
			.popup .close-btn {
			cursor:pointer;
			position:absolute;
			right:20px;
			top:20px;
			width:30px;
			height:30px;
			background:#222;
			color:#fff;
			font-size:25px;
			font-weight:600;
			line-height:30px;
			text-align:center;
			border-radius:50%%;
			}
		
			.popup.active .overlay {
			display:block;
			}
		
			.popup.active .content {
			transition:all 300ms ease-in-out;
			transform:translate(-50%%,-50%%) scale(1);
			}
		
			button {
			position:absolute;
			top:50%%;
			left:50%%;
			transform:translate(-50%%,-50%%);
			padding:15px;
			font-size:18px;
			border:2px solid #222;
			color:#222;
			text-transform:uppercase;
			font-weight:600;
			background:#fff;
			}
			body{
			
			position: relative;
			min-height: 100vh;
			}
			html, body, input, textarea, select, button {
				border-color: #736b5e;
				color: #e8e6e3;
				background-color: #131516;
			}
			* {
				scrollbar-color: #0f0f0f #454a4d;
			}
			#allA{
			text-align: center;
			margin-left: 5%%;
			margin-right: 5%%;
			width: 85%%;
			}
		
			#lastleft{
			font-size: 20px;
			font-weight: 600;
			font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
			text-decoration: none;
			color: #06A5EE;
			}
		
			#proj_title{
			font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
			}
			.list_class{
			font-size: 20px;
			font-weight: 600;
			font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
			text-decoration: none;
			color: #06A5EE;
			overflow-wrap: break-word;
			padding-left: 5%%;
			padding-right: 5%%;
			}
		
			#footer {
			position: absolute;
			bottom: 0;
			width: 100%%;
			height: 2.5rem;            /* Footer height */
			}
		</style>
		
		</head>
		
		<body>
			<div class="popup" id="popup-1">
			<div class="overlay"></div>
			<div class="content">
				<div class="close-btn" onclick="togglePopup(0)">&times;</div>
				<h1>Psst.. </h1>
				<p id="last"></p>
			</div>
			</div>
			<h2 style="text-align: center;" id="proj_title"></h2>
			<hr style="width: 80%%;">
			<center>
			<div id='allA'></div>
			</center>
			<br><br>
		
		
		<footer id='footer'><br><br><hr><hr>
		<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>
		<br><br>
		</footer>
		
		</body>
		
		<script type="text/javascript">
		
		document.getElementById('proj_title').innerText=proj_name;
		
		var all_li= document.getElementById('allA');
		for (var i = 0; i < pages_list.length; i++){
			var linkX =document.createElement('A');
			var linkContainer = document.createElement('DIV');
			linkContainer.className = 'sub_li_divs';
			linkX.href = pages_list[i]+ '/'+pages_list[i]+".html";
		
			linkX.innerHTML = pages_list[i];
			if(i%%2==0){
			linkContainer.style.backgroundColor = '#35393b' ;
			}
			else{
			linkContainer.style.backgroundColor = '#222426' ;
			}
		
			linkX.className = 'list_class';
			linkContainer.appendChild(linkX);
			linkContainer.appendChild(document.createElement('BR'));
			var hr_ = document.createElement('HR');
			linkContainer.appendChild(hr_);
			all_li.appendChild(linkContainer);
		}
			function togglePopup(on_or_off){
			document.getElementById("popup-1").classList.toggle("active");
			if(on_or_off==0){
			localStorage.setItem(proj_name, current_page_index);
			}
		
		}
			if(localStorage.getItem(proj_name)!=null){
			if(localStorage.getItem(proj_name)!=current_page_index){
			document.getElementById('last').innerHTML= "You left the page on <a id='lastleft' href='"+ pages_list[localStorage.getItem(proj_name)]+ '/'+pages_list[localStorage.getItem(proj_name)]+".html'>"+ pages_list[localStorage.getItem(proj_name)]+ '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
			togglePopup(1);
			}}
		
			else{
				localStorage.setItem(proj_name, current_page_index);
			}
		</script>"""


		dir_path = os_dirname(os_realpath(__file__))

		def make_pages(all_li, dir_list, project, seq, ext='', dir_sorted = False):   #func_code= 40001
			first_page=None
			dir_len = len(dir_list)

			if not dir_sorted: dir_list= natsort.natsorted(dir_list)
			first_page = dir_path+'/Download_projects/'+ project+'/'+project+'.html'
			for i in range(dir_len):
				temp=[]
				for j in range(len(all_li)):
					if all_li[j][1] == i:
						temp.append(html_escape(trans_str(html_unescape(get_file_name(all_li[j][0])
												), {'/\\|:*><?': '-', '"':"'"})+ext))

				temp=remove_duplicate(temp)

				if seq:
					box= return_sub_page(str(natsort.natsorted(temp)), str(dir_list), i, project)
				else:
					box= return_sub_page(str(temp), str(dir_list), i, project)

				writer(dir_list[i]+'.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
			writer(project+'.html', 'w', main_page_template%(str((dir_list)), project),'Download_projects/'+ project, f_code= '40001')
			return first_page

	except Exception as e:
		print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
		leach_logger('40000x-1||' + str(e.__class__.__name__) + '||' + str(e))
		print('40000x-1||' + str(e.__class__.__name__) + '||' + str(e))
		time.sleep(5)
		exit()

	try:
		# from basic_shared import *
		dir_path = os_dirname(os_realpath(__file__))
		import zipfile

		def make_cbz(all_li, dir_list, project, seq, ext='', dir_sorted = False):   #func_code= 50001
			first_page=None
			dir_len = len(dir_list)

			if not dir_sorted: dir_list= natsort.natsorted(dir_list)
			first_page = dir_path+'/Download_projects/'+ project+'/'+project+'.html'
			has_non_cbz = False
			missing_files = False
			cbz_ext = ['jpg', 'jpeg', 'png', 'gif']
			xprint('/y/Creating CBZ files\nPlease wait.../=/\n  [ 0 / %i ] done...'%dir_len)
			for i in range(dir_len):
				temp=[]

				for j in range(len(all_li)):
					if all_li[j][1] == i:
						file_name = get_file_name(all_li[j][0]
												).replace('/','-').replace('\\','-'
												).replace('|','-').replace(':','-'
												).replace('*','-').replace('"',"'"
												).replace('>','-').replace('<','-'
												).replace('?','-')+ext
						if get_file_ext(file_name).lower() not in cbz_ext:
							if has_non_cbz is False:
								has_non_cbz = True
								delete_last_line()
								print('Ignoring CBZ unsupported files\n')
								leach_logger('50001xU||'+project)
						else:
							temp.append(html_unescape(get_file_name(all_li[j][0])).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-'))

				temp=remove_duplicate(temp)

				if seq:
					temp= natsort.natsorted(temp)

				outpath= 'Download_projects/[CBZ]'+ project+'/'+dir_list[i]+'.cbz'
				writer(dir_list[i]+'.cbz', 'wb', b'', 'Download_projects/[CBZ]'+ project, '50001')

				with zipfile.ZipFile(outpath, 'w') as zip:
					for index, image in enumerate(temp):
						file = reader('Download_projects/'+ project+'/'+dir_list[i]+'/'+image, 'rb', on_missing= False, ignore_missing_log = True, f_code= '50001')
						if file==False:
							if missing_files==False:
								delete_last_line()
								xprint('/r/Some files are missing\n/y/Ignoring. Please try Updating the project to get the missing files./=/\n')
								leach_logger('50001xM||'+project)
								missing_files= True
							continue
						zip.writestr("%i.%s" % (index, get_file_ext(image)), file)
				delete_last_line()
				print('  [ %i / %i ] done'%(i+1, dir_len))
			return first_page

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


class web_leach:

	def __init__(self):      #func_code= 10001  v
		"""initialize variables on every start of a project"""

		self.total = 0	  # number of total files
		self.break_all = False	  # trigger to stop the download
		self.done = 0	  # total downloaded files
		self.errors = 0	# number or errors
		self.sp_extension = ''	# if custom file extension needed to be added with the downloaded file names
		self.sp_flags = []	# list of flags for special downloads like mangafreaks
		self.overwrite_bool = True	# bool for wheather replace the duplicate file or not
		self.partial_do_all = False	# will use the same detected homepage for every other pages with no home
		"""if partial link found while indexing, then the program will find the
		homepage and ask if it will be used for all other partial links or not"""

		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""

		self.homepage = ''	# just assigning the homepage variable
		self.indx_count = 0	# counts the number of indexed links
		self.all_list = []	# assigning a list of data links, but duplicates will be cancelled in process
		self.existing_found = False	# indicates if valid existing project is found
		self.dl_done = False	# indicates if the project scrapping was done or not
		self.has_missing = None		# indicates if the Project has any missing files. {5.4 and above}
		self.img_to_sort = True	# indicates if the files will be sorted or not
		self.dir_sorted = False
		self.update = False	# indicates if the project is getting an update or not
		self.corruptions = []	# list of corruptions in project data if there's any or empty
		self.sub_dirs = []	# list of sub directories on the project folder
		self.sub_links = [] # needed in requests.get() reference value (fixes many issues)
		self.homepage_searcher = re_compile('(https?://[^/]*)')	# compiled regex tool for getting homepage
		self.Project = ''	# project name (case insensitive *need to work on it)
		self.main_link = ''	# the main link
		self.file_types = set()	# set of file extensions to be downloaded
		self.file_starts = ''	# (str) each files must start with (used regex)
		self.link_startswith = ''	# (str) each sublink must start with
		self.error_triggers = []	# 0 to 9 the number of tasks
		self.open_file = False
		self.dl_chunks = 0
		self.from_file = False
		self.page_error = 0
		self.re_error = 0   # number of errors after retrying errors

		self.special_starts = {'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://w[^\/]+\.mangafreak.net/(?:M|m)anga/([^\?\#]+)',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(?:_\d+)[\?\#]?.*',
		'mf_read_chap':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(_\d+)[\?\#]?.*',
		'webtoon_ep':'https\:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/.*?\/viewer\?title_no\=(\d+)\&episode_no\=\d+',
		'webtoon': 'https:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/list\?title_no=(\d+)'}

		### download speed limit variables
		self.tictoc = 0
		self.dl_lim = 0
		self.current_chunks = 0
		self.dl_nap_time = 0
		### /download speed limit variables

		self.current_speed = '0 bytes'
		self.is_error = False


		self.port = running_port

	def catch_KeyboardInterrupt(self, func, *args):       #func_code= 11001  v
		"""Runs a function in a isolated area so that Keyboard cancal
		can be caught and processed accordingly

		args:
		-----
			func: The function to call inside the space
			*args: The args to send inside the program"""
		try:
			try:
				try:
					box = func(*args)
					return box
				except EOFError:
					raise LeachICancelError
				except KeyboardInterrupt:
					raise LeachICancelError
				except LeachICancelError:
					leach_logger('0x1||11001||input exit code L&infin;ping for unknown reason')
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError


	def speed_limiter(self):     #func_code = 1000D  v
		"""Limits download speed by arg
		`sp_arg_flag['max dlim']` in kbps"""

		if sp_arg_flag['max dlim'] == 0: return 0
		while not (self.dl_done or self.break_all):
			if self.current_chunks*sp_arg_flag["chunk_size"]>sp_arg_flag['max dlim']:
				if time.time()-self.tictoc<1:
					_temp = 1-(time.time()-self.tictoc)
					if _temp<1:
						self.dl_nap_time = _temp
					self.tictoc = time.time()
					self.current_chunks = 0
				else:
					self.tictoc = time.time()
					self.current_chunks = 0
			time.sleep(0.05)


	def speed_tester(self):     #func_code = 1000E  v
		"""Counts and prints download speed and
		shows download amount in thread"""

		last_chunks = 0
		while (not (self.dl_done or self.break_all)) or self.total == 0:
			_temp = self.dl_chunks
			self.current_speed = filesize_size((_temp-last_chunks)*sp_arg_flag['chunk_size']*2, filesize_alt)

			if self.break_all or self.total == 0: return 0
			percent = floor(((self.done)/self.total)*32)
			delete_last_line()
			print('Downloaded [' + '\u001b[7m' + (' '*percent) + '\u001b[0m' + ' '*(32-percent) + '] [' + str(self.done) + '/' + str(self.total) + ']', self.current_speed + '/s')
			time.sleep(.5)
			last_chunks = _temp


	def distribute(self, lists, task_id, is_error=False):      #func_code= 10002  v
		"""run downloads in this function from a list of download links

		args:
		-----
			lists: download links list
			task_id: task id (int) to keep resume point stored
			is_error: if the funtion is running to retry the failed files *False"""

		#global total, done, errors, sp_flags, sp_extension, overwrite_bool
		global err_hdr_list
		task_id = str(task_id)
		res = 0
		if self.existing_found:
			if os_exists('data/leach_projects/' + self.Project + '/t' + task_id + '.txt'):
				res = reader('data/leach_projects/' + self.Project + '/t' + task_id + '.txt').strip()
				res = eval(res) if res!='' else 0# resume point of the list (index # int)
		self.done += res

		session = requests.session()


		time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:
			if self.break_all == True: return 0
			download = True	# switch for download it or not
			streaming = not is_error
			if 'ignore_on_null_content' in self.sp_flags or 'stop_on_null_content' in self.sp_flags:
				streaming = False
			if is_error:
				i = list(j)
			else:
				i = list(self.all_list2[j])

			self.is_error = is_error

			if lists.index(j)>=res:
				current_header = header_()	# randomizes header from list on every download to at least try to fool server
				if self.sub_links!=[]: # if sub_links are available, then use them as header referer
					current_header['referer'] = self.sub_links[i[1]]

				try:
					if self.overwrite_bool == False:
						if self.sub_dirs[i[1]].endswith('/'):
							if os_isfile('Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + get_file_name(i[0]) + self.sp_extension): download = False
						else:
							if os_isfile('Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension): download = False
					if download:
						if sp_arg_flag['disable dl get'] == True:
							file = session.head(i[0], headers= current_header, timeout=2)
						else:
							file = session.get(i[0], headers= current_header, timeout=2, stream= streaming)
						if 'stop_on_null_content' in self.sp_flags: # do not save null files
							if len(file.content) == 0:
								break
						if 'ignore_on_null_content' in self.sp_flags: # do not save null files
							if len(file.content) == 0:
								continue



						if file:
							if self.break_all:return 0

							if sp_arg_flag['disable dl get']!=True:
								if self.break_all: return 0
								try:
									writer(get_file_name(i[0]) + self.sp_extension, 'wb', b'', 'Download_projects/' + self.Project + '/' + self.sub_dirs[i[1]], '10002')
									loaded_file = open('Download_projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension, 'wb')
								except IndexError:
									# TODO: something breaks the code here most of the time. FIX it.
									# xprint('\n/y/Something Went wrong, Returning to main Menu/=/\n')
									self.break_all = True
									return 0

								try:

									for chunk in file.iter_content(chunk_size=sp_arg_flag['chunk_size']):
										if sp_arg_flag['max dlim']!=0:
											time.sleep(self.dl_nap_time)

										if self.break_all:
											loaded_file.close()
											if os_exists('Download_projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension):
												remove('Download_projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension)

											return 0

										loaded_file.write(chunk)
										self.dl_chunks += 1
										self.current_chunks += 1

									loaded_file.close()

								except (requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
									loaded_file.close()
									_temp = remove_noscript(session.get(i[0], headers= current_header, timeout=2).content)
									writer(get_file_name(i[0]) + self.sp_extension, 'wb', _temp, 'Download_projects/' + self.Project + '/' + self.sub_dirs[i[1]], '10002')
									del _temp

								if 'dl unzip' in self.sp_flags:
									if os_isdir('./Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + '/') == False:
										makedirs('./Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + '/')
									with ZipFile('./Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension) as zf:
										zf.extractall(path='./Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]))
									if 'del dl zip' in self.sp_flags:
										remove('./Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension)

							if self.break_all: return 0
							writer('t' + task_id + '.txt', 'w', str(res), 'data/leach_projects/' + self.Project, '10002')

							res += 1
							self.done += 1
							if is_error:
								self.errors-=1

						else:
							if is_error == False:
								writer('errors.txt', 'a', str(i + [hdr(current_header, '10002')]) + '\n', 'data/leach_projects/' + self.Project, '10002')
								err_hdr_list += Counter([hdr(current_header, '10002')])
								writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '10002')
								self.errors += 1

							else:
								self.re_error += 1
								if self.re_error == 1: delete_last_line()
								delete_last_line()
								if self.re_error<4:
									print("Failed to download from '%s'\n\n"%i[0])
								else:
									if self.re_error!=4:delete_last_line()
									print("And %i others"%(self.re_error-3))
								writer('left_errors.txt', 'a', str(i + [hdr(current_header, '10002'), "Error dl"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
								leach_logger('10002x1||' + self.Project + '||' + hdr(current_header, '10002') + '||' + str(i) + '||' + str(file.status_code), user_name)
								continue

							res += 1

					else:
						writer('t' + task_id + '.txt', 'w', str(res), 'data/leach_projects/' + self.Project, '10002')

						delete_last_line()
						#print(done)
						percent = floor(((self.done + 1)/self.total)*32)

						print('Downloaded [' + '\u001b[7m' + (' '*percent) + '\u001b[0m' + ' '*(32-percent) + '] [' + str(self.done + 1) + '/' + str(self.total) + ']', task_id)
						res += 1
						self.done += 1
						if is_error:
							self.errors-=1

				except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
					if is_error == False:
						writer('errors.txt', 'a', str(i + [hdr(current_header, '10002')]) + '\n', 'data/leach_projects/' + self.Project, '10002')

						err_hdr_list += Counter([hdr(current_header, '10002')])
						writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '10002')
						self.errors += 1


					else:
						self.re_error += 1
						if self.re_error<4:
							print("Failed to download from '%s'"%i[0])
						else:
							if self.re_error!=4:delete_last_line()
							print("And %i others"%(self.re_error-3))
						writer('left_errors.txt', 'a', str(i + [hdr(current_header, '10002'), "Error dl"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
						leach_logger('10002x1||' + self.Project + '||' + hdr(current_header, '10002') + '||' + str(i) + '||' + str(e.__class__.__name__), user_name)
				except BadZipFile:
					if os_isfile('Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension):
						remove('Download_Projects/' + self.Project + '/' + self.sub_dirs[i[1]] + '/' + get_file_name(i[0]) + self.sp_extension)


					if is_error == False:
						writer('errors.txt', 'a', str(i + [hdr(current_header, '10002')] + ["Bad zip"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
						self.errors += 1
					else:
						self.re_error += 1
						if self.re_error<4:
							delete_last_line()
							print("Failed to download from '%s'\n"%i[0])
						else:
							if self.re_error!=4:
								delete_last_line()
								delete_last_line()
							print("And %i others\n"%(self.re_error-3))
						print("It seems every time it downloads a broken or unknown zip from '%s' (possible cause password protected zips, if yes extract them manually)" + i[0])
						writer('left_errors.txt', 'a', str(tuple(i) + (hdr(current_header, '10002'), "Bad zip")) + '\n', 'data/leach_projects/' + self.Project, '10002')

						leach_logger('10002x2||' + self.Project + '||' + hdr(current_header, '10002') + '||' + str(i), user_name)



				except: # for test only
					continue
					self.break_all = True
					print("=== Distribute TRACEBACK ===")
					traceback.print_exc()

		self.error_triggers.append(int(task_id))


	def list_writer(self, link, list_range, special=None,
					soup=None):      #func_code= 10003  v
		"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list

		args:
		-----
			link: single link or a list of links to index
			file_link_starts: (regex) string that will check and if the file links starts with
			list_range: a range objet containing the index of the links
			special: gives a headsup that if the link is from any special cases *None
			soup: a response soup object that will speed the indexing a little bit up *None"""

		start_checker = re_compile('^' + self.file_starts)



		if special!=None:
			if special.startswith('nhentai'):
				if special == "nhentai.xxx":
					xxx_search = re_compile("https://cdn.nhentai.xxx/g/\d+/\d*t..*")
					for imgs in soup.find_all('img'):
						img_link = imgs.get('data-src')

						if img_link == None:
							img_link = imgs.get('src')

						if xxx_search.search(img_link)!=None:
							self.all_list.append((''.join([img_link.rpartition('t')[0], img_link.rpartition('t')[2]]), 0))
							# img_link.rpartition('t')[1]

				elif special == "nhentai.to":
					to_search = re_compile("(https://nhentai.to/galleries/\d*/)|(https://cdn.dogehls.xyz/galleries/\d*/)")
					for imgs in soup.find_all('img'):
						img_link = imgs.get('data-src')
						if img_link == None:
							img_link = imgs.get('src')
						if img_link.startswith('/'):
							img_link = 'https://nhentai.to' + (img_link.replace('t', ''))
						if img_link.startswith('https://cdn.dogehls.xyz/galleries/'):
							img_link = img_link[::-1].replace('t', '', 1)[::-1]

						if to_search.search(img_link)!=None:
							self.all_list.append((img_link, 0))

				elif special == "nhentai.net":
					net_search = re_compile("https://i.nhentai.net/galleries/\d*/")
					for imgs in soup.find_all('img'):
						img_link = imgs.get('data-src')
						if img_link == None:
							img_link = imgs.get('src')

						if '/thumb.' in img_link:
							continue

						if 'cover' not in img_link:
							img_link = img_link.replace('s://t.', 's://i.')[::-1].replace('t', '', 1)[::-1]
						if net_search.search(img_link)!=None:
							self.all_list.append((img_link, 0))
				self.all_list = remove_duplicate(self.all_list)

		else:
			dir_len = len(self.sub_dirs)
			for i in list_range:
				if self.break_all:
					return 0

				if self.sub_dirs[i][-1] == '/':
					self.sub_dirs[i] = self.sub_dirs[i][:-1]

				self.sub_dirs[i] = self.sub_dirs[i].split('/')[-1]

				current_header = header_()
				try:
					page = requests.get(link[i], headers= current_header)
					if not page:
						print('\nFailed to connect "%s"\nPlease try the update option after downloading\n\n'%link[i])
						leach_logger("10003x1||" + self.Project + '||' + hdr(current_header, '10003') + '||' + link[i] + '||' + str(page.status_code) + '||' + 'None')
						continue
					soup = bs(page.content, parser)
				except (requests.exceptions.ChunkedEncodingError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
					print('\nFailed to connect "%s"\nPlease try the update option after downloading\n\n'%link[i])
					leach_logger("10003x1||" + self.Project + '||' + hdr(current_header, '10003') + '||' + link[i] + '||' + e.__class__.__name__ + '||' + str(e))
					continue

				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')
					if img_link == None:
						img_link = imgs.get('src')
					img_link = img_link.strip()

					if img_link.startswith('//'): img_link = 'https:' + img_link
					if img_link.startswith('/'):
						img_link = self.homepage_searcher.search(link[i]).groups()[0] + img_link

					if img_link.startswith('../'):
						temp_home = link[i]
						while img_link.startswith('../'):
							temp_home = go_prev_dir(temp_home)
							img_link = img_link.replace('../', '', 1)
						img_link = temp_home + img_link

					if '//' not in img_link:
						temp = self.homepage_searcher.search(link[i]).group()
						if temp.endswith('/'):
							if img_link.startswith('/'): img_link = temp + img_link[1:]
							else: img_link = temp + img_link
						else:
							if img_link.startswith('/'): img_link = temp + img_link
							else: img_link = temp + '/' + img_link

					if start_checker.search(str(img_link)) !=None and get_file_name(img_link, 'url').endswith(tuple(self.file_types)):
						self.all_list.append((img_link.split("#")[0].split("?")[0], i))
				delete_last_line()
				print('Indexed [' + str(self.indx_count + 1) + '/' + str(dir_len) + '] ' + link[i])
				self.indx_count += 1


	if os_name == 'Windows':
		def play_yamatte(self, vol):      #func_code= 10004  v
			"""just for parody"""
			writer('yamatte.mp3', 'wb', requests.get(random_choice(yamatte), headers = header_()).content, 'data/.temp', '10004')
			ex = mplay4.ex_vol
			mplay4.set_win_vol(vol)
			mplay4.load('data/.temp/yamatte.mp3').play()
			time.sleep(8)
			remove('data/.temp/yamatte.mp3')
			mplay4.set_win_vol(ex)
		play_yamatte_t = Process(target=play_yamatte, args=[80])


	def nhentai_link(self, link):      #func_code= 10005  v
		"""checks if the link is nhentai link and returns the available link and the title of the doujin
		else it will return 0"""

		if re_search(self.special_starts['nh_sc'], link):
			self.main_link = 'https://nhentai.net/g/' + str(re_search(self.special_starts['nh_sc'], link).group(1))
		link = self.main_link
		code = re_search('https://nhentai.[^/]*/g/((\d)*)', link)

		if code == None:
			return False, False
		code = code.groups()[0]

		current_header = header_()
		try:
			link_y = 'https://nhentai.net/g/' + code + '/'
			page = requests.get(link_y, headers=current_header, timeout=2)
			if page:
				site = ".net"
			else:
				raise requests.exceptions.ConnectionError
				#link_y = 'https://nhentai.to/g/' + code + '/'
				#page = requests.get(link_y, headers = headers)
				#site = '.to'
				# site = "https://nhentai.net/"
				# thumb_pattern = "https://t.nhentai.net/galleries/\d/\dt."

		except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
			leach_logger("606x1||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), user_name)
			print('nhentai.net server is not reachable, trying proxy server...')
			link_y = 'https://nhentai.xxx/g/' + code + '/'
			# link_y = 'https://nhentai.to/g/' + code + '/'
			try:
				page = requests.get(link_y, headers=header_())
				if page:
					site = ".xxx"
				else:
					raise requests.exceptions.ConnectionError
			except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
				delete_last_line()
				xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
				leach_logger("606x2||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), user_name)
				delete_last_line()
				print('nhentai.net server is not reachable, trying proxy server...(2)')
				link_y = 'https://nhentai.to/g/' + code + '/'

				try:
					page = requests.get(link_y, headers=header_())
					if page:
						site = ".to"
					else:
						raise requests.exceptions.ConnectionError
				except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
					# delete_last_line()
					xprint("/rh/Error code: 606x3\nLink not found, Please recheck the link and start a new project/=/")
					leach_logger("606x3||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), user_name)
					return False, False

		self.file_types = img
		if page:
			soup = bs(remove_noscript(page.content), parser)

			title = remove_non_uni(soup.find(id='info').find('h1').get_text(), '10005')
			print("Indexing from", title)
			self.file_starts = ''
			self.list_writer(code, 0, 'nhentai' + site, soup)
			self.sub_dirs.append(trans_str(parse.unquote(html_unescape(title)), {'/\\|:*><?': '-', '"':"'"}).strip())
			# print(self.sub_dirs)
			return link_y, title
		else:
			xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
			leach_logger("606x2||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), user_name)
			return False, False

	def check_sp_links(self, link, sp=None):      #func_code= 10006  v
		"""checks if the link has any special case and any specific special case

		args:
		-----
			link: link of the project
			sp: specifies the special case check *None"""

		if re_search(self.special_starts['nh_sc'], link):
			link = 'https://nhentai.net/g/' + str(re_search(self.special_starts['nh_sc'], link).group(1))
		if re_search(self.special_starts['mf_read'], link):
			link = 'https://w11.mangafreak.net/Manga/' + str(re_search(self.special_starts['mf_read'], link).group(1))
		if re_search(self.special_starts['mf_sc'], link):
			link = 'https://w11.mangafreak.net/Manga/' + str(re_search(self.special_starts['mf_sc'], link).group(1).replace(' ', '_'))

		if type(sp) == list:
			return any([self.check_sp_links(link, sp=i) for i in sp])
		if sp == 'nh':
			if re_search('^' + self.special_starts['nh'], link)!=None:
				return True
			else:
				return False
		elif sp == "mangafreak":
			if re_search('^' + self.special_starts['mangafreak'], link)!=None:
				return True
			else:
				return False
		elif sp == "pinterest":
			if re_search('^' + self.special_starts['pinterest'], link)!=None:
				return True
			else:
				return False
		elif sp == "pinterest-pin":
			if re_search('^' + self.special_starts['pinterest'] + 'pin/\d+$', link)!=None:
				return True
			else:
				return False
		elif sp == 'webtoon':
			if re_search('^' + self.special_starts['webtoon'], link)!=None:
				return True
			elif re_search('^' + self.special_starts['webtoon_ep'], link)!=None:
				return True
			else:
				return False
		elif sp == None:
			for i in self.special_starts.values():
				if re_search('^' + i, link)!=None:
					return True
			return False
		else:
			print("INvalid arg!\n    pLEaSe REcHECK\n=======> %s <=======\n WITH\n-------> %s <-------"%(self.main_link, str(sp)))
			raise ValueError

	def mangafreak_link(self, link):      #func_code= 10007  v
		"""checks if the link is a mangafreak link and makes indexing easier. but one limitation is it can't find weather the link is valid or not and cannot get the actual file links.
		*Note:: user needs to manually confirm last chapter"""

		_temp = re_search(self.special_starts['mf_sc'], link)
		if _temp:
			_temp = str(_temp.group(1))
			_temp = re_sub('[\!\:\.\'\, ]', '', _temp)
			_temp = re_sub('[\+\/\\ \"\<\>\?\-]', '_', _temp)
			link = 'https://w11.mangafreak.net/Manga/' + _temp
			link = re_sub('\_{2+}', '\_', link)

			try:
				if requests.head("http://images.mangafreak.net:8080/downloads/" + _temp + '_1').headers['content-length'] == 0:
					raise ValueError
				else:
					self.main_link = link

			except Exception:
				link = None
				print("Checking in google for the accurate link")
				query = 'mangafreak ' + _temp
				for i in g_search(query, tld="com", num=3, stop=3, pause=2):
					if re_search(self.special_starts['mf_read'], i):
						link = i
						print ("Link found - " + i)
						break
					elif re_search(self.special_starts['mangafreak'], i):
						link = i
						print ("Link found - " + i)
						break

			if link == None:
				print("It seems the title is incorrect. Please recheck the title and re-start the project")
				return ''

		_temp = re_search(self.special_starts['mf_read'], link)

		if _temp:
			link = 'https://w11.mangafreak.net/Manga/' + str(_temp.group(1))

		inp = re_search(self.special_starts['mangafreak'], link)

		self.main_link = link
		if inp!=None:
			title = inp.group(1)
			self.sp_flags.append('mangafreak')

		else:
			print("It seems the title is incorrect. Please recheck the title and re-start the project")
			return ""

		last_ch = -1
		_msg = "\n/gh/**/=/Please enter the last chapter number...\n leave it empty to auto detect\n\n >>"
		while True:
			try:
				last_ch = safe_input(_msg).strip()
			except LeachICancelError:
				xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
				leach_logger("000||10007||%s||f-Stop||is_mangafreak||did not ans Mangafreak chapter no"%self.Project)
				return 0

			if last_ch == '':
				last_ch = None
				break

			try:
				last_ch = int(last_ch)
				break
			except ValueError:
				_msg = "\n/rh/**/=/Just enter the last chapter number (like 135)...\n leave it empty to auto detect\n\n >> "

		self.sub_dirs = ['.']

		if last_ch == None:
			last_ch = 0
			print('Counting Links... (0)')
			while True:
				try:
					if requests.head("http://images.mangafreak.net:8080/downloads/" + title + '_' + str(last_ch + 1)).headers['content-length'] !=0:
						last_ch += 1
						delete_last_line()
						print('Counting Links... (%i)'% last_ch)
					else:
						break
				except Exception:
					break
			delete_last_line()
			print("Total %i links found from mangafreak.\nIf its not right, retry by pressing ctrl+C\n\n"%last_ch)

		for i in range(1, last_ch + 1):
			self.all_list.append(("http://images.mangafreak.net:8080/downloads/" + title + '_' + str(i), 0))

		self.sp_extension = '.zip'

		return "mangafreak.net"

	def pint_link(self):      #func_code= 1000?
		"""checks if the link is pinteresst link and indexes the files
		else it will return 0"""

		if self.check_sp_links(self.main_link, 'pinterest'):
			_ = input()

	def webtoon_link(self):		#func_code= 1000C  v
		"""checks for webtoon links and get chapterwise image links and sends it to `main` function"""

		self.temp_counter = 0

		def get_images(self, indx):     #func_code= 1000C1
			remove_type = re_compile('\?type\=.*.*')
			for j in  indx:
				i = self.sub_links[j]
				temp1 = bs(remove_noscript(session.get(i).content), parser)
				img_div = temp1.find('div', id='_imageList')

				for ii in img_div.find_all('img'):
					self.all_list.append(tuple((remove_type.sub('', ii.get('data-url')), j)))

				self.temp_counter += 1
				delete_last_line()
				print('Gathering Image links [%i / %i]'%(self.temp_counter, total_chapters))

		_t = re_search(self.special_starts['webtoon'] ,self.main_link)
		if _t:
			datas = _t.groups()
		else:
			_t = re_search(self.special_starts['webtoon_ep'] ,self.main_link)
			if _t:
				datas = _t.groups()  # category, title, code
			else:
				xprint("/r/Invalid link/y/\n please recheck the Main link/=/")
				return 0

		session = requests.Session()

		page_list = []
		prev_lists = []
		next_lists = []
		sub_links = []
		sub_dirs = []
		homepage = 'https://www.webtoons.com'

		input_link = "https://www.webtoons.com/en/%s/%s/list?title_no=%s"%(datas)
		input_page = session.get(input_link, headers = header_())
		if not input_page:
			xprint('/r/Webtoon Page not found. /y/Recheck the link/=/')
			return 0

		input_soup = bs(remove_noscript(input_page.content), parser)
		_temp = input_link

		paginate = input_soup.find_all("div", class_="paginate")[0]
		paginate__ = paginate
		paginate_ = paginate__.find_all('a', class_='pg_prev')
		page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
		while len(paginate_)!=0:
			prev_lists.append(get_link(paginate_[0].get('href'), _temp, homepage))
			page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			_temp = prev_lists[-1]
			paginate__ = bs(remove_noscript(session.get(_temp).content), parser).find_all("div", class_="paginate")[0]
			paginate_ = paginate__.find_all('a', class_='pg_prev')
			page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

		_temp = input_link
		paginate_ = paginate.find_all('a', class_='pg_next')
		paginate__ = paginate
		page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
		while len(paginate_)!=0:
			next_lists.append(get_link(paginate_[0].get('href'), _temp, homepage))
			page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			_temp = next_lists[-1]
			paginate__ = bs(remove_noscript(session.get(_temp).content), parser).find_all("div", class_="paginate")[0]
			paginate_ = paginate__.find_all('a', class_='pg_next')
			page_list += [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

		del paginate__

		page_list = natsort.natsorted(remove_duplicate(page_list))

		for i in page_list:
			temp1 = bs(remove_noscript(session.get(i).content), parser)
			ul = temp1.find_all('ul', id= "_listUl")[0].find_all('a')
			for ii in ul:
				sub_links.append(get_link(ii.get('href'), _temp, homepage))
				sub_dirs.append(ii.find('span', class_= 'subj').text.strip())

		self.sub_dirs = sub_dirs[::-1]
		self.sub_links = sub_links[::-1]

		total_chapters = len(sub_links)

		print('Found %i Chapters'%total_chapters)
		print('\nGathering Image links [%i / %i]'%(self.temp_counter, total_chapters))

		sub_range = range(total_chapters)
		indx1 = Process(target= get_images, args=(self, sub_range[::3]))
		indx2 = Process(target= get_images, args=(self, sub_range[1::3]))
		indx3 = Process(target= get_images, args=(self, sub_range[2::3]))

		try:

			indx1.start()
			indx2.start()
			indx3.start()
			try:
				indx1.join()
				indx2.join()
				indx3.join()

			except EOFError:
				leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
				xprint("/yh/Project indexing cancelled by Keyboard/=/")
				self.break_all = True
				return 0
			except KeyboardInterrupt:
				leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
				xprint("/yh/Project indexing cancelled by Keyboard/=/")
				self.break_all = True
				return 0

		except Exception as e:
			xprint("/rh/code: Error 607\n The program will break in 5 seconds/=/")
			leach_logger("10009x-1||%s||%s||%s"%(self.Project, e.__class__.__name__, str(e)), user_name)
			time.sleep(5)
			exit(0)

		self.dir_sorted = True
		self.overwrite_bool = False
		self.img_to_sort = False
		return 'all good'


	def retry_errors(self):      #func_code= 10008  v
		"""retries to download the error files on `no_buffering` mode after all the `distribute` threads are done
        and their triggers are called."""
		while sorted(self.error_triggers)!=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
			if self.break_all:
				return 0
			time.sleep(2)

		leach_logger("10008x0||" + self.Project + "||" + str(self.total) + '||' + str(self.errors), user_name)

		if self.errors>0:
			if os_exists('data/leach_projects/' + self.Project + '/errors.txt'):
				err_file = reader('data/leach_projects/' + self.Project + '/errors.txt', 'rb').split(b'\n')

				if self.break_all:
					return 0
				errs = []
				for i in err_file:
					if i.strip()!=b'':
						try:
							errs.append(eval(i.decode())[:2])
						except TypeError:
							print(i)
						except:
							pass

				self.distribute(errs, 11, is_error= True)
			else:
				print("Warning: Error file not found!\nPossible cause: data corruption")
				leach_logger("10008x1||" + self.Project, user_name)
		leach_logger("10008x2||" + self.Project + '||' + str(self.errors), user_name)

		if self.dl_done == False:
			writer(self.Project + '.proj', 'a', 'dl_done = True\n', 'data/leach_projects', '10008')
		if self.errors>0:
			print("\nPlease retry some time later to get higher chances to download some or all %d missing file/s"%self.errors)
			writer(self.Project + '.proj', 'a', 'has_missing = True\n', 'data/leach_projects', '10008')
		else:
			writer(self.Project + '.proj', 'a', 'has_missing = False\n', 'data/leach_projects', '10008')

		xprint("""\n\nDo you want to
\u29bf View the Project in Browser? /hui/ b /=/
\u29bf or Make CBZ files from the images? /hui/ cbz /=/
\u29bf otherwise just leave an Enter
  /gh/>>/=/ """, end='')

		self.dl_done = True
	def data_checkup(self, path=None, proj_name=None, offline=False, blind=False):     # f_code = 11000  v
		if path!=None:
			proj_path = path
			list_path = path[:-5] + '.list'
		else:
			proj_path = 'data/leach_projects/' + self.Project + '.proj'
			list_path = 'data/leach_projects/' + self.Project + '.list'
		if os_exists(proj_path) and os_exists(list_path):
			proj_good = True
			print('db found')
			run_FAD = False
			existing_data = reader(proj_path, 'rb', True, 'str').strip().split('\n')
			try:
				global Project, main_link, link_startswith, file_types, file_starts, sub_dirs, sp_flags
				global sp_extension, overwrite_bool, dimention, dl_done, sequence, sub_links, has_missing
				global dir_sorted


				for i in existing_data:
					exec(i, globals())
				self.main_link = main_link
				self.link_startswith = link_startswith
				self.file_types = file_types
				self.file_starts = file_starts
				self.sub_dirs = sub_dirs
				self.sp_flags = sp_flags
				self.sp_extension = sp_extension
				self.overwrite_bool = overwrite_bool
				self.dimention = dimention
				try:
					self.dl_done = dl_done
					del dl_done
				except: pass
				try:
					self.Project = Project
					del Project
				except:
					if path!=None:
						self.Project = get_file_name(path)[:-5]
				try:
					self.img_to_sort = sequence
					del sequence
				except:
					self.img_to_sort = None
				try:
					self.sub_links = sub_links
					del sub_links
				except:
					pass
				try:
					self.dir_sorted = dir_sorted
					del dir_sorted
				except:
					pass
				try:
					self.has_missing = has_missing
					del has_missing
				except:
					pass


				del main_link, link_startswith, file_types, file_starts, sub_dirs,
				sp_flags, sp_extension, overwrite_bool, dimention
				proj_good = True
			except Exception as e:
				traceback.print_exc()
				#print(existing_data)
				try:
					self.main_link = existing_data[0]
				except:
					self.corruptions += [1]
					xprint('/rh/Corrupted Data! Error code: 601x1/=/')
					proj_good = False
				if proj_good:
					try:
						self.link_startswith = existing_data[1]
					except:
						proj_good = False
						xprint('/rh/Corrupted Data! Error code: 601x2/=/')
						self.corruptions += [4]

				if proj_good:
					try:
						self.file_types = eval(existing_data[2])
					except Exception as e:

						proj_good = False
						xprint('/rh/Corrupted Data! Error code: 601x3/=/')
						self.corruptions += [4]

				if proj_good:
					try:
						self.file_starts = existing_data[3]
					except:
						proj_good = False
						xprint('/rh/Corrupted Data! Error code: 601x4/=/')
						self.corruptions += [4]

				if proj_good:
					try:
						self.sub_dirs = eval(existing_data[4]) #sub directory list
					except:
						proj_good = False
						xprint('/rh/Corrupted Data! Error code: 601x5/=/')
						self.corruptions += [2]
					try:  #added in v5.0 may not be in older files
						self.sp_flags = eval(existing_data[5])
						self.sp_extension = eval(existing_data[6])
						self.overwrite_bool = eval(existing_data[7])
					except IndexError: pass
				if proj_good:
					try:  #added in v5.1 may not be in older files
						self.dl_done = eval(existing_data[8])
					except IndexError:
						pass


			if proj_good:
				file = reader(list_path, 'rb', output = 'str')
				if file.strip() == '':
					list_good = False
					xprint('/rh/Corrupted Data! Error code: 601x6/=/')
					self.corruptions += [3]
				else:
					self.all_list = eval(str(file))
					print('list found')
					list_good = True

				#print(x)
			if proj_good and list_good:
				if os_exists('data/leach_projects/' + self.Project + '/errors.txt'):
					self.errors = len([i for i in open('data/leach_projects/' + self.Project + '/errors.txt').readlines() if len(i.strip()) == 0])
				else:
					self.errors = 0
				if self.has_missing == None:
					self.has_missing = self.errors > 0

				if path!=None:
					self.Project = get_file_name(path)[:-5]
				if offline: return (True, True)
				if self.dl_done:
					print('It seems  the old prject download was complete!!')
					if self.has_missing:
						xprint('/r/Also have some MISSING files/=/')
					try:
						temp = asker(out="""\u29bf Do you want to get updated data from the project link? %s
\u29bf If you want make a fresh start with that project name type /hui/ fresh /=///hui/ f /=/
\u29bf To open the project in Browser enter /hui/ b /=/
\u29bf To Create CBZ file(s) of the project in Browser enter /hui/ cbz /=/
/g/  >> /=/"""%(' /h/[Recommended]/=/' if self.has_missing == True else ''), extra_opt=('b', 'fresh', 'f', 'cbz'), extra_return = ('browser', 'fresh', 'fresh', 'cbz'))

					except LeachICancelError:
						xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
						leach_logger("000||11000||%s||f-Stop||was_done||don't want to update proj or anything"%(self.Project))
						return 0

					if temp == 'browser' or temp == 'cbz':
						if 'mangafreak' in self.sp_flags:
							if not os_exists('Download_projects/' + self.Project + '/'):
								xprint("\n  /hui/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
								return 0
							self.sub_dirs = natsort.natsorted([get_file_name(i[0]) for i in self.all_list if os_isdir('Download_projects/' + self.Project + '/' + get_file_name(i[0]))])
							self.all_list = []
							for i in range(len(self.sub_dirs)):
								for j in os_listdir('Download_projects/' + self.Project + '/' + self.sub_dirs[i]):
									# print(j)
									if os_isfile('Download_projects/' + self.Project + '/' + self.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
										self.all_list.append([j, i])

							self.img_to_sort = True
							self.sp_extension = ''
						if temp == 'browser':
							try:
								first_page = make_pages(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension, self.dir_sorted)

								run_in_local_server(self.port, host_dir='%s/%s.html'%(self.Project, self.Project))


							except EOFError:
								leach_logger('11000x40001x1||' + self.Project)
								print("Cancel command entered!\nReturning to main page")
								return 0
							except KeyboardInterrupt:
								leach_logger('11000x40001x1||' + self.Project)
								print("cancel command entered!\nReturning to main page")
								return 0
							except LeachICancelError:
								leach_logger('11000x40001x0||' + self.Project)
								print("cancel command entered!\nReturning to main page")
								return 0

							return 0

						else: # cbz
							try:
								first_page = make_cbz(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension)
								print('CBZ Created in "%s"'%first_page)
							except EOFError:
								leach_logger('11000x50001x0||' + self.Project)
								print("Cancel command entered!\nReturning to main page")
								return 0
							except KeyboardInterrupt:
								leach_logger('11000x50001x0||' + self.Project)
								print("cancel command entered!\nReturning to main page")
								return 0
							return 0
					elif temp == True:
						self.existing_found = False
						self.update = True
						self.overwrite_bool = False
						leach_logger('11000x2||%s'%self.Project, user_name)
					elif temp == 'fresh':
						#print("Okay! Enter a new project name in the next line.")

						Project = self.Project
						self.__init__()
						self.Project = Project
						self.existing_found = False
						leach_logger('11000x1||%s'%self.Project, user_name)


					elif temp == False: return 0

						#remove('data/leach_projects/'+ self.Project + '/')
					del temp
				else:
					try:
						temp = asker("""\u29bf Do you want to
resume the Project '%s'
yes/y to resume
\u29bf /hui/ fresh /=///hui/ f /=/ to Start fresh
/yh/(warning! last project data will be erased, /=/downloaded files will be safe, unless the program replaces the files with new ones)
/gh/  >> /=/"""%self.Project, extra_opt = ('f', 'fresh'), extra_return = ('fresh', 'fresh'))
					except LeachICancelError:
						xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
						leach_logger("000||11000||%s||f-Stop||was_paused||don't want to resume proj or anything"%self.Project)
						return 0
					if temp == True:
						print('============ Reloaded =============')
						leach_logger('11000x3||%s'%self.Project, user_name)
						self.existing_found = True
					elif temp == 'fresh':
						leach_logger('11000x4||%s'%self.Project, user_name)
						#clear file data
						#writer(self.Project + '.list', 'w', '', 'data/leach_projects', '10009')
						#writer(self.Project + '.proj', 'w', '', 'data/leach_projects', '10009')

						Project = self.Project
						self.__init__()
						self.Project = Project
						self.existing_found = False
					elif temp == False: return 0
				return (True, True)
			else:
				print("Could not load data from file. Please start over.")
				self.existing_found = False

				return (False, False)


				#print('error')

			#download_files(listx, state)
		elif not blind:
			# self.existing_found = 0
			print('Insufficient data!\n')
			self.corruptions += [0]
			return (False, False)
		else:
			self.corruption = []
			return (False, False)
	def main(self):      #func_code = 10009  v
		global death, sp_arg_flag, server_code, dying, death_talk
		"""runs the mainloop of the projects runtime code"""
		self.__init__()
		try:
			if not server_running: server_launcher.start()
		except:
			pass


		while True:
			try:
				if death or dying: raise LeachICancelError
				self.Project = safe_input('\nEnter Batch download directory (Project name): ').strip()

				if any(ord(i)<32 or ord(i) == 127 for i in self.Project) or self.Project!=remove_non_uni(self.Project, '10009'):
					xprint("/r/Invalid Charecter!\n/y/Please retry...\n/=/")
					continue

			except LeachICancelError:
				dying = True
				while dying:
					try:
						death_talk += 1
						death = True
						if death_talk<2: xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
						leach_logger("0x1||10009||User Exit-0")

						while server_code == None: time.sleep(.5)

						server_code.server_close()
						dying = False
						exit(0)
					except EOFError:
						return 0
					except KeyboardInterrupt:
						return 0
				# sys_exit(0)
			__command = self.Project.lower()
			if self.Project == '':
				print('You must enter a Project name here.')
			elif __command in ['?disable-dl-thread', '?d-dl-t']:
				sp_arg_flag['disable dl cancel'] = True
				print('Disabled download cancellation by adding join thread option')
				return 0

			elif __command in ['?enable-dl-thread', '?e-dl-t']:
				sp_arg_flag['disable dl cancel'] = False
				print('Enabled download cancellation by adding removing thread option [DEFAULT]')
				return 0
			elif __command in ['?disable-dl-get', '?d-dl']:
				sp_arg_flag['disable dl get'] = True
				print('Disabled download save by using requests.head')
				return 0

			elif __command in ['?enable-dl-get', '?e-dl'] :
				sp_arg_flag['disable dl get'] = False
				print('Enabled download save by using requests.get [DEFAULT]')
				return 0

			elif __command in ['?enable-ara-ara', '?e-noise'] :
				sp_arg_flag['ara_ara'] = True
				print('Enabled fun sounds [DEFAULT]')
				return 0

			elif __command in ['?disable-ara-ara', '?d-noise'] :
				sp_arg_flag['ara_ara'] = False
				print('Enabled fun sounds [DEFAULT]')

			elif __command in ['?disable-browser', '?d-br']:
				sp_arg_flag['no browser'] = True
				print('Disabled opening Downloads in browser')
				return 0

			elif __command in ['?enable-browser', '?e-br'] :
				sp_arg_flag['no browser'] = False
				print('Enabled opening Downloads in browser [DEFAULT]')
				return 0

			elif __command in ['?disable-download-limit', '?d-dlim']:
				sp_arg_flag['dl'] = True
				print('Disabled Download Limit [DEFAULT]')
				return 0

			elif any(__command.startswith(i) for i in ['?enable-downlaod-limit', '?e-dlim']) :
				try:
					_temp_ = float(__command.split()[1]) #input will be in KB 1*1024
				except:
					xprint("/y/Invalid Download Speed Limit/=/")
					return 0
				sp_arg_flag['max dlim'] = _temp_
				print('Enabled Download Limit at', _temp_, 'kbps')
				return 0

			else:
				break

		temp = self.Project
		temp1 = temp.replace('"', '')
		if temp1[0] == "'" and temp1[1] == "'": temp = temp[1:-1]
		try:
			from_file = True
			if temp1.endswith('.proj') and os_isfile(temp1):
				if asker("Project file detected.\n\u29bf Do you want re-open project from that file?\n >> "):
					leach_logger("10009x0||%s||fileOpen"%(self.Project), user_name)
					if self.data_checkup(path = temp1, proj_name= temp) == 0:
						return 0
				else: from_file = False
			else: from_file = False

			if from_file == False:
				if any([i in self.Project for i in '/\<>?"*|:']):
					print('Project name can\'t have these charecters : /\<>?"*|:\n\n')
					return 0

				# self.project_dir = self.Project[:].replace('/', '-').replace('\\', '-').replace('|', '-').replace(':', '-').replace('*', '-').replace('"', "'").replace('>', '-').replace('<', '-').replace('?', '-')
				leach_logger("10009x0||%s||Checking Project Database"%(self.Project), user_name)
				if self.Project in reader('data/projects.db').split('\n'):
					print('Existing Project name found!')
					proj_good = False
					list_good = False
					if self.data_checkup() == 0:
						return 0
				else: # runs a blunt scan if the file exists
					Project = self.Project
					if self.data_checkup(blind=True) == 0:
						self.__init__()
						self.Project = Project
			del from_file
		except LeachICancelError:
			xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
			leach_logger("000||10009||%s||f-Stop||is_proj_file||user probably freaked out for too much Ques"%self.Project)

			return 0


		del temp, temp1

		if any(i in self.Project for i in '\\/|:*"><?'):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0

		Ctitle('Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))

		if self.existing_found == False:
			if self.update:
				if os_exists('data/leach_projects/' + self.Project): rmdir('data/leach_projects/' + self.Project)

				self.all_list = []
				self.sub_dirs = []
				self.sub_links = []
				self.dl_done = False
				sub_links = []
				sub_dirs = []
				sub_links2 = []

				if not self.check_sp_links(self.main_link, ['nh', 'mangafreak', 'webtoon']):
					page = self.dl_page()
					if page:
						link_true = True
					else:
						self.main_link = safe_input("/rh/Link Unavailable! /=/It seems the previous link is unaccessable right now.\nPlease Retry the project sometimes later with stable internet connection\n(possible cause: no internet or wrong link)\n")
						return 0

				if self.check_sp_links(self.main_link, 'webtoon'):
					print("Checking for links, please wait...")
					if self.webtoon_link() == 'all good':
						pass
					else:
						xprint("/r/It seems the link is dead\n/y/please recheck the link and create a fresh Project/=/")
						return 0


				elif self.check_sp_links(self.main_link, 'mangafreak'):
					print("Update isn't available for mangafreak")
					self.sp_flags.append('ignore_on_null_content') # do not save null files
					#self.sp_flags.append('stop_on_null_content') # stops downloading after receiving a null file
					try:
						if asker('\u29bf Do you want to re-download files from the same link?\n >> '):
							will_unzip = asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

							if will_unzip:
								self.sp_flags.append("dl unzip")
								if asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
									self.sp_flags.append("del dl zip")
							try:
								self.link_startswith = self.mangafreak_link(self.main_link)

							except EOFError:
								print("Cancel command entered! stopping")
								return 0
							except KeyboardInterrupt:
								print("Cancel command entered! stopping")
								return 0
							if self.link_startswith == 0: # cancel code
								return 0


							self.file_types = ('zip', )
							self.file_starts = ''

							leach_logger('10009x1||%s||is_mangafreak||%s'%(self.Project, str(self.sp_flags)), user_name)

					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						leach_logger("000||10009||%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0

				elif self.check_sp_links(self.main_link, 'nh'):
					try:
						self.link_startswith, title =self.nhentai_link(self.main_link)

					except EOFError:
						print("Cancel command entered! stopping")
						return 0
					except KeyboardInterrupt:
						print("cancel command entered! stopping")
						return 0

					if self.link_startswith == False and title == False:
						print("Failed to get data from %s\nReturning back to main page."%self.main_link)
						return 0

					if title!=False and self.link_startswith!='':
						#sub_dirs.append(title.replace('/', '-').replace('?', '-').replace('\\', '-').replace('|', '-').replace(':', '-').replace('*', '-').replace('"', "'").replace('>', '-').replace('<', '-'))

						leach_logger('10009x0||%s||is_nh'%(self.Project), user_name)

				else:
					sub_links2 = []
					try:
						self.img_to_sort = asker("\n\n\u29bf Will download in sequncial order? ")
					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')

						leach_logger("000||10009||%s||f-Stop||UI||user left while asking self.img_to_sort "%self.Project)
						return 0

					link_startswith_re = re_compile('^' + self.link_startswith)

					try:
						if self.dimention == 0:
							xprint("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")
							try:
								self.dimention = int(safe_input("Enter the index of your choice (1/2/3): "))
							except ValueError:
								self.dimention = -1
							while self.dimention not in [1, 2, 3]:
								try:
									self.dimention = int(safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
								except ValueError:
									self.dimention = -1

							leach_logger('10009x1||%s||dimention||%s'%(self.Project, self.dimention), user_name)

						if self.dimention == 1 or self.dimention == 3:
							sub_links2 += [self.main_link]
						if self.dimention == 2 or self.dimention == 3:
							soup = bs(remove_noscript(page.content), parser)
							# link_startswith = input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")
							leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), user_name)
							sub_links2 += list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href')!=None]))

						Ctitle('[Indexing] Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))


						for i in sub_links2:

							if i.startswith('#'): continue
							elif i.startswith('//'): i = 'https:' + i

							elif i.startswith('../'):
								_temp = self.main_link
								while i.startswith('../'):
									_temp = go_prev_dir(_temp)
									i = i.replace('../', '', 1)
								i = _temp + i
								del _temp

							elif self.partial_do_all == 0 and i.startswith('/'):
								print("Partial link detected - ", i, "\nSearching for home page.")
								#print(start)
								self.homepage = self.homepage_searcher.search(self.main_link)
								#print(homepage)
								try:
									if self.homepage!=None:
										print("Home page detected: ", self.homepage.group())
										is_homepage = safe_input("\nIs this the homepage? \n(y for yes\nn for no\na for all)\n")
										if is_homepage == "a":
											self.partial_do_all = 1
											is_homepage = 'y'
										if is_homepage == 'y':
											self.homepage = self.homepage.group()
										elif is_homepage == 'n':
											self.homepage = safe_input("\nEnter the home page: ")
											io2 = safe_input('\nIs it for all other links?(y/n)')
											if io2 == 'y':
												self.partial_do_all = 1
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
										self.homepage = safe_input("\nEnter the home page: ")
										io2 = safe_input('Is it for all other links?(y/n)')
										if io2 == 'y':
											self.partial_do_all = 1
										elif io2!='n':
											print("Invalid input!")
											time.sleep(5)
											exit(0)
									i = self.homepage + i
								except LeachICancelError:
									xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
									leach_logger("000||10009||%s||f-Stop||asking4home||maybe user tired"%self.Project)
									return 0
							elif self.partial_do_all == 1 and i.startswith('/'):
								i = self.homepage + i
							if '//' not in i:
								temp = self.homepage_searcher.search(self.main_link).group()
								if temp.endswith('/'):
									if i.startswith('/'): i = temp + i[1:]
									else: i = temp + i
								else:
									if i.startswith('/'): i = temp + i
									else: i = temp + '/' + i

							if link_startswith_re.search(i)!=None:
								sub_links.append(i)

						del sub_links2

						self.sub_links = natsort.natsorted(remove_duplicate(sub_links), key = lambda x: x.lower())
						del sub_links

					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						leach_logger("000||10009||%s||f-Stop||asking4home||user probably freaked out for too much Ques"%self.Project)
						return 0



			else:
				if os_exists('data/leach_projects/' + self.Project): rmdir('data/leach_projects/' + self.Project)
				if self.corruptions!=[] and self.corruptions != [0]:
					leach_logger("10009x1||%s||Corruptions||%s||%s"%(self.Project,  str(self.corruptions), '<br>'.join(reader('data/leach_projects/' + self.Project + '.proj', 'rb', True, 'str').strip().split('\n'))), user_name)

				writer('errors.txt', 'a', '', 'data/leach_projects/' + self.Project, '10009') #reset error file


				self.all_list = []
				self.sub_dirs = []
				self.sub_links = []
				sub_links2 = []
				#sub_links_filtered = []
				self.file_types = set()
				self.link_startswith = ''
				self.file_starts = ''
				sub_links = []
				link_true = False
				try:
					self.main_link = safe_input("\nEnter the link: ")
					leach_logger('10009x1||%s||m_link||%s'%(self.Project, self.main_link), user_name)
					while link_true == False:
						if self.check_sp_links(self.main_link, ['nh', 'mangafreak', 'webtoon']):

							if self.check_sp_links(self.main_link, 'mangafreak'):
								print("mangafreak link detected!!")
								is_mangafreak = asker("\u29bf Do you want to download manga images from this links?? (/hui/ y /=///hui/ n /=/)\n>> ")
								if is_mangafreak:
									self.sp_flags.append('ignore_on_null_content') # do not save null files
									self.sp_flags.append('stop_on_null_content') # stops downloading after receiving a null file

									will_unzip = asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

									if will_unzip:
										self.sp_flags.append("dl unzip")
										if asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
											self.sp_flags.append("del dl zip")
									try:
										_temp = self.mangafreak_link(self.main_link)
										if _temp == 0:
											return 0
										if _temp!= '':
											self.link_startswith = _temp
											del _temp
											self.file_types = ('zip', )
											self.file_starts = ''

											leach_logger('10009x1||%s||is_mangafreak.sp_flags||%s'%(self.Project, str(self.sp_flags)), user_name)
											link_true = True
											break

									except EOFError:
										print("Cancel command entered! stopping")
										return 0
									except KeyboardInterrupt:
										print("cancel command entered! stopping")
										return 0
									# sub_links = ''
									#exit(0)


							if self.check_sp_links(self.main_link, 'webtoon'):
								xprint('/y/Webtoon link detected!/=/')
								is_webtoon = asker('\u29bf Do you want to download the Entire Web comic?? (/hui/ y /=///hui/ n /=/)\n/gh/>>/=/  ')

								if is_webtoon:
									xprint("/y/Checking for links, please wait.../=/")
									if self.webtoon_link() == 'all good':
										self.link_startswith = 'https://www.webtoons.com'
										link_true = True
									else:
										xprint("/r/It seems the link is dead\n/y/please recheck the links and your internet connection/=/")
										return 0


							if  self.check_sp_links(self.main_link, 'nh'): #main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
								xprint("/y/nhentai link detected!!/=/")
								is_nh = asker("\u29bf Do you want to download doujin images from this links?? (/hui/ y /=///hui/ n /=/)\n/gh/>>/=/  ")
								####( io )
								if is_nh:
									if os_name == 'Windows' and ara_ara:
										self.play_yamatte_t.start()

									self.link_startswith, title = self.nhentai_link(self.main_link)
									#print(link_startswith, title)
									if self.link_startswith == 0 and title == 0:
										return 0

									if title!=False and self.link_startswith!='':
										#sub_dirs.append(title.replace('/', '-').replace('?', '-').replace('\\', '-').replace('|', '-').replace(':', '-').replace('*', '-').replace('"', "'").replace('>', '-').replace('<', '-'))
										self.file_types = img
										self.file_starts = ''
										leach_logger('10009x1||%s||is_nh||True||Assigned after testing the link'%(self.Project), user_name)
										link_true = True
										break

							if self.check_sp_links(self.main_link, 'pinterest'):
								print("Pinterest link detected.\nDo you want to try the special features for pinterest images?\nWarning: All images may not be the same from the website as you see\n")
								if asker('>> '):

									if self.check_sp_links(self.main_link, 'pinterest-pin'):
										try:
											self.dimention = int(safe_input("Enter the index of your choice (1/2/3): "))
										except ValueError:
											self.dimention = -1
										while self.dimention not in [1, 2, 3]:
											try:
												self.dimention = int(safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
											except ValueError:
												self.dimention = -1



									self.link_startswith = 'https://www.pinterest.com'
						if link_true == False:
							try:
								while True:
									page = self.dl_page()
									if page:
										link_true = True
										break
							except LeachICancelError:
								xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
								return 0


					if self.link_startswith == '':

						print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")

						try:
							self.dimention = int(safe_input("Enter the index of your choice (1/2/3): "))
						except ValueError:
							self.dimention = -1
						while self.dimention not in [1, 2, 3]:
							try:
								self.dimention = int(safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
							except ValueError:
								self.dimention = -1
						leach_logger('10009x1||%s||dimention||%s'%(self.Project, self.dimention), user_name)

						if self.dimention == 1 or self.dimention == 3:
							sub_links2 += [self.main_link]

						if self.dimention == 2 or self.dimention == 3:
							#page = requests.get(main_link, headers=header_())
							#if not page:
							#	xprint('/rh/Error code 605x\nConnection Failed, The program will break in 5 second/=/')
							#	time.sleep(5)
							#	leach_logger("XXXX Program crashed opening: '" + main_link + "' Error code 605 from main function collecting current page.", ush)
							#	exit(0)
							#print(page.content)
							#time.sleep(1000)
							soup = bs(remove_noscript(page.content), parser)
							self.link_startswith = safe_input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")
							leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), user_name)
							sub_links2 += list(set([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href')!=None]))


						file_types_i = safe_input("\nEnter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg, mp3) or just write the category (ie: image, music, video): ")
						if file_types_i == 'image':
							self.file_types = img
						else:
							self.file_types = tuple(i.strip(i) for i in file_types_i.split(', '))
						leach_logger('10009x1||%s||f_types||%s'%(self.Project, str(self.file_types)), user_name)

						self.file_starts = safe_input("\nFile Links Starts With (if known or need to be specified): ")
						leach_logger('10009x1||%s||f_starts||%s'%(self.Project, self.file_starts), user_name)
						# project_path = Project[:]

						#if start[-1'/'): start += '/'
						#if start.startswith(): start = start[1:]
							#sub_dirs = []
						#len_sub_links = str(len(sub_links))
						# count = 0
						print('\n')



						self.img_to_sort = asker("\n\n\u29bf Will download in sequncial order? ")
						self.overwrite_bool = asker("\u29bf Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>")

				except LeachICancelError:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					leach_logger("000||10009||%s||f-Stop||asking4sequence||probably user didnt get it"%self.Project)
					return 0
				#else: all_list = list(all_list)
				#leach_logger(" + +%s' + '%s' + %s' + '%s' + +"%(main_link, link_startswith, str(file_types), file_starts), user_name)

				if self.sub_dirs == []:
					print("Checking links...")

					link_startswith_re = re_compile('^' + self.link_startswith)

					Ctitle('[Indexing] Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))

					for i in sub_links2:


						#sys.stdout.flush()
						#print(link)
						# print(i)
						if i.startswith('#'): continue
						elif i.startswith('//'): i = 'https:' + i

						elif i.startswith('../'):
							_temp = self.main_link
							while i.startswith('../'):
								_temp = go_prev_dir(_temp)
								i = i.replace('../', '', 1)
							i = _temp + i
							del _temp

						elif self.partial_do_all == 0 and i.startswith('/'):
							print("Partial link detected - ", i, "\nSearching for home page.")
							#print(start)
							self.homepage = self.homepage_searcher.search(self.main_link)
							#print(homepage)
							try:
								if self.homepage!=None:
									print("Home page detected: ", self.homepage.group())
									is_homepage = safe_input("\nIs this the homepage? \n(y for yes\nn for no\na for all)\n")
									if is_homepage == "a":
										self.partial_do_all = 1
										is_homepage = 'y'
									if is_homepage == 'y':
										self.homepage = self.homepage.group()
									elif is_homepage == 'n':
										self.homepage = safe_input("\nEnter the home page: ")
										io2 = safe_input('\nIs it for all other links?(y/n)')
										if io2 == 'y':
											self.partial_do_all = 1
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
									self.homepage = safe_input("\nEnter the home page: ")
									io2 = safe_input('Is it for all other links?(y/n)')
									if io2 == 'y':
										self.partial_do_all = 1
									elif io2!='n':
										print("Invalid input!")
										time.sleep(5)
										exit(0)
								i = self.homepage + i
							except LeachICancelError:
								xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
								leach_logger("000||10009||%s||f-Stop||asking4home||probablyuser tired"%self.Project)
								return 0
						elif self.partial_do_all == 1 and i.startswith('/'):
							i = self.homepage + i
						if '//' not in i:
							temp = self.homepage_searcher.search(self.main_link).group()
							if temp.endswith('/'):
								if i.startswith('/'): i = temp + i[1:]
								else: i = temp + i
							else:
								if i.startswith('/'): i = temp + i
								else: i = temp + '/' + i


						if link_startswith_re.search(i)!=None:
							sub_links.append(i)

					self.sub_links = natsort.natsorted(remove_duplicate(sub_links), key= lambda x: x.lower())
					del sub_links2, sub_links


			if self.sub_dirs == []:
				leach_logger("10009x2||%s||%i"%(self.Project, len(self.sub_links)), user_name)
				for i in self.sub_links:
					self.sub_dirs.append(trans_str(parse.unquote(html_unescape(get_dir(i))), {'/\\|:*><?': '-', '"':"'"}).strip())

				len_sub_links = len(self.sub_links)




				sub_range = range(len_sub_links)
				indx1 = Process(target=self.list_writer, args=(self.sub_links, sub_range[::3]))
				indx2 = Process(target=self.list_writer, args=(self.sub_links, sub_range[1::3]))
				indx3 = Process(target=self.list_writer, args=(self.sub_links, sub_range[2::3]))

				try:

					indx1.start()
					indx2.start()
					indx3.start()
					try:
						indx1.join()
						indx2.join()
						indx3.join()

					except EOFError:
						leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
						xprint("/yh/Project indexing cancelled by Keyboard/=/")
						self.break_all = True
						return 0
					except KeyboardInterrupt:
						leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
						xprint("/yh/Project indexing cancelled by Keyboard/=/")
						self.break_all = True
						return 0

				except Exception as e:
					xprint("/rh/code: Error 607\n The program will break in 5 seconds/=/")
					leach_logger("10009x-1||%s||%s||%s"%(self.Project, e.__class__.__name__, str(e)), user_name)
					time.sleep(5)
					exit(0)



			if self.img_to_sort: self.all_list = natsort.natsorted(self.all_list, key = lambda x: x[0].lower())


			writer('projects.db', 'a', self.Project + '\n', 'data', '10009')


		leach_logger("10009x3||%s||%i||%i"%(self.Project, len(self.sub_dirs), len(self.all_list)), user_name)

		# clean the files if exist
		writer(self.Project + '.list', 'w', '', 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'w', '', 'data/leach_projects', '10009')

		# write new data
		writer(self.Project + '.list', 'w', str(self.all_list), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'w', 'main_link= "%s"\n'%self.main_link, 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'link_startswith= "%s"\n'%self.link_startswith, 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'file_types = %s\n'%str(self.file_types), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'file_starts= "%s"\n'%self.file_starts, 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'sub_dirs = %s\n'%str(self.sub_dirs), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'sp_flags = %s\n'%str(self.sp_flags), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'sp_extension = "%s"\n'%self.sp_extension ,'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'overwrite_bool = %s\n'%str(self.overwrite_bool), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'dimention = %s\n'%str(self.dimention), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'sequence = %s\n'%str(self.img_to_sort), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'Project = "%s"\n'%str(self.Project), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'sub_links = %s\n'%str(self.sub_links), 'data/leach_projects', '10009')
		writer(self.Project + '.proj', 'a', 'dir_sorted = %s\n'%str(self.dir_sorted), 'data/leach_projects', '10009')


		print('\n')
		self.all_list2 = remove_duplicate(self.all_list)
		self.total = len(self.all_list2)

		self.done -= self.errors  # to remove duplicate count


		all_list_r = list(range(self.total))

		Ctitle('[Downloading] Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))


		try:
			makedirs('Download_projects/' + self.Project)
		except:
			pass

		t11 = Process(target=self.distribute, args=(all_list_r[::10], 1))
		t2 = Process(target=self.distribute, args=(all_list_r[1::10], 2))
		t3 = Process(target=self.distribute, args=(all_list_r[2::10], 3))
		t4 = Process(target=self.distribute, args=(all_list_r[3::10], 4))
		t5 = Process(target=self.distribute, args=(all_list_r[4::10], 5))
		t6 = Process(target=self.distribute, args=(all_list_r[5::10], 6))
		t7 = Process(target=self.distribute, args=(all_list_r[6::10], 7))
		t8 = Process(target=self.distribute, args=(all_list_r[7::10], 8))
		t9 = Process(target=self.distribute, args=(all_list_r[8::10], 9))
		t10 = Process(target=self.distribute, args=(all_list_r[9::10], 10))
		t99 = Process(target=self.retry_errors)

		if sp_arg_flag['max dlim']!=0:
			self.tictoc = time.time()
			sp_arg_flag['chunk_size'] = int(sp_arg_flag['max dlim']*102.4) + 1
			t_dlim = Process(target=self.speed_limiter)
			t_dlim.start()

		t_dl_speed = Process(target=self.speed_tester)
		t_dl_speed.start()


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

		if sp_arg_flag['disable dl cancel'] == True:
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

				if sp_arg_flag['max dlim']!=0: t_dlim.join()
				t_dl_speed.join()

				Ctitle('[Download Complete] Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))

			except EOFError:
				print("Hard cancel command entered! stopping")
				self.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.break_all = True

		will_open = None


		if not 'mangafreak' in self.sp_flags:
			try:
				first_page = make_pages(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension, self.dir_sorted)
			except EOFError:
				print("Hard cancel command entered! stopping")
				self.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.break_all = True

		while self.break_all == False and any([t11.is_alive(), t2.is_alive(), t3.is_alive(), t4.is_alive(), t5.is_alive(), t6.is_alive(), t7.is_alive(), t8.is_alive(), t9.is_alive(), t10.is_alive(), t99.is_alive()]):
			try:
				will_open = safe_input()
				# print([t11.is_alive(), t2.is_alive(), t3.is_alive(), t4.is_alive(), t5.is_alive(), t6.is_alive(), t7.is_alive(), t8.is_alive(), t9.is_alive(), t10.is_alive(), t99.is_alive()])
			except LeachICancelError:
				self.break_all = True
				leach_logger("000||10009||%s||D-Break||~||~"%(self.Project))
				break

		if self.break_all:
			xprint("/yh/Project continuation cancelled by Keyboard/=/")
			leach_logger("000||10009||%s||D-Stop||Downloading||%i|%i"%(self.Project, self.done, self.errors))
		else:
			if 'mangafreak' in self.sp_flags:
				if not os_exists('Download_projects/' + self.Project + '/'):
					xprint("\n  /hui/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
					return 0
				self.sub_dirs = natsort.natsorted([get_file_name(i[0]) for i in self.all_list if os_isdir('Download_projects/' + self.Project + '/' + get_file_name(i[0]))])
				self.all_list = []
				for i in range(len(self.sub_dirs)):
					for j in os_listdir('Download_projects/' + self.Project + '/' + self.sub_dirs[i]):
						# print(j)
						if os_isfile('Download_projects/' + self.Project + '/' + self.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
							self.all_list.append([j, i])
				try:
					first_page = make_pages(self.all_list, self.sub_dirs, self.Project, True, '', self.dir_sorted)
				except EOFError:
					leach_logger('10009x40001x0||' + self.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

				except KeyboardInterrupt:
					leach_logger('10009x40001x0||' + self.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

			if will_open == 'b':
				run_in_local_server(self.port, host_dir='%s/%s.html'%(self.Project, self.Project))
				return 0

			elif will_open == 'cbz': # cbz
				try:
					first_page = make_cbz(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension)
					print('CBZ Created in "%s"'%first_page)
				except EOFError:
					leach_logger('10009x50001x0||' + self.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				except KeyboardInterrupt:
					leach_logger('10009x50001x0||' + self.Project)
					print("cancel command entered!\nReturning to main page")
					return 0
				return




	def dl_page(self):		#func_code= 1000B  v
		try:
			page = requests.get(self.main_link, headers=header_(), timeout=5)
			writer(self.Project + '.html', 'wb', page.content, 'data/leach_projects/%s'%self.Project, '1000B')

		except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
			self.main_link = safe_input("/rh/Invalid URL!/=/ (possible cause: no internet or wrong link)\n\nPlease re-enter the link: ")
			return False

		return page



	def main_offline(self):		#func_code= 1000A  v
		global death, sp_arg_flag, server_code, dying, death_talk, server_launcher
		"""runs the mainloop of the projects runtime code"""
		self.__init__()
		try:
			server_launcher.start()
		except:
			pass


		while True:
			try:
				if death or dying: raise LeachICancelError
				self.Project = safe_input('\nEnter Batch download directory (Project name): ')

			except LeachICancelError:
				dying = True
				while dying:
					try:
						death_talk += 1
						death = True
						if death_talk<2: xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
						leach_logger("0x1||1000A||User Exit-0")

						while server_code == None: time.sleep(.5)

						server_code.server_close()
						dying = False
						exit(0)
					except EOFError:
						return 0
					except KeyboardInterrupt:
						return 0

			__command = self.Project.lower()
			if self.Project == '':
				print('You must enter a Project name here.')
			elif __command in ['?disable-dl-thread', '?d-dl-t']:
				sp_arg_flag['disable dl cancel'] = True
				print('Disabled download cancellation by adding join thread option')
				return 0

			elif __command in ['?enable-dl-thread', '?e-dl-t']:
				sp_arg_flag['disable dl cancel'] = False
				print('Enabled download cancellation by adding removing thread option [DEFAULT]')
				return 0
			elif __command in ['?disable-dl-get', '?d-dl']:
				sp_arg_flag['disable dl get'] = True
				print('Disabled download save by using requests.head')
				return 0

			elif __command in ['?enable-dl-get', '?e-dl'] :
				sp_arg_flag['disable dl get'] = False
				print('Enabled download save by using requests.get [DEFAULT]')
				return 0

			elif __command in ['?enable-ara-ara', '?e-noise'] :
				sp_arg_flag['ara_ara'] = True
				print('Enabled fun sounds [DEFAULT]')
				return 0

			elif __command in ['?disable-ara-ara', '?d-noise'] :
				sp_arg_flag['ara_ara'] = False
				print('Enabled fun sounds [DEFAULT]')

			elif __command in ['?disable-browser', '?d-br']:
				sp_arg_flag['no browser'] = True
				print('Disabled opening Downloads in browser')
				return 0

			elif __command in ['?enable-browser', '?e-br'] :
				sp_arg_flag['no browser'] = False
				print('Enabled opening Downloads in browser [DEFAULT]')
				return 0

			else:
				break

		temp = self.Project
		proj_good = False
		list_good = False
		temp1 = temp.replace('"', '')
		if temp1[0] == "'" and temp1[1] == "'": temp = temp[1:-1]
		try:
			from_file = True
			if temp1.endswith('.proj') and os_isfile(temp1):
				if asker("Project file detected.\n\u29bf Do you want re-open project from that file?\n >> "):
					leach_logger("1000Ax0||%s||fileOpen"%(self.Project), user_name)
					_temp = self.data_checkup(path = temp1, proj_name= temp, offline = True)
					if _temp == 0:
						return 0
					proj_good, list_good = _temp
				else: from_file = False
			else: from_file = False

			if from_file == False:
				if any([i in self.Project for i in '/\<>?"*|:']):
					print('Project name can\'t have these charecters : /\<>?"*|:\n\n')
					return 0

				# self.project_dir = self.Project[:].replace('/', '-').replace('\\', '-').replace('|', '-').replace(':', '-').replace('*', '-').replace('"', "'").replace('>', '-').replace('<', '-').replace('?', '-')
				leach_logger("1000Ax0||%s||Checking Project Database"%(self.Project), user_name)
				if self.Project in reader('data/projects.db').split('\n'):
					print('Existing Project name found!')
					_temp = self.data_checkup(offline = True)
					if _temp == 0:
						return 0
					proj_good, list_good = _temp
			del from_file
		except LeachICancelError:
			xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
			leach_logger("000||1000A||%s||f-Stop||is_proj_file||user probably freaked out for too much Ques"%self.Project)
			return 0


		del temp, temp1

		if any(i in self.Project for i in '\\/|:*"><?'):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0

		if proj_good and list_good:
			Ctitle('[Analizing] Project %s [%s%s] [:%i]'%(self.Project, mode_emoji[run_mod], run_mod.upper(), self.port))
			if 'mangafreak' in self.sp_flags:
				if self.dl_done:
					if not os_exists('Download_projects/' + self.Project + '/'):
						xprint("\n  /hiu/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
						return 0
					self.sub_dirs = natsort.natsorted([get_file_name(i[0]) for i in self.all_list if os_isdir('Download_projects/' + self.Project + '/' + get_file_name(i[0]))])
					self.all_list = []
					for i in range(len(self.sub_dirs)):
						for j in os_listdir('Download_projects/' + self.Project + '/' + self.sub_dirs[i]):
							# print(j)
							if os_isfile('Download_projects/' + self.Project + '/' + self.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
								self.all_list.append([j, i])


				else:
					print("can't generate web pages offline from incomplete manga freak download")
					return 0


			output_type = asker("""Do you want to
\u29bf View the Project in Browser? /hui/ b /=/
\u29bf or Make CBZ files from the images? /hui/ cbz /=/
\u29bf or Cancel /hui/ c /=/
  /gh/>>/=/ """, extra_opt=('b', 'cbz', 'c'), extra_return=('browser', 'cbz', None), on_error= None, )

			if output_type == None:
				return 0

			elif output_type == 'browser':
				try:
					first_page = make_pages(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension, self.dir_sorted)

					run_in_local_server(self.port, host_dir = '%s/%s.html'%(self.Project, self.Project))


				except EOFError:
					leach_logger('1000Ax40001x1||' + self.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				except KeyboardInterrupt:
					leach_logger('1000Ax40001x1||' + self.Project)
					print("cancel command entered!\nReturning to main page")
					return 0
				except LeachICancelError:
					leach_logger('1000Ax40001x0||' + self.Project)
					print("cancel command entered!\nReturning to main page")
					return 0

				return 0

			else: # cbz
				try:
					first_page = make_cbz(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension)
					print('CBZ Created in "%s"'%first_page)
				except EOFError:
					leach_logger('1000Ax50001x0||' + self.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				except KeyboardInterrupt:
					leach_logger('1000Ax50001x0||' + self.Project)
					print("cancel command entered!\nReturning to main page")
					return 0
				return 0


		else:
			print('Sorry, it seems there\'s no previous project with this name. \nThere is a chance that the project data was Corrupted!\nRetry when online...')


@atexit.register
def on_exit():
	leach_logger('0x1||00000||Program Terminated')


if __name__ == '__main__':
	#Update err_header.txt#######################################
	if os_isfile('data/err_header.txt'):
		error_hdr_file = reader('data/err_header.txt')
		temp_ = re_sub('\,{2,}', ',', error_hdr_file)

		if temp_[-1] == ',': temp_ = temp_[:-1]

		err_hdr_list = eval(temp_)
		#print(type(err_hdr_list))
		if type(err_hdr_list) == tuple:
			err_hdr_list = Counter(err_hdr_list)

			writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '00000')

		elif type(err_hdr_list) == list:
			_t = Counter()
			for i, j in err_hdr_list:
				_t[i] = j

			err_hdr_list = _t

			writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '00000')


		elif type(err_hdr_list) == dict:
			err_hdr_list = Counter(err_hdr_list)
	else:
		err_hdr_list = Counter()


	#############################################################



	try:
		init_upto = 'Importing Assets'
		print("Connecting to server...")
		Ctitle('Connecting to server 🌐')
		_connect_net()
		init_upto = 'Getting IP'
		leach_logger("001||" + _VERSION + "||" + dig_info.getSystemInfo() + "||" + user_net_ip + "||" + str(start_up_dt) + "||" + Nsys.get_tz() + "||" + str(time.time()-start_up) + 's', 'lock')
		server_start = time.time()


		run_mod = god_mode()

		init_upto = 'God mode'

		import getpass


		if run_mod == 'offline' :
			Ctitle('Connecting to server [OFFLINE]⚠')
			if os_exists('data/.temp/updateG.ext') and os_exists('data/.temp/updateL.ext'):
				exec(decrypt(reader('data/.temp/updateG.ext'), "lock").strip())
				exec(decrypt(reader('data/.temp/updateL.ext'), "lock").strip())
			else:
				xprint("/r/Failed to startup. /y/Please connet to the internet for the first initialization/=/")
				leach_logger('0x0')

				try:
					IloveAsuna = safe_input('Press enter to exit...', getpass.getpass)
					backdoor = IloveAsuna
					if hashlib_md5('RandomteXtZYIQrgYlb0sHdFLaIW' + backdoor[2] + '#testTubeAlabam@ToGBNr3SfYrIIfHQSY' + backdoor[0] + '2Jpx4Piks84XCvN8El' + backdoor[:-2:-1] + 'xf4wXXygZPILxsOUAP' + backdoor[::-2] + '#testTubeAlabam@%sToGBNr3SfYrIIfHQSY'%backdoor[::-1] + backdoor[0] + '2Jpx4Piks84XCvN8El' + backdoor[1::-2] + 'KgCaIWjP6X4W5h4P2G').hexdigest() == '751fa7e19763b50a399806fdcc5dee34':
						pass
					else:
						exit(0)
				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
					exit(0)

		elif run_mod == 'online':
			# exec(__update__G)
			# exec(__update__L)
			if float(_VERSION)<float(_latest_version):
				_version_updater(_latest_version, _latest_link, _latest_hash, _latest_filename, _latest_size, cloud_data_link)


		else: exit(0)

		init_upto = 'Loading backend server'


		'751fa7e19763b50a399806fdcc5dee34'

		try:
			if not os_isdir("./Download_projects"): makedirs("./Download_projects")
		except PermissionError:
			print("Can't write in this directory, either change the write permission or move this program to somewhere with write permission.\nError code: 00000x101")
			leach_logger("00000x101||Download_projects||1")
			sys_exit()

		init_upto = 'Dl folder making'


		print("Done!!")
		time.sleep(1)

		clear_screen()

		leach_logger('002||' + str(time.time()-server_start) + 's||' + server_version, 'leach')
		Ctitle('Log in [%s%s]'%(mode_emoji[run_mod], run_mod.upper()))
		ush = log_in()

		leach_logger('003||%s||%s'%(ush, Nsys.compressed_dt()), user_name)

		init_upto = 'user login'

	except EOFError:
		xprint(hard_cancel)
		leach_logger('0x1||00000||Hard Exit by User on Start up. Init upto - "%s"')
		exit(0)

	except KeyboardInterrupt:
		xprint(hard_cancel)
		leach_logger('0x1||00000||Hard Exit by User on Start up. Init upto - "%s"'%init_upto)
		exit(0)







	program_class = None

	main_port = (int(ush, 16) % (60000 - 49200 + 1)) + 49200

	server_status = check_server("http://localhost:%i"% main_port, '00000', timeout=2)

	if server_status == False:
		proxy_port = (int(ush, 16) % (64000 - 60001 + 1)) + 60001

	running_port = proxy_port if proxy_port else main_port

	if server_status == True:
		pass
	elif server_status in (False, None):
		server_launcher = Process(target=run_server_t, args= (server_status, 'Download_projects'))
	else:
		exit()

	program_class = web_leach()

	while True:
		Ctitle('Project ? [%s%s] [:%i]'%(mode_emoji[run_mod], run_mod.upper(), running_port))
		if check_internet('https://www.yahoo.com/', '00000', 2) or check_internet('https://www.bing.com', '00000', 2):
			run_mod = 'online'
			Ctitle('Project ? [%s%s] [:%i]'%(mode_emoji[run_mod], run_mod.upper(), running_port))
			program_class.main()
		else:
			run_mod = 'offline'
			Ctitle('Project ? [%s%s] [:%i]'%(mode_emoji[run_mod], run_mod.upper(), running_port, mode_emoji[run_mod]))
			program_class.main_offline()



