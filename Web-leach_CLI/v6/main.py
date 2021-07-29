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


# pylint: disable=anomalous-backslash-in-string, global-variable-not-assigned


requirements_all = ('requests',  'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pypiwin32', 'comtypes', 'psutil', 'lxml', 'pywin32-ctypes')
logger = True


# importing required packages

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


from print_text import XprintClass		#f_code = 60000

XprintEngine = XprintClass()
xprint = XprintEngine.slowtype

try:
	from constants import *		#f_code = 70000
	import ctypes
	def Ctitle(title):
		"""sets CLI winodw title
		title: Window title"""

		try:
			ctypes.windll.kernel32.SetConsoleTitleW(title)
		except:
			#print('\33]0;%s\a'%title, end='', flush=True)
			pass

	Ctitle('Loading Assets \u26ef')


	class server_code:
		"""creating fake class
		to bypass error"""

		def __init__(self=None):
			pass
		def server_close(self=None):
			pass
		def serve_forever(self=None):
			pass

	#########################################################


	# SYS tools #######################
	from sys import exit as sys_exit, executable as sys_executable
	exit = sys_exit

	from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
	from os import devnull as os_devnull
	import os
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


	import rcrypto		#f_code = 80000
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
	import json

	try:
		from bs4 import BeautifulSoup as bs
		parser = 'lxml'
		try:
			bs('<br>', parser)
		except:
			parser = 'html.parser'
		from googlesearch import search as g_search
		import requests, natsort, urllib3
		import _server001_		#f_code = 90000
		if os_name == 'Windows': import mplay4

		has_all_libs = True

	except:
		has_all_libs = False


	from headers_file import header_list        # f_code = 30000
	##########################################

	#Other Libs###############################
	from collections import Counter
	import functools
	import operator


	import dig_info		#f_code = A0000

	##########################################
except KeyboardInterrupt:
	xprint(Constants.hard_cancel)
	import sys
	sys.exit(0)
except EOFError:
	xprint(Constants.hard_cancel)
	import sys
	sys.exit(0)


# Re Define to speed up###################
len = len
range = range
##########################################

process_id = randint(2003, 9999) # a process ID to identify use multiple windows in the same time from log
boss = 0
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
												   #
class Error404(Exception): 						   #
	pass                                           #												   
#                                                  #
####################################################



class AboutApp_:
	_VERSION = '5.60000'
	_APP_NAME = 'Web-Leach'
	_APP_DESC = 'Web-Leach is a simple python script to download files from web'
	_APP_AUTHOR = 'Ratul Hasan'
	_APP_AUTHOR_EMAIL = 'wwwqweasd147[at]gmail[dot]com'
	_APP_URL = ''
	_APP_COPYRIGHT = 'Copyright (C) 2017 Ratul Hasan'
	_APP_LICENSE = 'GNU General Public License v3.0'
	_APP_LICENSE_URL = 'https://www.gnu.org/licenses/'
	_APP_VERSION = _VERSION
	_APP_PATH = os_realpath(__file__)
	_APP_ICON_PATH = 'web-leach.ico'
	_APP_LICENSE = 'MIT'
	_APP_LICENSE_URL = ''
	_APP_COPYRIGHT = 'Copyright (c) 2016, Ratul Hasan'
	_APP_COPYRIGHT_URL = ''
	_APP_REQUIREMENTS = requirements_all
	_APP_REQUIREMENTS_WIN = requirements_win
	_APP_REQUIREMENTS_MAC = []
	_APP_REQUIREMENTS_LINUX = []

	running_os = os_name
	Server_version = 'UNREACHED'

	cloud_data_link_global = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global(v5.5+).txt'
	cloud_data_link = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update (server v5.500004).txt'

	g_mode = None

	leach_projects = 'data/leach_projects/'

AboutApp = AboutApp_()

