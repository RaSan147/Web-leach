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

print("LOADING ASSETS...")
print(1) #x
requirements_all = ('requests',  'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pypiwin32', 'comtypes', 'psutil', 'lxml', 'pywin32-ctypes')
logger = True


# importing required packages

import Number_sys_conv as Nsys     #fc=1000
# different number based functions I made
start_up_dt = Nsys.compressed_dt() #stores when the program was launched

import time
start_up = time.time()

from platform import system as os_name
os_name = os_name()

if os_name == 'Windows':
	import console_mod     #fc=2000
	console_mod.enable_color()


from print_text import XprintClass     #fc=3000

XprintEngine = XprintClass()
xprint = XprintEngine.slowtype

try:
	from constants import *     #fc=4000
	import ctypes
	def Ctitle(title):     #fc=0001
		"""sets CLI winodw title
		title: Window title"""

		try:
			ctypes.windll.kernel32.SetConsoleTitleW(title)
		except:
			from os import system as os_system
			os_system('title ' + title)

	Ctitle('Loading Assets \u26ef')

	class server_code:     #fc=0002
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


	import rcrypto     #fc=5000
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
		import _server001_
		if os_name == 'Windows': import mplay4

		has_all_libs = True

	except:
		has_all_libs = False


	from headers_file import header_list
	##########################################

	#Other Libs###############################
	from collections import Counter
	import functools
	import operator


	import dig_info     #fc=6000

	##########################################
except EOFError:
	xprint(Constants.hard_cancel)
	import sys
	sys.exit(0)
except KeyboardInterrupt:
	xprint(Constants.hard_cancel)
	import sys
	sys.exit(0)


# Re Define to speed up###################
len = len
range = range
##########################################

process_id = randint(2003, 9999)
# a process ID to identify use multiple windows in the same time from log
boss = 0
server_launcher = Process()

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


print(2) #x
class AboutApp_:     #fc=A000
	""" Contains Information about the app and verion details"""

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

	cloud_data_link_global = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global_6.txt'
	cloud_data_link = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update%20server%20v6.00000.txt'

	g_mode = None

	leach_projects = 'data/leach_projects/'

AboutApp = AboutApp_()

class DefaultConfig:     #fc=0200
	""" Default configaration to load up on each start"""

	disable_lib_check = Constants.DEFAULT_DISABLE_LIB_CHECK
	# if True, the installed lib check will be skipped to speed up
	has_all_libs = has_all_libs
	# this is True when all libs are installed
	ara_ara = False
	#to control parody noise
	no_log = False
	#to stop logging
	death = False
	dying = False


	sp_arg_flag = {'disable dl cancel' : False,
			'disable dl get' : False,
			'ara ara': False if ara_ara == None else ara_ara,
			'no log': False if no_log == None else no_log,
			'no browser': False,
			'max dlim': 0, # in kbps
			'chunk_size': 8192, # in Bytes
			}
	# to control the downloader

	death_talk = 0

	mode_emoji = {
		'online': "🌐",
		'offline': "⚠"
	}
	# emojis for different states

	running_port = None
	# port number of running server by app
	server_running = False
	# is the server running in this app
	server_status = None
	# is the port being used
	# True : by this app/ another instance of this app
	# False: by other app, port locked
	# None : Ready to be used
	run_mod = None
	# is running online or offline

	download_dir = "Download_projects/"
	# download directory
	thread_data_dir = "data/leach_projects/" # + project name
	# location to store the thread data
	data_dir = "data/leach_projects/"
	# location to store project data



