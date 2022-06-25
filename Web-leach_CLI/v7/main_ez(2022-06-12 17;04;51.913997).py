"RUNNING FROM -- /storage/emulated/0/C_coding/Python/Web Leach/Web-leach/Web-leach_CLI/v7/main_ez.py"

#pylint:disable=W0201
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
# import post_online
print("LOADING ASSETS...")
print(1)  # x
requirements_all = ('requests', 'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pywin32-ctypes', 'comtypes', 'psutil', 'lxml', 'pywin32')


logger = True	# disable on publish 

# importing required packages

import Number_sys_conv as Nsys  # fc=1000

# different number based functions I made
start_up_dt = Nsys.compressed_dt()  # stores when the program was launched

import time

start_up = time.time()

from platform import system as os_name
os_name = os_name()

if os_name == 'Windows':
	import console_mod     #fc=2000
	console_mod.enable_color2() # to test

from print_text2 import xprint  # fc=3000


xprint('/=/', end='')

try:
	from constants import *  # fc=4000
	import ctypes

	def is_tool(name):  #fc=0000 xx
		"""Check whether `name` is on PATH and marked as executable."""
		from shutil import which
		return which(name) is not None


	def Ctitle(title):  # fc=0001
		"""sets CLI window title
		title: Window title"""

		try:
			ctypes.windll.kernel32.SetConsoleTitleW(title)
		except:
			if is_tool("title"):
				from os import system as os_system
				os_system('title ' + title)


	Ctitle('Loading Assets \u26ef')


	class server_code:  # fc=0002
		"""creating fake class
		to bypass error"""

		def __init__(self=None):
			pass

		def server_close(self=None):
			pass

		def serve_forever(self=None):
			pass

		def shutdown(self=None):
			pass


	#########################################################

	# SYS tools #######################
	from sys import exit as sys_exit, executable as sys_executable, getsizeof

	exit = sys_exit
	# sys_exit = exit

	from subprocess import call as subprocess_call, Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL
	from os import devnull as os_devnull, _exit as os_exit
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
	import re
	from re import search as re_search, compile as re_compile, sub as re_sub, findall as re_find_all

	from filesize import alternative as filesize_alt, size as filesize_size

	import rcrypto  # fc=5000
	import gen_uuid as uuid
	###################################

	# FILE system tools###############
	from os import makedirs, remove, rename, system as os_system, listdir as os_listdir, getcwd as os_getcwd
	from shutil import rmtree as rmdir, copyfile, move
	from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname, realpath as os_realpath
	from zipfile import ZipFile, BadZipFile
	import io	###################################



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
		import _server003_ as _server001_

		if os_name == 'Windows': import mplay4

		has_all_libs = True

	except:
		has_all_libs = False


	from headers_file import header_list
	##########################################

	# Other Libs###############################
	from collections import Counter
	from functools import reduce as functools_reduce
	from operator import iconcat as operator_iconcat
	
	import json

	import dig_info  # fc=6000

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


print(2) # x
class AboutApp_ :     #fc=A000
	""" Contains Information about the app and verion details"""

	_VERSION = '7.001'
	_Vcode = '007001'
	_APP_NAME = 'Web-Leach'
	_APP_DESC = 'Web-Leach is a simple python script to download files from web'
	_APP_AUTHOR = 'Ratul Hasan'
	_APP_AUTHOR_EMAIL = 'wwwqweasd147[at]gmail[dot]com'
	_APP_URL = ''
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
	server_version = 'UNREACHED'

	cloud_data_link_global = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/_global_6.txt'
	cloud_data_link = 'https://raw.githack.com/Ratulhasan14789/Web-Leach_pub/main/Backend_servers/update%20server%20v6.00000.txt'
	cloud_html_temp_link = 'https://raw.githack.com/RaSan147/Web-Leach_pub/main/page_template/wl-page-v3.html'
	cloud_html_temp_link_proxy = 'https://gitcdn.link/cdn/RaSan147/Web-Leach_pub/main/page_template/wl-page-v3.html'
	
	
	Cache_Scripts = {'hammer.min.js': "https://hammerjs.github.io/dist/hammer.js",
					'touch-emulator.js': "http://cdn.rawgit.com/hammerjs/touchemulator/master/touch-emulator.js",
	}

	Cache_Assets = {"emo_angel_titled_w400.png": 'https://i.ibb.co/D4KnFRC/emo-angel-titled-w400.png',
					"icon.ico": "https://cdn.jsdelivr.net/gh/Ratulhasan14789/Web-Leach_pub@main/resources/icon.ico",
					
	}


	g_mode = None

	leach_projects = 'data/leach_projects/'
	# location to store project data

	download_dir = "Download_projects/"
	# download directory
	thread_data_dir = "data/leach_projects/"  # + project name
	# location to store the thread data
	data_dir = "data/"
	# location to store app data
	temp_dir = data_dir + ".temp/"
	# location to store temp data
	cached_webpages_dir = data_dir + ".cached_webpages/"


AboutApp = AboutApp_()


class DefaultConfig :  # fc=0200
	""" Default configuration to load up on each start"""

	disable_lib_check = Constants.DEFAULT_DISABLE_LIB_CHECK
	# if True, the installed lib check will be skipped to speed up
	has_all_libs = has_all_libs
	# this is True when all libs are installed
	ara_ara = False
	# to control parody noise
	no_log = False
	# to stop logging
	death = False
	dying = False

	dir_limit = 150
	file_limit = 120

	sp_arg_flag = {'disable dl cancel': False,
	               'disable dl get': False,
	               'ara ara': False if ara_ara is None else ara_ara,
	               'no log': False if no_log is None else no_log,
	               'no browser': False,
	               'max dlim': 0,  # in kbps
	               'chunk_size': 8192,  # in Bytes
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






class AppConfig_ (DefaultConfig):     #fc=0300
	""" Configuration to load up on each start
	also initializes the default when needed

	loads and contains update log, user_list, server info
	"""

	def __init__(self):  # fc=0301
		""" Sets app config"""

		self.immutable_config()
		# self.__default__()

	def immutable_config(self):  # fc=0302
		""" Sets immutable config
		for one time set
		*won't change on self.__default__()"""
		self.__update__G = 'pass'
		self.__update__L = 'pass'
		self.user_list = ['bec6113e5eca1d00da8af7027a2b1b070d85b5ea', 'eb23efbb267893b699389ae74854547979d265bd',	'4e2ca20e54f5002d0a26ae868c4a9f520dc44de8']
		self.g_mode = None

		self.server_version = "0.6.0.0"

		self._latest_version = '5.5'
		self._latest_link = 'https://rawcdn.githack.com/Ratulhasan14789/Web-Leach_pub/ee5bcde7b25e1655e1dda2803ab002fdad982170/release/CLI/Web%20leach%200.5.5.4.zip'

		self._latest_hash = '97b804fb717c0ceee89d1825b79c5ade'
		self._latest_size = "7.4mb"
		self._latest_filename = 'Web leach 0.5.5.4'
		self._latest_check_exe_hash = True
		self._latest_check_zip_hash = True
		self._latest_exe_hash = self._latest_hash
		self._latest_zip_hash = '42bc93d2a66bf24bf40cb211bbb52bd6'

	def __default__(self):  # fc=0303
		""" Import config from default when needed"""

		for i in DefaultConfig.__dict__:
			if i[0] != '__':
				self.__dict__[i] = DefaultConfig.__dict__[i]

	def set_default(self, name):  # fc=0304
		""" Change the default config for specific name
		returns to the usual value on re-open

		name: Name of config variable
		"""
		self.__dict__[name] = DefaultConfig.__dict__[name]

	def set_config(self, name: str, value):  # fc=0305
		"""Sets config for specific name

		name: Name of config variable
		value: Variable value

		returns: Old value of config variable
		"""

		if hasattr(self, name):
			old = getattr(self, name)
		setattr(self, name, value)

		return old


	def god_mode(self, missing=None):  # fc=0306
		""" Downloads and executes cloud based scrips and also
			saves it for offline usage. Offline is only allowed if user
			has used online mode at least once

			missing: if a file is missing in runtime will either download or stop that action on failure
					1: who_r_u.mp3
					2: wl-page.html
					3: updateL.ext
					4: updateG.ext
					5: ?scripts
					6: ?assets
			
			TODO: make offline available  *idk how works offline* figured it out ✌🏻"""
		if missing is None:
			missing = [1, 2, 3, 4, 5, 6]
		if isinstance(missing, int):
			missing = [missing]


		if os_isdir(AboutApp.data_dir + 'projects'):
			rename(AboutApp.data_dir + 'projects', AboutApp.leach_projects)
		if os_isdir('./projects'):
			rename('./projects', AboutApp.download_dir)

		message = "failed initializing f()"
		err_print = True
		try:
			if 1 in missing:
				if os_name == 'Windows':
					message = "was DLing 'who_r_u.mp3'"
					link = Constants.who_r_u
					out = Netsys.link_downloader(link, AboutApp.temp_dir, 'who_r_u.mp3', '0306x1', '0306x2', False, err_print=err_print)
					err_print = out and err_print # if out is true then it will print the message on next error since there was no print ins the previous one

			if 2 in missing:
				message = "was DLing 'wl-page.html'"
				link = AboutApp.cloud_html_temp_link
				out = Netsys.link_downloader(link, AboutApp.temp_dir, 'wl-page.html', '0306x7', '0306x8', True, err_print=err_print, proxy=[AboutApp.cloud_html_temp_link_proxy,])
				err_print = out and err_print

			if 3 in missing:
				message = "was DLing 'updateL.ext'"
				link = AboutApp.cloud_data_link
				out = Netsys.link_downloader(link, AboutApp.temp_dir, 'updateL.ext', '0306x3', '0306x4', True, err_print=err_print)
				if out:
					config.__update__L = Fsys.reader(AboutApp.temp_dir + 'updateL.ext')
					exec(rcrypto.decrypt(config.__update__L, "lock").strip(), globals())
				
				err_print = out and err_print

			if 4 in missing:
				message = "was DLing 'updateG.ext'"
				link = AboutApp.cloud_data_link_global
				out = Netsys.link_downloader(link, AboutApp.temp_dir, 'updateG.ext', '0306x5', '0306x6', True, err_print=err_print)
				if out:
					config.__update__G = Fsys.reader(AboutApp.temp_dir + 'updateG.ext')
					exec(rcrypto.decrypt(config.__update__G, "lock").strip(), globals())
				err_print = out and err_print
				
			if 5 in missing:
				# TODO: NEED TO DOCUMENT
				message = "was DLing 'JS scripts'"
				links = AboutApp.Cache_Scripts
				
				for name in links.keys():
					link = links[name]
					out = Netsys.link_downloader(link, AboutApp.temp_dir+'scripts/', name, '0306x9', '0306xA', False, err_print=err_print, proxy=[AboutApp.cloud_html_temp_link_proxy,])
					err_print = out and err_print

			if 6 in missing:
				# TODO: NEED TO DOCUMENT
				message = "was DLing 'Asset files'"
				links = AboutApp.Cache_Assets
				
				for name in links.keys():
					link = links[name]
					out = Netsys.link_downloader(link, AboutApp.temp_dir+'assets/', name, '0306xB', '0306xC', False, err_print=err_print, proxy=[AboutApp.cloud_html_temp_link_proxy,])
					err_print = out and err_print



			return 'online' if err_print else 'offline'


		except Exception as e:
			print(rcrypto.decrypt(Fsys.reader(AboutApp.temp_dir + 'updateL.ext'), "lock").strip())
			xprint("/hui/", e.__class__.__name__, ": /=/ Unknown error occurred. Error code 0306x0\nPlease inform the author.")
			leach_logger(log(["0306x0", Netsys.hdr(Netsys.current_header, '0306'), link, e.__class__.__name__, e, message]), 'lock')
			time.sleep(5)
			exit(0)


config = AppConfig_()

print(3)  # x


class UserData_ :  # fc=0400
	""" Contains User data, log-in and user data collection functions"""

	def __init__(self):  # fc=0401
		""" initializes UserData and gets device info """
		self.Device_Data = dig_info.getSystemInfo()
		self.user_ip = {'ip': '0.0.0.0'}
		self.userhash = '0'
		self.user_name = None
		self.user_primary_port = None
		self.user_secondary_port = None

	def get_user_ip(self):  # fc=0402 v
		""" connects to the internet and returns the users global ip"""

		current_header = Netsys.header_()
		try:
			page = requests.get('https://api.myip.com/', headers=current_header, timeout=6)
			if page:
				self.user_ip = page.json()
				return self.user_ip
			else:
				xprint("/rh/Error code: 0402x1\nNo internet connection!/=/\nRunning offline mode")
				leach_logger(log(["0402x1", Netsys.hdr(current_header, '0402'), page.status_code]), 'lock')
				return '0.0.0.0'

		except NetErrors as e:
			xprint("/rh/Error code: 0402x2\nNo internet connection!/=/\nRunning offline mode")
			leach_logger(log(["0402x2", Netsys.hdr(current_header, '0402'), e.__class__.__name__, e]), 'lock')
			return '0.0.0.0'

		except Exception as e:
			xprint('/r/', e.__class__.__name__, "occurred. Please inform the Author.\nError code: 0402x0(%s)/=/"%e.__class__.__name__)
			leach_logger(log(["0402x0", Netsys.hdr(current_header, '0402'), e.__class__.__name__, e]), 'lock')
			time.sleep(5)
			exit(0)

	def log_in(self):  # fc=0403
		""" logs in the user and returns the users hash """
		if boss != 1:
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
						ex = mplay4.ex_vol()
						if not os_isfile(AboutApp.temp_dir + 'who_r_u.mp3'):
							if config.god_mode(1) == 'offline':
								continue
						mplay4.load(AboutApp.temp_dir + 'who_r_u.mp3').play()
					time.sleep(5)
					if os_name == 'Windows':
						mplay4.set_win_vol(ex)
		else:
			self.userhash = 'eb23efbb267893b699389ae74854547979d265bd'

		if not os_exists(AboutApp.data_dir + 'projects.db'):
			Fsys.writer('projects.db', 'a', '', 'data', '00016')
		if self.userhash == 'eb23efbb267893b699389ae74854547979d265bd':
			AboutApp.g_mode = 'Kirito'

		return self.userhash


UserData = UserData_()

print(4)  # x


class IOsys_ :  # fc=0500
	""" Contains Input and Output functions """

	def clear_screen(self):  # fc=0501 v
		"""clears terminal output screen"""

		if os_name == "Windows":
			os_system('cls')
		else:
			os_system('clear')

	def delete_last_line(self, lines=1):  # fc=0502 v
		"""Use this function to delete the last line in the STDOUT

		args:
		-----
			lines: total number of lines *1
				0 to delete current line"""

		# return 0
		if lines == 0:
			sys_write('\n')
			self.delete_last_line()
			return 0

		for _ in range(lines):
			# cursor up one line
			sys_write('\x1b[1A')

			# delete last line
			sys_write('\x1b[2K')

	def leach_logger(self, io, key='lock'):  # fc=0503 v
		"""saves encrypted logger data to file\n
		(new in 5.3_class: auto adds dt_() at the beginning)

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
						salt = hashlib_sha1(key.encode()).hexdigest()[:-6] + AboutApp._Vcode

						Fsys.writer('userlog.leach', 'ab', rcrypto.encrypt(salt + ('%s||'%Nsys.compressed_dt()) + str(process_id) + '||' + html_escape(io) + '||', _key).encode('utf-8') + b'\n', 'data', '00008')
						break
					except EOFError:
						pass
					except KeyboardInterrupt:
						pass
				except EOFError:
					pass
				except KeyboardInterrupt:
					pass

		except EOFError:
			self.leach_logger(io, key='lock')
		except KeyboardInterrupt:
			self.leach_logger(io, key='lock')

	def safe_input(self, msg='', i_func=input, o_func=xprint,
	               on_error=LeachICancelError):  # fc=0504 v
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
					# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
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
	          i_func=input, o_func=xprint, on_error=LeachICancelError,
	          condERR=Constants.condERR, no_bool=False):  # fc=0505 v
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

		if len(extra_opt) != len(extra_return):
			xprint('/r/Additional options and Additional return data don\'t have equal length/=/')
			raise LeachKnownError

		if no_bool:
			if len(extra_opt) < 1:
				xprint('/r/With no_bool arg, you must give at least 1 extra option [extra_arg & extra_return]/=/')
				raise LeachKnownError

		Ques2 = self.safe_input(out, i_func, o_func, on_error).lower()
		if default is not None and Ques2 == '':
			return default
		# Ques2 = Ques2
		while Ques2 not in (tuple() if no_bool else Constants.cond) + Nsys.flatten_array(extra_opt, tuple):
			Ques2 = self.safe_input(condERR, i_func, o_func, on_error).lower()
		# Ques2 = Ques2

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
def on_exit():  # fc=XXXX
	server_code.server_close()
	server_code.shutdown()
	server_launcher._stop()
	pass


print(5)  # x


class Fsys_ :  # fc=0600

	def get_sep(self, path):  # fc=0601
		"""returns the separator of the path"""
		if '/' in path:
			return '/'
		elif '\\' in path:
			return '\\'
		else:
			return os.sep

	def loc(self, path, _os_name='Linux'):  # fc=0602 v
		"""to fix dir problem based on os

		args:
		-----
			x: directory
			os_name: Os name *Linux"""

		if _os_name == 'Windows':
			return path.replace('/', '\\')
		else:
			return path.replace('\\', '/')

	def get_file_name(self, directory, mode='dir'):  # fc=0603 v
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
			if extra_removed == '':
				name = Netsys.gen_link_facts(directory)["host"]
			name = extra_removed.rpartition("/")[2]

			name = Datasys.trans_str(html_unescape(name), {'/\\|:*><?': '-',
			                                               '"': "'",
			                                               "\n\t\r": " "})
			return os_basename(name)
		elif mode == 'dir':
			return os_basename(directory)
		else:
			raise ValueError

	def get_file_ext(self, directory, mode='dir', no_format='noformat'):  # fc=0604 v
		"""to get the extension of a file directory

		args:
		-----
			directory: file directory relative or direct
			mode: url or file directory ** need to work with url
			no_format: returning format if no file extension was detected *noformat"""

		temp = self.get_file_name(directory, mode).split('.')
		if len(temp) == 1:
			return no_format
		else:
			return temp[-1]

	def get_dir(self, directory, mode='dir'):  # fc=0605 v
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
			while len(dirs) != 0 and dirs[-1] == '':
				dirs.pop()

			if dirs == []:
				return Netsys.gen_link_facts(directory)['host']

			directory = Datasys.trans_str(parse.unquote(html_unescape(dirs[-1])), {'/\\|:*><?': '-', '"': "'"})

			return directory
		elif mode == 'dir':
			if os_basename(directory) == '':
				return os_basename(os_dirname(directory))
			else:
				return os_basename(directory)
		else:
			raise ValueError

	def go_prev_dir(self, directory, preserve_sep=False):  # fc=0606 v
		"""returns the previous path str of web link or directory
		warning: returns only in linux directory format
		if preserve_sep is True, it will preserve the separator of the directory

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

	def reader(self, direc, read_mode='r', ignore_error=False, output=None,
	           encoding='utf-8', f_code='?????', on_missing=None,
	           ignore_missing_log=False):  # fc=0607 v
		"""reads file from given directory. If NOT found, returns `None`

		args:
		-----
			direc: file directory
			read_mode: `r` or `rb` *`r`
			ignore_error: ignores character encoding errors *`False`
			output: output type `bin`/`str`/`None` to auto detect *`None`
			encoding: read encoding charset *`utf-8`
			func_code: calling function *`????`
		"""

		if type(read_mode) != str:
			xprint("/rh/Invalid read type./yh/ Mode must be a string data/=/")
			leach_logger(log(['0607x3', f_code, direc, output, encoding, ignore_error, on_missing]))
			raise TypeError
		if read_mode in ('w', 'wb', 'a', 'ab', 'x', 'xb'):
			xprint("/r/Invaid read mode:/wh/ %s/=//y/ is not a valid read mode.\nTry using 'r' or 'rb' based on your need/=/")
			leach_logger(log(['0607x4',f_code, direc, output, encoding, ignore_error, on_missing]))
			raise LeachKnownError
		if 'b' in read_mode:
			read_mode = 'rb'

		else:
			read_mode = 'r'

		if (not os_isfile(self.loc(direc))):
			if (not ignore_missing_log):
				print(self.loc(direc), 'NOT found to read. Error code: 0607x1')
				leach_logger(log(['0607x1', f_code, direc, output, encoding, ignore_error, on_missing]))
			return on_missing

		try:
			with open(self.loc(direc), read_mode, encoding=None if 'b' in read_mode else encoding) as f:
				out = f.read()
		except PermissionError:
			if (not ignore_missing_log):
				xprint(self.loc(direc), 'failed to read due to /hui/ PermissionError /=/. Error code: 0607x2')
				leach_logger(log(['0607x2', f_code, direc, output, encoding, ignore_error, on_missing]))
			return on_missing
		if output is None:
			if read_mode == 'r':
				output = 'str'
			else:
				output = 'bin'
		if ignore_error:
			out = Datasys.remove_non_uni(out, '00013', output)

		else:
			if output == 'str' and read_mode == 'rb':
				try:
					out = out.decode()
				except Exception as e:
					xprint(f"/r/failed to decode /hui/{self.loc(direc)}/=//y/ to the specified character encoding. \nError code: 0607x5")
					leach_logger(log(['0607x3',f_code, direc, output, encoding, ignore_error, on_missing]))
					raise e
			elif output == 'bin' and read_mode == 'r':
				try:
					out = out.encode(encoding)
				except Exception as e:
					xprint(self.loc(direc), 'failed to encode to the specified character encoding. \nError code: 0607x5')
					leach_logger(log(['0607x4',f_code, direc, output, encoding, ignore_error, on_missing]))
					raise e

		return out

	def writer(self, fname, mode, data, direc=None, f_code='????',
	           encoding='utf-8'):  # fc=0608 v
		"""Writing on a file

		args:
		-----
			fname: filename
			mode: write mode (w, wb, a, ab)
			data: data to write
			direc: directory of the file, empty for current dir *None
			func_code: (str) code of the running func *empty string
			encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""

		def write(location):
			if 'b' not in mode:
				with open(location, mode, encoding=encoding) as file:
					file.write(data)
			else:
				with open(location, mode) as file:
					file.write(data)

		if type(mode) != str:
			xprint("\n/rh/Invalid write type./yh/ Mode must be a string data/=/Error code 0608x%s\n" % f_code)
			raise TypeError
		if mode not in ('w', 'wb', 'a', 'ab', 'r+', 'rb+', 'w+', 'wb+', 'a+', 'ab+'):
			xprint('\n/r/Invalid mode\nMust be a Writable Mode/=/Error code 0608x%s\n' % f_code)
			raise LeachKnownError

		if not isinstance(data, (str, bytes)):
			xprint("/rh/Invalid data type./yh/ Data must be a string or binary data/=/")
			leach_logger(log(['0608x3', f_code, direc, fname, mode, data, encoding]))
			raise TypeError
		mode = mode.replace('+', '').replace('r', 'w')

		if any(i in fname for i in ('/\\|:*"><?')):
			# these characters are forbidden to use in file or folder Names
			leach_logger(log(['0608x1', f_code, fname, direc, mode, type(data), encoding]))
			fname = Datasys.trans_str(fname, {'/\\|:*><?': '-', '"': "'"})

		if direc is None or direc == '':
			direc = './'
		# directory and file names are auto stripped by OS
		# or else shitty problems occurs

		direc = direc.strip()
		fname = fname.strip()

		try:
			if direc is None:
				locs = './'
				write(fname)
			else:
				locs = self.loc(direc, 'Linux')
				if any(i in locs for i in ('\\|:*"><?')):
					leach_logger(log(['0608x1', f_code, fname, direc, mode, type(data), encoding]))
					locs = Datasys.trans_str(locs, {'\\|:*><?': '-', '"': "'"})

				if not os_isdir(locs):
					# creates the directory, then write the file
					try:
						makedirs(locs, exist_ok=True)
					except FileExistsError:
						pass
					except Exception as e:
						if e.__class__.__name__ == "PermissionError":
							_temp = ''
							_temp2 = locs.split('/')
							_temp3 = 0
							while True:
								_temp += _temp2[_temp3] + '/'
								if not os_isdir(_temp): break
							leach_logger('||'.join(map(str,['0608x2', f_code, fname, direc, mode, type(data), encoding])))
							del _temp, _temp2, _temp3
						raise e
				if locs.endswith('/'):
					direc = self.loc(locs + fname)
				else:
					direc = self.loc(locs + '/' + fname)

				write(direc)

		except Exception as e:
			if logger: traceback.print_exc()
			if e.__class__.__name__ == "PermissionError":
				xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc is None else direc, '/y/\nPlease inform the author. Error code: %sx101/=/' % f_code)
				leach_logger('||'.join(map(str,['0608xP', f_code, fname, direc, mode, type(data), encoding])))
				raise LeachPermissionError
			else:
				leach_logger('||'.join(map(str,['0608x0', f_code, fname, direc, mode, type(data), encoding, e.__class__.__name__, e])))

				xprint('/r/', e.__class__.__name__, "occurred while writing", fname, 'in', 'current directory' if direc is None else direc, '/y/\nPlease inform the author. Error code: 00008x' + f_code, '/=/')
				raise e

Fsys = Fsys_()

print(6)  # x


class OSsys_ :  # fc=0700
	"""Operating System functions"""

	def install(self, pack, alias=None):  # fc=0701 v
		"""Just install package

		args:
		-----
			pack: the name the library (beautifulsoup4, requests)
			alias: if the pip package name is different from lib name, then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name) """

		if alias is None:
			alias = pack

		subprocess_call([sys_executable, "-m", "pip", "install", '--disable-pip-version-check', '--quiet', alias])

	def install_req(self, pkg_name, alias=None):  # fc=0702 v
		"""install requirement package if not installed

		args:
		-----
			pkg_name: Package name to search if installed
			alias: if the pip package name is different from lib name,
				then used alias (not required here) [beautifulsoup4 (pip)=> bs4 (lib name)] """

		if pkg_name not in self.get_installed():
			if not Constants.check_internet():
				xprint("/rh/No internet! Failed to install requirements/=/\n/ruh/Closing in 5 seconds/=/")
				return False
				
			xprint("/y/Installing missing libraries (%s)/=/"%pkg_name)
			self.install(pkg_name, alias)
			IOsys.delete_last_line()

		if pkg_name not in self.get_installed():
			xprint('/r/Failed to install and load required Library: "%s"/y/\nThe app will close in 5 seconds/=/'%pkg_name)
			try:
				pass #leach_logger('00006||%s||%s'%(pkg_name, str(Netsys.check_internet("https://pypi.org", '00006'))))
			except NameError:
				pass
			return False
		return True

	def get_installed(self):  # fc=0703 v
		"""returns a list of installed libraries"""

		import pkg_resources as pkg_r
		reload(pkg_r)

		return [pkg.key for pkg in pkg_r.working_set]

	def import_make(self, f_code="????"):  # fc=0704 v
		""" reads and exec() necessary files to create different formats of
		output [ie: html, cbz]
		args:
			f_code: caller function id
		"""
		try:
			exec(Fsys.reader('make_html4.py'), globals())
		except Exception as e:
			traceback.print_exc()
			xprint("\n\nSome error occurred while loading make_html file. \n/hui/Error code: 0704x0/=/\nReport to the author\nExiting in 5 seconds")
			leach_logger(log(['0704x0', f_code, 'make_html4.py', e.__class__.__name__, e]))

			time.sleep(5)
			exit()

		try:
			exec(Fsys.reader('make_cbz2.py'), globals())
		except Exception as e:
			xprint("\n\nSome error occurred while loading make_html file. \n/hui/Error code: 0704x0/=/\nReport to the author\nExiting in 5 seconds")
			leach_logger(log(['0704x0', f_code, 'make_cbz2.py', e.__class__.__name__, e]))
			time.sleep(5)
			exit()

	def catch_KeyboardInterrupt(self, func, f_code, *args):  # fc=0705 v
		"""Runs a function in a isolated area so that Keyboard cancel
		can be caught and processed accordingly

		args:
		-----
			func: The function to call inside the space
			f_code: The caller function id
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
					leach_logger(log(['0705x0',f_code, func.__name__, 'input exit code L&infin;ping for unknown reason']))
			except EOFError:
				raise LeachICancelError
			except KeyboardInterrupt:
				raise LeachICancelError
		except EOFError:
			raise LeachICancelError
		except KeyboardInterrupt:
			raise LeachICancelError

	def install_missing_libs(self):  # fc=0706 v
		""" installs missing libraries from the requirements variable"""

		if config.disable_lib_check:
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
						exit()  # required in mplay4

		config.has_all_libs = True
		xprint('/hu/Rebooting Program. Please wait/=/')
		try:
			subprocess_call(sys_executable + ' "' + os.path.realpath(__file__) + '"')
		except KeyboardInterrupt: pass
		except EOFError: pass
		finally:
			exit(0)

	def import_missing_libs(self, failed=False):  # fc=0707 v
		""" imports missing libs to global level and on missing installs and re-imports
		
		failed: failed once, won't retry"""
		# print(config.disable_lib_check)

		if config.disable_lib_check:
			return 0

		all_libs = OSsys.get_installed()
		
		has_all_libs = all(i in all_libs for i in requirements_all)
		if os_name=="Windows":
			has_all_libs = has_all_libs and all(i in all_libs for i in requirements_win)
		
		# print(has_all_libs, all_libs)
		if has_all_libs:
			return 0
		global bs, parser, g_search, requests, natsort, _server001_, mplay4
		self.install_missing_libs()

		######### RE-IMPORTING THE PYTHON 3RD PARTY LIBRARIES #########
		try:
			from bs4 import BeautifulSoup as bs
			print(7.2)  # x
			parser = 'lxml'
			try:
				bs('<br>', parser)
			except:
				parser = 'html.parser'
			print(7.3)  # x
			from googlesearch import search as g_search
			print(7.4)  # x
			import requests, natsort
			print(7.5)  # x
			import _server003_ as _server001_
			print(7.6)  # x
			if os_name == "Windows": import mplay4

		except:
			if failed:
				traceback.print_exc()
				xprint("/r/Failed to load required libraries.\n/=//yh/Possible cause 1st initialization without internet")

			else:
				self.import_missing_libs(failed=True)


