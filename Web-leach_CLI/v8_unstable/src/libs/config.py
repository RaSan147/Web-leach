from os.path import realpath as os_realpath, isdir as os_isdir
from random import randint
from os import rename, getpid as os_getpid
from hashlib import sha1 as hashlib_sha1
from html import unescape as html_unescape, escape as html_escape


from platform import system as _os_name
os_name = _os_name()

from constants import Constants
import rcrypto
import Number_sys_conv as Nsys

requirements_all = ('requests', 'beautifulsoup4', 'natsort', 'google', 'rjsmin')
requirements_win = ('pywin32-ctypes', 'comtypes', 'psutil', 'lxml', 'pywin32')


def get_pid():
	return os_getpid()%1000


class AboutApp_ :     #fc=A000
	""" Contains Information about the app and verion details"""

	_VERSION = '8.001'
	_Vcode = '008001'
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

	
	LOGGER = True

	disable_lib_check = Constants.DEFAULT_DISABLE_LIB_CHECK
	# if True, the installed lib check will be skipped to speed up
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

	running_port = 0
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

		self.process_id = get_pid()

		self.has_all_libs = None
		self.__update__G = 'pass'
		self.__update__L = 'pass'
		self.user_list = ['eb23efbb267893b699389ae74854547979d265bd', 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3']
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

config = AppConfig_()


def log(arr):
	
	for i in range(len(arr)):
		if type(arr) is str:
			continue
		if type(arr[i]) is bytes:
			arr[i] = arr[i].decode('utf-8')
		else:
			arr[i] = str(arr[i])

	return "||".join(arr)


def leach_logger(io, key=None, retry =False):  # fc=0503 v
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the beginning)

	args:
	-----
		io: the log message\n
		key: salt text"""
	key = "".join(map(str, [randint(1,100) for i in range(10)]))
	if config.sp_arg_flag['no log']:
		return None
	try:
		while True:
			if 1: # too lazy to remove tabs
				try:
					_key = "SECret"
					salt = hashlib_sha1(key.encode()).hexdigest()[:-6] + AboutApp._Vcode
					with open(AboutApp.data_dir+"userlog.leach", "ab") as f:
						f.write(rcrypto.encrypt(log([salt + Nsys.compressed_dt() ,str(config.process_id), html_escape(io), '']), _key).encode('utf-8') + b'\n')
					return
				except (KeyboardInterrupt, EOFError):
					pass
		
			

	except (KeyboardInterrupt, EOFError):
		if retry: return
		leach_logger(io, 'lock', True)


#test
def input_from_file(filename):
	import sys
	sys.stdin = open(filename)
	n=1
	line = ""
	while line!="q":
		line = input()
		print([n, line])
		
#test   input_from_file()