class AppConfig_(DefaultConfig):     #fc=0300
	""" Configuration to load up on each start
	also initializes the default when needed

	loads and contains update log, user_list, server infos
	"""
	def __init__(self):     #fc=0301
		""" Sets app config"""

		self.immutable_config()
		# self.__default__()


	def immutable_config(self):     #fc=0302
		""" Sets immutable config
		for one time set
		*won't change on self.__default__()"""
		self.__update__G = 'pass'
		self.__update__L = 'pass'
		self.user_list = ['bec6113e5eca1d00da8af7027a2b1b070d85b5ea', 'eb23efbb267893b699389ae74854547979d265bd']
		self.g_mode = None

		self.server_version="0.6.0.0"


		self._latest_version='5.5'
		self._latest_link='https://rawcdn.githack.com/Ratulhasan14789/Web-Leach_pub/ee5bcde7b25e1655e1dda2803ab002fdad982170/release/CLI/Web%20leach%200.5.5.4.zip'

		self._latest_hash='97b804fb717c0ceee89d1825b79c5ade'
		self._latest_size="7.4mb"
		self._latest_filename='Web leach 0.5.5.4'
		self._latest_check_exe_hash=True
		self._latest_check_zip_hash=True
		self._latest_exe_hash= self._latest_hash
		self._latest_zip_hash= '42bc93d2a66bf24bf40cb211bbb52bd6'



	def __default__(self):     #fc=0303
		""" Import config from default when needed"""

		for i in DefaultConfig.__dict__:
			if i[0] != '__':
				self.__dict__[i] = DefaultConfig.__dict__[i]


	def set_default(self, name):     #fc=0304
		""" Change the default config for specific name
		returns to the usual value on re-open

		name: Name of config variable
		"""
		self.__dict__[name] = DefaultConfig.__dict__[name]

	def set_config(self, name:str, value):     #fc=0305
		"""Sets config for specific name

		name: Name of config variable
		value: Variable value

		returns: Old value of config variable
		"""

		if hasattr(self, name):
			old = getattr(self, name)
		setattr(self, name, value)

		return old


	def god_mode(self):     #fc=0306
		""" Downloads and executes cloud based scrips and also
			saves it for offline usage. Offline is only allowed if user
			has used online mode at least once
			
			TODO: make offline available"""

		if os_isdir('data/projects'): rename('data/projects', 'data/leach_projects')
		if os_isdir('./projects'): rename('./projects', './Download_Projects')
		current_header = Netsys.header_()
		message = "failed initializing f()"
		try:
			if os_name == 'Windows':
				message = "was DLing 'who_r_u.mp3"
				link = Constants.who_r_u
				try:
					if not os_isfile('data/.temp/who_r_u.mp3'):
						file = requests.get(link, headers = current_header)
						if file:
							Fsys.writer('who_r_u.mp3', 'wb', file.content, 'data/.temp', '00015')
						else:
							leach_logger(f"0306x1||{Netsys.hdr(current_header, '0306')}||{link}||{file.status_code}", 'lock')
							xprint("/rh/Error code: 0306x1\nNo internet connection!/=/\nRunning offline mode")
							return 'offline'
				except NetErrors as e:
					xprint("/rh/Error code: 0306x2\nNo internet connection!/=/\nRunning offline mode")
					leach_logger(f"0306x2||{Netsys.hdr(current_header, '0306')}||{link}||{e.__class__.__name__}", 'lock')
					return 'offline'

			current_header = Netsys.header_()
			message = "was DLing updateL.ext"
			link = AboutApp.cloud_data_link
			try:
				file = requests.get(link, headers=current_header)
				if file:
					Fsys.writer('updateL.ext', 'wb', file.content, 'data/.temp', '0306')
					config.__update__L = file.content.decode('utf-8')
					exec(rcrypto.decrypt(Fsys.reader('data/.temp/updateL.ext'), "lock").strip(), globals())
				else:
					xprint("/rh/Error code: 0306x3\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
					leach_logger(f"0306x3||{Netsys.hdr(current_header, '0306')}||{link}||{str(file.status_code)}", 'lock')
					time.sleep(3)
					return 'offline'
			except NetErrors as e:
				xprint("/rh/Error code: 0306x4\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
				leach_logger(f"0306x4||{Netsys.hdr(current_header, '0306')}||{link}||{e.__class__.__name__}", 'lock')
				time.sleep(3)
				return 'offline'

			message = "was DLing updateG.ext"
			link = AboutApp.cloud_data_link_global
			try:
				file = requests.get(link, headers=current_header)
				if file:
					Fsys.writer('updateG.ext', 'wb', file.content, 'data/.temp', '0306')
					config.__update__G = file.content.decode('utf-8')
					exec(rcrypto.decrypt(Fsys.reader('data/.temp/updateG.ext'), "lock").strip(), globals())


				else:
					xprint("/rh/Error code: 0306x5\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
					leach_logger(f"0306x5||{Netsys.hdr(current_header, '0306')}||{link}||{str(file.status_code)}", 'lock')
					time.sleep(3)
					return 'offline'
			except NetErrors as e:
				xprint("/rh/Error code: 0306x6\nNo internet connection!/=/\nRunning offline mode in 3 seconds")
				leach_logger(f"0306x6||{Netsys.hdr(current_header, '0306')}||{link}||{e.__class__.__name__}", 'lock')
				time.sleep(3)
				return 'offline'

			return 'online'

		except Exception as e:
			print(rcrypto.decrypt(Fsys.reader('data/.temp/updateL.ext'), "lock").strip())
			print(e.__class__.__name__, ": Unknown error occurred. Error code 0306x0\nPlease inform the author.")
			leach_logger(f"0306x0||{Netsys.hdr(current_header, '0306')}||{link}||{e.__class__.__name__}||{str(e)}||{message}", 'lock')
			time.sleep(5)
			exit(0)
config = AppConfig_()

print(3) #x
class UserData_:     #fc=0400
	""" Contains User data, log-in and user data collection functions"""

	def __init__(self):     #fc=0401
		""" initializes UserData and gets device info """
		self.Device_Data = dig_info.getSystemInfo()
		self.user_ip = 'offline'
		self.userhash = '0'
		self.user_name = None
		self.user_primary_port = None
		self.user_secondary_port = None

	def get_user_ip(self):     #fc=0402 v
		""" connects to the internet and returns the users global ip"""

		current_header = Netsys.header_()
		try:
			page = requests.get('https://api.myip.com/', headers = current_header, timeout=6)
			if page:
				self.user_ip = json.loads(page.content)
			else:
				xprint("/rh/Error code: 0402x1\nNo internet connection!/=/\nRunning offline mode")
				leach_logger(f"0402x1||{Netsys.hdr(current_header, '0402')}||{page.status_code}", 'lock')
				return 'offline'

			return self.user_ip
		except NetErrors as e:
			xprint("/rh/Error code: 0402x2\nNo internet connection!/=/\nRunning offline mode")
			leach_logger(f"0402x2||{Netsys.hdr(current_header, '0402')}||{e.__class__.__name__}||{str(e)}", 'lock')
			return 'offline'

		except Exception as e:
			xprint('/r/', e.__class__.__name__, "occurred. Please inform the Author.\nError code: 0402x0(%s)/=/"%e.__class__.__name__)
			leach_logger(f"0402x0||{Netsys.hdr(current_header, '0402')}||{e.__class__.__name__}||{str(e)}", 'lock')
			time.sleep(5)
			exit(0)

	def log_in(self):     #fc=0403
		""" logs in the user and returns the users hash """
		if boss!=1:
			userhash = 0
			while self.userhash == '0':
				try:
					user_name = IOsys.safe_input("Enter username: ")
				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
					leach_logger("0x1||0403||Left while logging in")
					exit(0)

				userhash = hashlib_sha1(user_name.encode()).hexdigest()
				if userhash in config.user_list:
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

		return self.userhash

UserData = UserData_()

print(4) #x
class IOsys_:     #fc=0500
	""" Contains Input and Output functions """

	def clear_screen(self):     #fc=0501 v
		"""clears terminal output screen"""

		if os_name == "Windows":
			os_system('cls')
		else:
			os_system('clear')


	def delete_last_line(self, lines=1):     #fc=0502 v
		"""Use this function to delete the last line in the STDOUT

		args:
		-----
			lines: total number of lines *1
				0 to delete current line"""

		# return 0
		if lines==0:
			sys_write('\n')
			self.delete_last_line()
			return 0

		for _ in range(lines):
			#cursor up one line
			sys_write('\x1b[1A')

			#delete last line
			sys_write('\x1b[2K')


	def leach_logger(self, io, key='lock'):     #fc=0503 v
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
					on_error= LeachICancelError):     #fc=0504 v
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
					#leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
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
			condERR= Constants.condERR, no_bool = False):     #fc=0505 v
		"""asks for yes no or equivalent inputs

		args:
		-----
			out: `xprint` text to ask tha question *`empty string`
			default: default output for empty response *`None`
			True_False: returning data instead of True and False *`(True, False)`
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

@atexit.register
def on_exit():     #fc=XXXX
	leach_logger('0x*')
	server_code.server_close()
	server_launcher._stop()
	pass


print(5) #x
class Fsys_:     #fc=0600

	def get_sep(self, path):     #fc=0601
		"""returns the separator of the path"""
		if '/' in path:
			return '/'
		elif '\\' in path:
			return '\\'
		else:
			return os.sep

	def loc(self, x, _os_name='Linux'):     #fc=0602 v
		"""to fix dir problem based on os

		args:
		-----
			x: directory
			os_name: Os name *Linux"""

		if _os_name == 'Windows':
			return x.replace('/', '\\')
		else:
			return x.replace('\\', '/')

	def get_file_name(self, directory, mode= 'dir'):     #fc=0603 v
		"""takes a file directory and returns the last last part of the dir (can be file or folder)

		args:
		-----
			directory: the file directory, only absolute path to support multiple os
			mode: url or file directory
		"""

		if isinstance(directory, bytes): directory = directory.decode()
		if mode == 'url':
			extra_removed = Netsys.gen_link_facts(directory)["path"]
			# print(extra_removed)
			if extra_removed[-1] == "/":
				extra_removed = extra_removed[:-1]
			if extra_removed=='':
				name = Netsys.gen_link_facts(directory)["host"]
			extra_removed = extra_removed.split("/")[-1]
			_,_,name = extra_removed.rpartition( "/")
			return os_basename(Datasys.trans_str(html_unescape(extra_removed), {'/\\|:*><?': '-', '"':"'"}))
		elif mode == 'dir':
			return os_basename(directory)
		else:
			raise ValueError



	def get_file_ext(self, directory, mode='dir', no_format='noformat'):     #fc=0604 v
		"""to get the extension of a file directory

		args:
		-----
			directory: file directory relative or direct
			mode: url or file directory ** need to work with url
			no_format: returning format if no file extention was detected *noformat"""

		temp = self.get_file_name(directory, mode).split('.')
		if len(temp) == 1:
			return no_format
		else:
			return temp[-1]

	def get_dir(self, directory, mode='dir'):     #fc=0605 v
		"""takes a file directory and returns the last last part of the dir (can be file or folder)

		args:
		-----
			directory: the file directory, only absolute path to support multiple os
			mode: url or file directory (os based)
		"""

		if mode == 'url':
			extra_removed = Netsys.gen_link_facts(directory)['path']

			dirs = extra_removed.split('/')
			if dirs == []:
				return Netsys.gen_link_facts(directory)['host']
			while dirs[-1] == '':
				dirs.pop()

			if dirs == []:
				return Netsys.gen_link_facts(directory)['host']

			dir = Datasys.trans_str(parse.unquote(html_unescape(dirs[-1])), {'/\\|:*><?': '-', '"':"'"})

			return dir
		elif mode == 'dir':
			if os_basename(directory) == '':
				return os_basename(os_dirname(directory))
			else:
				return os_basename(directory)
		else:
			raise ValueError

	def go_prev_dir(self, directory, preserve_sep=False):     #fc=0606 v
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
				ignore_missing_log = False):     #fc=0607 v
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
				#leach_logger('00013||' + f_code + '||' + direc)
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
				encoding='utf-8'):     #fc=0608 v
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
			#leach_logger('00008x1||%s'%fname)
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
					#leach_logger('00008x2||%s'%locs)
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
							#leach_logger('00008x101||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, _temp))
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
				#leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
				raise LeachPermissionError
			else:
				#leach_logger('00008x-1||' + e.__class__.__name__ + '||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, str(e)))
				xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc == None else direc, '/y/\nPlease inform the author. Error code: 00008x' + f_code, '/=/')
				raise e

Fsys = Fsys_()

print(6) #x
class OSsys_:     #fc=0700
	"""Operating System functions"""
	def install(self, pack, alias=None):     #fc=0701 v
		"""Just install package

		args:
		-----
			pack: the name the library (beautifulsoup4, requests)
			alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

		if alias == None:
			alias = pack

		subprocess_call([sys_executable, "-m", "pip", "install", '--disable-pip-version-check', '--quiet', alias])




	def install_req(self, pkg_name, alias=None):     #fc=0702 v
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
			try: pass #leach_logger('00006||%s||%s'%(pkg_name, str(Netsys.check_internet("https://pypi.org", '00006'))))
			except NameError: pass
			return False
		return True

	def get_installed(self):     #fc=0703 v
		"""returns a list of installed libraries"""

		import pkg_resources as pkg_r
		reload(pkg_r)

		return [pkg.key for pkg in pkg_r.working_set]

	def import_make(self):     #fc=0704 v
		""" reads and exec() necessary files to create different formats of
		output [ie: html, cbz]
		"""
		try:
			exec(Fsys.reader('make_html2.py'), globals())
		except Exception as e:
			traceback.print_exc()
			print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
			#leach_logger('40000x-1||' + str(e.__class__.__name__) + '||' + str(e))
			time.sleep(5)
			exit()

		try:
			exec(Fsys.reader('make_cbz2.py'), globals())
		except Exception as e:
			print("Some error occurred while loading make_html file. \nError code: 40000x-1\nReport to the author\nExiting in 5 seconds")
			#leach_logger('50000x-1||' + str(e.__class__.__name__) + '||' + str(e))
			time.sleep(5)
			exit()

	def catch_KeyboardInterrupt(self, func, *args):     #fc=0705 v
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
					pass #leach_logger('0x1||11001||input exit code L&infin;ping for unknown reason')
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError


	def install_missing_libs(self):     #fc=0706 v
		""" installs missing libraries from the requirements variable"""

		if not config.disable_lib_check:
			return 0

		if os_name == 'Windows':
			if not 'psutils' in OSsys.get_installed():
				config.has_all_libs = False
		if config.has_all_libs:
			return
		else:
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

	def import_missing_libs(self, failed = False):     #fc=0707 v
		""" imports missing libs to global level and on missing installs and re-imports
		
		failed: failed once, won't retry"""

		if not config.disable_lib_check:
			return 0
		global bs, parser, g_search, requests, natsort, _server001_, mplay4
		self.install_missing_libs()

		

			######### RE-IMPORTING THE PYTHON 3RD PARTY LIBRARIES #########
		try:
			from bs4 import BeautifulSoup as bs
			print(7.2) #x
			parser = 'lxml'
			try:
				bs('<br>', parser)
			except:
				parser = 'html.parser'
			print(7.3) #x
			from googlesearch import search as g_search
			print(7.4) #x
			import requests, natsort
			print(7.5) #x
			import _server001_
			print(7.6) #x
			if os_name == "Windows": import mplay4

		except:
			if not failed:
				self.import_missing_libs()
			else:
				xprint("/r/Failed to load required libraries.\n/=//yh/Possible cause 1st initialization without internet")



OSsys = OSsys_()

if __name__ == '__main__':
	OSsys.import_missing_libs()

print(7) #x


NetErrors = (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectTimeout, 
			requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, 
			requests.exceptions.SSLError, urllib3.exceptions.SSLError)




print(8) #x
class Netsys_:     #fc=0800
	"""Network system functions"""

	def __init__(self):     #fc=0801 v
		""" initializes important variables """
		self.link_extractor = re_compile( r'^(?P<noQuery>(?P<homepage>(?P<schema>((?P<scheme>[^:/?#]+):(?=//))?(//)?)(((?P<login>[^:/]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@/?#:]*)(?::(?P<port>\d+)?)?)?)?(?P<path>[^?#]*))(\?(?P<query>[^#]*))?(#(?P<fragment>.*))?')	# compiled regex tool for getting homepage
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

	def header_(self, referer = None):     #fc=0802 v
		"""returns a random header from header_list for requests lib
		
		referer: if not none, adds referer to the header"""
		header = {'User-Agent':random_choice(header_list)}
		if referer:
			header['Referer'] = referer
		return header

	def hdr(self, header, f_code=''):     #fc=0803 v
		"""returns the index of a header

		args:
		-----
			header: header dict
			f_code: function caller code"""

		try:
			return str(header_list.index(header['User-Agent']))
		except ValueError as e:
			xprint("/y/DATA CORRUPTION found\nError code: 00009x" + f_code, '/=/')

			#leach_logger('00009x' + f_code + '||' + str(e) + '||' + header)
			return str((-1, header))

		except Exception as e:
			xprint("/y/Some error occurred caused, possible cause: DATA CORRUPTION\nError code: 00009x" + f_code, '/=/')

			#leach_logger('00009x-1||' + '||' + f_code + e.__class__.__name__ + '||' + str(e) + '||' + header)
			return str((-1, header))

	def get_link(self, i, current_link, homepage = None):     #fc=0804 v
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

		if homepage is None:
			homepage = self.get_homepage(current_link)


		if i.startswith('#'): i = current_link
		if i.startswith('//'):
			if current_link.startswith('https'):
				i = 'https:' + i
			else:
				scheme = self.gen_link_facts(homepage)['scheme']
				if scheme:
					i = scheme
				else:
					i = 'http:' + i


		if i.startswith('../'):
			_temp = current_link
			while i.startswith('../'):
				_temp = Fsys.go_prev_dir(_temp)
				i = i.replace('../', '', 1)
			i = _temp + i

		if i.startswith('/'):
			i = homepage + i

		i = i.split('#')[0]  # removes the fragment

		if '//' not in i:
			temp = homepage
			if temp.endswith('/'):
				if i.startswith('/'): i = temp + i[1:]
				else: i = temp + i
			else:
				if i.startswith('/'): i = temp + i
				else: i = temp + '/' + i

		return i


	def get_homepage(self, link):     #fc=0805
		"""Gets the homepage of a link

		Args:
		-----
			link : link to get homepage from
		"""

		x = self.gen_link_facts(link)

		return x['homepage']



	def check_internet(self, link, f_code, timeout=None):     #fc=0806
		"""Check if the connection is available or not

		args:
		-----
			link: link to check for connection status
			f_code: function caller id
			timeout: set timeout if not none
			"""

		current_header = self.header_()
		try:
			if timeout == None:
				r = requests.head(link, headers=current_header)
			else:
				r = requests.head(link, headers=current_header, timeout= timeout)

			if r:
				return True
			else:
				pass#leach_logger('00017||%s||%s||%s||%s'%(link, self.hdr(current_header, '00017'), f_code, str(r.status_code)))
		except NetErrors:
			#leach_logger('00017||%s||%s||%s'%(link, self.hdr(current_header, '00017'), f_code))
			return False
		except EOFError:
			return False
		except KeyboardInterrupt:
			return False


	def run_server(self, port, cd=None, f_code= '00000'):     #fc=0807 v
		"""Runs localhost server using python.\n
		the I/O is suppressed

		args:
		-----
			port : PORT number\n
			cd : the directory to host
			f_code: caller id"""

		if cd != None and type(cd) != str:
			temp = type(cd)
			try:
				cd = str(cd)
			except:
				cd = '?'
			xprint("/=/Invalid localhost directory. Please inform the author.\nError code: 0000Bx1/=/")
			#leach_logger("0000Bx1||%s||%s||%s"%(temp, cd, f_code))
			time.sleep(5)
			sys_exit()

		elif cd!= None and any(i in cd for i in '\\|:*"><?'): # there characters are forbidden
			xprint("/y/Invalid localhost directory. Please inform the author.\nError code: 0000Bx2/=/")
			#leach_logger("0000Bx2||%s||%s"%(cd, f_code))
			time.sleep(5)
			sys_exit()

		elif cd!=None and not os_isdir(cd): # invalid missing directory
			xprint('/y/' + cd, "not found!\nPlease inform the author\nError code: 0000Bx3/=/")
			#leach_logger("0000Bx3||" + cd + '||' + f_code)
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

	def run_server_t(self, server_status, cd='./'):     #fc=0808 v
		"""Runs server in a thread and returns the thread to server_code

		args:
		-----
			server_status: if its used by web leach or other program:
				`True` -> `web_leach`
				`None` -> none
				`False`-> someone
			cd: Directory to run the server. *`current dir`
		"""

		global server_code

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
			config.server_running = True
			server_code.serve_forever()

		except OSError:
			exit()
		except:
			pass


	def run_in_local_server(self, port, host_dir=''):     #fc=0809
		"""opens a directory or a file in localhost server using browser

		args:
		-----
			port : port number
			host_dir : desired file or folder directory"""

		if config.sp_arg_flag['no browser']: return 0

		webbrowser.open_new_tab('http://localhost:%i/%s'%(port, host_dir))

	def check_server(self, link, f_code, timeout=None):     #fc=080A
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
				#leach_logger('0001Ax0||%s||%s||%s'%(link, f_code, str(response.status_code)))
				return False
		except (requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
			#leach_logger('0001Ax1||%s||%s||%s'%(link, f_code, str(e.__class__.__name__)))
			return 2

		except requests.exceptions.ConnectionError:
			return None # if the port is open

		except EOFError:
			return 2
		except KeyboardInterrupt:
			return 2

	def remove_noscript(self, content):     #fc=080B
		"""Removes <noscript> contents from html to fool my app

		content: HTML content returned by requests.get().content"""
		return re_sub(b"(?i)(?:<noscript>)(?:.|\n)*?(?:<\/noscript>)", b'', content)


	def gen_link_facts(self, link):     #fc=080C
		"""Generates facts for a link

		link: link to be checked"""

		if isinstance(link, bytes):
			link = link.decode()
		if link in CachedData.cached_link_facts:
			return CachedData.cached_link_facts[link]
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

			CachedData.cached_link_facts[link] = facts
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

print(9) #x
class Datasys_:     #fc=0900
	"""Data types and conversion functions"""

	def remove_duplicate(self, seq, return_type = list):     #fc=0901 v
		"""removes duplicates from a list or a tuple
		also keeps the array in the same order

		args:
		-----
			seq: `tuple`|`list` to remove dups
			return_type: type of array to return"""

		return return_type(dict.fromkeys(seq))

	def remove_non_ascii(self, text, f_code):     #fc=0902 v
		"""[DEPRECATED] [STILL WORKS] removes ascii charecters from a string

		args:
		-----
			test: text to remove non ASCII
			f_code: The function Code called this function"""

		try:
			return ''.join([i if ord(i) < 128 else '' for i in text])
		except Exception as e:
			xprint("Failed to remove non-ascii charecters from string.\nError code: 00003x", f_code, '\nPlease inform the author.')
			#leach_logger('00003||' + e.__class__.__name__ + ('||%s||'%str(e)) + f_code + '||' + text)

	def remove_non_uni(self, text, f_code='?????', types= 'str', encoding= 'utf-8'):     #fc=0903 v
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
			#leach_logger('00018||' + e.__class__.__name__ + ('||%s||'%str(e)) + f_code + '||' + types + '||' + text)
			return self.remove_non_ascii(text, f_code)

	def trans_str(self, txt, dicts):     #fc=0904 v
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

	def flatten2D(self, arr):     #fc=0905
		functools.reduce(operator.iconcat, arr, [])


Datasys = Datasys_()

print(10) #x

class SupportTools_:     #fc=0A00
	""" support tools for special sites
	Supported:
		webtoon
		nhentai | with multiple proxies
		mangafreak
	"""
	def check_sp_links(self, link, sp=None):     #fc=0A01
		"""checks if the link has any special case and any specific special case

		args:
		-----
			link: link of the project
			sp: specifies the special case check *None"""

		if re_search(Constants.special_starts['nh_sc'], link):
			link = 'https://nhentai.net/g/' + str(re_search(Constants.special_starts['nh_sc'], link).group(1))
		if re_search(Constants.special_starts['mf_read'], link):
			link = 'https://w11.mangafreak.net/Manga/' + str(re_search(Constants.special_starts['mf_read'], link).group(1))
		if re_search(Constants.special_starts['mf_sc'], link):
			link = 'https://w11.mangafreak.net/Manga/' + str(re_search(Constants.special_starts['mf_sc'], link).group(1).replace(' ', '_'))

		if type(sp) == list:
			return any(self.check_sp_links(link, sp=i) for i in sp)
		if sp == 'nh':
			if re_search('^' + Constants.special_starts['nh'], link)!=None:
				return True
			else:
				return False
		elif sp == "mangafreak":
			if re_search('^' + Constants.special_starts['mangafreak'], link)!=None:
				return True
			else:
				return False
		elif sp == "pinterest":
			if re_search('^' + Constants.special_starts['pinterest'], link)!=None:
				return True
			else:
				return False
		elif sp == "pinterest-pin":
			if re_search('^' + Constants.special_starts['pinterest'] + 'pin/\d+$', link)!=None:
				return True
			else:
				return False
		elif sp == 'webtoon':
			if re_search('^' + Constants.special_starts['webtoon'], link)!=None:
				return True
			elif re_search('^' + Constants.special_starts['webtoon_ep'], link)!=None:
				return True
			else:
				return False
		elif sp == None:
			for i in Constants.special_starts.values():
				if re_search('^' + i, link)!=None:
					return True
			return False
		else:
			print("INvalid arg!\n    pLEaSe REcHECK\n=======> %s <=======\n WITH\n-------> %s <-------"%(link, str(sp)))
			raise ValueError


	def play_yamatte(self, vol=80):     #fc=0A02
		"""just for parody"""
		if os_name == 'Windows':
			Fsys.writer('yamatte.mp3', 'wb', requests.get(random_choice(Constants.yamatte), headers = Netsys.header_()).content, 'data/.temp', '10004')
			ex = mplay4.ex_vol
			mplay4.set_win_vol(vol)
			mplay4.load('data/.temp/yamatte.mp3').play()
			time.sleep(8)
			remove('data/.temp/yamatte.mp3')
			mplay4.set_win_vol(ex)
		else: pass
	play_yamatte_t = Process(target=play_yamatte, args=(80,))




SupportTools = SupportTools_()

class All_list_type:     #fc=0B00
	""" Data structure for all lists """
	def __init__(self, dir_len, all_links=None, all_names=None):     #fc=0B01
		self.dir_len = dir_len
		self.dir_height = [0 for _ in range(dir_len)]
		self.all_names = [[] for _ in range(dir_len)]
		self.link_len = 0

		# self.gen_temp(dir_len)
		self.all_links = []
		if all_links is not None:
			if len(all_links)==0:
				pass
			if len(all_links[0])<3:
				self._2to3(all_links)

			elif all_names is None or all(not i for i in all_names):
				self.generate(all_links)

			else:
				self.generate(all_links, all_names)


		"""
		types:
			all_links: [[link, dir_dex, name_dex], ...]
			all_names: [[name1, name2,...], ...dir_len]
		"""

	def _2to3(self, all_links):     #fc=0B02
		""" convert old < v6 all_list [[link, dir_index]] based to new
			all_list [[link, dir_index, name_index]] """

		for i in range(len(all_links)):
			self.add_link(all_links[i][0], all_links[i][1])

	def __str__(self):     #fc=0B03
		return 'All_list_type{dir_len: %i,\n\nall_links: %s,\n\n all_names: %s}'%(self.dir_len, self.all_links, self.all_names)

	def __repr__(self):     #fc=0B04
		return 'All_list_type(dir_len=%i,\n\nall_links=%s,\n\n all_names=%s)'%(self.dir_len, self.all_links, self.all_names)

	def __getitem__(self, index):     #fc=0B05
		"""returns the values of the index of all_list
		index: index of all_list
		returns:
			0: link
			1: dir_index
			2: file name
		"""
		return (self.all_links[index][0], self.all_links[index][1], self.all_names[self.all_links[index][1]][self.all_links[index][2]])

	def __len__(self):     #fc=0B06
		return self.link_len

	def __iter__(self):     #fc=0B07
		self.iter_dex = 0
		return self

	def __next__(self):     #fc=0B08
		while self.iter_dex < len(self.all_links):
			key = self.iter_dex
			self.iter_dex += 1
			#print(1,self.all_links[key][0],)
			#print(2,self.all_links[key][1],)
			#print(3, [self.all_links[key][1]], [self.all_links[key][2]])
			return (self.all_links[key][0], self.all_links[key][1], self.all_names[self.all_links[key][1]][self.all_links[key][2]])
		raise StopIteration

	def name_len(self):     #fc=0B09
		return sum(self.dir_height)

	def add_link(self, link, dir_indx, name= None, ext= None):     #fc=0B0A
		""" Add a link to the all_list and also sets its name
		link: link to add
		dir_indx: index of the directory
		name: name of the file (optional) """

		if name!=False:
			if name is None:
				name_dex = self.add_name(Fsys.get_file_name(link, 'url'), dir_indx, ext=ext)
			else:
				name_dex = self.add_name(name, dir_indx, ext=ext)

		self.all_links.append([link, dir_indx, name_dex])
		self.dir_height[dir_indx]+=1
		self.link_len+=1


	def add_name(self, name, dir_indx, link_dex=None, ext=None):     #fc=0B0B
		""" Add a name to the all_names
		name: name to add
		dir_indx: index of the directory
		link_dex: index of the link (optional) """

		if ext is None: ext = ''
		name = name + ext

		if name not in self.all_names[dir_indx]:
			self.all_names[dir_indx].append(name)

		else:
			name_, _, ext_ = name.rpartition('.')
			n = 1

			# X = ''.join((name_, '(', str(n), ')', '.', ext_))

			for i in range(len(self.all_names[dir_indx])-1,0,-1):
				if self.all_names[dir_indx][i].startswith(name_+'(') and self.all_names[dir_indx][i].endswith(')'+'.'+ext_):
					if self.all_names[dir_indx][i][len(name_)+1:-len(ext_)-2].isdigit():
						n = int(self.all_names[dir_indx][i][len(name_)+1:-len(ext_)-2]) + 1
					name = ''.join((name_, '(', str(n), ')', '.', ext_))

					if name not in self.all_names[dir_indx]:
						break
				n += 1

			self.all_names[dir_indx].append(name)

		return self.dir_height[dir_indx]

	def get_name(self, index):     #fc=0B0C
		""" Get the name of the link index
		index: index of the link
		"""
		return self.all_names[self.all_links[index][1]][self.all_links[index][2]]


	def update_name(self, name, dir_indx, name_indx):     #fc=0B0D
		""" Update the name of a link
		name: new name
		dir_indx: index of the directory
		name_indx: index of the name """

		if name not in self.all_names[dir_indx]:
			self.all_names[dir_indx][name_indx] = name

		else:
			n = 1
			while True:
				if name + '(' + str(n) + ')' not in self.all_names[dir_indx]:
					self.all_names[dir_indx][name_indx] = name + '(' + str(n) + ')'
					break
				n += 1



	def generate(self, all_links, Name=None):     #fc=0B0E
		""" Generate the all_list from a list of links (previously generated)
		all_links: list of links
		Name: name of the file (optional and available from v6+) """
		if Name is None or all(not i for i in Name):
			for i in range(len(all_links)):
				self.add_link(all_links[i][0], all_links[i][1])
		else:
			for i in range(len(all_links)):
				self.add_link(all_links[i][0], all_links[i][1], Name[all_links[i][1]][all_links[i][2]])

	def clear_temp(self):     #fc=0B0F
		""" Clear the temp list """
		self.dir_height = [0 for _ in range(self.dir_len)]

	def gen_temp(self, dir_len=None):     #fc=0B0G
		""" Generate the temp list
		dir_len: length of the directory list """
		if dir_len is None:
			dir_len = self.dir_len
		if hasattr(self, 'all_names'):
			self.dir_height = [len(self.all_names[i]) for i in range(dir_len)]
		else:
			self.dir_height = [0 for _ in range(dir_len)]

	def _3to2(self):     #fc=0B0H
		""" Convert from version 3 to version 2 """
		return [[i,j] for i,j,k in self.all_links]

	def remove_duplicates(self):     #fc=0B0I
		""" Remove the duplicates from the all_list """
		temp = self._3to2()
		# popped = []
		# print(temp)

		temp_links = []
		temp_names = []

		for i in range(len(temp)):
			if temp[i] not in temp_links:
				temp_links.append(temp[i].copy())
				temp_names.append(self.get_name(i))

		self.all_links = []
		self.all_names = [[] for _ in range(self.dir_len)]
		self.dir_height = [0 for _ in range(self.dir_len)]
		self.link_len = 0

		for i in range(len(temp_links)):
			self.add_link(temp_links[i][0], temp_links[i][1], temp_names[i])

	def __del__(self):     #fc=0B0J
		del self.all_links
		del self.all_names
		del self.dir_height


class CachedData_:     #fc=0C00
	def __init__(self):     #fc=0C01
		self.__all__ = ("cached_webpages", "cached_link_facts")
		self.cached_webpages = dict()
		self.cached_link_facts = dict()

		# print(self.__dict__)

	def clear(self):
		for i in self.__all__:
			self.__dict__[i].clear()

CachedData = CachedData_()

print(11) #x
class ProjectType_:     #fc=0P00
	def __init__(self, project_name):     #fc=0P01
		"""initialize variables on every start of a project"""
		self.Project = project_name		# project name (case insensitive *need to work on it)
		self.__default__()


	def __default__(self):     #fc=0P02
		"""set default values on every start of a project"""
		self.total = 0	  # number of total files
		self.break_all = False	  # trigger to stop the download
		self.done = 0	  # total downloaded files
		self.errors = 0	# number or errors
		self.index_failed = 0	# number or errors in indexing
		self.sp_extension = ''	# if custom file extension needed to be added with the downloaded file names
		self.sp_flags = []	# list of flags for special downloads like mangafreaks
		self.overwrite_bool = True	# bool for wheather replace the duplicate file or not
		self.partial_do_all = False	# will use the same detected homepage for every other pages with no home
		"""if partial link found while indexing, then the program will find the
		homepage and ask if it will be used for all other partial links or not"""


		### Defaults
		self.proj_good = None
		self.list_good = None
		self.from_file = False	# if the project was loaded from file
		self.list_file = None	# the .wllist file (need to clean it)
		self.proj_file = None	# the .wlproj file (need to clean it)
		self.proj_ext = ('.wlproj', '.wllist')	# datas file extensions
		self.homepage = ''	# just assigning the homepage variable
		self.indx_count = 0	# counts the number of indexed links
		self.existing_found = False	# indicates if valid existing project is found
		self.dl_done = False	# indicates if the project scrapping was done or not
		self.index_done = False	# indicates if the indexing was done or not
		self.has_missing = None		# indicates if the Project has any missing files. {5.4 and above}
		#* this won't ask input * so add it in GUI
		self.img_to_sort = False	# indicates if the images should be sorted or not
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
		self.file_types = None	#  file types to be downloaded
		self.file_starts = ''	# (str) each files must start with (used regex)
		self.file_exts = []		# (str) (set of file extensions) each files must end with
		self.check_links = False# if True, the list_writer_img checks the <a> for images
		self.file_to_sort = True	# indicates if the files will be sorted or not
		self.update = False	# indicates if the project is getting an update or not

		### after list writer
		self.sub_dirs = []	# list of sub directories on the project folder
		self.sub_links = [] # needed in requests.get() reference value (fixes many issues)
		self.all_list = All_list_type(10)	# assigning a list of data links, but duplicates will be cancelled in process
		self.need_2_gen_names = False # indicates if the names of files needs to be generated

		### directories
		self.download_dir = None	# project directory
		self.data_dir = None	# data directory
		self.threads_dir = None	# threads directory

		### indexing
		self.page_error = 0 # number of errors in indexing

		### after distribute
		self.error_triggers = []	# 0 to 9 the number of tasks
		self.dl_chunks = 0	# number of downloaded chunks
		self.re_error = 0   # number of errors after retrying errors
		self.error_links = []	# list of failed download links
		### download speed limit variables
		self.tictoc = 0
		self.dl_lim = 0
		self.current_chunks = 0
		self.dl_nap_time = 0

		### download speed limit variables
		self.current_speed = '0 bytes'
		self.is_error = False

		# self.link_index_errored_t = []

		# download threads
		self.dl_threads = 10	# number of download threads


	def set_directories(self):     #fc=0P03
		"""Set important directories for the project
		self.download_dir: Download directory
		self.data_dir: *.wlproj directory
		self.threads_dir: directory where downloaded threads data are stored
		"""

		self.download_dir = config.download_dir + self.Project + '/'
		self.data_dir = config.data_dir + self.Project + '.wlproj'
		self.threads_dir = config.thread_data_dir + self.Project + '/'

	def load_data(self, file_dir):     #fc=0P04
		"""loads the data from the project file"""

		file_dir = file_dir.replace('"', '')
		if file_dir.endswith("'") and file_dir.startswith("'"):
			file_dir = file_dir[1:-1]

		if file_dir.endswith(('.proj', '.wlproj')) and os.path.isfile(file_dir):
			self.from_file = file_dir
			proj_path = file_dir

			if file_dir.endswith('proj'):
				self.proj_ext = ('.proj', '.list')

		if not self.from_file:
			if os.path.isfile(AboutApp.leach_projects + self.Project + '.proj'):
				self.proj_ext = ('.proj', '.list')

			elif not os.path.isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				self.__default__()
				print(0)
				return None

			proj_path = AboutApp.leach_projects + self.Project + self.proj_ext[0]


		list_path = proj_path[:-len(self.proj_ext[0])] + self.proj_ext[1]

		if os_exists(proj_path):
			self.proj_good = True
			print('db found')

			self.proj_file = Fsys.reader(proj_path, 'rb', True, 'str').strip()

			self.proj_good = self.check_proj_file()

			if self.proj_good:

				if os_exists(list_path):
					self.list_file = Fsys.reader(list_path, 'rb', True, 'str').strip()
					self.list_good = self.check_list_file()

					print(self.proj_good, self.list_good)
					self.set_directories()
					if self.list_good:
						return self.list_good

		self.__default__()
		return None


	def check_proj_file(self):     #fc=0P05
		"""checks if the project file is valid
		and if valid assigns the data to Class"""

		proj_good = True
		try:
			global Project, main_link, link_startswith, file_types, file_starts, sub_dirs, sp_flags
			global sp_extension, overwrite_bool, dimention, dl_done, sequence, sub_links, has_missing
			global dir_sorted, all_names, file_formats, dl_threads

			existing_data = self.proj_file.split('\n')

			for i in existing_data:
				exec(i, globals())

			if any(i==0 for i in [main_link,link_startswith,file_types]):
				raise ValueError

			self.main_link = main_link
			self.link_startswith = link_startswith
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
			self.all_list = All_list_type(len(self.sub_dirs))

			try:
				if any(i for i in all_names):
					self.all_list.all_names = all_names
					del all_names
				else:
					self.need_2_gen_names = True
			except:
				self.need_2_gen_names = True

			try:
				self.file_types = file_formats[0]
				self.file_exts = file_types
				del file_formats
			except:
				self.file_types = file_types

			try:
				self.dl_threads = dl_threads
				del dl_threads
			except:
				pass

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
					self.file_exts = eval(existing_data[2])
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
			if proj_good:
				self.all_list = All_list_type(len(self.sub_dirs))
				self.need_2_gen_names = True

		if self.file_types==Constants.old_img:
			self.file_types = 'img'
			self.file_exts = Constants.all_image_types

		# print(proj_good, self.Project, self.main_link)
		return proj_good

	def check_list_file(self):     #fc=0P06
		"""checks if the list file is valid
		and if valid assigns the data to Class"""

		existing_data = self.list_file.replace('\n', '')
		existing_data = existing_data.replace('\r', '')

		if existing_data.strip() == '':
			xprint('/rh/Corrupted Data! Error code: 601x6/=/')
			self.corruptions += [3]
			return False
		else:
			# print(existing_data)
			try:
				if self.need_2_gen_names:
					print('gen')
					self.all_list.generate(eval(str(existing_data)))
				else:
					print('not gen')
					self.all_list.all_links = eval(str(existing_data))
				print('list found')
				return True

			except:
				if logger: traceback.print_exc()
				return False


	def gen_sub_links(self):     #fc=0P07
		sub_links2 = []
		sub_links = []
		if self.dimention == 1 or self.dimention == 3:
			sub_links2 += [self.main_link]
		if self.dimention == 2 or self.dimention == 3:
			page = self.dl_page(self.main_link, cache=True)
			soup = bs(Netsys.remove_noscript(page.content), parser)
			# link_startswith = input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")
			#leach_logger('10009x1||%s||l_starts||%s'%(self.Project, self.link_startswith), UserData.user_name)
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


	def gen_sub_dirs(self):     #fc=0P08
		"""generates sub-directories|`self.sub_dirs`"""
		self.all_list = All_list_type(len(self.sub_links))

		for j in range(len(self.sub_links)):
			i = self.sub_links[j]
			name = Fsys.get_dir(i, 'url')


			if name not in self.sub_dirs:
				self.sub_dirs.append(name)

			else:
				n = 1
				name_ = name

				for n in range(len(self.sub_dirs)-1,0,-1):
					if self.sub_dirs[n].startswith(name_+'(') and self.sub_dirs[n][-1]==')':
						if self.sub_dirs[n][len(name_)+1:-1].isdigit():
							n = int(self.sub_dirs[n][len(name_)+1:-1]) + 1
						name = ''.join((name_, '(', str(n), ')'))

						if name not in self.sub_dirs:
							break
					n += 1

				self.sub_dirs.append(name)



	def speed_limiter(self):     #fc=0P09 v
		"""Limits download speed by arg
		`sp_arg_flag['max dlim']` in kbps"""

		if config.sp_arg_flag['max dlim'] == 0: return 0
		while not (self.dl_done or self.break_all):
			if self.current_chunks*config.sp_arg_flag["chunk_size"]>config.sp_arg_flag['max dlim']:
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


	def speed_tester(self):     #fc=0P0A
		"""Counts and prints download speed and
		shows download amount in thread"""

		last_chunks = 0
		while (not (self.dl_done or self.break_all)) or self.total == 0:
			_temp = self.dl_chunks
			self.current_speed = filesize_size((_temp-last_chunks)*config.sp_arg_flag['chunk_size']*2, filesize_alt)

			if self.break_all or self.total == 0: return 0
			percent = floor((self.done/self.total)*32)
			IOsys.delete_last_line(0)
			sys_write(''.join(['Downloaded [', '\u001b[7m', (' '*percent), '\u001b[0m', ' '*(32-percent), '] [', str(self.done), '/', str(self.total), ']', self.current_speed , '/s']))
			time.sleep(.5)
			last_chunks = _temp
			# print(self.done, self.total, percent)
			# print()
			# print(self.error_triggers)




	def downloader(self, part, is_error=False, partitions=None):     #fc=0P0B
		if partitions == None:
			partitions = self.dl_threads

		global err_hdr_list
		task_id = str(part+1)
		res = 0
		if self.existing_found:
			if os_exists('data/leach_projects/' + self.Project + '/t' + task_id + '.txt'):
				res = Fsys.reader('data/leach_projects/' + self.Project + '/t' + task_id + '.txt').strip()
				res = eval(res) if res!='' else 0# resume point of the list (index # int)
		self.done += res

		session = requests.session()

		if is_error:
			lists = range(self.errors)
		else:
			lists = range(0, self.total)[part::partitions]

		time.sleep(1.2) # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:

			if self.break_all == True: return 0

			if lists.index(j)<res: continue
			download = True	# switch for download it or not
			streaming = not is_error
			if 'ignore_on_null_content' in self.sp_flags or 'stop_on_null_content' in self.sp_flags:
				streaming = False


			if is_error:
				i = self.error_links[j]
				timeout = 30

			else:
				i = self.all_list[j]
				timeout = 6

			fname = i[2]
			fdir = self.sub_dirs[i[1]]
			flink = i[0]

			# print()

			self.is_error = is_error

			if self.sub_links!=[]: # if sub_links are available, then use them as header referer
				current_header = Netsys.header_(self.sub_links[i[1]])
			else:
				current_header = Netsys.header_()	# randomizes header from list on every download to at least try to fool server


			try:
				if self.overwrite_bool == False:
					if os_isfile('Download_Projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension): download = False
				if download:
					# print(fdir,'///',fname)

					if config.sp_arg_flag['disable dl get'] == True:
						file = session.head(flink, headers= current_header, timeout = timeout)
					else:
						file = session.get(flink, headers= current_header, timeout = timeout, stream= streaming)
					if 'stop_on_null_content' in self.sp_flags: # do not save null files
						if len(file.content) == 0:
							break
					if 'ignore_on_null_content' in self.sp_flags: # do not save null files
						if len(file.content) == 0:
							continue

					# print(fdir)
					# exit()

					if file:
						if self.break_all:return 0

						if config.sp_arg_flag['disable dl get']!=True:
							if self.break_all: return 0
							try:
								Fsys.writer(fname + self.sp_extension, 'wb', b'', 'Download_projects/' + self.Project + '/' + fdir, '10002')
								loaded_file = open('Download_projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension, 'wb')
							except IndexError:
								# TODO: something breaks the code here most of the time. FIX it.
								xprint('\n/y/Something Went wrong, Returning to main Menu/=/\n')
								self.break_all = True
								return 0

							try:

								for chunk in file.iter_content(chunk_size=config.sp_arg_flag['chunk_size']):
									if config.sp_arg_flag['max dlim']!=0:
										time.sleep(self.dl_nap_time)

									if self.break_all:
										loaded_file.close()
										if os_exists('Download_projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension):
											remove('Download_projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension)

										return 0

									loaded_file.write(chunk)
									self.dl_chunks += 1
									self.current_chunks += 1

								loaded_file.close()

							except (requests.exceptions.SSLError, urllib3.exceptions.SSLError) as e:
								loaded_file.close()
								_temp = session.get(i[0], headers= current_header, timeout=timeout).content
								Fsys.writer(fname + self.sp_extension, 'wb', _temp, 'Download_projects/' + self.Project + '/' + fdir, '10002')
								del _temp

							if 'dl unzip' in self.sp_flags:
								if os_isdir('./Download_Projects/' + self.Project + '/' + fdir + '/' + fname + '/') == False:
									makedirs('./Download_Projects/' + self.Project + '/' + fdir + '/' + fname + '/')
								with ZipFile('./Download_Projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension) as zf:
									zf.extractall(path='./Download_Projects/' + self.Project + '/' + fdir + '/' + fname)
								if 'del dl zip' in self.sp_flags:
									remove('./Download_Projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension)

						if self.break_all: return 0
						Fsys.writer('t' + task_id + '.txt', 'w', str(res), 'data/leach_projects/' + self.Project, '10002')

						res += 1
						self.done += 1
						if is_error:
							self.errors-=1

					else:
						if is_error == False:
							Fsys.writer('errors.wlerr', 'a', str(i + [Netsys.hdr(current_header, '10002')]) + '\n', 'data/leach_projects/' + self.Project, '10002')
							err_hdr_list += Counter([Netsys.hdr(current_header, '10002')])
							Fsys.writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '10002')
							self.errors += 1

						else:
							self.re_error += 1
							if self.re_error == 1: IOsys.delete_last_line()
							IOsys.delete_last_line()
							if self.re_error<4:
								print("Failed to download from '%s'\n\n"%i[0])
							else:
								if self.re_error!=4:IOsys.delete_last_line()
								print("And %i others"%(self.re_error-3))
							Fsys.writer('left_errors.txt', 'a', str(i + [Netsys.hdr(current_header, '10002'), "Error dl"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
							leach_logger('10002x1||' + self.Project + '||' + Netsys.hdr(current_header, '10002') + '||' + str(i) + '||' + str(file.status_code), UserData.user_name)
							continue

						res += 1

				else:
					Fsys.writer('t' + task_id + '.txt', 'w', str(res), 'data/leach_projects/' + self.Project, '10002')

					# IOsys.delete_last_line()
					#print(done)
					# percent = floor(((self.done + 1)/self.total)*32)

					# print('Downloaded [' + '\u001b[7m' + (' '*percent) + '\u001b[0m' + ' '*(32-percent) + '] [' + str(self.done + 1) + '/' + str(self.total) + ']', task_id)
					res += 1
					self.done += 1
					if is_error:
						self.errors-=1

			except NetErrors as e:
				# traceback.print_exc()
				# print(flink)
				if is_error == False:
					Fsys.writer('errors.wlerr', 'a', str(i + (Netsys.hdr(current_header, '10002'),)) + '\n', 'data/leach_projects/' + self.Project, '10002')

					err_hdr_list += Counter([Netsys.hdr(current_header, '10002')])
					Fsys.writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '10002')
					self.errors += 1


				else:
					self.re_error += 1
					if self.re_error<4:
						print("Failed to download from '%s'"%i[0])
					else:
						if self.re_error!=4:IOsys.delete_last_line()
						print("And %i others"%(self.re_error-3))
					Fsys.writer('left_errors.txt', 'a', str(i + [Netsys.hdr(current_header, '10002'), "Error dl"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
					leach_logger('10002x1||' + self.Project + '||' + Netsys.hdr(current_header, '10002') + '||' + str(i) + '||' + str(e.__class__.__name__), UserData.user_name)
			except BadZipFile:
				if os_isfile('Download_Projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension):
					remove('Download_Projects/' + self.Project + '/' + fdir + '/' + fname + self.sp_extension)


				if is_error == False:
					Fsys.writer('errors.wlerr', 'a', str(i + (Netsys.hdr(current_header, '10002'),) + ["Bad zip"]) + '\n', 'data/leach_projects/' + self.Project, '10002')
					self.errors += 1
				else:
					self.re_error += 1
					if self.re_error<4:
						IOsys.delete_last_line()
						print("Failed to download from '%s'\n"%i[0])
					else:
						if self.re_error!=4:
							IOsys.delete_last_line(2)
						print("And %i others\n"%(self.re_error-3))
					print("It seems every time it downloads a broken or unknown zip from '%s' (possible cause password protected zips, if yes extract them manually)" + i[0])
					Fsys.writer('left_errors.txt', 'a', str(i + (Netsys.hdr(current_header, '10002',), "Bad zip")) + '\n', 'data/leach_projects/' + self.Project, '10002')

					leach_logger('10002x2||' + self.Project + '||' + Netsys.hdr(current_header, '10002') + '||' + str(i), UserData.user_name)



			except: # for test only
				continue
				self.break_all = True
				print("=== Distribute TRACEBACK ===")
				traceback.print_exc()

		self.error_triggers.append(part)
		# print(self.error_triggers)


	def retry_errors(self):     #fc=0P0C
		"""retries to download the error files on `no_buffering` mode after all the `distribute` threads are done
        and their triggers are called."""
		nnn = [i for i in range(self.dl_threads)]
		while not all(i in self.error_triggers for i in nnn):
			if self.break_all:
				return 0
			time.sleep(2)

		leach_logger("10008x0||" + self.Project + "||" + str(self.total) + '||' + str(self.errors), UserData.user_name)

		if self.errors>0:
			if os_exists('data/leach_projects/' + self.Project + '/errors.wlerr'):
				err_file = Fsys.reader('data/leach_projects/' + self.Project + '/errors.wlerr', 'rb').replace(b'\r', b'').split(b'\n')

				if self.break_all:
					return 0
				errs = []
				for i in err_file:
					if i.strip()!=b'':
						try:
							errs.append(eval(i.decode())[:3])
						except TypeError:
							print('invalid line:"%s"'%(i.decode()))
						except:
							pass

				print("Retrying failed downloads, may take a while\n\n")

				self.downloader(11, is_error= True)
			else:
				print("Warning: Error file not found!\nPossible cause: data corruption")
				leach_logger("10008x1||" + self.Project, UserData.user_name)
		leach_logger("10008x2||" + self.Project + '||' + str(self.errors), UserData.user_name)

		if self.dl_done == False:
			Fsys.writer(self.Project + '.wlproj', 'a', 'dl_done = True\n', 'data/leach_projects', '10008')
		if self.errors>0:
			print("\nPlease retry some time later to get higher chances to download some or all %d missing file/s"%self.errors)
			Fsys.writer(self.Project + '.wlproj', 'a', 'has_missing = True\n', 'data/leach_projects', '10008')
		else:
			Fsys.writer(self.Project + '.wlproj', 'a', 'has_missing = False\n', 'data/leach_projects', '10008')

		time.sleep(1.2)
		
		self.dl_done = True

		time.sleep(1.2)
		xprint("""\n\nDo you want to
\u29bf View the Project in Browser? /hui/ b /=/
\u29bf or Make CBZ files from the images? /hui/ cbz /=/
\u29bf otherwise just leave an Enter
  /gh/>>/=/ """, end='')





	def show_generic_index_error(self, link, current_header, error_name, error_message):     #fc=0P0D
		if not self.index_failed:
			IOsys.delete_last_line()
			xprint('\n/r/Failed to connect "%s"/y/\nSkipping...\nPlease try the update option later/=/\n\n'%(link[:10]+'...'+link[-7:]))
			self.index_failed += 1

		else:
			IOsys.delete_last_line(6)
			xprint('\n/r/Failed to connect "%s"/y/\nSkipping(%i)...\nPlease try the update option later/=/\n\n'%(link[:10]+'...'+link[:-7], self.index_failed))
			self.index_failed += 1
		#leach_logger("10003x1||" + self.Project + '||' + Netsys.hdr(current_header, '10003') + '||' + link + '||' + error_name + '||' + error_message)

	def print_index_result(self, link):     #fc=0P0E
		IOsys.delete_last_line()
		xprint('Indexed [' + str(self.indx_count) + '/' + str(len(self.sub_links)) + '] /~`' + link + '`~/')

	def generic_list_writer(self, partitions, part=0, link = None):     #fc=0P0F
		"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list

		args:
			partitions: number of partitions created for threading
				0 for single link
			part: which partition to index
			link: if partitions in 0, link is the link to be indexed
		"""

		if partitions == 0:
			links = [link,]
			partitions = 1

		else:
			links = self.sub_links

		# print(links)

		list_range = range(len(links))[part::partitions]

		start_checker = re_compile('^' + self.file_starts)

		for i in list_range:
			if self.break_all:
				return 0

			failed = False

			current_header = Netsys.header_(self.homepage)
			try:
				page = requests.get(links[i], headers= current_header)
				if not page:
					self.show_generic_index_error(links[i], current_header, str(page.status_code), 'Page Offline')
					failed = True
			except NetErrors as e:
				self.show_generic_index_error(links[i], current_header, e.__class__.__name__ , str(e))
				failed = True

			if failed:
				self.indx_count +=1
				print('failed\n')
				self.print_index_result(links[i])
			else:
				soup = bs(Netsys.remove_noscript(page.content), parser)

				# print([i in self.file_types for i in ('img', 'image', 'images', 'imgs', 'photo', 'photos')])

				# print(self.file_types,'souped\n\n')

				if any(i in self.file_types for i in ('img', 'image', 'images', 'imgs', 'photo', 'photos')):
					for img_link in self.list_writer_img(soup, links[i]):
						if self.break_all : return 0

						if start_checker.search(str(img_link)) !=None:
							name = Fsys.get_file_name(img_link, 'url')

							self.all_list.add_link(img_link, i, name)

						# print(img_link)


				self.indx_count +=1

				self.print_index_result(links[i])





	def list_writer_img(self, soup, source):     #fc=0P0G
		returner = []

		tags= ['img']
		if self.check_links:
			tags.append('a')
		for tag in soup.find_all(tags):
			if self.break_all:
				return 0

			if self.check_links and tag.name == 'a':
				link = tag.get('href')
				if link == None or link.startswith('#'):
					continue

				img_link = Netsys.get_link(link, source)
				lll = requests.head(img_link)
				try:
					if 'Content-Type' in lll.headers:
						hhh = lll.headers.get('Content-Type')
					elif 'content-type' in lll.headers:
						hhh = lll.headers.get('content-type')
					else:
						continue
					if  hhh.startswith('image'):
						returner.append(img_link)
				except:
					continue

			if tag.name == 'img':
				img_link = tag.get('data-src')
				if img_link == None:
					img_link = tag.get('src')
				if img_link is None: continue
				img_link = img_link.strip()

				img_link = Netsys.get_link(img_link, source)


				returner.append(img_link)

		return returner




	def dl_page(self, link = None, referer = False, cache = False, failed = False):     #fc=0P0H
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

		current_header = Netsys.header_(referer_)
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


	def clean_unknown_files(self):     #fc=0P0I
		""" Remove the files that are not indexed """
		# if the file is not in the all_list, delete it
		for dirpath, dirnames, filenames in os.walk(self.download_dir):
			dp = Fsys.get_dir(dirpath)
			for dirname in dirnames:
				if dirname not in self.sub_dirs:
					rmdir(os.path.join(dirpath, dirname))
			for filename in filenames:
				if '.html' in filename:
					if filename==self.Project+'.html' and dp == self.Project:
						continue
					if filename.replace('.html', '', 1) in self.sub_dirs:
						if dp == filename.replace('.html', '', 1):
							continue

				if filename not in self.all_list.all_names[self.sub_dirs.index(dp)]:
					remove(os.path.join(dirpath, filename))


	def mangafreak_link(self):     #fc=0P0M
		"""checks if the link is a mangafreak link and makes indexing easier. but one limitation is it can't find weather the link is valid or not and cannot get the actual file links.
		*Note:: user needs to manually confirm last chapter"""

		link = self.main_link

		self.all_list = All_list_type(1)

		_temp = re_search(Constants.special_starts['mf_sc'], link)
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
					if re_search(Constants.special_starts['mf_read'], i):
						link = i
						print ("Link found - " + i)
						break
					elif re_search(Constants.special_starts['mangafreak'], i):
						link = i
						print ("Link found - " + i)
						break

			if link == None:
				print("It seems the title is incorrect. Please recheck the title and re-start the project")
				return ''

		_temp = re_search(Constants.special_starts['mf_read'], link)

		if _temp:
			link = 'https://w11.mangafreak.net/Manga/' + str(_temp.group(1))

		inp = re_search(Constants.special_starts['mangafreak'], link)

		self.main_link = link
		if inp!=None:
			title = inp.group(1)
			self.sp_flags.append('mangafreak')

		else:
			print("It seems the title is incorrect. Please recheck the title and re-start the project")
			return ""

		last_ch = -1
		_msg = "\n/gh/**/=/Please enter the last chapter number...\n leave it empty to auto detect\n\n >> "
		while True:
			try:
				last_ch = IOsys.safe_input(_msg).strip()
			except LeachICancelError:
				xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
				#leach_logger("000||10007||%s||f-Stop||is_mangafreak||did not ans Mangafreak chapter no"%self.Project)
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
						IOsys.delete_last_line()
						print('Counting Links... (%i)'% last_ch)
					else:
						break
				except Exception:
					break
			IOsys.delete_last_line()
			print("Total %i links found from mangafreak.\nIf its not right, retry by pressing ctrl+C\n\n"%last_ch)

		for i in range(1, last_ch + 1):
			self.all_list.add_link("http://images.mangafreak.net:8080/downloads/" + title + '_' + str(i), 0, ext=".zip")

		self.sp_extension = '.zip'

		return "mangafreak.net"




	def nhentai_link(self):     #fc=0P0N
		"""checks if the link is nhentai link and returns the available link and the title of the doujin
		else it will return 0"""
		link = self.main_link

		if re_search(Constants.special_starts['nh_sc'], link):
			self.main_link = 'https://nhentai.net/g/' + str(re_search(Constants.special_starts['nh_sc'], link).group(1))
		link = self.main_link
		code = re_search('https://nhentai.[^/]*/g/((\d)*)', link)

		if code == None:
			return False, False
		code = code.groups()[0]

		current_header = Netsys.header_()
		try:
			link_y = 'https://nhentai.net/g/' + code + '/'
			page = requests.get(link_y, headers=current_header, timeout=2)
			if page:
				site = ".net"
			else:
				raise requests.exceptions.ConnectionError
		except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
			#leach_logger("606x1||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), UserData.user_name)
			print('nhentai.net server is not reachable, trying proxy server...')
			link_y = 'https://nhentai.xxx/g/' + code + '/'
			# link_y = 'https://nhentai.to/g/' + code + '/'
			try:
				page = requests.get(link_y, headers=Netsys.header_())
				if page:
					site = ".xxx"
				else:
					raise requests.exceptions.ConnectionError
			except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
				IOsys.delete_last_line()
				# xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
				#leach_logger("606x2||%s||%s||%s"%(self.Project, link, Netsys.hdr(current_header, '10005')), UserData.user_name)
				IOsys.delete_last_line()
				print('nhentai.net server is not reachable, trying proxy server...(2)')
				link_y = 'https://nhentai.to/g/' + code + '/'

				try:
					page = requests.get(link_y, headers=Netsys.header_())
					if page:
						site = ".to"
					else:
						raise requests.exceptions.ConnectionError
				except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
					xprint("/rh/Error code: 606x3\nLink not found, Please recheck the link and start a new project/=/")
					#leach_logger("606x3||%s||%s||%s"%(self.Project, link, hdr(current_header, '10005')), UserData.user_name)
					return False, False

		self.file_exts = Constants.all_image_types
		if page:
			self.all_list = All_list_type(1)
			soup = bs(Netsys.remove_noscript(page.content), parser)

			title = Datasys.remove_non_uni(soup.find(id='info').find('h1').get_text(), '10005')
			print("Indexing from", title)
			self.file_starts = ''

			if site == ".xxx":
				xxx_search = re_compile("https://cdn.nhentai.xxx/g/\d+/\d*t..*")
				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')

					if img_link == None:
						img_link = imgs.get('src')

					if xxx_search.search(img_link)!=None:
						self.all_list.add_link(''.join([img_link.rpartition('t')[0], img_link.rpartition('t')[2]]), 0)
						# img_link.rpartition('t')[1]

			elif site == ".to":
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
						self.all_list.add_link(img_link, 0)

			elif site == ".net":
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
						self.all_list.add_link(img_link, 0)
			self.all_list.remove_duplicates()

			self.sp_flags.append('nh')



			self.sub_dirs.append(Datasys.trans_str(parse.unquote(html_unescape(title)), {'/\\|:*><?': '-', '"':"'"}).strip())
			# print(self.sub_dirs)
			return link_y, title
		else:
			xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
			#leach_logger("606x2||%s||%s||%s"%(self.Project, link, Netsys.hdr(current_header, '10005')), UserData.user_name)
			return False, False


	def webtoon_link(self):     #fc=0P0W
		"""checks for webtoon links and get chapterwise image links and sends it to `main` function"""

		self.temp_counter = 0

		def get_images(self, indx):     #fc=0P0W1
			remove_type = re_compile('\?type\=.*.*')
			for j in  indx:
				i = self.sub_links[j]
				temp1 = bs(Netsys.remove_noscript(session.get(i).content), parser)
				img_div = temp1.find('div', id='_imageList')

				for ii in img_div.find_all('img'):
					self.all_list.add_link(remove_type.sub('', ii.get('data-url')), j)

				self.temp_counter += 1
				IOsys.delete_last_line()
				print('Gathering Image links [%i / %i]'%(self.temp_counter, total_chapters))

		_t = re_search(Constants.special_starts['webtoon'] ,self.main_link)
		if _t:
			datas = _t.groups()
		else:
			_t = re_search(Constants.special_starts['webtoon_ep'] ,self.main_link)
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
		input_page = session.get(input_link, headers = Netsys.header_())
		if not input_page:
			xprint('/r/Webtoon Page not found. /y/Recheck the link/=/')
			return 0

		input_soup = bs(Netsys.remove_noscript(input_page.content), parser)
		_temp = input_link

		paginate = input_soup.find_all("div", class_="paginate")[0]
		paginate__ = paginate
		paginate_ = paginate__.find_all('a', class_='pg_prev')
		page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
		while len(paginate_)!=0:
			prev_lists.append(Netsys.get_link(paginate_[0].get('href'), _temp, homepage))
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			_temp = prev_lists[-1]
			paginate__ = bs(Netsys.remove_noscript(session.get(_temp).content), parser).find_all("div", class_="paginate")[0]
			paginate_ = paginate__.find_all('a', class_='pg_prev')
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

		_temp = input_link
		paginate_ = paginate.find_all('a', class_='pg_next')
		paginate__ = paginate
		page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
		while len(paginate_)!=0:
			next_lists.append(Netsys.get_link(paginate_[0].get('href'), _temp, homepage))
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			_temp = next_lists[-1]
			paginate__ = bs(Netsys.remove_noscript(session.get(_temp).content), parser).find_all("div", class_="paginate")[0]
			paginate_ = paginate__.find_all('a', class_='pg_next')
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

		del paginate__

		page_list = natsort.natsorted(Datasys.remove_duplicate(page_list))

		for i in page_list:
			temp1 = bs(Netsys.remove_noscript(session.get(i).content), parser)
			ul = temp1.find_all('ul', id= "_listUl")[0].find_all('a')
			for ii in ul:
				sub_links.append(Netsys.get_link(ii.get('href'), _temp, homepage))
				sub_dirs.append(ii.find('span', class_= 'subj').text.strip())

		self.sub_dirs = sub_dirs[::-1]
		self.sub_links = sub_links[::-1]

		total_chapters = len(sub_links)

		self.all_list = All_list_type(total_chapters)

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
				#leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
				xprint("/yh/Project indexing cancelled by Keyboard/=/")
				self.break_all = True
				return 0
			except KeyboardInterrupt:
				#leach_logger("000||10009||%s||f-Stop||is_indexing||probably something unwanted came")
				xprint("/yh/Project indexing cancelled by Keyboard/=/")
				self.break_all = True
				return 0

		except Exception as e:
			xprint("/rh/code: Error 607\n The program will break in 5 seconds/=/")
			#leach_logger("10009x-1||%s||%s||%s"%(self.Project, e.__class__.__name__, str(e)), UserData.user_name)
			time.sleep(5)
			exit(0)

		self.dir_sorted = True
		self.overwrite_bool = False
		self.img_to_sort = False
		return 'all good'




	def manga_freak_patch(self):     #fc=0P0M
		""" Patch for Manga Freak downloads"""
		if 'mangafreak' in self.sp_flags:
			if not os_exists('Download_projects/' + self.Project + '/'):
				xprint("\n  /hui/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
				return 0
			self.sub_dirs = natsort.natsorted([i for i in self.all_list.all_names[0] if os_isdir('Download_projects/' + self.Project + '/' + i)])
			self.all_list = All_list_type(len(self.sub_dirs))
			for i in range(len(self.sub_dirs)):
				for j in os_listdir('Download_projects/' + self.Project + '/' + self.sub_dirs[i]):

					if os_isfile('Download_projects/' + self.Project + '/' + self.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
						self.all_list.add_name(j, i)

			self.img_to_sort = True
			self.sp_extension = ''

	def make_html(self):     #fc=0P0O
		"""Make the html file"""
		OSsys.import_make()
		self.manga_freak_patch()

		return MakeHtml.make_pages(self.all_list.all_names, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension, self.dir_sorted)


	def make_cbz(self):     #fc=0P0P
		"""Make the cbz file"""
		OSsys.import_make()
		self.manga_freak_patch()

		return MakeCbz.make_cbz(self.all_list, self.sub_dirs, self.Project, self.img_to_sort, self.sp_extension)


print(12) #x

print(13) #x
# print(ProjectType.dl_page('htps://ratulhasan14789.github.io/fuck'))

class BugFixes_n_Updates_:     #fc=0D00
	def fix_err_header(self):     #fc=0D01
		"""Fixes the data/err_header.txt file"""
		global err_hdr_list
		if os_isfile('data/err_header.txt'):
			error_hdr_file = Fsys.reader('data/err_header.txt')
			temp_ = re_sub('\,{2,}', ',', error_hdr_file)

			if temp_[-1] == ',': temp_ = temp_[:-1]

			err_hdr_list = eval(temp_)
			#print(type(err_hdr_list))
			if type(err_hdr_list) == tuple:
				err_hdr_list = Counter(err_hdr_list)

				Fsys.writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '00000')

			elif type(err_hdr_list) == list:
				_t = Counter()
				for i, j in err_hdr_list:
					_t[i] = j

				err_hdr_list = _t

				Fsys.writer('err_header.txt', 'w', str(err_hdr_list), 'data/', '00000')


			elif type(err_hdr_list) == dict:
				err_hdr_list = Counter(err_hdr_list)
		else:
			err_hdr_list = Counter()

BugFixes_n_Updates = BugFixes_n_Updates_()

class Main():     #fc=0M00
	def __init__(self):     #fc=0M01
		IOsys.delete_last_line()
		print("Connecting to server...")
		Ctitle('Connecting to server 🌐')
		self.dl_threads = []

	def get_user(self):     #fc=0M02
		UserData.get_user_ip()

		BugFixes_n_Updates.fix_err_header()
		config.run_mod = config.god_mode()
		UserData.log_in()

	def make_required_dirs(self):     #fc=0M03
		"""Make the required directories"""
		for i in ['Download_projects', 'data', 'data/.temp', 'data/leach_projects']:
			if not os_exists(i):
				makedirs(i)


	def boot_server(self):     #fc=0M04
		global server_launcher
		UserData.user_primary_port = (int(UserData.userhash, 16) % (60000 - 49200 + 1)) + 49200

		server_status = Netsys.check_server("http://localhost:%i"%UserData.user_primary_port, '00000', timeout=2)

		print([UserData.userhash])
		if server_status == False:
			UserData.user_secondary_port = (int(UserData.userhash, 16) % (64000 - 60001 + 1)) + 60001

		config.running_port = UserData.user_secondary_port if UserData.user_secondary_port else UserData.user_primary_port

		if server_status == True:
			config.server_running = True
			pass
		elif server_status in (False, None):
			server_launcher = Process(target=Netsys.run_server_t, args= (server_status, 'Download_projects'))
			server_launcher.start()
		else:
			exit()

	def main_loop(self):     #fc=0M05
		global Keep_main_running
		self.boot_server()

		self.link_indexed = False

		while True:
			try:
				self.COMM = IOsys.safe_input('\nEnter Batch download directory (Project name): ').strip()

				if any(ord(i)<32 or ord(i) == 127 for i in self.COMM) or self.COMM!=Datasys.remove_non_uni(self.COMM, '10009'):
					xprint("/r/Invalid Charecter!\n/y/Please retry...\n/=/")
					continue

			except LeachICancelError:
				try:
					xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
					#leach_logger("0x1||10009||User Exit-0")

					Keep_main_running = False

					while server_code == None: time.sleep(.5)
					server_code.server_close()
					exit(0)
				except EOFError:
					return 0
				except KeyboardInterrupt:
					return 0
			__command = self.COMM.lower()
			if __command == '':
				print('You must enter a Project name here.')
			elif __command in ['?disable-dl-thread', '?d-dl-t']:
				config.sp_arg_flag['disable dl cancel'] = True
				print('Disabled download cancellation by adding join thread option')
				return 0

			elif __command in ['?enable-dl-thread', '?e-dl-t']:
				config.sp_arg_flag['disable dl cancel'] = False
				print('Enabled download cancellation by adding removing thread option [DEFAULT]')
				return 0
			elif __command in ['?disable-dl-get', '?d-dl']:
				config.sp_arg_flag['disable dl get'] = True
				print('Disabled download save by using requests.head')
				return 0

			elif __command in ['?enable-dl-get', '?e-dl'] :
				config.sp_arg_flag['disable dl get'] = False
				print('Enabled download save by using requests.get [DEFAULT]')
				return 0

			elif __command in ['?enable-ara-ara', '?e-noise'] :
				config.sp_arg_flag['ara ara'] = True
				print('Enabled fun sounds [DEFAULT]')
				return 0

			elif __command in ['?disable-ara-ara', '?d-noise'] :
				config.sp_arg_flag['ara ara'] = False
				print('Enabled fun sounds [DEFAULT]')

			elif __command in ['?disable-browser', '?d-br']:
				config.sp_arg_flag['no browser'] = True
				print('Disabled opening Downloads in browser')
				return 0

			elif __command in ['?enable-browser', '?e-br'] :
				config.sp_arg_flag['no browser'] = False
				print('Enabled opening Downloads in browser [DEFAULT]')
				return 0

			elif __command in ['?disable-download-limit', '?d-dlim']:
				config.sp_arg_flag['dl'] = True
				print('Disabled Download Limit [DEFAULT]')
				return 0

			elif any(__command.startswith(i) for i in ['?enable-downlaod-limit', '?e-dlim']) :
				try:
					_temp_ = float(__command.split()[1]) #input will be in KB 1*1024
				except:
					xprint("/y/Invalid Download Speed Limit/=/")
					return 0
				config.sp_arg_flag['max dlim'] = _temp_
				print('Enabled Download Limit at', _temp_, 'kbps')
				return 0

			elif __command in ['?clean-project', '?c-p']:
				p_name = IOsys.safe_input("Enter the project name")
				P = ProjectType_(p_name)
				P.load_data(p_name)
				if P.list_good:
					P.clean_unknown_files()
				else:
					print('Project not found')
				return 0
			else:
				break


		print('shit', __command)

		self.P = ProjectType_(self.COMM)
		check_project = self.P.load_data(self.COMM)
		print(self.P.Project)

		if any(i in '\\/|:*"><?' for i in self.P.Project):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0

		Ctitle(f'Project {self.P.Project} [{config.mode_emoji[config.run_mod]}] [:{config.running_port}]')

		if check_project == True:
			if self.P.dl_done == True:
				xprint('/h/It seems  the old prject download was complete!!/=/')
				if self.P.has_missing:
					xprint('/r/Also have some MISSING files/=/')
				try:
					temp = IOsys.asker(out="""\u29bf Do you want to get updated data from the project link? (/hui/ y /=///hui/ n /=/)  %s
\u29bf If you want make a fresh start with that project name type /hui/ fresh /=///hui/ f /=/
\u29bf To open the project in Browser enter /hui/ b /=/
\u29bf To Create CBZ file(s) of the project in Browser enter /hui/ cbz /=/
/g/  >> /=/"""%(' /h/[Recommended]/=/' if self.P.has_missing == True else ''), extra_opt=('b', 'fresh', 'f', 'cbz'), extra_return = ('browser', 'fresh', 'fresh', 'cbz'))

				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
					#leach_logger("000||11000||%s||f-Stop||was_done||don't want to update proj or anything"%(self.P.Project))
					return 0

				if temp == 'browser' or temp == 'cbz':

					OSsys.import_make()
					if 'mangafreak' in self.P.sp_flags:
						if not os_exists('Download_projects/' + self.P.Project + '/'):
							xprint("\n  /hui/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
							return 0
						self.P.sub_dirs = natsort.natsorted([i for i in self.P.all_list.all_names[0] if os_isdir('Download_projects/' + self.P.Project + '/' + i)])
						self.P.all_list = All_list_type(len(self.P.sub_dirs))
						for i in range(len(self.P.sub_dirs)):
							for j in os_listdir('Download_projects/' + self.P.Project + '/' + self.P.sub_dirs[i]):

								if os_isfile('Download_projects/' + self.P.Project + '/' + self.P.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
									self.P.all_list.add_name(j, i)

						self.P.img_to_sort = True
						self.P.sp_extension = ''
					if temp == 'browser':
						try:
							first_page = self.P.make_html()

							Netsys.run_in_local_server(config.running_port, host_dir='%s/%s.html'%(self.P.Project, self.P.Project))


						except EOFError:
							#leach_logger('11000x40001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						except KeyboardInterrupt:
							#leach_logger('11000x40001x1||' + self.P.Project)
							print("cancel command entered!\nReturning to main page")
							return 0
						except LeachICancelError:
							#leach_logger('11000x40001x0||' + self.P.Project)
							print("cancel command entered!\nReturning to main page")
							return 0

						return 0

					else: # cbz
						try:
							first_page = self.P.make_cbz()
							print('CBZ Created in "%s"'%first_page)
						except EOFError:
							#leach_logger('11000x50001x0||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						except KeyboardInterrupt:
							#leach_logger('11000x50001x0||' + self.P.Project)
							print("cancel command entered!\nReturning to main page")
							return 0
						return 0

				elif temp == True:
					self.P.existing_found = False
					self.P.update = True
					self.P.overwrite_bool = False
					#leach_logger('11000x2||%s'%self.P.Project, UserData.user_name)

				elif temp == 'fresh':
					#print("Okay! Enter a new project name in the next line.")

					Project = self.P.Project
					self.P = ProjectType_(Project)
					self.P.existing_found = False
					#leach_logger('11000x1||%s'%self.P.Project, UserData.user_name)


				elif temp == False: return 0


			else:
				try:
					temp = IOsys.asker("""\u29bf Do you want to
resume the Project '%s'
yes/y to resume
\u29bf /hui/ fresh /=///hui/ f /=/ to Start fresh
/yh/(warning! last project data will be erased, /=/downloaded files will be safe, unless the program replaces the files with new ones)
/gh/  >> /=/"""%self.P.Project, extra_opt = ('f', 'fresh'), extra_return = ('fresh', 'fresh'))
				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
					#leach_logger("000||11000||%s||f-Stop||was_paused||don't want to resume proj or anything"%self.P.Project)
					return 0
				if temp == True:
					print('============ Reloaded =============')
					#leach_logger('11000x3||%s'%self.P.Project, UserData.user_name)
					self.P.existing_found = True
				elif temp == 'fresh':
					#leach_logger('11000x4||%s'%self.P.Project, UserData.user_name)
					#clear file data
					#writer(self.Project + '.list', 'w', '', 'data/leach_projects', '10009')
					#writer(self.Project + '.proj', 'w', '', 'data/leach_projects', '10009')

					Project = self.P.Project

					self.P = ProjectType_(Project)
					self.P.existing_found = False
				elif temp == False: return 0

		else:
			print("Could not load data from file. Please start over.")
			self.P.existing_found = False


		if self.P.existing_found is False:
			if self.P.update:
				if os_exists('data/leach_projects/' + self.P.Project):
					rmdir('data/leach_projects/' + self.P.Project)
					print('removed tdata')

				self.P.all_list = []
				self.P.sub_dirs = []
				self.P.sub_links = []
				self.P.dl_done = False
				sub_links = []
				sub_dirs = []
				sub_links2 = []

				if not any(i in self.P.sp_flags for i in['nh', 'mangafreak', 'webtoon']):
					page = self.P.dl_page()
					if page:
						link_true = True
					else:
						IOsys.safe_input("/rh/Link Unavailable! /=/It seems the previous link is unaccessable right now.\nPlease Retry the project sometimes later with stable internet connection\n(possible cause: no internet or wrong link)\n")
						return 0

				if 'webtoon' in self.P.sp_flags:
					print("Checking for links, please wait...")
					if self.P.webtoon_link() == 'all good':
						self.link_indexed = True
					else:
						xprint("/r/It seems the link is dead\n/y/please recheck the link and create a fresh Project/=/")
						return 0


				elif 'mangafreak' in self.P.sp_flags:
					print("Update isn't available for mangafreak")
					self.P.sp_flags.append('ignore_on_null_content') # do not save null files
					#self.P.sp_flags.append('stop_on_null_content') # stops downloading after receiving a null file
					try:
						if IOsys.asker('\u29bf Do you want to re-download files from the same link?\n >> '):
							will_unzip = IOsys.asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

							if will_unzip:
								self.P.sp_flags.append("dl unzip")
								if IOsys.asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
									self.P.sp_flags.append("del dl zip")
							try:
								self.P.link_startswith = self.P.mangafreak_link()

							except EOFError:
								print("Cancel command entered! stopping")
								return 0
							except KeyboardInterrupt:
								print("Cancel command entered! stopping")
								return 0
							if self.P.link_startswith == 0: # cancel code
								return 0

							self.P.file_exts = ('zip', )
							self.P.file_starts = ''
							self.link_indexed = True

							#leach_logger('10009x1||%s||is_mangafreak||%s'%(self.Project, str(self.P.sp_flags)), UserData.user_name)

					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						#leach_logger("000||10009||%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0


				elif 'nh' in self.P.sp_flags:
					try:
						self.P.link_startswith, title =self.P.nhentai_link()

					except EOFError:
						print("Cancel command entered! stopping")
						return 0
					except KeyboardInterrupt:
						print("cancel command entered! stopping")
						return 0

					if self.P.link_startswith == False and title == False:
						print("Failed to get data from %s\nReturning back to main page."%self.P.main_link)
						return 0

					if title!=False and self.P.link_startswith!='':
						self.link_indexed = True
						#leach_logger('10009x0||%s||is_nh'%(self.Project), UserData.user_name)

				else:
					sub_links2 = []
					try:
						self.P.img_to_sort = IOsys.asker("\n\n\u29bf Will download in sequncial order? ")
					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')

						pass#leach_logger("000||10009||%s||f-Stop||UI||user left while asking self.P.img_to_sort "%self.P.Project)
						return 0

					link_startswith_re = re_compile('^' + self.P.link_startswith)

					try:
						if self.P.dimention == 0:
							xprint("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")
							try:
								self.P.dimention = int(IOsys.safe_input("Enter the index of your choice (1/2/3): "))
							except ValueError:
								self.P.dimention = -1
							except LeachICancelError:
								xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
								return 0
							while self.P.dimention not in [1, 2, 3]:
								try:
									self.P.dimention = int(IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
								except ValueError:
									self.P.dimention = -1
								except LeachICancelError:
									xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
									return 0

							pass#leach_logger('10009x1||%s||dimention||%s'%(self.P.Project, self.P.dimention), UserData.user_name)

						self.P.gen_sub_links()
						self.P.gen_sub_dirs()


					except EOFError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						return 0
					except KeyboardInterrupt:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						return 0


			else:
				if os_exists('data/leach_projects/' + self.P.Project): rmdir('data/leach_projects/' + self.P.Project)
				if self.P.corruptions!=[] and self.P.corruptions != [0]:
					pass#leach_logger("10009x1||%s||Corruptions||%s||%s"%(self.P.Project,  str(self.P.corruptions), '<br>'.join(Fsys.reader('data/leach_projects/' + self.Project + '.proj', 'rb', True, 'str').strip().split('\n'))), UserData.user_name)

				Fsys.writer('errors.wlerr', 'a', '', 'data/leach_projects/' + self.P.Project, '10009') #reset error file

				self.P = ProjectType_(self.P.Project)

				sub_links = []
				link_true = False

				try:

					self.P.main_link = IOsys.safe_input("\nEnter the link: ")
					pass#leach_logger('10009x1||%s||m_link||%s'%(self.Project, self.P.main_link), UserData.user_name)
					while link_true == False:
						if SupportTools.check_sp_links(self.P.main_link, ['nh', 'mangafreak', 'webtoon']):

							if SupportTools.check_sp_links(self.P.main_link, 'mangafreak'):
								print("mangafreak link detected!!")
								is_mangafreak = IOsys.asker("\u29bf Do you want to download manga images from this links?? (/hui/ y /=///hui/ n /=/)\n>> ")
								if is_mangafreak:
									self.P.sp_flags.append('ignore_on_null_content') # do not save null files
									self.P.sp_flags.append('stop_on_null_content') # stops downloading after receiving a null file

									will_unzip = IOsys.asker("\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

									if will_unzip:
										self.P.sp_flags.append("dl unzip")
										if IOsys.asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
											self.P.sp_flags.append("del dl zip")
									try:
										_temp = self.P.mangafreak_link()
										if _temp == 0:
											return 0
										if _temp!= '':
											self.P.link_startswith = _temp
											del _temp
											self.P.file_exts = ('zip', )
											self.P.file_starts = ''

											pass#leach_logger('10009x1||%s||is_mangafreak.sp_flags||%s'%(self.Project, str(self.P.sp_flags)), UserData.user_name)
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


							if SupportTools.check_sp_links(self.P.main_link, 'webtoon'):
								xprint('/y/Webtoon link detected!/=/')
								is_webtoon = IOsys.asker('\u29bf Do you want to download the Entire Web comic?? (/hui/ y /=///hui/ n /=/)\n/gh/>>/=/  ')

								if is_webtoon:
									xprint("/y/Checking for links, please wait.../=/")
									if self.P.webtoon_link() == 'all good':
										self.P.link_startswith = 'https://www.webtoons.com'
										link_true = True
										self.link_indexed = True
									else:
										xprint("/r/It seems the link is dead\n/y/please recheck the links and your internet connection/=/")
										return 0


							if  SupportTools.check_sp_links(self.P.main_link, 'nh'): #main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
								xprint("/y/nhentai link detected!!/=/")
								is_nh = IOsys.asker("\u29bf Do you want to download doujin images from this links?? (/hui/ y /=///hui/ n /=/)\n/gh/>>/=/  ")
								####( io )
								if is_nh:
									if os_name == 'Windows' and config.sp_arg_flag['ara ara']:
										SupportTools.play_yamatte_t.start()

									self.P.link_startswith, title = self.P.nhentai_link()
									#print(link_startswith, title)
									if self.P.link_startswith == 0 and title == 0:
										return 0

									if title!=False and self.P.link_startswith!='':
										self.P.file_starts = ''

										self.link_indexed = True
										#leach_logger('10009x1||%s||is_nh||True||Assigned after testing the link'%(self.Project), UserData.user_name)
										link_true = True
										break

							if SupportTools.check_sp_links(self.P.main_link, 'pinterest'):
								print("Pinterest link detected.\nDo you want to try the special features for pinterest images?\nWarning: All images may not be the same from the website as you see\n")
								if IOsys.asker('>> '):

									if SupportTools.check_sp_links(self.P.main_link, 'pinterest-pin'):
										try:
											self.P.dimention = int(IOsys.safe_input("Enter the index of your choice (1/2/3): "))
										except ValueError:
											self.P.dimention = -1
										while self.P.dimention not in [1, 2, 3]:
											try:
												self.P.dimention = int(IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
											except ValueError:
												self.P.dimention = -1




									self.P.link_startswith = 'https://www.pinterest.com'
						if link_true == False:
							try:
								try:
									page = self.P.dl_page()
								except NetErrors:
									page = False
								if page:
									link_true = True
									break
								else:
									self.P.main_link = IOsys.safe_input('Link not found\nPlease Re-enter the link')
							except LeachICancelError:
								xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
								return 0


					if self.link_indexed==False:

						print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")

						try:
							self.P.dimention = int(IOsys.safe_input("Enter the index of your choice (1/2/3): "))
						except ValueError:
							self.P.dimention = -1
						while self.P.dimention not in [1, 2, 3]:
							try:
								self.P.dimention = int(IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
							except ValueError:
								self.P.dimention = -1
						pass#leach_logger('10009x1||%s||dimention||%s'%(self.P.Project, self.P.dimention), UserData.user_name)

						if self.P.dimention in (2,3):
							self.P.link_startswith = IOsys.safe_input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")

						file_types_i = IOsys.safe_input("\nEnter file formats (separate multiple by commas) *no need to add . in formats (ie: png, jpg, mp3) or just write the category (ie: image, music, video): ")
						if file_types_i in ('img', 'image', 'images', 'imgs', 'photo', 'photos'):
							self.P.file_exts = Constants.all_image_types
							self.P.file_types = file_types_i
						else:
							self.P.file_types = file_types_i
							self.P.file_exts = tuple(i.strip(i) for i in file_types_i.replace(' ', '').split(',')+file_types_i.split(' '))
						# leach_logger('10009x1||%s||f_types||%s'%(self.Project, str(self.file_types)), UserData.user_name)



						self.P.file_starts = IOsys.safe_input("\nFile Links Starts With (if known or need to be specified): ")
						# leach_logger('10009x1||%s||f_starts||%s'%(self.Project, self.file_starts), UserData.user_name)

						print('\n')


						self.P.img_to_sort = IOsys.asker("\n\n\u29bf Will download in sequncial order? ")
						self.P.overwrite_bool = IOsys.asker("\u29bf Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>")



						self.P.gen_sub_links()


				except LeachICancelError:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					# leach_logger("000||10009||%s||f-Stop||asking4sequence||probably user didnt get it"%self.Project)
					return 0

				except EOFError:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					# leach_logger("000||10009||%s||f-Stop||asking4sequence||probably user didnt get it"%self.Project)
					return 0

				except KeyboardInterrupt:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					# leach_logger("000||10009||%s||f-Stop||asking4sequence||probably user didnt get it"%self.Project)
					return 0


			if self.link_indexed == False:
				# leach_logger("10009x2||%s||%i"%(self.Project, len(self.sub_links)), UserData.user_name)

				if self.P.sub_dirs ==[]:
					self.P.gen_sub_dirs()

				len_sub_links = len(self.P.sub_links)

				self.P.all_list = All_list_type(len_sub_links)




				xprint('Indexed [0 / ' + str(len_sub_links) + ']')

				indx1 = Process(target=self.P.generic_list_writer, args=(3, 0))
				indx2 = Process(target=self.P.generic_list_writer, args=(3, 1))
				indx3 = Process(target=self.P.generic_list_writer, args=(3, 2))

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
					# leach_logger("10009x-1||%s||%s||%s"%(self.Project, e.__class__.__name__, str(e)), UserData.user_name)
					time.sleep(5)
					exit(0)



			if self.P.img_to_sort: self.P.all_list.all_links = natsort.natsorted(self.P.all_list.all_links, key = lambda x: x[0].lower())

			Fsys.writer('projects.db', 'a', self.P.Project + '\n', 'data', '10009')



		xprint('/y/ Processing /=/')
		Ctitle('[Processing] Project %s [%s%s] [:%i]'%(self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))


		# clean the files if exist
		Fsys.writer(self.P.Project + '.wllist', 'w', '', 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'w', '', 'data/leach_projects', '10009')

		# write new data
		Fsys.writer(self.P.Project + '.wllist', 'w', str(self.P.all_list.all_links), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'w', 'main_link= "%s"\n'%self.P.main_link, 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'link_startswith= "%s"\n'%self.P.link_startswith, 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'file_types = %s\n'%str(self.P.file_exts), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'file_starts= "%s"\n'%self.P.file_starts, 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'sub_dirs = %s\n'%str(self.P.sub_dirs), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'sp_flags = %s\n'%str(self.P.sp_flags), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'sp_extension = "%s"\n'%self.P.sp_extension ,'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'overwrite_bool = %s\n'%str(self.P.overwrite_bool), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'dimention = %s\n'%str(self.P.dimention), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'sequence = %s\n'%str(self.P.img_to_sort), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'Project = "%s"\n'%str(self.P.Project), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'sub_links = %s\n'%str(self.P.sub_links), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'dir_sorted = %s\n'%str(self.P.dir_sorted), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'all_names = %s\n'%str(self.P.all_list.all_names), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'file_formats = %s\n'%str([self.P.file_types]), 'data/leach_projects', '10009')
		Fsys.writer(self.P.Project + '.wlproj', 'a', 'dl_threads = %s\n'%str(self.P.dl_threads), 'data/leach_projects', '10009')

		print('\n')

		self.P.all_list.remove_duplicates()

		self.P.total = len(self.P.all_list)

		self.P.done -= self.P.errors  # to remove duplicate count


		# all_list_r = list(range(self.P.total))

		Ctitle('[Downloading] Project %s [%s%s] [:%i]'%(self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

		del self.dl_threads[:]
		self.dl_threads = []
		for i in range(self.P.dl_threads):
			self.dl_threads.append( Process(target = self.P.downloader, args = [i]))
			self.dl_threads[i].start()
		t99 = Process(target=self.P.retry_errors)
		t99.start()



		if config.sp_arg_flag['max dlim']!=0:
			self.P.tictoc = time.time()
			config.sp_arg_flag['chunk_size'] = int(config.sp_arg_flag['max dlim']*102.4) + 1
			t_dlim = Process(target=self.P.speed_limiter)
			t_dlim.start()
		else:
			t_dlim = Process()


		t_dl_speed = Process(target=self.P.speed_tester)
		t_dl_speed.start()


		if config.sp_arg_flag['disable dl cancel'] == True:
			try:
				for i in self.dl_threads:
					i.join()


				if config.sp_arg_flag['max dlim']!=0: t_dlim.join()
				t_dl_speed.join()

				Ctitle('[Download Complete] Project %s [%s%s] [:%i]'%(self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

			except EOFError:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True



		will_open = None

		OSsys.import_make()

		if not 'mangafreak' in self.P.sp_flags:
			try:
				first_page = self.P.make_html()
			except EOFError:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True

		while self.P.break_all == False and any(i.is_alive() for i in self.dl_threads+[t99, t_dlim, t_dl_speed]):
			try:
				will_open = IOsys.safe_input()
				print([i.is_alive() for i in self.dl_threads])
			except LeachICancelError:
				self.P.break_all = True
				leach_logger("000||10009||%s||D-Break||~||~"%(self.P.Project))
				break
		# print(self.P.dl_chunks*config.sp_arg_flag["chunk_size"])
		if self.P.break_all:
			xprint("/yh/Project continuation cancelled by Keyboard/=/")
			leach_logger("000||10009||%s||D-Stop||Downloading||%i|%i"%(self.P.Project, self.P.done, self.P.errors))
		else:
			if 'mangafreak' in self.P.sp_flags:
				try:
					first_page = self.P.make_html()
				except EOFError:
					leach_logger('10009x40001x0||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

				except KeyboardInterrupt:
					leach_logger('10009x40001x0||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

			if will_open == 'b':
				print(0)
				Netsys.run_in_local_server(config.running_port, host_dir='%s/%s.html'%(self.P.Project, self.P.Project))
				print(1)
				return 0

			elif will_open == 'cbz': # cbz
				try:
					first_page = self.P.make_cbz()
					print('CBZ Created in "%s"'%first_page)
				except EOFError:
					leach_logger('10009x50001x0||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				except KeyboardInterrupt:
					leach_logger('10009x50001x0||' + self.P.Project)
					print("cancel command entered!\nReturning to main page")
					return 0
				return



Keep_main_running = True

main = Main()
if __name__ == '__main__':
	main.make_required_dirs()
	main.get_user()
	while Keep_main_running:
		main.make_required_dirs()
		main.main_loop()

"""
Ray
nh
https://nhentai.to/g/301600/1/
n
3
img

n
n

"""