OSsys = OSsys_()

if __name__ == '__main__':
	OSsys.import_missing_libs()
	from response_cache import Cached_Response

print(7)  # x

NetErrors = (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError,
             requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema,
             requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError)

print(8)  # x


class Netsys_ :  # fc=0800
	"""Network system functions"""

	def __init__(self):  # fc=0801 v
		""" initializes important variables """
		self.link_extractor = re_compile( r'^(?P<noQuery>(?P<homepage>(?P<schema>((?P<scheme>[^:/?#]+):(?=//))?(//)?)(((?P<login>[^:/]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@/?#:]*)(?::(?P<port>\d+)?)?)?)?(?P<path>[^?#]*))(\?(?P<query>[^#]*))?(#(?P<fragment>.*))?')  # compiled regex tool for getting homepage
		self.current_header = ''
		# https://regex101.com/r/UKWPmt/1
		# noQuery: https://regex101.com/r/UKWPmt/1
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

	def header_(self, referer=None):  # fc=0802 v
		"""returns a random header from header_list for requests lib
		
		referer: if not none, adds referer to the header"""
		header = {'User-Agent': random_choice(header_list)}
		if referer:
			header['Referer'] = referer
		return header

	def hdr(self, header, f_code='????'):  # fc=0803 v
		"""returns the index of a header

		args:
		-----
			header: header dict
			f_code: function caller code"""

		try:
			return str(header_list.index(header['User-Agent']))
		except ValueError:
			xprint("/y/DATA CORRUPTION found\nError code: 00009x" + f_code, '/=/')

			leach_logger(log(['0803x1', f_code, header]))
			return str((-1, header))

		except Exception as e:
			xprint("/y/Some error occurred caused, possible cause: DATA CORRUPTION\nError code: 00009x" + f_code, '/=/')

			leach_logger(log(['0803x1', f_code, header, e.__class__.__name__, e]))
			return str((-1, header))

	def get_link(self, i, current_link, homepage=None):  # fc=0804 v
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

		i = i.partition('#')[0]  # removes the fragment

		if '//' not in i:
			temp = homepage
			if temp.endswith('/'):
				if i.startswith('/'):
					i = temp + i[1:]
				else:
					i = temp + i
			else:
				if i.startswith('/'):
					i = temp + i
				else:
					i = temp + '/' + i

		return i

	def get_homepage(self, link):  # fc=0805
		"""Gets the homepage of a link

		Args:
		-----
			link : link to get homepage from
		"""

		x = self.gen_link_facts(link)

		return x['homepage']

	def check_internet(self, link, f_code='????', timeout=None, no_log=False):  # fc=0806
		"""Check if the connection is available or not

		args:
		-----
			link: link to check for connection status
			f_code: function caller id
			timeout: set timeout if not none
			"""

		current_header = self.header_()
		try:
			if timeout is None:
				r = requests.head(link, headers=current_header)
			else:
				r = requests.head(link, headers=current_header, timeout=timeout)

			if r:
				return True
			else:
				if not no_log:
					leach_logger('||'.join(map(str,['0806x2', f_code, link, self.hdr(current_header, '0806'), timeout, r.status_code])))
		except NetErrors as e:
			if not no_log:
				leach_logger('||'.join(map(str,['0806x2', f_code, link, self.hdr(current_header, '0806'), timeout, e.__class__.__name__, e])))
			return False
		except EOFError:
			return False
		except KeyboardInterrupt:
			return False

	def check_network_available(self):
		"""check if the computer has internet access"""

		current_header = self.header_()

		try:
			r = requests.head('https://www.google.com', headers = current_header)
			if not r:
				time.sleep(2)
				_ = requests.head('https://www.bing.com', headers = self.header_())

			return True

		except NetErrors:
			return False





	def run_server(self, port, cd=None, f_code='????'):  # fc=0807 v
		"""Runs localhost server using python.\n
		the I/O is suppressed

		args:
		-----
			port : PORT number\n
			cd : the directory to host
			f_code: caller id"""

		if cd is None:
			cd = '.'

		if any(i in cd for i in '\\|:*"><?'):  # there characters are forbidden
			xprint("\n/y/Invalid localhost directory. Please inform the author.\nError code: 0000Bx2/=/")
			leach_logger(log(['0807x1', f_code, port, cd]))
			time.sleep(5)
			os_exit(1)

		if not os_isdir(cd):  # invalid missing directory
			xprint('\n/y/' + cd, "not found!\nPlease inform the author\nError code: 0000Bx3/=/")
			leach_logger(log(['0807x2', f_code, port, cd]))
			time.sleep(5)
			os_exit(1)

		try:
			if config.server_status in (False, None):
				if cd != '.':
					return _server001_.run_server(port, cd, AboutApp.temp_dir)
				else:
					return _server001_.run_server(port, data_dir=AboutApp.temp_dir)
			else:
				return 0
		except EOFError:
			pass
		except KeyboardInterrupt:
			pass
		except OSError: #TODO: add note in files
			if logger: traceback.print_exc()
			leach_logger(log(['0807x-1', f_code, port, cd]))

	def run_server_t(self, server_status, cd='.'):  # fc=0808 v
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

		if config.server_status:
			return

		port = config.running_port  # user specified port or proxy port

		_t = self.run_server(port=port, cd=cd)
		if _t != 0:
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

	def run_in_local_server(self, port, host_dir=''):  # fc=0809
		"""opens a directory or a file in localhost server using browser

		args:
		-----
			port : port number
			host_dir : desired file or folder directory"""

		if config.sp_arg_flag['no browser']: return 0

		webbrowser.open_new_tab('http://localhost:%i/%s' % (port, host_dir))

	def check_server(self, link, f_code, timeout=None):  # fc=080A
		"""Checks if localhost server is running perfectly or the port is occupied

		link: site link with port [adds /root?response on request]
		f_code: caller id
		timeout: request timeout
		"""

		try:
			response = requests.get(link + '/root?response')
			if response:
				if response.content.startswith(b'Web-leach'):
					return True  # web-leach server
				else:
					leach_logger(log(['080Ax2', link, f_code, response.status_code, response.text[:20]]))
					return False  # not web-leach server or older server

			else:
				leach_logger(log(['080Ax3', link, f_code, response.status_code]))
				return False  # not web-leach server

		except (requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError,
		        urllib3.exceptions.SSLError) as e:
			leach_logger(log(['080Ax1', link, f_code, e.__class__.__name__, e]))
			return 2

		except requests.exceptions.ConnectionError:
			return None  # port is open

		except EOFError:
			return 2
		except KeyboardInterrupt:
			return 2

		except Exception as e:
			leach_logger(log(['080Ax0', link, f_code, e.__class__.__name__, e]))
			return 2

	def remove_noscript(self, content):  # fc=080B
		"""Removes <noscript> contents from html to fool my app

		content: HTML content returned by requests.get().content or requests.get().text"""
		if isinstance(content, bytes):
			if b'<noscript>' in content:
				return re_sub(b"(?i)(?:<noscript>)(?:.|\n)*?(?:<\/noscript>)", b'', content)
		elif isinstance(content, str):
			if '<noscript>' in content:
				return re_sub("(?i)(?:<noscript>)(?:.|\n)*?(?:<\/noscript>)", '', content)

		return content

	def gen_link_facts(self, link):  # fc=080C
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

			facts['has homepage'] = (facts['homepage'] is not None)
			facts['after homepage'] = link.startswith('/')
			facts['needs scheme'] = link.startswith('//')
			facts['is absolute'] = (facts['scheme'] is not None and facts['host'] is not None)

			CachedData.cached_link_facts[link] = facts
			return facts

		else:
			return None

		# self.link_extractor = re_compile( r'^(?P<noQuery>(?P<schema>((?P<scheme>[^:/?#]+):(?=//))?(//)?)(((?P<login>[^:]+)(?::(?P<password>[^@]+)?)?@)?(?P<host>[^@/?#:]*)(?::(?P<port>\d+)?)?)?(?P<path>[^?#]*))(\?(?P<query>[^#]*))?(#(?P<fragment>.*))?')	# compiled regex tool for getting homepage
		# https://regex101.com/r/UKWPmt/1
		# noQuery: https://regex101.com/r/UKWPmt/1
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

	
	def get_page(self, link=None, referer=False, header=None, cache=False, failed=False, do_not_cache=True,
	            session=None, return_none=True, raise_error=False):  # fc=080D
		"""Gets a page from the internet and returns the page object

		link: page link
		referer: page referer, default = self.main_link, None means don't use referer
		header: header string
		cache: get or store the page object from Cached_data.cached_webpages by calling Cached_data.get_webpage or Cached_data.add_webpage
		failed: if failed in previous try
		do_not_cache: if True, don't cache the page object to file
		session: if requests.session is avaialbe
		return_none: if True, return None if page is not found, else return the page object
		raise_error: if True, raise an error if an Error occured while getting the page"""

		def retry():
			return self.get_page(link=link, referer=False if referer == False else referer, cache=cache, failed=True,
										do_not_cache=do_not_cache, session=session, return_none=return_none, raise_error=raise_error)

		if cache:
			if link in CachedData.cached_webpages:
				__x = CachedData.get_webpage(link)
				# print(__x)
				if __x is not None:
					return __x

		if session is None:
			session = requests

		if not referer:
			referer_ = Netsys.get_homepage(link)
		else:
			referer_ = referer

		if header is None:
			current_header = Netsys.header_(referer_)
		else:
			current_header = header
			
		page = None
		try:
			page = session.get(link, headers=current_header, timeout=5)
			if not page:
				if not failed:
					page = retry()
				else:
					if return_none:
						return None
					else:
						return page
		except NetErrors as e:
			if not failed:
				page = retry()
			else:
				if raise_error:
					raise e
				else:
					return None

		if cache and page:
			if not do_not_cache:
				CachedData.add_webpage(link, page)
		return page
	def link_downloader(self, link, file_loc, filename, server_error_code, internet_error_code, overwrite, err_print=True, allow_old=True, proxy=[]):  # fc=080E
		"""
		Just to keep the code clean
			link: link to download
			file_loc: location to save file
			filename: name of file
			server_error_code: error code when server returns error (>200 code)
			internet_error_code: error code when internet is not working
			overwrite: if file is already there, overwrite it
			err_print: if error should be printed
			allow_old: if old file is allowed to be used when failed to download
			proxy: list of proxy links
		"""

		try:
			# check if the proxy link is a list or string, usable or not.
			if isinstance(proxy, str):
				proxy = [proxy]
			elif not isinstance(proxy, list):
				proxy = list(proxy)

			proxy.insert(0, link) # add link to top of proxy list
		except:
			# invalid proxy type is ignored
			proxy = [link]


		self.current_header = Netsys.header_()
		returner = True
		try:
			if not overwrite and  os_isfile(file_loc + filename):
				return True

			for link in proxy:
				file = self.get_page(link, header=self.current_header, cache=False, raise_error=True, return_none=False)
				if file:
					break
			if file:
				Fsys.writer(filename, 'wb', file.content, file_loc, '0306')
				return True
			else:
				leach_logger(log([server_error_code, Netsys.hdr(self.current_header, '080D'), link, file.status_code]), 'lock')
				if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%server_error_code)
				returner = False
		except NetErrors as e:
			if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%internet_error_code)
			leach_logger(log([internet_error_code, Netsys.hdr(self.current_header, '080D'), link, e.__class__.__name__, e]), 'lock')
			returner = False

		if not returner and allow_old:
			return os_isfile(file_loc + filename)