class DefaultConfig:
	has_all_libs = has_all_libs
	ara_ara = True #to control parody noise
	no_log = False #to stop logging
	death = False
	dying = False

	proxy_port = 0

	ara_ara = False #to control parody noise

	sp_arg_flag = {'disable dl cancel' : False,
			'disable dl get' : False,
			'ara ara': False if ara_ara == None else ara_ara,
			'no log': False if no_log == None else no_log,
			'no browser': False,
			'max dlim': 0, # in kbps
			'chunk_size': 8192, # in Bytes
			}

	death_talk = 0

	mode_emoji = {
		'online': "🌐",
		'offline': "⚠"
	}

	running_port = None
	server_running = False
	server_status = None
	run_mod = None


class AppConfig_(DefaultConfig):
	def __init__(self):
		"""Sets app config"""

		self.immutable_config()
		# self.__default__()


	def immutable_config(self):
		"""Sets immutable config
		for one time set
		*won't change on self.__default__()"""
		self.__update__G = 'pass'
		self.__update__L = 'pass'
		self.user_list = ['bec6113e5eca1d00da8af7027a2b1b070d85b5ea', 'eb23efbb267893b699389ae74854547979d265bd']
		self.g_mode = None


	def __default__(self):
		"""Import config from default"""

		for i in DefaultConfig.__dict__:
			if i[0] != '__':
				self.__dict__[i] = DefaultConfig.__dict__[i]


	def set_default(self, name):
		"""Sets default config for specific name

		name: Name of config variable
		"""
		self.__dict__[name] = DefaultConfig.__dict__[name]

	def set_config(self, name:str, value):
		"""Sets config for specific name

		name: Name of config variable
		value: Variable value

		returns: Old value of config variable
		"""

		if hasattr(self, name):
			old = getattr(self, name)
		setattr(self, name, value)

		return old

config = AppConfig_()


class UserData_:
	def __init__(self):
		self.Device_Data = dig_info.getSystemInfo()
		self.user_ip = 'offline'
		self.userhash = 0
		self.user_name = None

	def get_user_ip(self):
		"""connects to the internet and returns the users global ip"""

		current_header = Netsys.header_()
		try:
			self.user_ip = json.loads(requests.get('https://api.myip.com/', headers = current_header, timeout=3).content)
			return self.user_ip
		except NetErrors as e:
			xprint("/r/Error code: 605x1\nNo internet connection!/=/")
			leach_logger("605x1||%s||%s"%(Netsys.hdr(current_header, '0000C'), e.__class__.__name__), 'lock')
			return 'offline'

		except Exception as e:
			xprint('/r/', e.__class__.__name__, "occurred. Please inform the Author.\nError code: 0000Cx-1(%s)/=/"%e.__class__.__name__)
			leach_logger("0000Cx-1||" + Netsys.hdr(current_header, '0000C') + '||%s||%s'%(e.__class__.__name__, str(e)), 'lock')
			time.sleep(5)
			exit(0)

	def log_in(self):      #func_code=00016  v
		if boss!=1:
			userhash = 0
			while self.userhash == 0:
				try:
					user_name = IOsys.safe_input("Enter username: ")
				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
					leach_logger("0x1||00016||Login exit")
					exit(0)

				userhash = hashlib_sha1(user_name.encode()).hexdigest()
				for x in config.user_list:
					if userhash == x:
						self.userhash = userhash
						self.user_name = user_name
						break
				else:
					xprint("/rh/User not found!/=/ \nWait a minute! WHO are YOU?!!")
					if os_name == "Windows":
						ex = mplay4.ex_vol
						mplay4.load('data/.temp/who_r_u.mp3').play()
					time.sleep(5)
					if os_name == 'Windows':
						mplay4.set_win_vol(ex)
		else:
			self.userhash = 'eb23efbb267893b699389ae74854547979d265bd'

		if not os_exists('data/projects.db'):
			Fsys.writer('projects.db', 'a', '', 'data', '00016')
		if self.userhash == 'eb23efbb267893b699389ae74854547979d265bd':
			AboutApp.g_mode = 'Kirito'

