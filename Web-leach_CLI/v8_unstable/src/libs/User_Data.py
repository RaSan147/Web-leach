import time
import requests
from hashlib import sha1 as hashlib_sha1
from os.path import isfile as os_isfile, exists as os_exists, isdir as os_isdir
from os import rename



from config import log, leach_logger, config, os_name, AboutApp
from constants import Ctitle, Constants
from print_text2 import xprint
import dig_info
import FNDsys
import rcrypto

from FNDsys import (Fsys, Netsys, Datasys, IOsys, NetErrors, push_config as FND_push_config,
LeachICancelError, LeachKnownError, LeachPermissionError)


config = config
def push_config(config_):
	global config
	config = config_
	FND_push_config(config)

Netsys.init()

if os_name == 'Windows':
	import mplay4

boss = 0
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
		Ctitle("User Log In")
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
							if self.god_mode(1) == 'offline':
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



UserData = UserData_()