Netsys = Netsys_()

print(9)  # x


class Datasys_ :  # fc=0900
	"""Data types and conversion functions"""

	def remove_duplicate(self, seq, return_type=list):  # fc=0901 v
		"""removes duplicates from a list or a tuple
		also keeps the array in the same order

		args:
		-----
			seq: `tuple`|`list` to remove dups
			return_type: type of array to return"""

		return return_type(dict.fromkeys(seq))

	def remove_non_ascii(self, text, f_code='????'):  # fc=0902 v
		"""[DEPRECATED] [STILL WORKS] removes ascii characters from a string

		args:
		-----
			test: text to remove non ASCII
			f_code: The function Code called this function"""

		try:
			return ''.join([i if ord(i) < 128 else '' for i in text])
		except Exception as e:
			xprint("Failed to remove non-ascii characters from string.\nError code: 00003x", f_code, '\nPlease inform the author.')
			leach_logger(log(['0902x0', text, e.__class__.__name__, e]))

	def remove_non_uni(self, text, f_code='????', types='str', encoding='utf-8'):  # fc=0903 v
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
				if types == 'bin':
					return text
				return text.decode(encoding)
			if types == 'bin':
				return text.decode(encoding, 'ignore').encode(encoding)
			return text.decode(encoding, 'ignore')
		except Exception as e:
			xprint("/r/Failed to remove non-Unicode characters from string.\nError code: 00018x", f_code, '/y/\nPlease inform the author./=/')
			leach_logger(log(['0903x0', text, types, encoding,  e.__class__.__name__, e]))
			return self.remove_non_ascii(text, f_code)

	def trans_str(self, txt, dicts):  # fc=0904 v
		"""replaces all the matching characters of a string for multiple times

		args:
		-----
			txt: string data
			dicts: dict of { find : replace }"""

		for i in dicts.keys():
			a = dicts[i]
			for j in i:
				txt = txt.replace(j, a)
		return txt

	def flatten2D(self, arr):  # fc=0905
		functools_reduce(operator_iconcat, arr, [])

	def is_json(self, data=None, raise_=False): # fc=xxxx
		if isinstance(data, (io.TextIOBase,
		io.BufferedIOBase,
		io.RawIOBase,
		io.IOBase)):
			func = json.load
		elif isinstance(data, (str, bytes)): 
			func = json.loads
		else:
			return False
		try:
			func(data)
			return True
		except Exception as e:
			# if logger: traceback.print_exc()
			if raise_: raise e
			return False
	


Datasys = Datasys_()

print(10)  # x


class SupportTools_ :  # fc=0A00
	""" support tools for special sites
	Supported:
		webtoon
		nhentai | with multiple proxies
		mangafreak
	"""

	def check_sp_links(self, link, sp=None):  # fc=0A01
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
			if re_search('^' + Constants.special_starts['nh'], link) is not None:
				return True
			else:
				return False
		elif sp == "mangafreak":
			if re_search('^' + Constants.special_starts['mangafreak'], link) is not None:
				return True
			else:
				return False
		elif sp == "pinterest":
			if re_search('^' + Constants.special_starts['pinterest'], link) is not None:
				return True
			else:
				return False
		elif sp == "pinterest-pin":
			if re_search('^' + Constants.special_starts['pinterest'] + 'pin/\d+$', link) is not None:
				return True
			else:
				return False
		elif sp == 'webtoon':
			if re_search('^' + Constants.special_starts['webtoon'], link) is not None:
				return True
			elif re_search('^' + Constants.special_starts['webtoon_ep'], link) is not None:
				return True
			else:
				return False
		elif sp is None:
			for i in Constants.special_starts.values():
				if re_search('^' + i, link) is not None:
					return True
			return False
		else:
			xprint("/u/INvalid arg!/=/\n    pLEaSe REcHECK\n=======> %s <=======\n WITH\n-------> %s <-------"%(link, str(sp)))
			raise ValueError

	def play_yamatte(self, vol=80):  # fc=0A02
		"""just for parody"""
		if os_name == 'Windows':
			link = random_choice(Constants.yamatte)
			try:
				x = requests.get(link, headers=Netsys.header_())
				if not x:
					leach_logger(log(['0A02', '1', link, x.status_code]))
					return 0
			except NetErrors as e:
				leach_logger(log(['0A02', '2', link, e.__class__.__name__, e]))
				return 0

			Fsys.writer('yamatte.mp3', 'wb', x.content, AboutApp.temp_dir, '0A02')
			ex = mplay4.ex_vol
			mplay4.set_win_vol(vol)
			mplay4.load(AboutApp.temp_dir + 'yamatte.mp3').play()
			time.sleep(8)
			remove(AboutApp.temp_dir + 'yamatte.mp3')
			mplay4.set_win_vol(ex)
		else:
			pass

	play_yamatte_t = Process(target=play_yamatte, args=(80,))


SupportTools = SupportTools_()


class All_list_type :  # fc=0B00
	""" Data structure for all lists """

	def __init__(self, dir_len, all_links=None, all_names=None):  # fc=0B01
		self.dir_len = dir_len
		self.dir_height = [0 for _ in range(dir_len)]
		self.all_names = [[] for _ in range(dir_len)]
		self.link_len = 0
		
		#print(len(all_names))

		# self.gen_temp(dir_len)
		self.all_links = []
		if all_links is not None:
			if len(all_links) == 0:
				pass
			if len(all_links[0]) < 3:
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
		
	def update_values(self):
		self.dir_height = [len(self.all_names[i]) for i in range(self.dir_len)]

	def _2to3(self, all_links):  # fc=0B02
		""" convert old < v6 all_list [[link, dir_index]] based to new
			all_list [[link, dir_index, name_index]] """

		for i in range(len(all_links)):
			self.add_link(all_links[i][0], all_links[i][1])

	def __str__(self):  # fc=0B03
		return 'All_list_type{dir_len: %i,\n\nall_links: %s,\n\n all_names: %s}' % (
			self.dir_len, self.all_links, self.all_names)

	def __repr__(self):  # fc=0B04
		return 'All_list_type(dir_len=%i,\n\nall_links=%s,\n\n all_names=%s)' % (
			self.dir_len, self.all_links, self.all_names)

	def __getitem__(self, index):  # fc=0B05
		"""returns the values of the index of all_list
		index: index of all_list
		returns:
			0: link
			1: dir_index
			2: file name
		"""
		return (self.all_links[index][0], self.all_links[index][1],
		        self.all_names[self.all_links[index][1]][self.all_links[index][2]])

	def __setattr__(self, name, value):
		if name == 'all_links':
			self.link_len = len(value)
		
		self.__dict__[name] = value
		


	def __len__(self):  # fc=0B06
		return self.link_len

	def __iter__(self):  # fc=0B07
		self.iter_dex = 0
		return self

	def __next__(self):  # fc=0B08
		while self.iter_dex < self.link_len:
			key = self.iter_dex
			self.iter_dex += 1
			# print(1,self.all_links[key][0],)
			# print(2,self.all_links[key][1],)
			# print(3, [self.all_links[key][1]], [self.all_links[key][2]])
			return (self.all_links[key][0], self.all_links[key][1],
			        self.all_names[self.all_links[key][1]][self.all_links[key][2]])
		raise StopIteration

	def __sizeof__(self):  # fc=0B0S
		xprint("/h/This process may take a second")
		in_list = 0
		for i in self.all_links:
			in_list += getsizeof(i)

		for i in self.all_names:
			in_list += getsizeof(i)

		for i in self.dir_height:
			in_list += getsizeof(i)
		return (getsizeof(self.all_links) + getsizeof(self.all_names) + getsizeof(self.dir_height) +
		        getsizeof(self.dir_len) + getsizeof(self.link_len) + in_list)

	def name_len(self):  # fc=0B09
		return sum(self.dir_height)

	def add_link(self, link, dir_indx, name=None, ext=None):  # fc=0B0A
		""" Add a link to the all_list and also sets its name
		link: link to add
		dir_indx: index of the directory
		name: name of the file (optional) """

		if name is not False:
			if name is None:
				name_dex = self.add_name(Fsys.get_file_name(link, 'url'), dir_indx, ext=ext)
			else:
				name_dex = self.add_name(name, dir_indx, ext=ext)
		
		else:
			name_dex = 0

		self.all_links.append([link, dir_indx, name_dex])
		self.dir_height[dir_indx]+=1
		self.link_len+=1

	def add_name(self, name, dir_indx, link_dex=None, ext=None):  # fc=0B0B
		""" Add a name to the all_names
		name: name to add
		dir_indx: index of the directory
		link_dex: index of the link (optional) """

		name = Datasys.trans_str(name, {'/\\|:*><?': '-',
		                                '"': "'",
		                                "\n\t\r": " "})

		name = name.strip()

		if len(name) > config.file_limit:
			name = re_sub('\s{2,}', ' ', name)

		if len(name) > config.file_limit:
			name = name[:config.file_limit - 3] + '...'

		if ext is None: ext = ''
		name = name + ext

		if name not in self.all_names[dir_indx]:
			self.all_names[dir_indx].append(name)

		else:
			name_, _, ext_ = name.rpartition('.')
			n = 1

			# X = ''.join((name_, '(', str(n), ')', '.', ext_))

			for i in range(len(self.all_names[dir_indx]) - 1, 0, -1):
				if self.all_names[dir_indx][i].startswith(name_ + '(') and self.all_names[dir_indx][i].endswith(
						')' + '.' + ext_):
					if self.all_names[dir_indx][i][len(name_) + 1:-len(ext_) - 2].isdigit():
						n = int(self.all_names[dir_indx][i][len(name_) + 1:-len(ext_) - 2]) + 1
					name = ''.join((name_, '(', str(n), ')', '.', ext_))

					if name not in self.all_names[dir_indx]:
						break
				n += 1

			self.all_names[dir_indx].append(name)

		return self.dir_height[dir_indx]

	def get_name(self, index):  # fc=0B0C
		""" Get the name of the link index
		index: index of the link
		"""
		return self.all_names[self.all_links[index][1]][self.all_links[index][2]]

	def update_name(self, name, dir_indx, name_indx, ext=None):  # fc=0B0D
		""" Update the name of a link
		name: new name
		dir_indx: index of the directory
		name_indx: index of the name """

		if ext is None: ext = ''
		name = name + ext

		if self.all_names[dir_indx][name_indx] == name:
			return 0

		if name not in self.all_names[dir_indx]:
			self.all_names[dir_indx][name_indx] = name

		else:
			name_, _, ext_ = name.rpartition('.')
			n = 1

			# X = ''.join((name_, '(', str(n), ')', '.', ext_))

			for i in range(len(self.all_names[dir_indx]) - 1, 0, -1):
				if self.all_names[dir_indx][i].startswith(name_ + '(') and self.all_names[dir_indx][i].endswith(')' + '.' + ext_):
					if self.all_names[dir_indx][i][len(name_) + 1:-len(ext_) - 2].isdigit():
						n = int(self.all_names[dir_indx][i][len(name_) + 1:-len(ext_) - 2]) + 1
					name = ''.join((name_, '(', str(n), ').', ext_))

					if name not in self.all_names[dir_indx]:
						break
				n += 1

			self.all_names[dir_indx][name_indx] = name

	def generate(self, all_links, Name=None):  # fc=0B0E
		""" Generate the all_list from a list of links (previously generated)
		all_links: list of links
		Name: name of the file (optional and available from v6+) """
		if Name is None or all(not i for i in Name):
			for i in range(len(all_links)):
				self.add_link(all_links[i][0], all_links[i][1])
		else:
			for i in range(len(all_links)):
				self.add_link(all_links[i][0], all_links[i][1], Name[all_links[i][1]][all_links[i][2]])
				
	def get_all_list(self, sort_by_name = False, sort_by_link = False):
		"""create a list of lists based on directories like all_names"""
		all_links = [
				[j for j in range(self.dir_height[i])
			] for i in range(self.dir_len)]
			
		name_ids = [
				[j for j in range(self.dir_height[i])
			] for i in range(self.dir_len)]
			
		
			
		for i in range(self.link_len):
			link, dir_id, name_id = self.all_links[i]
			all_links[dir_id][name_id] = link


		if sort_by_name:
			for i in range(self.dir_len):
				name_serial = natsort.index_natsorted(self.all_names[i])
				
				all_links[i] = natsort.order_by_index(all_links[i], name_serial)
				
		if sort_by_link:
			for i in range(self.dir_len):
				all_links[i] = natsort.natsorted(all_links[i])
				
		return all_links
		


	def clear_temp(self):  # fc=0B0F
		""" Clear the temp list """
		self.dir_height = [0 for _ in range(self.dir_len)]

	def gen_temp(self, dir_len=None):  # fc=0B0G
		""" Generate the temp list
		dir_len: length of the directory list """
		if dir_len is None:
			dir_len = self.dir_len
		if hasattr(self, 'all_names'):
			self.dir_height = [len(self.all_names[i]) for i in range(dir_len)]
		else:
			self.dir_height = [0 for _ in range(dir_len)]

	def _3to2(self):  # fc=0B0H
		""" Convert from version 3 to version 2 """
		return [[i, j] for i, j, k in self.all_links]

	def remove_duplicates(self):  # fc=0B0I
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

	def __del__(self):  # fc=0B0J
		self.all_links.clear()
		self.all_names.clear()
		self.dir_height.clear()