UserData = UserData_()


class IOsys_:

	def clear_screen(self):    #func_code= 00001 vvv
		"""clears terminal output screen"""

		if os_name == "Windows":
			os_system('cls')
		else:
			os_system('clear')


	def delete_last_line(self, lines=1):      #func_code=00002 vvv
		"""Use this function to delete the last line in the STDOUT

		args:
		-----
			lines: total number of lines *1"""

		for _ in range(lines):
			#cursor up one line
			sys_write('\x1b[1A')

			#delete last line
			sys_write('\x1b[2K')

	def leach_logger(self, io, key='lock'):   #func_code=0000A  v
		"""saves encrypted logger data to file\n
		(new in 5.3_class: auto adds dt_() at the begining)

		args:
		-----
			io: the log message\n
			key: salt text"""

		if config.sp_arg_flag['no log']:
			return None
		try:
			while True:
				try:
					try:
						_key = "Asuna"
						salt = hashlib_sha1(key.encode()).hexdigest()
						Fsys.writer('userlog.leach', 'ab', rcrypto.encrypt(salt + ('%s||'%Nsys.compressed_dt()) + str(process_id) + '||' + io + '||', _key).encode('utf-8') + b'\n', 'data', '00008')
						break
					except EOFError: pass
					except KeyboardInterrupt: pass
				except EOFError: pass
				except KeyboardInterrupt: pass

		except EOFError: self.leach_logger(io, key='lock')
		except KeyboardInterrupt: self.leach_logger(io, key='lock')

	def safe_input(self, msg='', i_func=input, o_func=xprint,
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
	def asker(self, out='', default=None, True_False=(True, False),
			extra_opt=tuple(), extra_return=tuple(),
			i_func=input, o_func=xprint, on_error= LeachICancelError,
			condERR= Constants.condERR, no_bool = False):      #func_code=00010  v
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

		Ques2 = self.safe_input(out, i_func, o_func, on_error).lower()
		if default!= None and Ques2 == '':
			return default
		#Ques2 = Ques2
		while Ques2 not in (tuple() if no_bool else Constants.cond) + Nsys.flatten_array(extra_opt, tuple):
			Ques2 = self.safe_input(condERR, i_func, o_func, on_error).lower()
			#Ques2 = Ques2

		if not no_bool and Ques2 in Constants.cond:
			if Ques2 in Constants.yes:
				return True_False[0]
			else:
				return True_False[1]
		else:
			return extra_return[extra_opt.index(Ques2)]


IOsys = IOsys_()

leach_logger = IOsys.leach_logger


class Fsys_:

	def get_sep(self, path):
		if '/' in path:
			return '/'
		elif '\\' in path:
			return '\\'
		else:
			return os.sep

	def loc(self, x, _os_name='Linux'):    #func_code=00007  v
		"""to fix dir problem based on os

		args:
		-----
			x: directory
			os_name: Os name *Linux"""

		if _os_name == 'Windows':
			return x.replace('/', '\\')
		else:
			return x.replace('\\', '/')

	def get_file_name(self, directory, mode= 'dir'):
		"""takes a file directory and returns the last last part of the dir (can be file or folder)

		args:
		-----
			directory: the file directory, only absolute path to support multiple os
			mode: url or file directory
		"""

		if isinstance(directory, bytes): directory = directory.decode()
		if mode == 'url':
			extra_removed = Netsys.gen_link_facts(directory)['path']
			if extra_removed[-1] == "/":
				return ""
			return os_basename(extra_removed)
		elif mode == 'dir':
			return os_basename(directory)
		else:
			raise ValueError



	def get_file_ext(self, directory, mode='dir', no_format='noformat'):      #func_code=00012  v
		"""to get the extension of a file directory

		args:
		-----
			directory: file directory relative or direct
			no_format: returning format if no file extention was detected *noformat"""

		temp = self.get_file_name(directory, mode).split('.')
		if len(temp) == 1:
			return no_format
		else:
			return temp[-1]

	def get_dir(self, directory, mode='dir'):      #func_code=0001D  v
		"""takes a file directory and returns the last last part of the dir (can be file or folder)

		args:
		-----
			directory: the file directory, only absolute path to support multiple os
			mode: url or file directory (os based)
		"""

		if mode == 'url':
			extra_removed = Netsys.gen_link_facts(directory)['path']

			

			dirs = extra_removed.split('/')
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

	def go_prev_dir(self, directory, preserve_sep=False):    #func_code=0000E  v
		"""returns the previous path str of web link or directory
		warning: returns only in linux directory format
		if preseve_sep is True, it will preserve the separator of the directory

		directory: the file directory, only absolute path to support multiple os
		preserve_sep: if True, it will preserve the separator of the directory
		"""

		if not preserve_sep:
			directory = self.loc(directory, 'Linux')
		
		sep = self.get_sep(directory)

		if directory.endswith(sep):
			return sep.join(directory[:-1].split(sep)[:-2]) + sep
		else:
			return sep.join(directory.split(sep)[:-2]) + sep


	def reader(self, direc, read_mode='r', ignore_error= False, output = None,
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

		if (not os_isfile(self.loc(direc))):
			if (not ignore_missing_log):
				print(self.loc(direc), 'NOT found to read. Error code: 00013')
				leach_logger('00013||' + f_code + '||' + direc)
			return on_missing

		with open(self.loc(direc), read_mode) as f:
			out = f.read()
		if output == None:
			if read_mode == 'r':
				output = 'str'
			else:
				output = 'bin'
		if ignore_error:
			out = Datasys.remove_non_uni(out, '00013', output)

		else:
			if output == 'str' and read_mode == 'rb':
				out = out.decode()
			elif output == 'bin' and read_mode == 'r':
				out = out.encode(encoding)

		return out

	def writer(self, fname, mode, data, direc=None, f_code='None',
				encoding='utf-8'):    #func_code=00008  vvv
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

		if any(i in fname for i in ('/\\|:*"><?')):
			# these charecters are forbidden to use in file or folder Names
			leach_logger('00008x1||%s'%fname)
			fname = Datasys.trans_str(fname, {'/\\|:*><?': '-', '"':"'"})


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
				locs = self.loc(direc, 'Linux')
				if any(i in locs for i in ('\\|:*"><?')):
					leach_logger('00008x2||%s'%locs)
					locs = Datasys.trans_str(locs, {'\\|:*><?': '-', '"':"'"})

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
				if locs.endswith('/'): direc = self.loc(locs + fname)
				else: direc = self.loc(locs + '/' + fname)

				if 'b' not in mode:
					with open(direc, mode, encoding=encoding) as f:
						f.write(data)
				else:
					with open(direc, mode) as f:
						f.write(data)

		except Exception as e:
			if logger: traceback.print_exc()
			if e.__class__.__name__ == "PermissionError":
				xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc == None else direc, '/y/\nPlease inform the author. Error code: %sx101/=/'%f_code)
				leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
				raise LeachPermissionError
			else:
				leach_logger('00008x-1||' + e.__class__.__name__ + '||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, str(e)))
				xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc == None else direc, '/y/\nPlease inform the author. Error code: 00008x' + f_code, '/=/')
				raise e

Fsys = Fsys_()


class OSsys_:
	"""Operating System functions"""
	def install(self, pack, alias=None):    #func_code=00005  v
		"""Just install package

		args:
		-----
			pack: the name the library (beautifulsoup4, requests)
			alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

		if alias == None:
			alias = pack

		subprocess_call([sys_executable, "-m", "pip", "install", '--disable-pip-version-check', '--quiet', alias])


	

	def install_req(self, pkg_name, alias=None):     #func_code=00006  vvv
		"""install requirement package if not installed

		args:
		-----
			pkg_name: Package name to search if installed
			alias: if the pip package name is different from lib name,
				then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

		if pkg_name not in self.get_installed():
			xprint("/y/Installing missing libraries/=/")
			self.install(pkg_name, alias)
			IOsys.delete_last_line()
		
		if pkg_name not in self.get_installed():
			xprint('/r/Failed to install and load required Library: "%s"/y/\nThe app will close in 5 seconds/=/'%pkg_name)
			try: leach_logger('00006||%s||%s'%(pkg_name, str(Netsys.check_internet("https://pypi.org", '00006'))))
			except NameError: pass
			return False
		return True

	def get_installed(self):
		"""returns a list of installed libraries"""

		import pkg_resources as pkg_r
		reload(pkg_r)

		return [pkg.key for pkg in pkg_r.working_set]

	def import_make(self):      #func_code= 0001F  v
		""" reads and exec() necessary files to create different formats of
		output [ie: html, cbz]
		"""
		try:
			exec(Fsys.reader('make_html2.py'), globals())      # f_code= 40000
		except Exception as e:
			print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
			leach_logger('40000x-1||' + str(e.__class__.__name__) + '||' + str(e))
			time.sleep(5)
			exit()

		try:
			exec(Fsys.reader('make_cbz2.py'), globals())      # f_code= 50000
		except Exception as e:
			print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
			leach_logger('50000x-1||' + str(e.__class__.__name__) + '||' + str(e))
			time.sleep(5)
			exit()

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


OSsys = OSsys_()


def install_missing_libs():
	if os_name == 'Windows':
		if not 'psutils' in OSsys.get_installed():
			config.has_all_libs = False

	if config.has_all_libs == False:
		for i in requirements_all:
			if not OSsys.install_req(i):
				time.sleep(5)
				exit()

		if os_name == "Windows":
			for i in requirements_win:
				if not OSsys.install_req(i):
					time.sleep(5)
					exit()    #required in mplay4
	
	config.has_all_libs = True


install_missing_libs()

######### RE-IMPORTING THE PYTHON 3RD PARTY LIBRARIES #########

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


NetErrors = (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, requests.exceptions.ConnectionError, urllib3.exceptions.SSLError)



class Netsys_:
	"""Network system functions"""

	def __init__(self):
		self.link_extractor = re_compile( r'^(?P<noQuery>(?P<homepage>(?P<schema>((?P<scheme>[^:/?#]+):(?=//))?(//)?)(((?P<login>[^:]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@/?#:]*)(?::(?P<port>\d+)?)?)?)?(?P<path>[^?#]*))(\?(?P<query>[^#]*))?(#(?P<fragment>.*))?')	# compiled regex tool for getting homepage
		# https://regex101.com/r/UKWPmt/1
		# noQuerry: https://regex101.com/r/UKWPmt/1
		# homepage: https://regex101.com
		# schema: https://
		# scheme: https
		# login: 
		# password: 
		# host: regex101.com
		# port: 
		# path: /r/UKWPmt/1
		# query: ? part
		# fragment: # part

	def header_(self):    #func_code=00004  v
		"""returns a random header from header_list for requests lib"""

		return( {'User-Agent':random_choice(header_list)})

	def hdr(self, header, f_code=''):    #func_code=00009  v
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

	def get_link(self, i, current_link, homepage):		#func_code= 0001E  v
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
				_temp = Fsys.go_prev_dir(_temp)
				i = i.replace('../', '', 1)
			i = _temp + i

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


	def get_homepage(self, link):
		"""Gets the homepage of a link

		Args:
		-----
			link : link to get homepage from
		"""
		self.homepage_searcher=re_compile('(https?://[^/]*)')	# compiled regex tool for getting homepage
		x = self.homepage_searcher.search(link)
		if x:
			return x.group(1)
		else:
			return False
		


	def check_internet(self, link, f_code, timeout=None):       #f_code=00017  v
		"""Check if the connection is available or not

		args:
		-----
			link: link to check for connection status"""
		current_header = self.header_()
		try:
			if timeout == None:
				r = requests.head(link, headers=current_header)
			else:
				r = requests.head(link, headers=current_header, timeout= timeout)

			if r:
				return True
			else:
				leach_logger('00017||%s||%s||%s||%s'%(link, self.hdr(current_header, '00017'), f_code, str(r.status_code)))
		except NetErrors:
			leach_logger('00017||%s||%s||%s'%(link, self.hdr(current_header, '00017'), f_code))
			return False
		except KeyboardInterrupt:
			return False
		except EOFError:
			return False


	def run_server(self, port, cd=None, f_code= '00000'):      #func_code=0000B  v
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
			if config.server_status in (False, None):
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

	def run_server_t(self, server_status, cd='./'):      #func_code=0001B  v
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

		if config.server_status == True:
			return

		port = config.running_port # user specified port or proxy port

		_t = self.run_server(port= port, cd= cd)
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


	def run_in_local_server(self, port, host_dir=''):     #func_code=0000D  v
		"""opens a directory or a file in localhost server using browser

		args:
		-----
			port : port number
			host_dir : desired file or folder directory"""

		if config.sp_arg_flag['no browser']: return 0

		webbrowser.open_new_tab('http://localhost:%i/%s'%(port, host_dir))

	def check_server(self, link, f_code, timeout=None):       #f_code=0001A  v
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

	def remove_noscript(self, content): # f_code=00021
		"""Removes <noscript> contents from html to fool my app

		content: HTML content returned by requests.get().content"""
		return re_sub(b"(?i)(?:<noscript>)(?:.|\n)*?(?:<\/noscript>)", b'', content)


	def gen_link_facts(self, link):
		"""Generates facts for a link

		link: link to be checked"""

		if isinstance(link, bytes):
			link = link.decode()
		facts = dict()
		x = self.link_extractor.search(link)
		if x:
			facts['is link'] = True
			facts['scheme'] = x.group('schema')
			facts['scheme'] = x.group('scheme')
			facts['login'] = x.group('login')
			facts['host'] = x.group('host')
			facts['port'] = x.group('port')
			facts['path'] = x.group('path')
			facts['query'] = x.group('query')
			facts['fragment'] = x.group('fragment')
			facts['noQuery'] = x.group('noQuery')
			facts['homepage'] = x.group('homepage')

			facts['has homepage'] = (facts['homepage']!=None)
			facts['after homepage'] = link.startswith('/')
			facts['needs scheme'] = link.startswith('//')
			facts['is absolute'] = (facts['scheme']!=None and facts['host']!=None)

			return facts
		
		else:
			return None


		# self.link_extractor = re_compile( r'^(?P<noQuery>(?P<schema>((?P<scheme>[^:/?#]+):(?=//))?(//)?)(((?P<login>[^:]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@/?#:]*)(?::(?P<port>\d+)?)?)?(?P<path>[^?#]*))(\?(?P<query>[^#]*))?(#(?P<fragment>.*))?')	# compiled regex tool for getting homepage
		# https://regex101.com/r/UKWPmt/1
		# noQuerry: https://regex101.com/r/UKWPmt/1
		# homepage: https://regex101.com
		# schema: https://
		# scheme: https
		# login: 
		# password: 
		# host: regex101.com
		# port: 80
		# path: /r/UKWPmt/1
		# query: ? part
		# fragment: # part

Netsys = Netsys_()

print(Netsys.gen_link_facts("hhj"))

class Datasys_:
	"""Data types and conversion functions"""

	def remove_duplicate(self, seq, return_type = list):	#func_code= 00000  vvv
		"""removes duplicates from a list or a tuple
		also keeps the array in the same order

		args:
		-----
			seq: `tuple`|`list` to remove dups
			return_type: type of array to return"""

		return return_type(dict.fromkeys(seq))

	def remove_non_ascii(self, text, f_code):    #func_code=00003 vvv
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

	def remove_non_uni(self, text, f_code='?????', types= 'str', encoding= 'utf-8'):    #func_code=00018  vvv
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
			return self.remove_non_ascii(text, f_code)

	def trans_str(self, txt, dicts): #func_code= 00019 vvv
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

	def flatten2D(self, arr):     # f_code=00020
		functools.reduce(operator.iconcat, arr, [])


Datasys = Datasys_()

class ProjectType_:
	def __init__(self, project_name):
		"""initialize variables on every start of a project"""
		self.Project = project_name		# project name (case insensitive *need to work on it)
		self.__default__()


	def __default__(self):
		"""set default values on every start of a project"""
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


		### Defaults
		self.from_file = None	# if the project was loaded from file
		self.list_file = None
		self.proj_file = None
		self.proj_ext = ('.wlproj', '.wllist')
		self.homepage = ''	# just assigning the homepage variable
		self.indx_count = 0	# counts the number of indexed links
		self.existing_found = False	# indicates if valid existing project is found
		self.dl_done = False	# indicates if the project scrapping was done or not
		self.has_missing = None		# indicates if the Project has any missing files. {5.4 and above}
		#* this won't ask input * so add it in GUI 
		self.dir_sorted = False		# will sort directories by name
		self.corruptions = []	# list of corruptions in project data if there's any or empty

		### Need input
		self.main_link = None	# the main link
		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""
		self.link_startswith = ''	# (str) each sublink must start with
		self.file_types = None	# set of file extensions to be downloaded
		self.file_starts = ''	# (str) each files must start with (used regex)
		self.file_to_sort = True	# indicates if the files will be sorted or not
		self.update = False	# indicates if the project is getting an update or not

		### after list writer 
		self.sub_dirs = []	# list of sub directories on the project folder
		self.sub_links = [] # needed in requests.get() reference value (fixes many issues)
		self.all_list = []	# assigning a list of data links, but duplicates will be cancelled in process

		### after distribute
		self.error_triggers = []	# 0 to 9 the number of tasks
		self.dl_chunks = 0
		self.page_error = 0
		self.re_error = 0   # number of errors after retrying errors

		### download speed limit variables
		self.tictoc = 0
		self.dl_lim = 0
		self.current_chunks = 0
		self.dl_nap_time = 0
		### /download speed limit variables

		self.current_speed = '0 bytes'
		self.is_error = False



	def load_data(self, file_dir):
		"""loads the data from the project file"""

		file_dir = file_dir.replace('"', '')

		if file_dir.endswith(('.proj', '.wlproj')) and os.path.isfile(file_dir):
			self.from_file = file_dir
			proj_path = file_dir

		if not self.from_file:
			if os.path.isfile(AboutApp.leach_projects + self.Project + '.proj'):
				self.proj_ext = ('.proj', '.list')

			elif not os.path.isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				self.__default__()
				return None

			proj_path = os.path.isfile(AboutApp.leach_projects + self.Project + self.proj_ext[0])


		list_path = proj_path[:0-(len(self.proj_ext[0]))] + self.proj_ext[1]

		if os_exists(proj_path):
			self.proj_good = True
			print('db found')

			self.proj_file = Fsys.reader(proj_path, 'rb', True, 'str').strip()

			self.proj_good = self.check_proj_file()

			if self.proj_good:
				if os_exists(list_path):
					self.list_file = Fsys.reader(list_path, 'rb', True, 'str').strip()
					self.list_good = self.check_list_file()

					return self.list_good

			else:
				self.__default__()
				return None

		else:
			self.__default__()
			return None


	def check_proj_file(self):
		"""checks if the project file is valid
		and if valid assigns the data to Class"""

		proj_good = True
		try:
			global Project, main_link, link_startswith, file_types, file_starts, sub_dirs, sp_flags
			global sp_extension, overwrite_bool, dimention, dl_done, sequence, sub_links, has_missing
			global dir_sorted

			existing_data = self.proj_file.split('\n')

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
				if self.from_file:
					self.Project = Fsys.get_file_name(self.Project)[:0-(len(self.proj_ext[0]))]
			try:
				self.file_to_sort = sequence
				del sequence
			except:
				self.file_to_sort = None
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


			del main_link, link_startswith, file_types, file_starts, sub_dirs
			del sp_flags, sp_extension, overwrite_bool, dimention
			proj_good = True
		except:
			if logger: traceback.print_exc()
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
				except:

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

		return proj_good

	def check_list_file(self):
		"""checks if the list file is valid
		and if valid assigns the data to Class"""

		existing_data = self.list_file.replace('\n', '')
		existing_data = existing_data.replace('\r', '')

		if existing_data.strip() == '':
			xprint('/rh/Corrupted Data! Error code: 601x6/=/')
			self.corruptions += [3]
			return False
		else:
			try:
				self.all_list = eval(str(existing_data))
				print('list found')
				return True

			except:
				if logger: traceback.print_exc()
				return False


	def gen_sub_links(self):
		sub_links2 = []
		sub_links = []
		if self.dimention == 1 or self.dimention == 3:
			sub_links2 += [self.main_link]
		if self.dimention == 2 or self.dimention == 3:
			page = self.dl_page(self.main_link, cache=True)
			soup = bs(Netsys.remove_noscript(page.content), parser)
			# link_startswith = input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")
			leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), UserData.user_name)
			sub_links2 += Datasys.remove_duplicate([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href')!=None])

		Ctitle('[Indexing] Project %s [%s%s] [:%i]'%(self.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

		link_startswith_re = re_compile('^' + self.link_startswith)

		self.homepage = Netsys.get_homepage(self.main_link)

		for i in sub_links2:
			i = Netsys.get_link(i, self.main_link, self.homepage)

			if link_startswith_re.search(i)!=None:
				sub_links.append(i)

		del sub_links2

		self.sub_links = Datasys.remove_duplicate(sub_links)
		if self.dir_sorted:
			self.sub_links = natsort.natsorted(self.sub_links[0], key = lambda x: x[0])
		del sub_links


	def gen_sub_dis(self):
		"""generates sub-directories self.sub_dirs"""
		for i in self.sub_links:
			self.sub_dirs.append(Datasys.trans_str(parse.unquote(html_unescape(Fsys.get_dir(i))), {'/\\|:*><?': '-', '"':"'"}).strip())

	


	def dl_page(self, link = None, referer = False, cache = False, failed = False):		#func_code= 1000B  v
		"""Gets a page from the internet and returns the page object
		
		link: page link
		referer: page referer, default = self.main_link, None means don't use referer
		cache: get or store the page object from Cached_data.cached_webpages
		failed: if failed in previous try"""
		if link == None:
			link = self.main_link

		if cache:
			if link in CachedData.cached_webpages:
				return CachedData.cached_webpages[link]


		if referer == False:
			referer_ = Netsys.get_homepage(link)
		else:
			referer_ = referer

		current_header = Netsys.header_()
		if referer:
			current_header['referer'] = referer_
		try:
			page = requests.get(link, headers=current_header, timeout=5)
			
			if not page:
				raise Error404
		except (*NetErrors, Error404) as e:
			if not failed:
				page = self.dl_page(link=link, referer = False if referer==False else referer, cache=cache, failed=True)
			else:
				return None

		if cache:
			CachedData.cached_webpages[link] = page
		return page


ProjectType = ProjectType_('test')



class CachedData_:
	def __init__(self):
		self.cached_webpages = {} 

CachedData = CachedData_()

print(ProjectType.dl_page('htps://ratulhasan14789.github.io/fuck'))

