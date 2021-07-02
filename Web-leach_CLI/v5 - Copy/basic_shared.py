import time
# from basic_vars import *
import Number_sys_conv as Nsys           #f_code = 20000
from print_text import XprintClass
XprintEngine = XprintClass()
xprint =XprintEngine.slowtype

########################################################

##########################################
from random import choice as random_choice, randint

process_id= randint(2003,9999) # a process ID to identify use multiple windows in the same time from log


#########################################################


# SYS tools #######################
from sys import exit as sys_exit,executable as sys_executable
exit = sys_exit
from platform import system as os_name
os_name=os_name()
from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
from os import devnull as os_devnull
from sys import stdout as sys_stdout
from importlib import reload
# from functools import partial
import atexit, traceback
sys_write=sys_stdout.write
del sys_stdout
###################################

# MATH tools ######################
from math import floor
from random import choice as random_choice, randint
from hashlib import sha1 as hashlib_sha1, md5 as hashlib_md5
from re import search as re_search,compile as re_compile, sub as re_sub

from filesize import alternative as filesize_alt, size as filesize_size


from rcrypto import encrypt, decrypt
###################################



# FILE system tools###############
from os import makedirs, remove, rename, system as os_system, listdir as os_listdir, getcwd as os_getcwd
from shutil import rmtree as rmdir
from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname, realpath as os_realpath
from zipfile import ZipFile, BadZipFile
###################################



from threading import Thread as Process



# HTML tools##############################
from html import unescape as html_unescape, escape as html_escape
from urllib import parse
import webbrowser

from headers_file import header_list        # f_code = 30000
##########################################

#Other Libs###############################
from collections import Counter
import dig_info

##########################################

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


class server_code:
	"""creating fake class
	to bypass error"""

	def __init__(self=None):
		pass
	def server_close(self=None):
		pass
	def serve_forever(self=None):
		pass


# import __main__ # used to load assets in global (idea from pydroid)

# ✓
# ✘

def remove_duplicate(seq, return_type = list):	#func_code=00000 vx
	"""removes duplicates from a list or a tuple

	args:
	-----
		seq: `tuple`|`list` to remove dups
		return_type: type of array to return"""

	return return_type(dict.fromkeys(seq))

def trans_str(txt, dicts): #func_code=00019 ✓
	"""replaces all the matching charecters of a string for multuple times

	args:
	-----
		txt: string data
		dicts: dict of { find : replace }"""

	for i in dicts.keys():
		a= dicts[i]
		for j in i:
			txt = txt.replace(j, a)
	return txt

def clear_screen():    #func_code=00001 ✓
	"""clears terminal output screen"""

	if os_name=="Windows":
		os_system('cls')
	else:
		os_system('clear')



def delete_last_line(lines=1):      #func_code=00002 ✓
	"""Use this function to delete the last line in the STDOUT

	args:
	-----
		lines: total number of lines *1"""

	for _ in range(lines):
		#cursor up one line
		sys_write('\x1b[1A')

		#delete last line
		sys_write('\x1b[2K')


def remove_non_ascii(text, f_code):    #func_code=00003 ✓
	"""[DEPRECATED] [STILL WORKS] removes ascii charecters from a string

	args:
	-----
		test: text to remove non ASCII
		f_code: The function Code called this function"""

	try:
		return ''.join([i if ord(i) < 128 else '' for i in text])
	except Exception as e:
		xprint("Failed to remove non-ascii charecters from string.\nError code: 00003x",f_code,'\nPlease inform the author.')
		leach_logger('00003x-1||'+e.__class__.__name__+('||%s||'%str(e))+f_code+'||'+text)

def remove_non_uni(text, f_code='?????', types= 'str', encoding= 'utf-8'):    #func_code=00018 v
	"""Converts a string or binary to unicode string or binary by removing all non unicode char

	args:
	-----
		text: str to work on
		f_code: caller func code
		types: output type ('str' or 'bytes')
		encoding: output encoding *utf-8"""

	try:
		if type(text)==str:
			text =text.encode(encoding, 'ignore')
			if types=='bin': return text
			return text.decode(encoding)
		if types=='bin': return text.decode(encoding,'ignore').encode(encoding)
		return text.decode(encoding,'ignore')
	except Exception as e:
		xprint("/r/Failed to remove non-Unicode charecters from string.\nError code: 00018x",f_code,'/y/\nPlease inform the author./=/')
		leach_logger('00018x-1||'+e.__class__.__name__+('||%s||'%str(e))+f_code+'||'+types+'||'+text)
		return remove_non_ascii(text, f_code)

def header_():    #func_code=00004 v
	"""returns a random header from header_list for requests lib"""
	
	return( {'User-Agent':random_choice(header_list)})