class CachedData_ :  # fc=0C00
	def __init__(self):  # fc=0C01
		self.data_vars = ("cached_webpages", "cached_link_facts")
		self.cached_webpages = dict()
		self.cached_link_facts = dict()

	def add_webpage(self, url, response):
		""" Add a webpage to the cache
		url: url of the webpage 
		response: response object"""

		# TODO: use JSON

		__x = Cached_Response(status_code=response.status_code, headers=response.headers, content=response.content,
		                      encoding=response.encoding, url=response.url)
		file_id = str(process_id) + '-' + uuid.random()
		with open(AboutApp.cached_webpages_dir + file_id, 'w') as f:
			f.write(repr(__x))
		self.cached_webpages[url] = file_id

	def get_webpage(self, url):
		""" Get a webpage from the cache
		url: url of the webpage """

		if url in self.cached_webpages:
			if os_isfile(AboutApp.cached_webpages_dir + self.cached_webpages[url]):
				with open(AboutApp.cached_webpages_dir + self.cached_webpages[url], 'r') as f:
					__x = eval(f.read()) # TODO: remove it. use JSON
				return __x

		return None

	def clean_cached_webpages(self):
		""" Cleans the cached_webpages from storage"""
		for i in os_listdir(AboutApp.cached_webpages_dir):
			if i.startswith(str(process_id) + '-'):
				try:
					remove(AboutApp.cached_webpages_dir + i)
				except:
					pass

	def clear(self):
		"""Cleans both from memory and storage""" 
		self.clean_cached_webpages()
		for i in self.data_vars:
			self.__dict__[i].clear()


CachedData = CachedData_()


print(11)  # x


