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


# importing required packages

import libs.Number_sys_conv as Nsys  # fc=1000

# different number based functions I made
start_up_dt = Nsys.compressed_dt()  # stores when the program was launched

import time

start_up = time.time()

from platform import system as os_name
os_name = os_name()

from shutil import get_terminal_size

if os_name == 'Windows':
	from libs import console_mod     #fc=2000
	console_mod.enable_color2() # to test

from libs.print_text2 import xprint, oneLine  # fc=3000

oneline = oneLine()
xprint('/=/', end='')

try:
	from libs.constants import *  # fc=4000

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

	from subprocess import call as subprocess_call
	from os import _exit as os_exit
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
	from random import choice as random_choice
	from hashlib import sha1 as hashlib_sha1
	import re
	from re import search as re_search, compile as re_compile, sub as re_sub, findall as re_find_all

	from libs.filesize import alternative as filesize_alt, size as filesize_size

	from libs import rcrypto  # fc=5000
	#import libs.gen_uuid as uuid
	###################################

	# FILE system tools###############
	from os import makedirs, remove, rename, system as os_system, listdir as os_listdir
	from shutil import rmtree as rmdir
	from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile
	from zipfile import ZipFile, BadZipFile
	#import io	###################################



	from threading import Thread as Process



	# HTML tools##############################
	from html import unescape as html_unescape
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
		import libs._server003_ as _server001_

		if os_name == 'Windows': import libs.mplay4 as mplay4

		has_all_libs = True

	except:
		has_all_libs = False


	#from libs.headers_file import header_list
	##########################################

	# Other Libs###############################
	from collections import Counter
	#from functools import reduce as functools_reduce
	#from operator import iconcat as operator_iconcat
	
	import json

	from libs import dig_info  # fc=6000

	##########################################
except (KeyboardInterrupt, EOFError):
	xprint(Constants.hard_cancel)
	import sys
	sys.exit(0)


# Re Define to speed up###################
len = len
range = range
##########################################


# a process ID to identify use multiple windows in the same time from log
boss = 0
server_launcher = Process(target= null_func)
"""
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
####################################################"""
from libs.ERR import LeachUnknownError, LeachNetworkError, LeachCorruptionError, Error404

print(2) # x

from libs.config import AboutApp, requirements_win, requirements_all, leach_logger, log

from libs.config import config

from libs.FNDsys import (Fsys, Netsys, Datasys, IOsys, NetErrors, push_config as FND_push_config,
LeachICancelError, LeachKnownError, LeachPermissionError)

FND_push_config(config)

print(3)  # x


print(4)  # x


@atexit.register
def on_exit():  # fc=XXXX
	server_code.server_close()
	server_code.shutdown()
	server_launcher._stop()
	pass


print(5)  # x


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
				except (KeyboardInterrupt, EOFError):
					raise LeachICancelError
					
				except LeachICancelError:
					leach_logger(log(['0705x0',f_code, func.__name__, 'input exit code L&infin;ping for unknown reason']))
			except (KeyboardInterrupt, EOFError):
				raise LeachICancelError
		except (KeyboardInterrupt, EOFError):
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
		except (KeyboardInterrupt, EOFError): pass
		
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
			import libs._server003_ as _server001_
			print(7.6)  # x
			if os_name == "Windows": import libs.mplay4 as mplay4

		except:
			if failed:
				traceback.print_exc()
				xprint("/r/Failed to load required libraries.\n/=//yh/Possible cause 1st initialization without internet")

			else:
				self.import_missing_libs(failed=True)


OSsys = OSsys_()

if __name__ == '__main__':
	OSsys.import_missing_libs()

print(7)  # x

Netsys.init() # to import requests and patch NetErrors

print(8)  # x

from libs.User_Data import UserData, push_config as UserData_push_config
UserData_push_config(config)
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





print(11)  # x

print(12)  # x

print(13)  # x


# print(ProjectType.get_page('htps://ratulhasan14789.github.io/fuck'))



