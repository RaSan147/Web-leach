# pylint: disable=anomalous-backslash-in-string
import mimetypes
from os.path import realpath as os_realpath
# for testing
Project = main_link = link_startswith = file_types = file_starts = sub_dirs = sp_flags= sp_extension = overwrite_bool = dimention = dl_done = sequence = sub_links = has_missing = dir_sorted = 0

from platform import system as os_name
os_name = os_name()

from requirements import  requirements_all, requirements_win

from random import  randint

process_id = randint(2003, 9999)

class Constants:
	"""Stores most commonly used constants
	"""

	# file types
	all_image_types = "3FR 3G2 3GP ARW AVI CANVAS CAPTION CR2 CR3 CRW CUBE CUT DCM DCR DCRAW DFONT DNG EMF ERF FILE FRACTAL FTP GRADIENT HALD HEIC HEIF HTTP HTTPS IIQ JNX K25 KDC LABEL MAC MEF MRW NEF NRW ORA ORF OTF PANGO PATTERN PEF PES PFA PFB PIX PLASMA PWP RADIAL-GRADIENT RAF RAW RGB565 RLA RLE RMF RW2 SCR SCREENSHOT SCT SFW SR2 SRF STEGANO TEXT TILE TIM TM2 TTC TTF WMF WPG X3F XC XCF XPS JPG PNG TIFF GIF WEBP BMP EPS PDF APNG A AAI AI ART AVIF AVS B BGR BGRA BGRO BMP2 BMP3 C CAL CALS CIN CLIP CLIPBOARD CMYK CMYKA CUR DATA DCX DDS DPX DXT1 DXT5 EPDF EPI EPSF EPSI EPT EPT2 EPT3 EXR FARBFELD FAX FF FITS FL32 FLIF FLV FTS G G3 G4 GIF87 GRAY GRAYA GROUP4 HDR HRZ ICB ICO ICON INLINE IPL J2C J2K JNG JP2 JPC JPE JPEG JPM JPS JPT JXL K M M2V M4V MAP MASK MAT MIFF MKV MNG MONO MOV MP4 MPC MPEG MPG MSL MSVG MTV MVG NULL O OTB PAL PALM PAM PBM PCD PCDS PCL PCT PCX PDB PDFA PFM PGM PGX PHM PICON PICT PJPEG PNG00 PNG24 PNG32 PNG48 PNG64 PNG8 PNM POCKETMOD PPM PS PSB PSD PTIF R RAS RGB RGBA RGBO RGF RSVG SGI SIX SIXEL SUN SVG SVGZ TGA TIFF64 TXT UYVY VDA VICAR VID VIFF VIPS VST WBMP WEBM WMV XBM XPM XV Y YCbCr YCbCrA YUV ASHLAR BRF CIP EPS2 EPS3 HISTOGRAM HTM HTML INFO ISOBRL ISOBRL6 JSON MATTE PS2 PS3 SHTML SPARSE-COLOR THUMBNAIL UBRL UBRL6 UIL YAML A AAI APNG ASHLAR AVIF AVS B BGR BGRA BGRO C CLIP CMYK CMYKA DATA DCX DDS DXT1 DXT5 EPS3 EPT3 FAX FLIF FLV G GIF GRAY GRAYA HDR ICO INFO INLINE IPL JSON K M M2V M4V MASK MAT MATTE MIFF MKV MNG MOV MP4 MPC MPEG MPG MSL MSVG MTV O PALM PAM PBM PCL PDB PDF PDFA PFM PGM PHM PNM POCKETMOD PPM PS PS2 PS3 PSB PSD PTIF R RAS RGB RGBA RGBO RSVG SGI SPARSE-COLOR SUN SVG SVGZ THUMBNAIL TIFF TIFF64 TXT VID VIFF VIPS WEBM WEBP WMV XV Y YAML YCbCr YCbCrA".lower().split()
	all_video_types = "webm mkv flv vob ogv ogg drc gif apng gifv mng avi mts m2ts ts mov qt wmv yuv rm rmvb viv ask amv mp4 m4p m4v mpg mp2 mpeg mpe mpv m2v 3gp 3g2 mxf roq nsv flv f4v f4p f4a f4b asf wmv avi divx evo avi mkv mk3d m2p ps mpg m2ts mxf ogg ogv ogx mov qt vob mpa mpe mpv2 lsf lsx asf asr asxavi movie".lower().split()
	all_audio_types = "3gp aa aac aax act aiff alac amr ape au awb dss dvf flac gsm iklax ivs m4 m4b m4p mmf mp3 mpc msv nmf ogg oga mogg opus ra rm raw rf64 sln tta voc vox wav wma wvwebm 8svx cda snd mid rmi aif aifc m3u ra ram".lower().split()

	# DLC links
	who_r_u = 'https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
	yamatte = ('https://www.myinstants.com/media/sounds/yamatte.mp3', 'https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3')

	# conversation words
	yes = ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yep', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yep', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yep')
	no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
	cond = yes + no
	condERR = "/y/Sorry,  I can't understand what you are saying./=/\n Just type yes or no.   "
	hard_cancel = '/y/Hand Cancel Command entered.\nExiting.../=/'

	special_starts = {'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://[^\/]+\.mangafreak.net/(?:M|m)anga/([^\?\#]+)',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(?:_\d+)[\?\#]?.*',
		'mf_read_chap':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(_\d+)[\?\#]?.*',
		'webtoon_ep':'https\:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/.*?\/viewer\?title_no\=(\d+)\&episode_no\=\d+',
		'webtoon': 'https:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/list\?title_no=(\d+)'}

	extensions_map = mimetypes.types_map.copy()
	extensions_map.update({
		'': 'application/octet-stream', # Default
		'.py': 'text/plain',
		'.c': 'text/plain',
		'.h': 'text/plain',
		})

	old_img = ('jpeg', 'jpg', 'png', 'gif', 'webp', 'bmp', 'tif')

	DEFAULT_DISABLE_LIB_CHECK = False # temporarily disabled

true = True
false = False
none = None


def leach_logger(*args):
	pass

def log(arr):
	
	for i in range(len(arr)):
		if type(arr) is str:
			continue
		if type(arr[i]) is bytes:
			arr[i] = arr[i].decode('utf-8')
		else:
			arr[i] = str(arr[i])

	return "||".join(map(str, arr))

class __Make_proxy:
	def make_pages(self, *args):
		pass
	def make_cbz(self, *args):
		pass

MakeHtml = MakeCbz = None

class AboutApp_:     #fc=A000
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
	cloud_html_temp_link = 'https://raw.githack.com/RaSan147/Web-Leach_pub/main/page_template/wl-page-v2.html'
	cloud_html_temp_link_proxy = 'https://gitcdn.link/cdn/RaSan147/Web-Leach_pub/main/page_template/wl-page-v1.html'

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


class DefaultConfig:  # fc=0200
	""" Default configuration to load up on each start"""

	disable_lib_check = Constants.DEFAULT_DISABLE_LIB_CHECK
	# if True, the installed lib check will be skipped to speed up
	has_all_libs = None
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






class AppConfig_(DefaultConfig):     #fc=0300
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
		self.user_list = ['bec6113e5eca1d00da8af7027a2b1b070d85b5ea', 'eb23efbb267893b699389ae74854547979d265bd']
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



		self.process_id = process_id
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
			
			TODO: make offline available  *idk how works offline* figured it out ✌🏻"""
		if missing is None:
			missing = [1, 2, 3, 4]
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

			return 'online' if err_print else 'offline'

		except Exception as e:
			print(rcrypto.decrypt(Fsys.reader(AboutApp.temp_dir + 'updateL.ext'), "lock").strip())
			print(e.__class__.__name__, ": Unknown error occurred. Error code 0306x0\nPlease inform the author.")
			leach_logger(log(["0306x0", Netsys.hdr(Netsys.current_header, '0306'), link, e.__class__.__name__, e, message]), 'lock')
			time.sleep(5)
			exit(0)