class ProjectType_ :  # fc=0P00
	def __init__(self, project_name):  # fc=0P01
		"""initialize variables on every start of a project"""
		self.Project = project_name  # project name (case insensitive *need to work on it)
		self.__default__()

	def __default__(self):  # fc=0P02
		"""set default values on every start of a project"""
		self.total = 0  # number of total files
		self.break_all = False  # trigger to stop the download
		self.done = 0  # total downloaded files
		self.errors = 0  # number or errors
		self.index_failed = 0  # number or errors in indexing
		self.sp_extension = ''  # if custom file extension needed to be added with the downloaded file names
		self.sp_flags = set()  # set of flags for special downloads like mangafreaks
		self.overwrite_bool = True  # bool for whether replace the duplicate file or not
		self.partial_do_all = False  # will use the same detected homepage for every other pages with no home
		"""if partial link found while indexing, then the program will find the
		homepage and ask if it will be used for all other partial links or not"""


		### Defaults
		self.proj_good = None
		self.list_good = None
		self.from_file = False  # if the project was loaded from file
		self.list_file = None  # the .wllist file (need to clean it)
		self.proj_file = None  # the .wlproj file (need to clean it)
		self.proj_ext = ('.wlproj', '.wllist')  # data's file extensions
		self.homepage = ''  # just assigning the homepage variable
		self.indx_count = 0  # counts the number of indexed links
		self.existing_found = False  # indicates if valid existing project is found
		self.dl_done = False  # indicates if the project scrapping was done or not
		self.index_done = False  # indicates if the indexing was done or not
		self.has_missing = None  # indicates if the Project has any missing files. {5.4 and above}
		# * this won't ask input * so add it in GUI
		self.file_to_sort = False  # indicates if the images should be sorted or not
		self.dir_sorted = True  # will sort directories by name
		self.corruptions = []  # list of corruptions in project data if there's any or empty
		self.sub_dirs_count = 0  # number of sub directories named in the project data

		### Project creation data
		self.first_created = '0'  # Nsys.cdt_() of the time when the project was first created
		self.last_update = '0'  # Nsys.cdt_() of the time when the project was last modified
		self.leacher_version = AboutApp._VERSION  # version of the scrapper
		self.server_version = config.server_version  # version of the server while scrapping
		self.user_ip = UserData.user_ip  # user's ip address
		self.all_names = [] #To load data
		self.magic_number = 0

		### Need input
		self.main_link = None  # the main link
		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""
		self.link_startswith = ''  # (str) each sublink must start with
		self.file_types = []  # file types to be downloaded, list
		self.file_starts = ''  # (str) each files must start with (used regex)
		self.file_exts = []  # (list) (list of file extensions) each files must end with
		self.check_links = False  # if True, the list_writer_img checks the <a> for images
		self.update = False  # indicates if the project is getting an update or not


		### after list writer
		self.sub_dirs = []  # list of sub directories on the project folder
		self.sub_links = []  # needed in requests.get() reference value (fixes many issues)
		self.all_list = All_list_type(10)  # assigning a list of data links, but duplicates will be cancelled in process
		self.need_2_gen_names = True  # indicates if the names of files needs to be generated

		### directories
		self.download_dir = None  # project directory
		self.data_dir = None  # data directory
		self.threads_dir = None  # threads directory
		self.get_html_title = False  # indicates if the program should get the html title or not


		### indexing
		self.page_error = 0  # number of errors in indexing

		### after distribute
		self.error_triggers = []  # 0 to 9 the number of tasks
		self.dl_chunks = 0  # number of downloaded chunks
		self.re_error = 0  # number of errors after retrying errors
		self.error_links = []  # list of failed download links
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
		self.dl_threads = 10  # number of download threads
		self.index_threads = 3  # number of indexing threads

	def set_directories(self):  # fc=0P03
		"""Set important directories for the project
		self.download_dir: Download directory
		self.data_dir: *.wlproj directory
		self.threads_dir: directory where downloaded threads data are stored
		"""

		self.download_dir = AboutApp.download_dir + self.Project + '/'
		self.data_dir = AboutApp.leach_projects + self.Project + '.wlproj'
		self.threads_dir = AboutApp.thread_data_dir + self.Project + '/'
		
	def store_current_data(self): #fc=????
		# patch self.first_created issue
		if self.first_created in ('0', 'False'):
			self.first_created = Nsys.cdt_()

		if self.last_update in (0, "0", "False", False):
			self.last_update = Nsys.cdt_()
		

		# patch
		if self.file_exts == Constants.all_image_types:
			self.file_exts = []

		class SetEncoder (json.JSONEncoder):
			def default(self, obj):
				if isinstance(obj, set):
					return list(obj)
				return json.JSONEncoder.default(self, obj)

		dataset= {"Project": self.Project,
		'main_link': self.main_link,
		 'link_startswith': self.link_startswith, 
		 'file_starts': self.file_starts,
		 'sp_flags': self.sp_flags,
		 'sp_extension': self.sp_extension,
		 'overwrite_bool': self.overwrite_bool,
		 'dimention': self.dimention,
		 'file_to_sort':self.file_to_sort,
		 'dir_sorted': self.dir_sorted,
		 'file_types': self.file_types,
		 'dl_threads': self.dl_threads,
		 'first_created': self.first_created, 
		 'last_update': Nsys.cdt_(),
		 'leacher_version': AboutApp._VERSION,
		 'magic_number': Nsys.compressed_ip(UserData.user_ip["ip"]),
		 'server_version': config.server_version,
		 'get_html_title': self.get_html_title,
		 'dl_done': self.dl_done,
		 'has_missing': self.has_missing,
		 'file_exts': self.file_exts,
		 'sub_links': self.sub_links,
		 'sub_dirs': self.sub_dirs,
		 'all_names': self.all_list.all_names
		}
		
		json_proj = json.dumps(dataset, cls=SetEncoder, indent=4)
		json_list = json.dumps({"all_list": self.all_list.all_links}, cls=SetEncoder, indent=4)
		
		# clean the files if exist
		Fsys.writer(self.Project + '.wllist', 'w', '', AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'w', '', AboutApp.leach_projects, '0M05')

		# write new data
		Fsys.writer(self.Project + '.wllist', 'w', json_list, AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'w', json_proj, AboutApp.leach_projects, '0M05')
		del json_proj, json_list
		

	def store_current_data_old(self): # fc=????
		
		# clean the files if exist
		Fsys.writer(self.Project + '.wllist', 'w', '', AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'w', '', AboutApp.leach_projects, '0M05')

		# patch self.first_created issue
		if self.first_created in ['0', 'False']:
			self.first_created = Nsys.cdt_()

		if self.last_update == 0:
			self.last_update = Nsys.cdt_()


		# write new data
		Fsys.writer(self.Project + '.wllist', 'w', str(self.all_list.all_links), AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'w', 'main_link= "%s"\n' % self.main_link, AboutApp.leach_projects,
		            '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'link_startswith= "%s"\n' % self.link_startswith,
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'file_types = %s\n' % str(self.file_exts),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'file_starts= "%s"\n' % self.file_starts,
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'sub_dirs = %s\n' % str(self.sub_dirs), AboutApp.leach_projects,
		            '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'sp_flags = %s\n' % str(self.sp_flags), AboutApp.leach_projects,
		            '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'sp_extension = "%s"\n' % self.sp_extension,
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'overwrite_bool = %s\n' % str(self.overwrite_bool),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'dimention = %s\n' % str(self.dimention),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'sequence = %s\n' % str(self.file_to_sort),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'Project = "%s"\n' % str(self.Project), AboutApp.leach_projects,
		            '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'sub_links = %s\n' % str(self.sub_links),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'dir_sorted = %s\n' % str(self.dir_sorted),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'all_names = %s\n' % str(self.all_list.all_names),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'file_formats = %s\n' % str([self.file_types]),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'dl_threads = %s\n' % str(self.dl_threads),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', 'first_created = "%s"\n' % str(self.first_created),
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'last_update = "{Nsys.cdt_()}"\n', 
					AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'leacher_version = "{AboutApp._VERSION}"\n',
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'magic_number = "{Nsys.compressed_ip(UserData.user_ip["ip"])}"\n',
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'server_version = "{config.server_version}"\n',
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'get_html_title = {self.get_html_title}\n',
		            AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'dl_done = {self.dl_done}\n',
					AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'a', f'has_missing = {self.has_missing}\n',
					AboutApp.leach_projects, '0M05')
					
					
	def load_data(self, file_dir):
		new = True
		file_dir = file_dir.replace('"', '')
		if file_dir.endswith("'") and file_dir.startswith("'"):
			file_dir = file_dir[1:-1]

		if file_dir.endswith('.proj'):
			new=False			
		

		if new and not self.from_file:
			if os.path.isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				pass
			elif os.path.isfile(AboutApp.leach_projects + self.Project + '.proj'):
				new = False

			else:
				self.__default__()
				return False

		else:
			return self.load_old_data(file_dir)
			
		
		proj_path = AboutApp.leach_projects + self.Project + self.proj_ext[0]

		list_path = proj_path[:-len(self.proj_ext[0])] + self.proj_ext[1]


		if os_exists(proj_path):
			self.proj_good = True
			self.proj_file = Fsys.reader(proj_path, 'r', True).strip()

			if not new or not Datasys.is_json(self.proj_file):
				return self.load_old_data(file_dir)
		else:
			return False
	
		try:
			loaded_data_set = json.loads(self.proj_file)
			
			for keys in loaded_data_set.keys():
				self.__setattr__(keys, loaded_data_set[keys])

			self.sp_flags = set(self.sp_flags)

			
			self.all_list = All_list_type(len(self.sub_dirs))

			
			if any(self.all_names):
				self.all_list.all_names = self.all_names
				self.all_list.update_values()
				self.all_names = [] # reset coz there's no further use of it
				self.need_2_gen_names = False

			self.last_user_ip = Nsys.dec_ip(self.magic_number)

			self.dir_sorted = True  # loaded_data_set['dir_sorted'] ## need to fix
			self.has_missing = loaded_data_set['has_missing']

			_temp = loaded_data_set['first_created']
			self.first_created = '0' if _temp in ['False', '0'] else _temp
			
			del _temp

			
			proj_good = True

		except:
			if logger: traceback.print_exc()
			
			self.corruptions += ["J"]
			xprint('/rh/Corrupted Data! Error code: 601xJ/=/') # fc = xxxx 601xJ json issue
			return False


		try:
			self.list_file = Fsys.reader(list_path, 'rb', True, 'str')
			_list_json = json.loads(self.list_file)["all_list"]
			if self.need_2_gen_names:
				xprint('/uh/Generating Names.../=/')
				self.all_list.generate(_list_json)
			else:
				self.all_list.all_links = _list_json
			del _list_json
			self.list_file=True
			self.proj_file=True
			self.list_good = True

			
			self.set_directories()


			return True
		except:
			if logger: traceback.print_exc()
			
			return False
			
			
	def load_old_data(self, file_dir):  # fc=0P04
		"""loads the data from the project file
			returns: None if failed to load file
					False if there is no project file"""

		file_dir = file_dir.replace('"', '')
		if file_dir.endswith("'") and file_dir.startswith("'"):
			file_dir = file_dir[1:-1]

		if file_dir.endswith(('.proj', '.wlproj')) and os.path.isfile(file_dir):
			self.from_file = file_dir
			proj_path = file_dir

			if file_dir.endswith('.proj'):
				self.proj_ext = ('.proj', '.list')
				

		if not self.from_file:
			if os.path.isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				pass
			elif os.path.isfile(AboutApp.leach_projects + self.Project + '.proj'):
				self.proj_ext = ('.proj', '.list')

			else:
				self.__default__()
				return False

			proj_path = AboutApp.leach_projects + self.Project + self.proj_ext[0]

		list_path = proj_path[:-len(self.proj_ext[0])] + self.proj_ext[1]


		if os_exists(proj_path):
			self.proj_good = True

			self.proj_file = Fsys.reader(proj_path, 'rb', True, 'str').strip()

			self.proj_good = self.check_old_proj_file()

			if self.proj_good:

				if os_exists(list_path):
					self.list_file = Fsys.reader(list_path, 'rb', True, 'str').strip()
					self.list_good = self.check_old_list_file()

					self.set_directories()
					if self.list_good:
						# print(getsizeof(self.all_list))
						self.store_current_data()
						return self.list_good

		self.__default__()
		return None

	def check_old_proj_file(self):  # fc=0P05
		"""checks if the project file is valid
		and if valid assigns the data to Class"""

		proj_good = True
		try:
			loaded_data_set = dict()
			existing_data = self.proj_file.split('\n')

			for i in existing_data:
				exec(i, locals(), loaded_data_set)

			if any(i not in loaded_data_set for i in ['main_link', 'link_startswith', 'file_types']):
				raise ValueError

			self.main_link = loaded_data_set['main_link']
			self.link_startswith = loaded_data_set['link_startswith']
			self.file_starts = loaded_data_set['file_starts']
			self.sub_dirs = loaded_data_set['sub_dirs']
			self.sp_flags = set(loaded_data_set['sp_flags'])
			self.sp_extension = loaded_data_set['sp_extension']
			self.overwrite_bool = loaded_data_set['overwrite_bool']
			self.dimention = loaded_data_set['dimention']

			if 'dl_done' in loaded_data_set:
				self.dl_done = loaded_data_set['dl_done']

			if 'Project' in loaded_data_set:
				self.Project = loaded_data_set['Project']
			else:
				if self.from_file:
					self.Project = Fsys.get_file_name(self.Project)[:0 - (len(self.proj_ext[0]))]
			if 'sequence' in loaded_data_set:
				self.file_to_sort = loaded_data_set['sequence']

			if 'sub_links' in loaded_data_set:
				self.sub_links = loaded_data_set['sub_links']

			if 'dir_sorted' in loaded_data_set:
				self.dir_sorted = True  # loaded_data_set['dir_sorted'] ## need to fix

			if 'has_missing' in loaded_data_set:
				self.has_missing = loaded_data_set['has_missing']

			self.all_list = All_list_type(len(self.sub_dirs))

			if 'all_names' in loaded_data_set:
				__all_names__ = loaded_data_set['all_names']
				if any(i for i in __all_names__):
					self.all_list.all_names = __all_names__
					del __all_names__
				
					self.need_2_gen_names = False

			if 'file_formats' in loaded_data_set:
				self.file_types = loaded_data_set['file_formats']
				self.file_exts = loaded_data_set['file_types']
			else:
				self.file_types = loaded_data_set['file_types']

			if 'dl_threads' in loaded_data_set:
				self.dl_threads = loaded_data_set['dl_threads']

			if 'first_created' in loaded_data_set:
				_temp = loaded_data_set['first_created']
				self.first_created = '0' if _temp in ['False', '0'] else _temp

			if 'last_update' in loaded_data_set:
				self.last_update = loaded_data_set['last_update']

			if 'leacher_version' in loaded_data_set:
				self.leacer_version = loaded_data_set['leacher_version']
			

			if 'magic_number' in loaded_data_set:
				self.last_user_ip = Nsys.dec_ip(loaded_data_set['magic_number'])

			if 'get_html_title' in loaded_data_set:
				self.get_html_title = loaded_data_set['get_html_title']

			proj_good = True

		except:
			if logger: traceback.print_exc()

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
					self.sub_dirs = eval(existing_data[4])  # sub directory list
				except:
					proj_good = False
					xprint('/rh/Corrupted Data! Error code: 601x5/=/')
					self.corruptions += [2]
				try:  # added in v5.0 may not be in older files
					self.sp_flags = set(eval(existing_data[5]))
					self.sp_extension = eval(existing_data[6])
					self.overwrite_bool = eval(existing_data[7])
				except IndexError:
					pass
			if proj_good:
				try:  # added in v5.1 may not be in older files
					self.dl_done = eval(existing_data[8])
				except IndexError:
					pass
			if proj_good:
				self.all_list = All_list_type(len(self.sub_dirs))
				

		if self.file_types == Constants.old_img:
			self.file_types = ['img']
			# self.file_exts = Constants.all_image_types

		return proj_good

	def check_old_list_file(self):  # fc=0P06
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
				if self.need_2_gen_names:
					print('/uh/Generating Names.../=/')
					self.all_list.generate(eval(str(existing_data)))
				else:
					self.all_list.all_links = eval(str(existing_data))
				return True

			except:
				if logger: traceback.print_exc()
				return False

	def gen_sub_links(self):  # fc=0P07
		"""generates the sub links for the project"""

		xprint("Getting Mainpage", end='')
		sub_links2 = []
		sub_links = []
		if self.dimention == 1 or self.dimention == 3:
			sub_links2 += [self.main_link]
		if self.dimention == 2 or self.dimention == 3:
			page = Netsys.get_page(self.main_link, cache=True, do_not_cache=False)
			if not page:
				xprint("/r/Failed to download Main link/=//y/\n==Possible cause: /h/No internet/=/\n")
				return False
			xprint('.', end='')
			soup = bs(Netsys.remove_noscript(page.content), parser)

			# link_startswith = input("\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")
			# leach_logger('0M05x1||%s||l_starts||%s'%(self.Project, self.link_startswith), UserData.user_name)
			sub_links2 += Datasys.remove_duplicate([sub_link.get('href').strip() for sub_link in soup.find_all('a') if sub_link.get('href') is not None])
		#todo: add leach logger
		Ctitle('[Indexing] Project %s [%s%s] [:%i]'%(self.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

		link_startswith_re = re_compile('^' + self.link_startswith)

		self.homepage = Netsys.get_homepage(self.main_link)

		for i in sub_links2:
			i = Netsys.get_link(i, self.main_link, self.homepage)

			if link_startswith_re.search(i) is not None:
				sub_links.append(i)

		xprint('.')
		del sub_links2

		self.sub_links = Datasys.remove_duplicate(sub_links)

		self.sub_dirs = list('' for i in range(len(self.sub_links)))

		self.all_list = All_list_type(len(self.sub_links))

		del sub_links
		
		return True

	def update_sub_dirs(self, name, index):  # fc=0P0J
		"""Update the sub_dirs list with the new name
		
		name: the name of the sub_dir
		index: the index of the sub_dir in the list `sub_dirs`
		"""

		if len(self.sub_dirs) - 1 < index:
			self.sub_dirs += ['.'] * (index - (len(self.sub_dirs) - 1))

		if name.endswith(('.html', '.php', '.htm')):
			name = name.rpartition('.')[0]

		name = Datasys.trans_str(name, {'/\\|:*><?': '-',
		                                '"': "'",
		                                "\n\t\r": " "})

		name = name.strip()

		if len(name) > config.dir_limit:
			name = re_sub('\s{2,}', ' ', name)

		if len(name) > config.dir_limit:
			name = name[:config.dir_limit - 3] + '...'

		if name == self.sub_dirs[index]:
			return 0

		if name not in self.sub_dirs:
			self.sub_dirs[index] = name
		else:
			name_ = name

			for n in range(len(self.sub_dirs) - 1, 0, -1):
				try:
					if self.sub_dirs[n].startswith(name_ + '(') and self.sub_dirs[n][-1] == ')':
						if self.sub_dirs[n][len(name_) + 1:-1].isdigit():
							n = int(self.sub_dirs[n][len(name_) + 1:-1]) + 1
						name = ''.join((name_, '(', str(n), ')'))

						if name not in self.sub_dirs:
							break
				except Exception:
					traceback.print_exc()
				n += 1

			self.sub_dirs[index] = name

	def _gen_sub_dirs(self, part):  # fc=0P0K
		"""generates directory name from page title and stores the soup in CachedDatato reuse while indexing
		part: threading partition to speed up the process"""
		try:
			list_range = range(len(self.sub_links))[part::3]

			with requests.Session() as _session:

				for j in list_range:
					if self.break_all: return 0
					i = self.sub_links[j]
					__x = 0
					if self.get_html_title:
						page = Netsys.get_page(i, referer=self.main_link, cache=True, do_not_cache=False, session=_session)
						if page:
							soup = bs(Netsys.remove_noscript(page.content), parser)
							self.update_sub_dirs(html_unescape(soup.title.text).strip(), j)
							__x = 1

					if __x == 0:
						name = Fsys.get_dir(i, 'url')
						self.update_sub_dirs(name, j)
					IOsys.delete_last_line()

					self.sub_dirs_count += 1
					if self.break_all: return 0
					xprint("Getting pages [%i/%i]" % (self.sub_dirs_count, len(self.sub_links)))

		except EOFError:
			self.break_all = True
			raise LeachICancelError
		except KeyboardInterrupt:
			self.break_all = True
			raise LeachICancelError

	def gen_sub_dirs(self):  # fc=0P08
		"""Generates sub-directories|`self.sub_dirs`"""

		index_thread_list = [Process(target=self._gen_sub_dirs, args=(i,)) for i in range(self.index_threads)]

		try:

			for i in range(self.index_threads):
				index_thread_list[i].start()

			while any([i.is_alive() for i in index_thread_list]):
				if self.break_all:
					return False
				time.sleep(0.3)

			if self.dir_sorted:
				index = natsort.index_natsorted(self.sub_dirs)
				self.sub_dirs = natsort.order_by_index(self.sub_dirs, index)
				self.sub_links = natsort.order_by_index(self.sub_links, index)

			return True

		except EOFError:
			leach_logger(log(['000', '0P0K', self.Project, 'f-Stop', 'was generating sub_dir names', 'Indexing Stopped']))
			xprint("/yh/Project indexing cancelled by Keyboard/=/")
			self.break_all = True
			return 0
		except KeyboardInterrupt:
			leach_logger(log(['000', '0P0K', self.Project, 'f-Stop', 'was generating sub_dir names', 'Indexing Stopped']))
			xprint("/yh/Project indexing cancelled by Keyboard/=/")
			self.break_all = True
			return 0

		except LeachICancelError:
			leach_logger(log(['000', '0P0K', self.Project, 'f-Stop', 'was generating sub_dir names', 'Indexing Stopped']))
			xprint("/yh/Project indexing cancelled by Keyboard/=/")
			self.break_all = True
			return 0

	def speed_limiter(self):  # fc=0P09 v
		"""Limits download speed by arg
		`sp_arg_flag['max dlim']` in kbps"""

		if config.sp_arg_flag['max dlim'] == 0: return 0
		while not (self.dl_done or self.break_all):
			if self.current_chunks * config.sp_arg_flag["chunk_size"] > config.sp_arg_flag['max dlim']:
				if time.time() - self.tictoc < 1:
					_temp = 1 - (time.time() - self.tictoc)
					if _temp < 1:
						self.dl_nap_time = _temp
					self.tictoc = time.time()
					self.current_chunks = 0
				else:
					self.tictoc = time.time()
					self.current_chunks = 0
			time.sleep(0.05)

	def speed_tester(self):  # fc=0P0A
		"""Counts and prints download speed and
		shows download amount in thread"""

		last_chunks = 0
		while (not (self.dl_done or self.break_all)) or self.total == 0:
			_temp = self.dl_chunks
			self.current_speed = filesize_size((_temp - last_chunks) * config.sp_arg_flag['chunk_size'] * 2, filesize_alt)

			if self.break_all or self.total == 0: return 0
			percent = floor((self.done / self.total) * 30)
			IOsys.delete_last_line()
			sys_write(''.join(['Download [', '\u001b[32;1m', ('━'*percent), '\u001b[30;1m╺' if percent<30 else '━', '━'*(30-percent), '\u001b[0m][', str(self.done), '/', str(self.total), ']', self.current_speed , '/s\n']))
			time.sleep(.5)
			last_chunks = _temp

	def downloader(self, part, is_error=False, partitions=None):  # fc=0P0B
		if partitions is None:
			partitions = self.dl_threads

		global err_hdr_list
		task_id = str(part + 1)
		res = 0
		if self.existing_found:
			if os_exists(AboutApp.thread_data_dir + self.Project + '/t' + task_id + '.txt'):
				res = Fsys.reader(AboutApp.thread_data_dir + self.Project + '/t' + task_id + '.txt').strip()
				res = int(res) if res.isdigit() else 0  # resume point of the list (index # int)
		self.done += res

		session = requests.session()

		if is_error:
			lists = range(self.errors)
			timeout = 30
		else:
			lists = range(0, self.total)[part::partitions]
			timeout = 6

		time.sleep(1.2)  # to make sure other threads started safely and the restore points are calculated correctly

		for j in lists:

			if self.break_all: return 0

			if lists.index(j) < res: continue
			download = True  # switch for download it or not
			streaming = not is_error
			if 'ignore_on_null_content' in self.sp_flags or 'stop_on_null_content' in self.sp_flags:
				streaming = False


			if is_error:
				i = self.error_links[j]

			else:
				i = self.all_list[j]

			fname = i[2]
			fdir = self.sub_dirs[i[1]]
			flink = i[0]

			self.is_error = is_error

			if self.sub_links!=[]: # if sub_links are available, then use them as header referer
				current_header = Netsys.header_(self.sub_links[i[1]])
			else:
				current_header = Netsys.header_()  # randomizes header from list on every download to at least try to fool server


			try:
				if not self.overwrite_bool:
					if os_isfile(
						self.download_dir + fdir + '/' + fname + self.sp_extension):
							download = False
				if download:

					if config.sp_arg_flag['disable dl get']:
						file = session.head(flink, headers=current_header, timeout=timeout)
					else:
						file = session.get(flink, headers=current_header, timeout=timeout, stream=streaming)
					if 'stop_on_null_content' in self.sp_flags:  # do not save null files
						if len(file.content) == 0:
							break
					if 'ignore_on_null_content' in self.sp_flags:  # do not save null files
						if len(file.content) == 0:
							continue

					if file:
						if self.break_all: return 0

						if not config.sp_arg_flag['disable dl get']:
							if self.break_all: return 0
							try:
								Fsys.writer(fname + self.sp_extension, 'wb', b'', self.download_dir + fdir, '0P0B')
								loaded_file = open(self.download_dir + fdir + '/' + fname + self.sp_extension, 'wb')
							except IndexError:
								# TODO: something breaks the code here most of the time. FIX it.
								# NOTE: well not anymore, idk how

								xprint('\n/y/Something Went wrong, Returning to main Menu/=/\n')
								self.break_all = True
								return 0

							try:

								for chunk in file.iter_content(chunk_size=config.sp_arg_flag['chunk_size']):
									if config.sp_arg_flag['max dlim'] != 0:
										time.sleep(self.dl_nap_time)

									if self.break_all:
										loaded_file.close()
										if os_exists(self.download_dir + fdir + '/' + fname + self.sp_extension):
											remove(self.download_dir + fdir + '/' + fname + self.sp_extension)

										return 0

									loaded_file.write(chunk)
									self.dl_chunks += 1
									self.current_chunks += 1

								loaded_file.close()

							except (requests.exceptions.SSLError, urllib3.exceptions.SSLError):
								loaded_file.close()
								_temp = session.get(i[0], headers=current_header, timeout=timeout)
								if _temp: _temp = _temp.content
								else: raise requests.exceptions.ConnectionError
								Fsys.writer(fname + self.sp_extension, 'wb', _temp, self.download_dir + fdir, '0P0B')
								del _temp

							if 'dl unzip' in self.sp_flags:
								if not os_isdir(self.download_dir + fdir + '/' + fname + '/'):
									makedirs(self.download_dir + fdir + '/' + fname + '/')
								try:
									with ZipFile(self.download_dir + fdir + '/' + fname + self.sp_extension) as zf:
										zf.extractall(path=self.download_dir + fdir + '/' + os.path.splitext(fname)[0])
								except Exception as e:
									leach_logger(log(['0P0Bx3', self.Project, Netsys.hdr(current_header, '0P0B'), flink, fname, fdir, e.__class__.__name__, e]), UserData.user_name)

								if 'del dl zip' in self.sp_flags:
									remove(self.download_dir + fdir + '/' + fname + self.sp_extension)


						if self.break_all: return 0
						Fsys.writer('t' + task_id + '.txt', 'w', str(res), AboutApp.thread_data_dir + self.Project, '0P0B')

						res += 1
						self.done += 1
						if is_error:
							self.errors -= 1

					else:
						if not is_error:
							Fsys.writer('errors.wlerr', 'a', str(i + (Netsys.hdr(current_header, '0P0B'),)) + '\n', AboutApp.leach_projects + self.Project, '0P0B')
							err_hdr_list += Counter([Netsys.hdr(current_header, '0P0B')])
							Fsys.writer('err_header.txt', 'w', str(err_hdr_list), AboutApp.data_dir, '0P0B')
							self.errors += 1

						else:
							self.re_error += 1
							if self.re_error == 1: IOsys.delete_last_line()
							IOsys.delete_last_line()
							if self.re_error < 4:
								print("Failed to download from '%s'\n\n" % i[0])
							else:
								if self.re_error != 4: IOsys.delete_last_line()
								print("And %i others" % (self.re_error - 3))
							Fsys.writer('left_errors.txt', 'a',
							            str(i + (Netsys.hdr(current_header, '0P0B'), "Error dl")) + '\n',
							            AboutApp.leach_projects + self.Project, '0P0B')
							leach_logger(
								log(['0P0Bx1', self.Project, Netsys.hdr(current_header, '0P0B'), flink, fname, fdir,
								     file.status_code, '']), UserData.user_name)

							continue

						res += 1

				else:
					Fsys.writer('t' + task_id + '.txt', 'w', str(res), AboutApp.thread_data_dir + self.Project, '0P0B')

					res += 1
					self.done += 1
					if is_error:
						self.errors -= 1

			except NetErrors as e:
				# traceback.print_exc()
				# print(flink)
				if not is_error:
					Fsys.writer('errors.wlerr', 'a', str(i + (Netsys.hdr(current_header, '0P0B'),)) + '\n',
					            AboutApp.leach_projects + self.Project, '0P0B')

					
					leach_logger(log(['0P0Bx2', self.Project, Netsys.hdr(current_header, '0P0B'), flink, fname, fdir,
					                  e.__class__.__name__, e]), UserData.user_name)
			

					err_hdr_list += Counter([Netsys.hdr(current_header, '0P0B')])
					Fsys.writer('err_header.txt', 'w', str(err_hdr_list), AboutApp.data_dir, '0P0B')
					self.errors += 1


				else:
					self.re_error += 1
					if self.re_error < 4:
						print("Failed to download from '%s'" % i[0])
					else:
						if self.re_error != 4: IOsys.delete_last_line()
						print("And %i others" % (self.re_error - 3))
					Fsys.writer('left_errors.txt', 'a',
					            str(i + (Netsys.hdr(current_header, '0P0B'), "Error dl")) + '\n',
					            AboutApp.leach_projects + self.Project, '0P0B')
			except BadZipFile as e:
				if os_isfile(self.download_dir + fdir + '/' + fname + self.sp_extension):
					remove(self.download_dir + fdir + '/' + fname + self.sp_extension)

				if not is_error:
					Fsys.writer('errors.wlerr', 'a',
					            str(i + (Netsys.hdr(current_header, '0P0B'),) + ["Bad zip"]) + '\n',
					            AboutApp.leach_projects + self.Project, '0P0B')
					self.errors += 1
				else:
					self.re_error += 1
					if self.re_error < 4:
						IOsys.delete_last_line()
						print("Failed to Extract Zip from '%s'\n" % i[0])
					else:
						if self.re_error != 4:
							IOsys.delete_last_line(2)
						print("And %i others\n" % (self.re_error - 3))
					print("It seems every time it downloads a broken or unknown zip from '%s'\n(possible cause password protected zips, if yes extract them manually)\n"%i[0])
					Fsys.writer('left_errors.txt', 'a',
					            str(i + (Netsys.hdr(current_header, '0P0B', ), "Bad zip")) + '\n',
					            AboutApp.leach_projects + self.Project, '0P0B')

					leach_logger(log(['0P0Bx3', self.Project, Netsys.hdr(current_header, '0P0B'), flink, fname, fdir,
					                  e.__class__.__name__, e]), UserData.user_name)
			except Exception as e:
				traceback.print_exc()
				leach_logger(log(['0P0Bx0', self.Project, Netsys.hdr(current_header, '0P0B'), flink, fname, fdir,
				                  e.__class__.__name__, e]), UserData.user_name)




			except:  # for test only
				continue
				self.break_all = True
				print("=== Distribute TRACEBACK ===")
				traceback.print_exc()

		self.error_triggers.append(part)

	def retry_errors(self):  # fc=0P0C
		"""retries to download the error files on `no_buffering` mode after all the `distribute` threads are done
        and their triggers are called."""
		nnn = [i for i in range(self.dl_threads)]
		while not all(i in self.error_triggers for i in nnn):
			if self.break_all:
				return 0
			time.sleep(2)

		leach_logger(log(["0P0CxI", self.Project, self.total, self.total - self.errors, self.errors]),
		             UserData.user_name)

		if self.errors > 0:
			if os_exists(AboutApp.leach_projects + self.Project + '/errors.wlerr'):
				err_file = Fsys.reader(AboutApp.leach_projects + self.Project + '/errors.wlerr', 'rb').replace(b'\r',
				                                                                                               b'').split(
					b'\n')

				if self.break_all:
					return 0
				self.error_links = []
				for i in err_file:
					if i.strip() != b'':
						try:
							self.error_links.append(eval(i.decode())[:3])
						except TypeError:
							print('invalid line:"%s"' % (i.decode()))
						except:
							pass

				self.errors = len(self.error_links)

				print("Retrying failed downloads, may take a while\n\n")

				self.downloader(11, is_error=True)
			else:
				print("Warning: Error file not found!\nPossible cause: data corruption")
				leach_logger(log(["0P0Cx1", self.Project, self.total, self.total - self.errors, self.errors]),
				             UserData.user_name)

		leach_logger(log(["0P0Cx2", self.Project, self.total, self.total - self.errors, self.errors]),
		             UserData.user_name)

		time.sleep(1)

		if not self.dl_done:
			Fsys.writer(self.Project + '.wlproj', 'a', 'dl_done = True\n', AboutApp.leach_projects, '0P0C')
			self.dl_done = True
		if self.errors>0:
			xprint("\n\n/h/Please retry some time later to get higher chances to download some or all %d missing file(s)/=/" % self.errors)
			self.has_missing = True
		else:
			self.has_missing = False

		time.sleep(1.2)

		
		self.manga_freak_patch()

		self.store_current_data()

		time.sleep(1.2)

		xprint("""\n\nDo you want to
\u29bf View the Project in Browser? /hui/ b /=/
\u29bf or Make CBZ files from the images? /hui/ cbz /=/
\u29bf otherwise just leave an Enter
  /gh/>>/=/ """, end='')

	def show_generic_index_error(self, link, current_header, error_name, error_message):  # fc=0P0D
		if not self.index_failed:
			IOsys.delete_last_line()
			xprint('\n/r/Failed to connect "%s"/y/\nSkipping...\nPlease try the update option later/=/\n\n' % (
					link[:10] + '...' + link[-7:]))
			self.index_failed += 1

		else:
			IOsys.delete_last_line(7)
			xprint('\n/r/Failed to connect "%s"/y/\nSkipping(%i)...\nPlease try the update option later/=/\n\n' % (
				link[:10] + '...' + link[-7:], self.index_failed))
			self.index_failed += 1
		leach_logger(log(["0P0Dx1", self.Project, Netsys.hdr(current_header, '0P0D'), link, error_name, error_message]),
		             UserData.user_name)

	def print_index_result(self, link):  # fc=0P0E
		IOsys.delete_last_line()
		xprint('Indexed [' + str(self.indx_count) + '/' + str(len(self.sub_links)) + '] /~`' + link + '`~/')

	def generic_list_writer(self, partitions, part=0, link=None):  # fc=0P0F
		"""indexes the list of links or a single link and and adds & aligns files (of specified file formats) by relative folders in the all_list list

		args:
			partitions: number of partitions created for threading
				0 for single link
			part: which partition to index
			link: if partitions in 0, link is the link to be indexed
		"""

		if partitions == 0:
			links = [link, ]
			partitions = 1

		else:
			links = self.sub_links

		list_range = range(len(links))[part::partitions]

		start_checker = re_compile('^' + self.file_starts)

		with requests.Session() as session:

			for i in list_range:
				if self.break_all: return 0

				failed = False

				current_header = Netsys.header_(self.homepage)

				try:
					page = Netsys.get_page(links[i], cache=True, session=session, do_not_cache=True, return_none = False, raise_error=True)

					
					if not page:
						self.show_generic_index_error(links[i], current_header, str(page.status_code) ,
														'Page Offline')
						failed = True
						
					if self.break_all: return 0

				except NetErrors as e:
					self.show_generic_index_error(links[i], current_header, e.__class__.__name__, str(e))
					failed = True
					# return
				except Exception as e:
					if self.break_all:
						return 0
					xprint('/r/Something went wrong/=/')
					# traceback.print_exc()
					# return

				if self.break_all: return 0
					
				if failed:
					self.indx_count += 1
					self.print_index_result(links[i])
					continue
				else:
					soup = bs(Netsys.remove_noscript(page.text), parser)

				if any(j in self.file_types for j in ('img', 'image', 'images', 'imgs', 'photo', 'photos')):
					for img_link in self.list_writer_img(soup, links[i]):
						
						if self.break_all: return 0

						if start_checker.search(str(img_link)) is not None:
							name = Fsys.get_file_name(img_link, 'url')

							self.all_list.add_link(img_link, i, name)

				# print(img_link)

				self.indx_count += 1

				self.print_index_result(links[i])

	def list_writer_img(self, soup, source):  # fc=0P0G
		returner = []

		tags = ['img']
		if self.check_links:
			tags.append('a')
		for tag in soup.find_all(tags):
			if self.break_all:
				return []

			if self.check_links and tag.name == 'a':
				link = tag.get('href')
				if link is None or link.startswith('#'):
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
					if hhh.startswith('image'):
						returner.append(img_link)
				except Exception:
					continue

			if tag.name == 'img':
				img_link = tag.get('data-src')
				if img_link is None:
					img_link = tag.get('data-img-src')
				if img_link is None:
					img_link = tag.get('data-lazy-src')
				if img_link is None:
					img_link = tag.get('src')
				if img_link is None:
					continue
				img_link = img_link.strip()

				img_link = Netsys.get_link(img_link, source)

				returner.append(img_link)

		return returner


	def clean_unknown_files(self):  # fc=0P0I
		""" Remove the files that are not indexed """
		# if the file is not in the all_list, delete it

		home_done = False

		failed_del = []
		has_older_V = False
		permission_issue = False

		to_del = None

		Ending_msg = set()
		print(self.download_dir)

		for dirpath, dirnames, filenames in os.walk(self.download_dir):
			dp = Fsys.get_dir(dirpath)

			for dirname in dirnames:
				try:
					if dp == self.Project and dirname not in self.sub_dirs:
						to_del = os.path.join(dirpath, dirname)
						rmdir(to_del)
						xprint('/i/[REMOVING]/=/ ', to_del)

					if dp in self.sub_dirs:    # deleting folders that are inside the sub_dirs
						to_del = os.path.join(dirpath, dirname)
						rmdir(to_del)
						xprint('/i/[REMOVING]/=/ ',to_del)

				except PermissionError:
					permission_issue = True
					failed_del.append(to_del)




			for filename in filenames:
				try:
					if dp == self.Project:
						if filename in ['index.html', "index.html.json"]:
							continue

						if self.sub_dirs[0] == '.':
							if filename not in self.all_list.all_names[0]:
								to_del = os.path.join(dirpath, dirname)
								remove(to_del)
								xprint('/i/[REMOVING]/=/ ',dp, '\t>\t', to_del)
								


					if filename == self.Project + '.html':
						to_del = os.path.join(dirpath, filename)
						remove(to_del)
						xprint('/i/[REMOVING]/=/ ',dp, '\t>\t', to_del)
						has_older_V = True

					if dp in self.sub_dirs:
						if filename in ['index.html', "index.html.json"]:
							# print(os.path.join(dirpath, filename))
							continue

						if filename not in self.all_list.all_names[self.sub_dirs.index(dp)]:
							to_del = os.path.join(dirpath, filename)
							remove(to_del)
							xprint('/i/[REMOVING]/=/ ',dp, '\t>\t', to_del)
				except PermissionError:
					permission_issue = True
					failed_del.append(to_del)

		if has_older_V:
			xprint('/y/Older version HTML file detected. Deleting and /h/please update the Project or open with browser using this app/=/\n')
						
		
		if permission_issue:
			xprint("Failed to delete some files due to Permission Error.\n /i/Try deleting them manually/=/\n")
						
		if failed_del:
			print(failed_del, '\n')



	def print_project_info(self):
		""" Print the project info """
		align_format = "/hi/{0: <30}/=/"

		xprint(align_format.format('Project name: '), self.Project)
		xprint(align_format.format('Main URL: '), self.main_link)
		xprint(align_format.format('Sub-link regex: '), self.link_startswith)
		xprint(align_format.format('File-link regex: '), self.file_starts)
		xprint(align_format.format('File format: '), self.file_types)
		if self.dimention==1:
			_dimention = 'Only Main page'
		elif self.dimention==3:
			_dimention = 'Main page and sub-pages'
		else:
			_dimention = 'Only Sub-Pages'

		xprint(align_format.format('Search Dimensions: '), f'({self.dimention})', _dimention)
		xprint(align_format.format('Will Overwrite: '), self.overwrite_bool)
		xprint(align_format.format('Sort files A-Z: '), self.file_to_sort)
		xprint(align_format.format('Sort folders A-Z: '), self.dir_sorted, '\n')

		xprint(align_format.format('Sub-folders: '), len(self.sub_dirs))
		xprint(align_format.format('Files count: '), len(self.all_list), '\n')

		xprint(align_format.format('Special Flags: '), self.sp_flags)
		xprint(align_format.format('Special .ext: '), self.sp_extension)
		xprint(align_format.format('Get HTML Tile: '), self.get_html_title)
		xprint(align_format.format('First Created: '), Nsys.dec_dt(self.first_created))
		xprint(align_format.format('Last Updated: '), Nsys.dec_dt(self.last_update), '\n')

		xprint(align_format.format('Leach Version: '), self.leacher_version)
		xprint(align_format.format('Last used IP: '), self.last_user_ip)
		xprint(align_format.format('Server Version: '), self.server_version, '\n')

		xprint(align_format.format('DL done: '), self.dl_done)
		xprint(align_format.format('Has Missing: '), self.has_missing)






	def mangafreak_link(self):  # fc=0P0M
		"""checks if the link is a mangafreak link and makes indexing easier. but one limitation is it can't find weather the link is valid or not and cannot get the actual file links.
		*Note:: user needs to manually confirm last chapter"""

		link = self.main_link

		self.all_list = All_list_type(1)

		_temp = re_search(Constants.special_starts['mf_sc'], link)
		if _temp:
			_temp = str(_temp.group(1))
			_temp = re_sub('[\!\:\.\'\, ]', '', _temp)
			_temp = re_sub('[\+\/\\ \"\<\>\?\-]', '_', _temp)
			link = 'https://mangafreak.net/Manga/' + _temp
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
						print("Link found - " + i)
						break
					elif re_search(Constants.special_starts['mangafreak'], i):
						link = i
						print("Link found - " + i)
						break

			if link is None:
				print("It seems the title is incorrect. Please recheck the title and re-start the project")
				return ''

		_temp = re_search(Constants.special_starts['mf_read'], link)

		if _temp:
			link = 'https://mangafreak.net/Manga/' + str(_temp.group(1))

		inp = re_search(Constants.special_starts['mangafreak'], link)

		self.main_link = link
		if inp is not None:
			title = inp.group(1)
			self.sp_flags.add('mangafreak')

		else:
			print("It seems the title is incorrect. Please recheck the title and re-start the project")
			return ""

		last_ch = -1
		start = None
		end = None
		chapters = False
		last_ch_ = False

		page = Netsys.get_page(link, cache=True, referer='https://mangafreak.net/', header=Netsys.header_())
		# print(page.content.decode())

		if page:
			if re_search('<div>\n*<a href=\".*?\">\n*Chapter [^\s]*.*\n*</a>\n*</div>', page.content.decode()):
				print('Front page found!')
				last_ch_ = int(re_search('<div>\n*<a href=\".*?\">\n*Chapter ([^\s]*).*\n*</a>\n*</div>', page.content.decode()).group(1))

				_all = re_find_all("<td>.*?<a href=\".*?\">.*?(Chapter (\d*).*?)[\s\n]*?</a></td>.*?<td>.*?</td>.*?<td>.*?<a .*?href=\"(.*?)\".*?</a>.*?</td>", page.text, re.IGNORECASE | re.DOTALL)
				# chapters = {chapter: (name, dl link)}
				chapters = dict([(chap, (name, link)) for name, chap, link in _all])

		_msg = "\n/gh/**/=/Please enter the last chapter number or chapter range (ie: start:end or leave empty for last)...\n leave it empty to auto detect\n\n >> "
	
		if chapters:
			ch_keys = list(chapters.keys())
			start = ch_keys[0]

		while True:
			try:
				last_ch__ = IOsys.safe_input(_msg).strip()
			except LeachICancelError:
				xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
				# leach_logger("000||10007||%s||f-Stop||is_mangafreak||did not ans Mangafreak chapter no"%self.Project)
				return 0

			if last_ch__ == '':
				if last_ch_:
					last_ch = last_ch_
				break
			try:
				if ":" in last_ch__:
					start, end = last_ch__.split(':')
					if start == '': 
						if chapters:
							start = ch_keys[0]
						else:
							start = -1 # will get the 1st chapter later
					else: start = int(start)
					if end == '': 
						if chapters:
							end = ch_keys[-1]
						else:
							end = -1
					else: end = int(end)

					break
				else:
					last_ch = int(last_ch__)
					break
			except ValueError:
				_msg = "\n/rh/**/=/Just enter the last chapter number (like 135)...\n leave it empty to auto detect\n\n >> "

		self.sub_dirs = ['.']

		# try to get from html


		if last_ch == -1:
			start_ = 0 #starting point if failed to detect automatically
			last_ch = 0
			print('Counting Links... (0)')
			while True:
				try:
					if requests.head("http://images.mangafreak.net:8080/downloads/" + title + '_' + str(last_ch + 1)).headers['content-length'] !=0:
						last_ch += 1
						IOsys.delete_last_line()
						print('Counting Links... (%i)' % last_ch)
					else:
						if last_ch == 0:
							start_ = 1
						else:
							break
				except Exception:
					if last_ch == 0:
						start_ = 1
					else:
						break

			IOsys.delete_last_line()
			print("Total %i links found from mangafreak.\nIf its not right, retry by pressing ctrl+C\n\n" % last_ch)

		if start == -1 or start is None:
			start = start_
		if end == -1 or end is None:
			end = last_ch

		print([start, end])

		if chapters:
			for i in ch_keys:
				name, link = chapters[str(i)]
				xprint('\n/yh/%s/=/:\t%s\t%s' % (i,*chapters[i]))
				self.all_list.add_link(link, 0, name=name)
		
		else:
			for i in range(start, end + 1):
				link = "http://images.mangafreak.net:8080/downloads/" + title + '_' + str(i)
				self.all_list.add_link(link, 0)#, ext='.zip')

		self.sp_extension = '.zip'

		if "mangafreak-patched" in self.sp_flags:
			self.sp_flags.remove("mangafreak-patched")

		return "mangafreak.net"

	def nhentai_link(self):  # fc=0P0N
		"""checks if the link is nhentai link and returns the available link and the title of the doujin
		else it will return 0"""
		link = self.main_link

		if re_search(Constants.special_starts['nh_sc'], link):
			self.main_link = 'https://nhentai.net/g/' + str(re_search(Constants.special_starts['nh_sc'], link).group(1))
		link = self.main_link
		code = re_search('https://nhentai.[^/]*/g/((\d)*)', link)

		if code is None:
			return False, False
		code = code.groups()[0]

		current_header = Netsys.header_()
		with requests.Session() as _session:
			try:
				link_y = 'https://nhentai.net/g/' + code + '/'
				page = _session.get(link_y, headers=current_header, timeout=2)
				if page:
					site = ".net"
				else:
					raise requests.exceptions.ConnectionError
			except (
					requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
					requests.exceptions.ReadTimeout,
					requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema, requests.exceptions.SSLError,
					urllib3.exceptions.SSLError):
				leach_logger(log(["0P0Nx1", self.Project, link, Netsys.hdr(current_header, '0P0N')]),
				             UserData.user_name)
				print('nhentai.net server is not reachable, trying proxy server...')
				link_y = 'https://nhentai.xxx/g/' + code + '/'
				try:
					page = _session.get(link_y, headers=Netsys.header_())
					if page:
						site = ".xxx"
					else:
						raise requests.exceptions.ConnectionError
				except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
				        requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema,
				        requests.exceptions.MissingSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError):
					IOsys.delete_last_line()
					# xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
					leach_logger(log(["0P0Nx3", self.Project, link, Netsys.hdr(current_header, '0P0N')]),
					             UserData.user_name)
					IOsys.delete_last_line()
					print('nhentai.net server is not reachable, trying proxy server...(2)')
					link_y = 'https://nhentai.to/g/' + code + '/'

					try:
						page = _session.get(link_y, headers=Netsys.header_())
						if page:
							site = ".to"
						else:
							raise requests.exceptions.ConnectionError
					except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
					        requests.exceptions.ReadTimeout, requests.exceptions.InvalidSchema,
					        requests.exceptions.MissingSchema, requests.exceptions.SSLError,
					        urllib3.exceptions.SSLError):
						xprint(
							"/rh/Error code: 606x3\nLink not found, Please recheck the link and start a new project/=/")
						leach_logger(log(["0P0Nx2", self.Project, link, Netsys.hdr(current_header, '0P0N')]),
						             UserData.user_name)
						return False, False

		self.file_exts = Constants.all_image_types
		if page:
			self.all_list = All_list_type(1)
			soup = bs(Netsys.remove_noscript(page.text), parser)

			title = Datasys.remove_non_uni(soup.find(id='info').find('h1').get_text(), '0P0N')
			print("Indexing from", title)
			self.file_starts = ''

			if site == ".xxx":
				xxx_search = re_compile("https://cdn.nhentai.xxx/g/\d+/\d*t..*")
				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')

					if img_link is None:
						img_link = imgs.get('src')

					if xxx_search.search(img_link) is not None:
						self.all_list.add_link(''.join([img_link.rpartition('t')[0], img_link.rpartition('t')[2]]), 0)
				# img_link.rpartition('t')[1]

			elif site == ".to":
				to_search = re_compile("(https://nhentai.to/galleries/\d*/)|(https://cdn.dogehls.xyz/galleries/\d*/)")
				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')
					if img_link is None:
						img_link = imgs.get('src')
					if img_link.startswith('/'):
						img_link = 'https://nhentai.to' + (img_link.replace('t', ''))
					if img_link.startswith('https://cdn.dogehls.xyz/galleries/'):
						img_link = img_link[::-1].replace('t', '', 1)[::-1]

					if to_search.search(img_link) is not None:
						self.all_list.add_link(img_link, 0)

			elif site == ".net":
				net_search = re_compile("https://i.nhentai.net/galleries/\d*/")
				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')
					if img_link is None:
						img_link = imgs.get('src')

					if '/thumb.' in img_link:
						continue

					if 'cover' not in img_link:
						img_link = img_link.replace('s://t.', 's://i.')[::-1].replace('t', '', 1)[::-1]
					if net_search.search(img_link) is not None:
						self.all_list.add_link(img_link, 0)
			self.all_list.remove_duplicates()

			self.sp_flags.add('nh')

			title = Datasys.trans_str(parse.unquote(html_unescape(title)), {'/\\|:*><?': '-', '"': "'"}).strip()[
			        :config.dir_limit]

			self.update_sub_dirs(
				Datasys.trans_str(parse.unquote(html_unescape(title)), {'/\\|:*><?': '-', '"': "'"}).strip()[ :config.dir_limit], 0)

			# print(self.sub_dirs)
			return link_y, title
		else:
			xprint("/rh/Error code: 606x2\nLink not found, Please recheck the link and start a new project/=/")
			# leach_logger("606x2||%s||%s||%s"%(self.Project, link, Netsys.hdr(current_header, '10005')), UserData.user_name)
			return False, False

	def webtoon_link(self):  # fc=0P0W
		"""checks for webtoon links and get chapterwise image links and sends it to `main` function"""

		self.temp_counter = 0

		def get_images(self, indx):  # fc=0P0W1
			remove_type = re_compile('\?type\=.*.*')
			for j in indx:
				i = self.sub_links[j]
				temp1 = bs(Netsys.remove_noscript(session.get(i).text), parser)
				img_div = temp1.find('div', id='_imageList')

				for ii in img_div.find_all('img'):
					self.all_list.add_link(remove_type.sub('', ii.get('data-url')), j)

				self.temp_counter += 1
				IOsys.delete_last_line()
				print('Gathering Image links [%i / %i]' % (self.temp_counter, total_chapters))

		_t = re_search(Constants.special_starts['webtoon'], self.main_link)
		if _t:
			datas = _t.groups()
		else:
			_t = re_search(Constants.special_starts['webtoon_ep'], self.main_link)
			if _t:
				datas = _t.groups()  # category, title, code
			else:
				xprint("/r/Invalid link/y/\n please recheck the Main link/=/")
				leach_logger(log(['0P0WxX', self.Project, self.main_link, 'Failed to pass the regex testing']),
				             UserData.user_name)
				return 0

		page_list = []
		prev_lists = []
		next_lists = []
		sub_links = []
		sub_dirs = []
		homepage = 'https://www.webtoons.com'

		with requests.Session() as session:
			input_link = "https://www.webtoons.com/en/%s/%s/list?title_no=%s" % (datas)
			input_page = session.get(input_link, headers=Netsys.header_())
			if not input_page:
				xprint('/r/Webtoon Page not found. /y/Recheck the link/=/')
				return 0

			self.sp_flags.add('webtoon')

			input_soup = bs(Netsys.remove_noscript(input_page.text), parser)
			_temp = input_link

			paginate = input_soup.find_all("div", class_="paginate")[0]
			paginate__ = paginate
			paginate_ = paginate__.find_all('a', class_='pg_prev')
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			while len(paginate_) != 0:
				prev_lists.append(Netsys.get_link(paginate_[0].get('href'), _temp, homepage))
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
				_temp = prev_lists[-1]
				paginate__ = bs(Netsys.remove_noscript(session.get(_temp).text), parser).find_all("div", class_="paginate")[0]
				paginate_ = paginate__.find_all('a', class_='pg_prev')
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

			_temp = input_link
			paginate_ = paginate.find_all('a', class_='pg_next')
			paginate__ = paginate
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			while len(paginate_) != 0:
				next_lists.append(Netsys.get_link(paginate_[0].get('href'), _temp, homepage))
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
				_temp = next_lists[-1]
				paginate__ = bs(Netsys.remove_noscript(session.get(_temp).text), parser).find_all("div", class_="paginate")[0]
				paginate_ = paginate__.find_all('a', class_='pg_next')
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

			del paginate__

			page_list = natsort.natsorted(Datasys.remove_duplicate(page_list))

			for i in page_list:
				temp1 = bs(Netsys.remove_noscript(session.get(i).text), parser)
				ul = temp1.find_all('ul', id="_listUl")[0].find_all('a')
				for ii in ul:
					sub_links.append(Netsys.get_link(ii.get('href'), _temp, homepage))
					sub_dirs.append(ii.find('span', class_='subj').text.strip())

		self.sub_dirs = sub_dirs[::-1]
		self.sub_links = sub_links[::-1]

		total_chapters = len(sub_links)

		self.all_list = All_list_type(total_chapters)

		print('Found %i Chapters' % total_chapters)
		print('\nGathering Image links [%i / %i]' % (self.temp_counter, total_chapters))

		sub_range = range(total_chapters)

		index_thread_list = [Process(target= get_images, args=(self, sub_range[i::self.index_threads])) for i in range(self.index_threads)]

		try:

			for i in range(self.index_threads):
				index_thread_list[i].start()

			while any([i.is_alive() for i in index_thread_list]):
				if self.break_all:
					return False
				time.sleep(0.3)

		except EOFError:
			leach_logger(log(['000', '0P0W', self.Project, 'f-Stop', 'was indexing Images from webtoon', 'Indexing Stopped']))
			xprint("/yh/Project indexing cancelled by Keyboard/=/")
			self.break_all = True
			return 0
		except KeyboardInterrupt:
			leach_logger(log(['000', '0P0W', self.Project, 'f-Stop', 'was indexing Images from webtoon', 'Indexing Stopped']))
			xprint("/yh/Project indexing cancelled by Keyboard/=/")
			self.break_all = True
			return 0

		except Exception as e:
			xprint("/rh/code: Error 607\n The program will break in 5 seconds/=/")
			leach_logger(log(['0P0Wx0', self.Project, self.main_link, e.__class__.__name__, e]))
			time.sleep(5)
			exit(0)

		self.dir_sorted = True
		self.overwrite_bool = False
		self.file_to_sort = False
		return 'all good'

	def manga_freak_patch(self):  # fc=0P0MP
		""" Patch for Manga Freak downloads"""
		if 'mangafreak' in self.sp_flags and 'mangafreak-patched' not in self.sp_flags:
			
			if 'dl unzip' in self.sp_flags:
				if 'del dl zip' in self.sp_flags:
					self.sub_dirs = []

				if not os_exists(self.download_dir):
					xprint("\n  /hui/Project folder not found./=/\nPlease recheck or update the download project\n*its required for Manga Freak Projects")
					return 0
				self.sub_dirs += natsort.natsorted(
					[os.path.splitext(i)[0] for i in self.all_list.all_names[0] if os_isdir(self.download_dir + os.path.splitext(i)[0])])
				self.all_list = All_list_type(len(self.sub_dirs))
				for i in range(len(self.sub_dirs)):
					for j in os_listdir(self.download_dir + self.sub_dirs[i]):

						if os_isfile(self.download_dir + self.sub_dirs[i] + '/' + j) and (not j.endswith('.html')):
							self.all_list.add_name(j, i)

				self.file_to_sort = True
				self.sp_extension = ''

			self.sp_flags.add('mangafreak-patched')

			self.store_current_data()

	def make_html(self):  # fc=0P0O
		"""Make the html file"""
		OSsys.import_make()
		self.manga_freak_patch()

		return MakeHtml.make_pages(self.all_list.all_names, self.sub_dirs, self.Project, self.file_to_sort,
		                           self.sp_extension, self.dir_sorted)
		                           
	def make_online_html(self):  # fc=0P0O
		"""Make the html file"""
		OSsys.import_make()
		#self.manga_freak_patch()

		return MakeHtml.make_online_page(self.all_list.get_all_list(), self.sub_dirs, self.Project, self.file_to_sort,
		                           self.sp_extension, self.dir_sorted)

	def make_cbz(self):  # fc=0P0P
		"""Make the cbz file"""
		OSsys.import_make()
		self.manga_freak_patch()

		return MakeCbz.make_cbz(self.all_list, self.sub_dirs, self.Project, self.file_to_sort, self.sp_extension)

	def post_online(self):
		"""Sends project images to online 
		adds source links and online file links in """

		pass