class Server:  # fc=
	
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

		Ctitle("WL ~ Running PORT:%i"%config.running_port)


		try:
			if config.server_status in (False, None):
				if cd != '.':
					return _server001_.run_server(port, cd, AboutApp.temp_dir)
				else:
					return _server001_.run_server(port, data_dir=AboutApp.temp_dir)
			else:
				return 0
		except (KeyboardInterrupt, EOFError):
			pass

		except OSError: #TODO: add note in files
			if config.LOGGER: traceback.print_exc()
			leach_logger(log(['0807x-1', f_code, port, cd]))

	def run_server_t(self, cd='.'):  # fc=0808 v
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
		
		server_status = Netsys.check_server("http://localhost:%i" % UserData.user_primary_port, '0M04', timeout=5)

		if config.server_status:
			return
			
		if server_status:
			config.server_running = True
			return

		elif server_status in (False, None):
			config.running_port = UserData.user_primary_port

			port = config.running_port  # user specified port or proxy port
			try:
				_t = self.run_server(port=port, cd=cd)
			except OSError:
				try:
					config.running_port = UserData.user_secondary_port

					port = config.running_port 
					 
					_t = self.run_server(port=port, cd=cd)
				except OSError:
					xprint("/rhi/Failed to run local server/=/")
					return
					
		else:
			exit()

		# xprint("\n/i/ Running port /=/ :", config.running_port)
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

		if config.sp_arg_flag['no browser'] or port==None: return 0

		webbrowser.open_new_tab('http://localhost:%i/%s' % (port, host_dir))

Serversys = Server()


from libs.DS import ProjectType_, All_list_type, SubDirs_Type, push_config as DS_push_config
DS_push_config(config)