def install(pack, alias=None):    #func_code=00005 v
	"""Just install package

	args:
	-----
		pack: the name the library (beautifulsoup4, requests)\n
		alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

	if alias == None:
		alias = pack

	subprocess_call([sys_executable, "-m", "pip", "install",'--disable-pip-version-check','--quiet', alias])


import pkg_resources as pkg_r
# installed_pkgs=[pkg.key for pkg in pkg_resources.working_set] # list of installed packages

# print(pkg_resources)

def install_req(pkg_name):     #func_code=00006 v
	"""install requirement package if not installed
	
	args:
	-----
		pkg_name: Package name to search if installed"""

	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
		xprint("/y/Installing missing libraries/=/")
		install(pkg_name)
		delete_last_line()
	reload(pkg_r)
	if pkg_name not in (pkg.key for pkg in pkg_r.working_set):
		xprint('/r/Failed to install and load required Library: "%s"/y/\nThe app will close in 5 seconds/=/'%pkg_name)
		try: leach_logger('00006||%s||%s'%(pkg_name, str(check_internet("https://pypi.org", '00006'))))
		except NameError: pass
		return False
	return True



# if os_name=='Windows':
# 	if not 'psutils' in (pkg.key for pkg in pkg_r.working_set):
# 		has_all_libs = False

# if has_all_libs == False:
# 	for i in requirements_all: 
# 		if not install_req(i):
# 			time.sleep(5)
# 			exit()

# 	if os_name=="Windows":
# 		for i in requirements_win: 
# 			if not install_req(i):
# 				time.sleep(5)
# 				exit()    #required in mplay4

# 	from bs4 import BeautifulSoup as bs
# 	parser='lxml'
# 	try:
# 		bs('<br>', parser)
# 	except:
# 		parser = 'html.parser'
# 	from googlesearch import search as g_search
# 	import requests, natsort, urllib3
# 	import _server001_
# 	if os_name=="Windows": import mplay4


def loc(x, _os_name='Linux'):    #func_code=00007 v
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
			encoding='utf-8'):    #func_code=00008 v
	"""Writing on a file

	args:
	-----
		fname: filename
		mode: write mode (w,wb,a,ab)
		data: data to write
		direc: directory of the file, empty for current dir *None
		func_code: (str) code of the running func *empty string
		encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""

	if mode in ('r', 'rb'):
		xprint('/r/Invalid mode\nMust be a Writable Mode/=/')

	if any(i in fname for i in ('\\|:*"><?')):
		leach_logger('00008x1||%s'%fname)
		fname= trans_str(fname, {'/\\|:*><?': '-', '"':"'"})
	if direc == None:
		direc='./'
	direc = direc.strip()
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
				locs= trans_str(locs, {'\\|:*><?': '-', '"':"'"})

			if not os_isdir(locs):
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
						
	except Exception as e:
		if e.__class__.__name__== "PermissionError":
			xprint('/r/',e.__class__.__name__,"occurred while writing", fname, 'in', 'current directory' if direc==None else direc,'/y/\nPlease inform the author. Error code: %sx101/=/'%f_code)
			leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
			raise LeachPermissionError
		else:
			leach_logger('00008x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc,str(e)))
			xprint('/r/',e.__class__.__name__,"occurred while writing", fname, 'in', 'current directory' if direc==None else direc,'/y/\nPlease inform the author. Error code: 00008x'+f_code, '/=/')
			raise e



def hdr(header, f_code=''):    #func_code=00009 v
	"""returns the index of a header
	
	args:
	-----
		header: header dict
		f_code: function caller code"""

	try:
		return str(header_list.index(header['User-Agent']))
	except ValueError as e:
		xprint("/y/DATA CORRUPTION found\nError code: 00009x"+f_code,'/=/')

		leach_logger('00009x'+f_code+'||'+ str(e)+'||'+header)
		return str((-1, header))

	except Exception as e:
		xprint("/y/Some error occurred caused, possible cause: DATA CORRUPTION\nError code: 00009x"+f_code,'/=/')

		leach_logger('00009x-1||'+'||' +f_code+e.__class__.__name__+'||'+ str(e)+'||'+header)
		return str((-1, header))


def leach_logger(io, key='lock'):   #func_code=0000A v
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


def connect_net():      #func_code=0000C v
	"""connects to the internet and returns the users global ip

    return: void, but sets global variable `user_net_ip`"""

	global user_net_ip
	current_header=header_()
	try:
		user_net_ip=requests.get('https://api.myip.com/',headers=current_header, timeout=3).content.decode()
		
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
		xprint("/r/40mError code: 605x1\nNo internet connection!/=/\nChecking Offline mode...")
		leach_logger("605x1||%s||%s"%(hdr(current_header,'0000C'), e.__class__.__name__), 'lock')


	except Exception as e:
		xprint('/r/',e.__class__.__name__, "occurred. Please inform the Author.\nError code: 0000Cx-1(%s)/=/"%e.__class__.__name__)
		leach_logger("0000Cx-1||"+hdr(current_header,'0000C')+'||%s||%s'%(e.__class__.__name__, str(e)), 'lock')
		time.sleep(5)
		exit(0)


def run_in_local_server(port, host_dir=''):     #func_code=0000D v
	"""opens a directory or a file in localhost server using browser

	args:
	-----
		port : port number
		host_dir : desired file or folder directory"""

	if sp_arg_flag['no browser']: return 0

	webbrowser.open_new_tab('http://localhost:%i/%s'%(port, host_dir))

def import_paste():      #func_code=0001C v
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
import_paste_t=Process(target=import_paste)

import_paste_t.start()

boss=0


def go_prev_dir(link):    #func_code=0000E
	"""returns the previous path str of web link or directory
	warning: returns only in linux directory format
	-------"""

	link=loc(link,'Linux')
	if link.endswith('/'):
		return '/'.join(link[:-1].split('/')[:-2])+'/'
	else:
		return '/'.join(link.split('/')[:-2])+'/'



# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
def safe_input(msg='', i_func=input, o_func=xprint,
				on_error= LeachICancelError):     #func_code=0000F
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
				box= i_func()
				return box
			except EOFError:
				if on_error==LeachICancelError:
					raise LeachICancelError
				else:
					return on_error
			except KeyboardInterrupt:
				raise LeachICancelError
			except LeachICancelError:
				leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
				exit(0)
		except EOFError:
			if on_error==LeachICancelError:
				raise LeachICancelError
			else:
				return on_error
		except KeyboardInterrupt:
			if on_error==LeachICancelError:
				raise LeachICancelError
			else:
				return on_error
	except EOFError:
		if on_error==LeachICancelError:
			raise LeachICancelError
		else:
			return on_error
	except KeyboardInterrupt:
		if on_error==LeachICancelError:
			raise LeachICancelError
		else:
			return on_error
def asker(out='', default=None, True_False=(True, False), 
		  extra_opt=tuple(), extra_return=tuple(),
		  i_func=input, o_func=xprint, on_error= LeachICancelError,
		  condERR= condERR, no_bool = False):      #func_code=00010
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
	if default!= None and Ques2=='':
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



def get_file_name(directory, mode= 'dir'):      #func_code=00011
	"""takes a file directory and returns the last last part of the dir (can be file or folder)

	args:
	-----
		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory
	"""

	if isinstance(directory, bytes): directory = directory.decode()
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

	args:
	-----
		directory: file directory relative or direct
		no_format: returning format if no file extention was detected *noformat"""

	temp= get_file_name(directory, mode)
	if len(temp.split('.'))==1:
		return no_format
	else:
		return temp.split('.')[-1]

def get_dir(directory, mode='dir'):      #func_code=0001D
	"""takes a file directory and returns the last last part of the dir (can be file or folder)

	args:
	-----
	directory: the file directory, only absolute path to support multiple os
	mode: url or file directory (os based)
	"""

	if mode=='url':
		fragment_removed = directory.split("#")[0]  # keep to left of first #
		query_string_removed = fragment_removed.split("?")[0]
		scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]

		dirs= scheme_removed.split('/')
		if dirs[-1]=='':
			dirs.pop()
		if dirs==[]:
			return '__HomePage__'
		else:
			return dirs[-1]
	elif mode=='dir':
		if os_basename(directory)=='':
			return os_basename(os_dirname(directory))
		else:
			return os_basename(directory)
	else:
		raise ValueError

def get_link(i,current_link, homepage):		#func_code= 0001E
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
	if i.startswith('#'): i= current_link
	elif i.startswith('//'): i='https:'+i

	elif i.startswith('../'):
		_temp= current_link
		while i.startswith('../'):
			_temp= go_prev_dir(_temp)
			i= i.replace('../', '', 1)
		i= _temp+i
		del _temp

	elif i.startswith('/'):
		i= homepage+i
	if '//' not in i:
		temp=homepage
		if temp.endswith('/'):
			if i.startswith('/'): i=temp+i[1:]
			else: i=temp+i
		else:
			if i.startswith('/'): i=temp+i
			else: i=temp+'/'+i

	return i


def reader(direc, read_mode='r', ignore_error= False, output = None,
			encoding = 'utf-8', f_code= '?????', on_missing= None,
			ignore_missing_log = False):      #func_code=00013
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
		read_mode='rb'

	else:
		read_mode = 'r'

	if (not os_isfile(loc(direc))):
		if (not ignore_missing_log):
			print(loc(direc), 'NOT found to read. Error code: 00013')
			leach_logger('00013||'+f_code+'||'+direc)
		return on_missing

	with open(loc(direc), read_mode) as f:
		out=f.read()
	if output==None:
		if read_mode == 'r':
			output='str'
		else:
			output = 'bin'
	if ignore_error:
		out=remove_non_uni(out, '00013', output)

	else:
		if output=='str' and read_mode=='rb':
			out= out.decode()
		elif output=='bin' and read_mode=='r':
			out = out.encode(encoding)

	return out


def check_internet(link, f_code, timeout=None):       #f_code=00017
	"""Check if the connection is available or not

	args:
	-----
		link: link to check for connection status"""
	current_header=header_()
	try:
		if timeout==None: r=requests.head(link, headers=current_header)
		else: r=requests.head(link, headers=current_header, timeout= timeout)

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

def check_server(link, f_code, timeout=None):       #f_code=0001A
	"""Checks if localhost server is running perfectly or the port is occupied

	link: site link with port [adds /?response on request]
	f_code: caller id
	timeout: request timeout
	"""

	try:
		response = requests.get(link+ '/root?response')
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