print(12)  # x

print(13)  # x


# print(ProjectType.get_page('htps://ratulhasan14789.github.io/fuck'))

class BugFixes_n_Updates_ :  # fc=0D00
	"""some minor bug fixed from version change and new setup"""

	def fix_err_header(self):  # fc=0D01
		"""Fixes the data/err_header.txt file"""
		global err_hdr_list
		if os_isfile(AboutApp.data_dir + 'err_header.txt'):
			error_hdr_file = Fsys.reader(AboutApp.data_dir + 'err_header.txt')
			temp_ = re_sub('\,{2,}', ',', error_hdr_file)

			if temp_[-1] == ',': temp_ = temp_[:-1]

			err_hdr_list = eval(temp_)
			# print(type(err_hdr_list))
			if type(err_hdr_list) == tuple:
				err_hdr_list = Counter(err_hdr_list)

				Fsys.writer('err_header.txt', 'w', str(err_hdr_list), AboutApp.data_dir, '0D00')

			elif type(err_hdr_list) == list:
				_t = Counter()
				for i, j in err_hdr_list:
					_t[i] = j

				err_hdr_list = _t

				Fsys.writer('err_header.txt', 'w', str(err_hdr_list), AboutApp.data_dir, '0D00')


			elif type(err_hdr_list) == dict:
				err_hdr_list = Counter(err_hdr_list)
		else:
			err_hdr_list = Counter()