class Main :  # fc=0M00
	def __init__(self):  # fc=0M01
		IOsys.delete_last_line()
		print("Connecting to server...")
		Ctitle('Connecting to server 🌐')
		self.dl_threads = []

	def get_user(self):  # fc=0M02
		UserData.get_user_ip()

		server_ping = time.time()
		config.run_mod = UserData.god_mode()
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
		
		UserData.user_secondary_port = (int(UserData.userhash, 16) % (64000 - 60001 + 1)) + 60001
		#
		
		server_launcher = Process(target=Serversys.run_server_t, args=(AboutApp.download_dir,))
		server_launcher.start()

	def main_loop(self):  # fc=0M05
		global Keep_main_running
		self.boot_server()
		Netsys.Cache_clear()

		Ctitle("Web Leach")
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
				except (KeyboardInterrupt, EOFError):
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
  11   /y/?online-page/=/               make online version of the site using original image links as src

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
  -11  /g/?o/=/                      same as 11
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

			elif __command in ["?edit-page", "?e"]:
				p_name = IOsys.safe_input("Enter the project name: ")
				self.P = ProjectType_(p_name)
				check_project = self.P.load_data(p_name)
				if check_project:
					self.P.edit_page()
				else:
					print('Project not found')

			elif __command in ["?test", "?t"]:
				proj = IOsys.safe_input("Enter Project name: ")
				
				self.P = ProjectType_(proj)
				check_project = self.P.load_data(proj)
				print(check_project)
				if check_project:
					sub_dirs = SubDirs_Type()
					sub_dirs.import_from_All_list_type(self.P.all_list, self.sub_links, self.sub_dirs)

				
			elif __command in ["?online-page", "?o"]:
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
					Serversys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))
				pass

			elif __command in ['?re', "?reload"]:
				return "reload"


			else:
				break


			
			
		self.P = ProjectType_(self.COMM)
		check_project = self.P.load_data(self.COMM)
		# print(check_project)
		Ctitle(f'Project {self.P.Project} [{config.mode_emoji[config.run_mod]}] [:{config.running_port}]')
		
		self.ask_for_links = True # ask for main link, sub_link bla bla bla
		
		if not check_project: # =0 no project found
			if any(i in '\\/|:*"><?' for i in __command):
				print("\n>> Project name can't have ")
				print("\\ / | : * \" > < ?\n".center(20))
				return 0

		if check_project==2: # both project and list found
			self.P.store_current_data() # patches if something wrong
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

					self.P.import_make()
					self.P.manga_freak_patch()
					if temp == 'browser':
						try:
							first_page = self.P.make_html()
							if not first_page:
								xprint('Failed to generate sub-page. /y/wl-page.html not found/=/')
								leach_logger(log(['7002x1', self.P.Project, AboutApp.cloud_html_temp_link]))
								return 0
							

							Serversys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))


						except (KeyboardInterrupt, EOFError):
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
						except (KeyboardInterrupt, EOFError):
							leach_logger('8001x1||' + self.P.Project)
							print("Cancel command entered!\nReturning to main page")
							return 0
							
						return 0

				elif temp == 'fresh':
					#TODO: Need logging

					Project = self.P.Project
					self.P = ProjectType_(Project)
					# self.P.existing_found = False
				# leach_logger('11000x1||%s'%self.P.Project, UserData.user_name)

				elif temp is True:
					#TODO: Need logging
					# self.P.existing_found = False
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

		elif check_project == 0:
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


							except (KeyboardInterrupt, EOFError):
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

					except (KeyboardInterrupt, EOFError):
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






					except (KeyboardInterrupt, EOFError):
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


									except (KeyboardInterrupt, EOFError):
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

				except (KeyboardInterrupt, EOFError):
					xprint('\n/yh/Cancellation command entered, returning to main menu.../=/\n\n')
					leach_logger("000||0M05||%s||f-Stop||asking4sequence||probably user didnt get it" % self.P.Project)
					return 0




			if not self.link_indexed:
				# leach_logger("0M05x2||%s||%i"%(self.Project, len(self.sub_links)), UserData.user_name)

				len_sub_links = len(self.P.sub_links)

				self.P.all_list = All_list_type(len_sub_links)



				oneline.new()
				oneline.update('Indexed [0 / ' + str(len_sub_links) + ']')

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

				except (KeyboardInterrupt, EOFError):
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

			if self.P.file_to_sort: 
				self.P.all_list.all_links = natsort.natsorted(self.P.all_list.all_links,
															key=lambda x: x[0].lower())

			Fsys.writer('projects.db', 'a', self.P.Project + '\n', 'data', '0M05')



		xprint('/y/ Processing /=/')
		print(config.run_mod)
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
		
		xprint('Downloaded [/gh/', ('━'*0), '/=h/╺' if 0<30 else '━', '━'*(30-0), '/=/][', self.P.done, '/', self.P.total, ']', self.P.current_speed , '/s', sep="")

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

		self.P.import_make()

		if not 'mangafreak' in self.P.sp_flags:
			try:
				first_page = self.P.make_html()
			except (KeyboardInterrupt, EOFError):
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

			except (KeyboardInterrupt, EOFError):
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
				except (KeyboardInterrupt, EOFError):
					leach_logger('7001x1||' + self.P.Project)
					print("Cancel command entered!\nReturning to main page")
					return 0



				except Exception as e:
					leach_logger(log(['7001x0', self.P.Project, e.__class__.__name__, e]))
					print("Cancel command entered!\nReturning to main page")


			if will_open == 'b':
				Serversys.run_in_local_server(config.running_port, host_dir='%s/index.html' % (self.P.Project))
				return 0

			elif will_open == 'cbz':  # cbz
				try:
					first_page = self.P.make_cbz()
					print('CBZ Created in "%s"' % first_page)
				except (KeyboardInterrupt, EOFError):
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

	except LeachICancelError:
		xprint(Constants.hard_cancel)
		import sys
		sys.exit(0)

	except (KeyboardInterrupt, EOFError):
		xprint(Constants.hard_cancel)
		import sys
		sys.exit(0)
	except SystemExit:
		raise SystemExit
	except Exception as err:
		print(isinstance(err, LeachICancelError))
		traceback.print_exc()
		print(err)
		print(err.__class__.__name__)
		
		server_code.server_close()
		server_code.shutdown()
		exit()
		

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
				Keep_main_running = False
			except LeachICancelError:
				exit()
	if flush_ in ('y', 're', 'reload', 'yes'):
		flush = True

	if flush:
		server_code.server_close()
		server_code.shutdown()
		# re-open current python file
		exec(open(os.path.abspath(__file__), encoding='utf-8').read(), globals())
		exit()