BugFixes_n_Updates = BugFixes_n_Updates_()


class Main :  # fc=0M00
	def __init__(self):  # fc=0M01
		IOsys.delete_last_line()
		print("Connecting to server...")
		Ctitle('Connecting to server 🌐')
		self.dl_threads = []

	def get_user(self):  # fc=0M02
		UserData.get_user_ip()

		BugFixes_n_Updates.fix_err_header()

		server_ping = time.time()
		config.run_mod = config.god_mode()
		server_pong = time.time()

		leach_logger('002||' + str(server_pong - server_ping) + 's||' + config.server_version, 'leach')

		UserData.log_in()

	def make_required_dirs(self):  # fc=0M03
		"""Make the required directories"""
		for i in [AboutApp.download_dir, AboutApp.data_dir, AboutApp.temp_dir, AboutApp.leach_projects,
		          AboutApp.cached_webpages_dir]:
			if not os_exists(i):
				makedirs(i)

	def boot_server(self):  # fc=0M04
		global server_launcher
		UserData.user_primary_port = (int(UserData.userhash, 16) % (60000 - 49200 + 1)) + 49200
		xprint("/i/ Running port /=/ :",UserData.user_primary_port)

		server_status = Netsys.check_server("http://localhost:%i" % UserData.user_primary_port, '0M04', timeout=5)
		

		if server_status is False:
			UserData.user_secondary_port = (int(UserData.userhash, 16) % (64000 - 60001 + 1)) + 60001

		config.running_port = UserData.user_secondary_port if UserData.user_secondary_port else UserData.user_primary_port

		if server_status:
			config.server_running = True
			pass
		elif server_status in (False, None):
			server_launcher = Process(target=Netsys.run_server_t, args=(server_status, AboutApp.download_dir))
			server_launcher.start()
		else:
			exit()

	def main_loop(self):  # fc=0M05
		global Keep_main_running
		self.boot_server()
		CachedData.clear()

		self.link_indexed = False

		while True:
			try:
				self.COMM = IOsys.safe_input('\nEnter Batch download directory (Project name): ').strip()

				if any(ord(i) < 32 or ord(i) == 127 for i in self.COMM) or self.COMM != Datasys.remove_non_uni(
						self.COMM, '0M05'):
					xprint("/r/Invalid character!\n/y/Please retry...\n/=/")
					continue

			except LeachICancelError:
				try:
					xprint("\n/yh/Cancellation command entered.\nExiting peacefully/=/")
					leach_logger("0x1||0M05||User Exit-0")
					
					Keep_main_running = False

					while server_code is None: 
						time.sleep(.5)
					server_code.server_close()
					server_code.shutdown()
					
					exit()
				except EOFError:
					exit()
				except KeyboardInterrupt:
					exit()
			__command = self.COMM.lower()
			if __command == '':
				print('You must enter a Project name here.')
			elif __command in ['?disable-dl-thread', '?d-dl-t']:
				config.sp_arg_flag['disable dl cancel'] = True
				print('Disabled download cancellation by adding join thread option')
				return 0

			elif __command in ['?help', '?sc', '?']:
				xprint('''
Index    SP project Names                   Works
======   =================      =====================================================
  1    /y/?enable-dl-thread/=/           `sp_arg_flag['disable dl cancel'] = True` 
                                  Disables download cancellation by adding 
                                  join thread option

  2    /y/?disable-dl-thread/=/          `sp_arg_flag['disable dl cancel'] = False` 
                                  Enables download cancellation by adding 
                                  removing thread option /h/[DEFAULT]/=/

  3    /y/?disable-dl-get/=/             `sp_arg_flag['disable dl get'] = True`
                                  Disabled download save by using requests.head

  4    /y/?enable-dl-get/=/              `sp_arg_flag['disable dl get'] = False`
                                  Enabled download save by using requests.get /h/[DEFAULT]/=/

  5    /y/?disable-browser/=/            `sp_arg_flag['disable browser'] = True`
                                  Disabled opening Downloads in browser
  6    /y/?enable-browser/=/             `sp_arg_flag['disable browser'] = False`
                                  Enabled opening Downloads in browser /h/[DEFAULT]/=/

  7    /y/?clean-project/=/              asks the project name and delete unwanted files made by user or program

  8    /y/?enable-download-limit (%d)/=/ enables download limit (max dlim) with (%d) kbps

  9    /y/?disable-download-limit/=/    disables download limit (sets "max dlim" to 0)

  10   /y/?project-info/=/               shows project information

  -1   /g/?E-dl-T/=/                 same as 1
  -2   /g/?D-dl-T/=/                 same as 2
  -3   /g/?D-dl/=/                   same as 3
  -4   /g/?E-dl/=/                   same as 4
  -5   /g/?D-br/=/                   same as 5
  -6   /g/?E-br/=/                   same as 6
  -7   /g/?c-p/=/                    same as 7
  -8   /g/?E-dlim/=/                 same as 8
  -9   /g/?D-dlim/=/                 same as 9
  -10  /g/?i-p/=/                    same as 10
====================================================================

/i/ Current settings /=/
========================
Option               Value
------------        -----------
''')
				for i, j in config.sp_arg_flag.items():
					xprint('{:<20} {:<}'.format(i, j))

				return 0

			elif __command in ['?enable-dl-thread', '?e-dl-t']:
				config.sp_arg_flag['disable dl cancel'] = False
				print('Enabled download cancellation by adding removing thread option [DEFAULT]')
				return 0
			elif __command in ['?disable-dl-get', '?d-dl']:
				config.sp_arg_flag['disable dl get'] = True
				print('Disabled download save by using requests.head')
				return 0

			elif __command in ['?enable-dl-get', '?e-dl']:
				config.sp_arg_flag['disable dl get'] = False
				print('Enabled download save by using requests.get [DEFAULT]')
				return 0

			elif __command in ['?enable-ara-ara', '?e-noise']:
				config.sp_arg_flag['ara ara'] = True
				print('Enabled fun sounds [DEFAULT]')
				return 0

			elif __command in ['?disable-ara-ara', '?d-noise']:
				config.sp_arg_flag['ara ara'] = False
				print('Enabled fun sounds [DEFAULT]')

			elif __command in ['?disable-browser', '?d-br']:
				config.sp_arg_flag['no browser'] = True
				print('Disabled opening Downloads in browser')
				return 0

			elif __command in ['?enable-browser', '?e-br']:
				config.sp_arg_flag['no browser'] = False
				print('Enabled opening Downloads in browser [DEFAULT]')
				return 0

			elif __command in ['?disable-download-limit', '?d-dlim']:
				config.sp_arg_flag['max dlim'] = 0
				print('Disabled Download Limit [DEFAULT]')
				return 0

			elif any(__command.startswith(i) for i in ['?enable-download-limit', '?e-dlim']):
				try:
					_temp_ = float(__command.split()[1])  # input will be in KB 1*1024
				except ValueError:
					xprint("/y/Invalid Download Speed Limit/=/")
					return 0
				config.sp_arg_flag['max dlim'] = _temp_
				print('Enabled Download Limit at', _temp_, 'kbps')
				return 0

			elif __command in ['?clean-project', '?c-p']:
				p_name = IOsys.safe_input("Enter the project name: ")
				P = ProjectType_(p_name)
				P.load_data(p_name)
				if P.list_good:
					P.clean_unknown_files()
				else:
					print('Project not found')
				return 0
				
			

			
			elif __command in ['?project-info', '?i-p']:
				p_name = IOsys.safe_input("Enter the project name: ")
				P = ProjectType_(p_name)
				P.load_data(p_name)
				if P.list_good:
					P.print_project_info()
				else:
					print('Project not found')
				return 0
				
			elif __command in ["?html", "?o"]:
				proj = IOsys.safe_input("Enter Project name: ")
				
				self.P = ProjectType_(proj)
				check_project = self.P.load_data(proj)
				print(check_project)
				if check_project:
					self.P.store_current_data()
					if 'mangafreak' in self.P.sp_flags:
						xprint("/rh/Sorry can't make online version of MangaFreak Page/=/")
						return 0
					try:
						self.P.make_online_html()
					except LeachICancelError:
						print("\nCancelled! ! !")
						return 0
					Netsys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))
				pass

			elif __command in ['?re', "?reload"]:
				return "reload"


			else:
				break


		if any(i in '\\/|:*"><?' for i in __command):
			print("\n>> Project name can't have ")
			print("\\ / | : * \" > < ?\n".center(20))
			return 0
			
			
		self.P = ProjectType_(self.COMM)
		check_project = self.P.load_data(self.COMM)
		Ctitle(f'Project {self.P.Project} [{config.mode_emoji[config.run_mod]}] [:{config.running_port}]')

		if check_project:
			self.P.store_current_data()
			if self.P.dl_done:
				xprint('/h/It seems  the old project download was complete!!/=/')
				if self.P.has_missing:
					xprint('/r/Also have some MISSING files/=/')
				try:
					####################################
					# self.P.make_html()
					# return 0
					####################################





					temp = IOsys.asker(out="""\u29bf Do you want to get updated data from the project link? (/hui/ y /=///hui/ n /=/)  %s
\u29bf If you want make a fresh start with that project name type /hui/ fresh /=///hui/ f /=/
\u29bf To open the project in Browser enter /hui/ b /=/
\u29bf To Create CBZ file(s) of the project in Browser enter /hui/ cbz /=/

/g/  >> /=/""" % (' /h/[Recommended]/=/' if self.P.has_missing == True else ''), extra_opt=('b', 'fresh', 'f', 'cbz'),
					                   extra_return=('browser', 'fresh', 'fresh', 'cbz'))

				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
					# leach_logger("000||11000||%s||f-Stop||was_done||don't want to update proj or anything"%(self.P.Project))
					return 0


				if temp == 'browser' or temp == 'cbz':

					OSsys.import_make()
					self.P.manga_freak_patch()
					if temp == 'browser':
						try:
							first_page = self.P.make_html()
							if not first_page:
								xprint('Failed to generate sub-page. /y/wl-page.html not found/=/')
								leach_logger(log(['7002x1', self.P.Project, AboutApp.cloud_html_temp_link]))
								return 0
							

							Netsys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))


						except EOFError:
							leach_logger('7001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						except KeyboardInterrupt:
							leach_logger('7001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						except LeachICancelError:
							leach_logger('7001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0

						return 0

					else:  # cbz
						try:
							first_page = self.P.make_cbz()
							print('CBZ Created in "%s"' % first_page)
						except EOFError:
							leach_logger('8001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						except KeyboardInterrupt:
							leach_logger('8001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
						return 0

				elif temp == 'fresh':
					#TODO: Need logging

					Project = self.P.Project
					self.P = ProjectType_(Project)
					self.P.existing_found = False
				# leach_logger('11000x1||%s'%self.P.Project, UserData.user_name)

				elif temp is True:
					#TODO: Need logging
					self.P.existing_found = False
					self.P.update = True
					self.P.overwrite_bool = False
				# leach_logger('11000x2||%s'%self.P.Project, UserData.user_name)


				elif not temp:
					return 0


			else:
				try:
					temp = IOsys.asker("""\u29bf Do you want to
resume the Project '%s'
yes/y to resume
\u29bf /hui/ fresh /=///hui/ f /=/ to Start fresh
/yh/(warning! last project data will be erased, /=/downloaded files will be safe, unless the program replaces the files with new ones)
/gh/  >> /=/""" % self.P.Project, extra_opt=('f', 'fresh'), extra_return=('fresh', 'fresh'))
				except LeachICancelError:
					xprint("\n/yh/Cancellation command entered.\nReturning to main options/=/")
					#Todo: leach_logger("000||11000||%s||f-Stop||was_paused||don't want to resume proj or anything"%self.P.Project)
					return 0
				if temp == 'fresh': #Todo: need logging
					# leach_logger('11000x4||%s'%self.P.Project, UserData.user_name)
					# clear file data
					# writer(self.Project + '.list', 'w', '', AboutApp.leach_projects, '0M05')
					# writer(self.Project + '.proj', 'w', '', AboutApp.leach_projects, '0M05')

					Project = self.P.Project

					self.P = ProjectType_(Project)
					self.P.existing_found = False
				elif temp is True:
					print('============ Reloaded =============')
					#Todo: leach_logger('11000x3||%s'%self.P.Project, UserData.user_name)
					self.P.existing_found = True
				elif not temp:
					return 0

		elif check_project is None:
			print("Could not load data from file. Please start over.")
			self.P.existing_found = False


		if self.P.existing_found is False:
			if self.P.update:
				if os_exists(AboutApp.leach_projects + self.P.Project):
					rmdir(AboutApp.leach_projects + self.P.Project)
					print('removed tdata')

				self.P.all_list = []
				self.P.sub_dirs = []
				self.P.sub_links = []
				self.P.dl_done = False

				if 'webtoon' in self.P.sp_flags or (
						self.P.file_types == [] and self.P.link_startswith == "https://www.webtoons.com"):
					print("Checking for links, please wait...")
					if self.P.webtoon_link() == 'all good':
						self.link_indexed = True
						link_true = True
					else:
						xprint("/r/It seems the link is dead\n/y/please recheck the link and create a fresh Project/=/")
						return 0


				elif 'mangafreak' in self.P.sp_flags:
					print("Update isn't available for mangafreak")
					self.P.sp_flags.add('ignore_on_null_content')  # do not save null files
					# self.P.sp_flags.add('stop_on_null_content') # stops downloading after receiving a null file
					try:
						if IOsys.asker('\u29bf Do you want to re-download files from the same link?\n >> '):
							will_unzip = IOsys.asker(
								"\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

							if will_unzip:
								self.P.sp_flags.add("dl unzip")
								if IOsys.asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
									self.P.sp_flags.add("del dl zip")
							try:
								self.P.link_startswith = self.P.mangafreak_link()


							except EOFError:
								print("Cancel command entered! stopping")
								return 0
							except KeyboardInterrupt:
								print("Cancel command entered! stopping")
								return 0
							if self.P.link_startswith == 0:  # cancel code
								return 0

							self.P.file_exts = ('zip',)
							self.P.file_starts = ''
							self.link_indexed = True
							link_true = True

					# leach_logger('0M05x1||%s||is_mangafreak||%s'%(self.Project, str(self.P.sp_flags)), UserData.user_name)

					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						# leach_logger("000||0M05||%s||f-Stop||is_mangafreak||user probably freaked out for too much Ques"%self.Project)
						return 0


				elif 'nh' in self.P.sp_flags or (
						self.P.main_link.startswith("https://nhentai.net/g/") and self.P.link_startswith.startswith(
					"https://nhentai.xxx/g/")):
					try:
						self.P.link_startswith, title = self.P.nhentai_link()

					except EOFError:
						print("Cancel command entered! stopping")
						return 0
					except KeyboardInterrupt:
						print("Cancel command entered! stopping")
						return 0

					if self.P.link_startswith == False or title == False:
						print("Failed to get data from %s\nReturning back to main page." % self.P.main_link)
						return 0

					if title != False and self.P.link_startswith != '':
						self.P.file_starts = ''

						self.link_indexed = True
						# leach_logger('0M05x1||%s||is_nh||True||Assigned after testing the link'%(self.Project), UserData.user_name)
						link_true = True

				# leach_logger('0M05x0||%s||is_nh'%(self.Project), UserData.user_name)

				if not any(i in self.P.sp_flags for i in ['nh', 'mangafreak', 'webtoon']):
					page = Netsys.get_page(self.P.main_link)
					if page:
						link_true = True
					else:
						xprint("/rh/Link Unavailable! /=/It seems the previous link is unaccessable right now.\nPlease Retry the project sometimes later with stable internet connection\n(possible cause: no internet or wrong link)\n/s4/")
						#TODO: Need logging
						return 0


					try:
						self.P.file_to_sort = IOsys.asker("\n\n\u29bf Will download in sequncial order? ", default=False)
					except LeachICancelError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')

						pass
						#todo: leach_logger("000||0M05||%s||f-Stop||UI||user left while asking self.P.file_to_sort "%self.P.Project)
						return 0


					try:
						if self.P.dimention == 0:
							xprint("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")
							try:
								_temp = IOsys.safe_input("Enter the index of your choice (1/2/3): ")
								if _temp=="": _temp=2
				
								self.P.dimention = int(_temp)
							except ValueError:
								self.P.dimention = -1
							except LeachICancelError:
								xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
								return 0
							while self.P.dimention not in [1, 2, 3]:
								try:
									_temp = IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  ")
									
									if _temp=="": _temp=2
									else: print([_temp])
									self.P.dimention = int(_temp)
								
								except ValueError:
									self.P.dimention = -1
								except LeachICancelError:
									xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
									return 0

							pass  #todo:  leach_logger('0M05x1||%s||dimention||%s'%(self.P.Project, self.P.dimention), UserData.user_name)

						if not self.P.gen_sub_links():
							return 0

						if not self.P.gen_sub_dirs():
							return 0






					except EOFError:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						return 0
					except KeyboardInterrupt:
						xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
						return 0


			else:
				if os_exists(AboutApp.leach_projects + self.P.Project): rmdir(AboutApp.leach_projects + self.P.Project)
				if self.P.corruptions != [] and self.P.corruptions != [0]:
					pass  #todo:  leach_logger("0M05x1||%s||Corruptions||%s||%s"%(self.P.Project,  str(self.P.corruptions), '<br>'.join(Fsys.reader(AboutApp.leach_projects + self.Project + '.proj', 'rb', True, 'str').strip().split('\n'))), UserData.user_name)

				Fsys.writer('errors.wlerr', 'a', '', AboutApp.leach_projects + self.P.Project,
				            '0M05')  # reset error file

				self.P = ProjectType_(self.P.Project)


				link_true = False

				try:

					self.P.main_link = IOsys.safe_input("\nEnter the link: ")
					pass  # leach_logger('0M05x1||%s||m_link||%s'%(self.Project, self.P.main_link), UserData.user_name)
					while not link_true:
						if SupportTools.check_sp_links(self.P.main_link, ['nh', 'mangafreak', 'webtoon']):

							if SupportTools.check_sp_links(self.P.main_link, 'mangafreak'):
								print("mangafreak link detected!!")
								is_mangafreak = IOsys.asker(
									"\u29bf Do you want to download manga images from this links?? (/hui/ y /=///hui/ n /=/)\n>> ", default=True)
								if is_mangafreak:
									self.P.sp_flags.add('ignore_on_null_content')  # do not save null files
									self.P.sp_flags.add('stop_on_null_content')  # stops downloading after receiving a null file

									will_unzip = IOsys.asker(
										"\nThe download files are in zip format.\n\u29bf Do you wish to Extract them?\n>> ")

									if will_unzip:
										self.P.sp_flags.add("dl unzip")
										if IOsys.asker("\u29bf Shall I delete the downloaded zip files?\n>> "):
											self.P.sp_flags.add("del dl zip")
									try:
										_temp = self.P.mangafreak_link()
										if _temp == 0:
											return 0
										if _temp!= '':
											self.P.link_startswith = _temp
											del _temp
											
											self.P.file_exts = ('zip',)
											self.P.file_starts = ''
											self.link_indexed = True
											link_true = True
											break


									except EOFError:
										print("Cancel command entered! stopping")
										return 0
									except KeyboardInterrupt:
										print("Cancel command entered! stopping")
										return 0
									# sub_links = ''
									#exit(0)


							if SupportTools.check_sp_links(self.P.main_link, 'webtoon'):
								xprint('/y/Webtoon link detected!/=/')
								is_webtoon = IOsys.asker('\u29bf Do you want to download the Entire Web comic?? (/hui/ y /=///hui/ n /=/)\n/gh/>>/=/  ', default=True)

								if is_webtoon:
									xprint("/y/Checking for links, please wait.../=/")
									if self.P.webtoon_link() == 'all good':
										self.P.link_startswith = 'https://www.webtoons.com'
										link_true = True
										self.link_indexed = True
									else:
										xprint(
											"/r/It seems the link is dead\n/y/please recheck the links and your internet connection/=/")
										return 0

							if SupportTools.check_sp_links(self.P.main_link,
							                               'nh'):  # main_link.startswith('https://nhentai.net/g/') or main_link.startswith('https://nhentai.to/g/'):
								xprint("/y/nhentai link detected!!/=/")
								is_nh = IOsys.asker(
									"\u29bf Do you want to download doujin images from this links?? /hui/ y /=///hui/ n /=/\n /gh/>>/=/  ", default=True)

								if is_nh:
									if os_name == 'Windows' and config.sp_arg_flag['ara ara']:
										SupportTools.play_yamatte_t.start()

									self.P.link_startswith, title = self.P.nhentai_link()
									# print(link_startswith, title)
									if self.P.link_startswith == 0 and title == 0:
										return 0

									if title != False and self.P.link_startswith != '':
										self.P.file_starts = ''

										self.link_indexed = True
										# leach_logger('0M05x1||%s||is_nh||True||Assigned after testing the link'%(self.Project), UserData.user_name)
										link_true = True
										break

							if SupportTools.check_sp_links(self.P.main_link, 'pinterest'):
								print(
									"Pinterest link detected.\nDo you want to try the special features for pinterest images?\nWarning: All images may not be the same from the website as you see\n")
								if IOsys.asker('>> '):

									if SupportTools.check_sp_links(self.P.main_link, 'pinterest-pin'):
										try:
											self.P.dimention = int(
												IOsys.safe_input("Enter the index of your choice (1/2/3): "))
										except ValueError:
											self.P.dimention = -1
										while self.P.dimention not in [1, 2, 3]:
											try:
												self.P.dimention = int(
													IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  "))
											except ValueError:
												self.P.dimention = -1




									self.P.link_startswith = 'https://www.pinterest.com'
						if not link_true:
							try:
								try:
									page = Netsys.get_page(self.P.main_link)
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


					if not self.link_indexed:

						print("Do you want to\n1. Download data from current link\n2. Download data from sub links of current link\n3. or Both Current and Sub links?")

						try:
							_temp = IOsys.safe_input("Enter the index of your choice (1/2/3): ")
							if _temp=="": _temp=2
				
							self.P.dimention = int(_temp)
						except ValueError:
							self.P.dimention = -1
						while self.P.dimention not in [1, 2, 3]:
							try:
								_temp = IOsys.safe_input("/rh/Invalid input!/=/\nEnter 1 or 2 or 3:  ")
								if _temp=="": _temp=2
				
								self.P.dimention = int(_temp)
							
							except ValueError:
								self.P.dimention = -1
						pass  # leach_logger('0M05x1||%s||dimention||%s'%(self.P.Project, self.P.dimention), UserData.user_name)

						if self.P.dimention in (2, 3):
							self.P.link_startswith = IOsys.safe_input(
								"\n(optional but recommended to be more precise):\n1. Sub-Links Starts With : ")

						file_types_i = IOsys.safe_input(
							"\nEnter file formats (separate multiple by commas)\n *for extensions add . (ie: .png, .jpg, .mp3) or just write the category (ie: image, music, video): ")
						if file_types_i =="":
							file_types_i = "img"
						f_t =[]
						f_e=[]
						for i in file_types_i.split(","):
							_f = i.strip()
							if _f.startswith("."): f_e.append(_f)
							else: f_t.append(_f)
							
						self.P.file_types = f_t
						self.P.file_exts = f_e
						
						del _f,f_t,f_e,file_types_i
							

						# leach_logger('0M05x1||%s||f_types||%s'%(self.Project, str(self.file_types)), UserData.user_name)

						self.P.file_starts = IOsys.safe_input(
							"\nFile Links Starts With (if known or need to be specified): ")
						# leach_logger('0M05x1||%s||f_starts||%s'%(self.Project, self.file_starts), UserData.user_name)

						print('\n')

						self.P.file_to_sort = IOsys.asker("\n\n\u29bf Will download in sequential order? ", default=False)
						self.P.overwrite_bool = IOsys.asker(
							"\u29bf Will overwrite data??\nyes to overwrite old data if found.\nno to only download the updates\n>>", default=False)

						if not self.P.gen_sub_links():
							return 0


						if not self.P.gen_sub_dirs():
							return 0




				except LeachICancelError:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					leach_logger("000||0M05||%s||f-Stop||asking4sequence||probably user didnt get it" % self.P.Project)
					return 0

				except EOFError:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					leach_logger("000||0M05||%s||f-Stop||asking4sequence||probably user didnt get it" % self.P.Project)
					return 0

				except KeyboardInterrupt:
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					leach_logger("000||0M05||%s||f-Stop||asking4sequence||probably user didnt get it" % self.P.Project)
					return 0


			if not self.link_indexed:
				# leach_logger("0M05x2||%s||%i"%(self.Project, len(self.sub_links)), UserData.user_name)

				len_sub_links = len(self.P.sub_links)

				self.P.all_list = All_list_type(len_sub_links)




				xprint('Indexed [0 / ' + str(len_sub_links) + ']')

				try:

					index_thread_list = []
					for i in range(self.P.index_threads):
						index_thread_list.append(
							Process(target=self.P.generic_list_writer, args=(self.P.index_threads, i)))
						index_thread_list[i].start()

					while any([i.is_alive() for i in index_thread_list]):
						if self.P.break_all:
							return False
						time.sleep(0.3)

				except EOFError:
					leach_logger("000||0P0F||%s||f-Stop||is_indexing||probably something unwanted came")
					xprint("/yh/Project indexing cancelled by Keyboard/=/")
					self.P.break_all = True
					return 0
				except KeyboardInterrupt:
					leach_logger("000||0P0F||%s||f-Stop||is_indexing||probably something unwanted came")
					xprint("/yh/Project indexing cancelled by Keyboard/=/")
					self.P.break_all = True
					return 0

				except Exception as e:
					xprint("/rh/code: Error 0P0F\n The program will break in 5 seconds/=/")
					leach_logger(log(["0P0Fx0", self.P.Project, e.__class__.__name__, e]), UserData.user_name)
					self.P.break_all = True
					time.sleep(5)
					exit(0)

			if self.P.file_to_sort: self.P.all_list.all_links = natsort.natsorted(self.P.all_list.all_links,
			                                                                     key=lambda x: x[0].lower())

			Fsys.writer('projects.db', 'a', self.P.Project + '\n', 'data', '0M05')



		xprint('/y/ Processing /=/')
		Ctitle('[Processing] Project %s [%s%s] [:%i]' % (
			self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

		self.P.set_directories()

		self.P.store_current_data()

		print('\n')

		###########################################
		# self.P.clean_unknown_files()
		###########################################

		self.P.all_list.remove_duplicates()

		self.P.total = len(self.P.all_list)

		self.P.done -= self.P.errors  # to remove duplicate count


		# all_list_r = list(range(self.P.total))

		Ctitle('[Downloading] Project %s [%s%s] [:%i]' % (
			self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

		self.dl_threads = []
		for i in range(self.P.dl_threads):
			self.dl_threads.append(Process(target=self.P.downloader, args=[i]))
			self.dl_threads[i].start()
		self.dl_threads.append(Process(target=self.P.retry_errors))
		self.dl_threads[-1].start()

		if config.sp_arg_flag['max dlim'] != 0:
			self.P.tictoc = time.time()
			config.sp_arg_flag['chunk_size'] = int(config.sp_arg_flag['max dlim'] * 102.4) + 1
			t_dlim = Process(target=self.P.speed_limiter)
			t_dlim.start()
		else:
			t_dlim = Process()


		t_dl_speed = Process(target=self.P.speed_tester)
		t_dl_speed.start()




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





		if config.sp_arg_flag['disable dl cancel']:
			try:
				for i in self.dl_threads:
					i.join()

				if config.sp_arg_flag['max dlim'] != 0: t_dlim.join()
				t_dl_speed.join()

				Ctitle('[Download Complete] Project %s [%s%s] [:%i]' % (
					self.P.Project, config.mode_emoji[config.run_mod], config.run_mod.upper(), config.running_port))

				will_open = IOsys.safe_input()

			except EOFError:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True
			except KeyboardInterrupt:
				print("Hard cancel command entered! stopping")
				self.P.break_all = True



		else:
			while self.P.break_all == False and any(i.is_alive() for i in self.dl_threads + [t_dlim, t_dl_speed]):
				try:
					will_open = IOsys.safe_input()
				# print([i.is_alive() for i in self.dl_threads])
				except LeachICancelError:
					self.P.break_all = True
					leach_logger("000||0M05||%s||D-Break||~||~" % (self.P.Project))
					break
		# print(self.P.dl_chunks*config.sp_arg_flag["chunk_size"])
		if self.P.break_all:
			xprint("/yh/Project continuation cancelled by Keyboard/=/")
			leach_logger("000||0M05||%s||D-Stop||Downloading||%i|%i" % (self.P.Project, self.P.done, self.P.errors))
		else:
			if 'mangafreak' in self.P.sp_flags:
				try:
					first_page = self.P.make_html()
				except EOFError:
					leach_logger('7001x1||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

				except KeyboardInterrupt:
					leach_logger('7001x1||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0

				except Exception as e:
					leach_logger(log(['7001x0', self.P.Project, e.__class__.__name__, e]))
					print("Cancel command entered!\nReturning to main page")


			if will_open == 'b':
				Netsys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))
				return 0

			elif will_open == 'cbz':  # cbz
				try:
					first_page = self.P.make_cbz()
					print('CBZ Created in "%s"' % first_page)
				except EOFError:
					leach_logger('8001x1||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				except KeyboardInterrupt:
					leach_logger('8001x1||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0
				return



Keep_main_running = True


main = Main()
if __name__ == '__main__':
	leach_logger(log(['001', AboutApp._VERSION, UserData.Device_Data, UserData.user_ip, start_up_dt, Nsys.get_tz(),
	                  str(time.time() - start_up) + 's']))
	flush, flush_ = False, False
	try:
		main.make_required_dirs()
		main.get_user()


	except EOFError:
		xprint(Constants.hard_cancel)
		import sys
		sys.exit(0)
	except KeyboardInterrupt:
		xprint(Constants.hard_cancel)
		import sys
		sys.exit(0)
	except:
		traceback.print_exc()
		
		server_code.server_close()
		server_code.shutdown()
		exit(0)
		

	while Keep_main_running:
		main.make_required_dirs()
		try:
			flush_ = main.main_loop()
		except SystemExit:
			raise SystemExit
		except:
			traceback.print_exc()
			
			server_code.server_close()
			server_code.shutdown()

			try:
				flush_ = IOsys.safe_input("want to reload?")
				break
			except LeachICancelError:
				exit()
		if flush_ in ('y', 're', 'reload', 'yes'):
			flush = True
			break

	if flush:
		server_code.server_close()
		server_code.shutdown()
		# re-open current python file
		exec(open(os.path.abspath(__file__), encoding='utf-8').read(), globals())
		exit()