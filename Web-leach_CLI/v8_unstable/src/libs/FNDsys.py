# Fsys, Netsys, Datasys
import os, traceback, time, json, io
from html import unescape as html_unescape, escape as html_escape
from os.path import isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname
from re import compile as re_compile, sub as re_sub
from random import choice as random_choice
from os import remove, system as os_system
from functools import reduce as functools_reduce
from operator import iconcat as operator_iconcat
from sys import stdout as sys_stdout
sys_write = sys_stdout.write

from urllib import parse

from headers_file import header_list
from constants import Constants
from ERR import LeachICancelError, LeachKnownError, LeachPermissionError

from response_cache import Cached_Response
import gen_uuid as uuid
from config import AboutApp, os_name, leach_logger, log, config
import Number_sys_conv as Nsys


from print_text2 import xprint

NetErrors = Exception # to patch unimported libs, will be replaced later

try:
	import requests, urllib3
	from bs4 import BeautifulSoup as bs
except:
	requests, urllib3, bs = 0,0,0
config = config
def push_config(config_):
	global config
	config = config_

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
						os.makedirs(locs, exist_ok=True)
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
			global logger
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

		self.data_vars = ("cached_webpages", "cached_link_facts")
		self.cached_webpages = dict()
		self.cached_link_facts = dict()

		self.PARSER = None # parser lxml or html.parser

	def init(self):
		global requests, urllib3, NetErrors, bs
		import requests, urllib3
		
		from bs4 import BeautifulSoup as bs

		NetErrors = (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError,
			 requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.MissingSchema,
			 requests.exceptions.InvalidSchema, requests.exceptions.SSLError, urllib3.exceptions.SSLError)

		if self.PARSER is None:
			self.PARSER = 'lxml'
			try:
				bs('<br>', self.PARSER)
			except:
				self.PARSER = 'html.parser'



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


	def Cache_add_webpage(self, url, response):
		""" Add a webpage to the cache
		url: url of the webpage 
		response: response object"""

		# TODO: use JSON

		__x = Cached_Response(status_code=response.status_code, headers=response.headers, content=response.content,
		                      encoding=response.encoding, url=response.url)
		file_id = str(config.process_id) + '-' + uuid.random()
		with open(AboutApp.cached_webpages_dir + file_id, 'w') as f:
			f.write(repr(__x))
		self.cached_webpages[url] = file_id

	def Cache_get_webpage(self, url):
		""" Get a webpage from the cache
		url: url of the webpage """

		if url in self.cached_webpages:
			if os_isfile(AboutApp.cached_webpages_dir + self.cached_webpages[url]):
				with open(AboutApp.cached_webpages_dir + self.cached_webpages[url], 'r') as f:
					__x = eval(f.read()) # TODO: remove it. use JSON
				return __x

		return None

	def Cache_clean_webpages(self):
		""" Cleans the cached_webpages from storage"""
		for i in os.listdir(AboutApp.cached_webpages_dir):
			if i.startswith(str(config.process_id) + '-'):
				try:
					remove(AboutApp.cached_webpages_dir + i)
				except:
					pass

	def Cache_clear(self):
		"""Cleans both from memory and storage""" 
		self.Cache_clean_webpages()
		for i in self.data_vars:
			self.__dict__[i].clear()



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
		if link in self.cached_link_facts:
			return self.cached_link_facts[link]
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

			self.cached_link_facts[link] = facts
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
			if link in self.cached_webpages:
				__x = self.Cache_get_webpage(link)
				# print(__x)
				if __x is not None:
					return __x

		if session is None:
			session = requests

		if not referer:
			referer_ = self.get_homepage(link)
		else:
			referer_ = referer

		if header is None:
			current_header = self.header_(referer_)
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
				self.Cache_add_webpage(link, page)
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


		self.current_header = self.header_()
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
				leach_logger(log([server_error_code, self.hdr(self.current_header, '080D'), link, file.status_code]), 'lock')
				if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%server_error_code)
				returner = False
		except NetErrors as e:
			if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%internet_error_code)
			leach_logger(log([internet_error_code, self.hdr(self.current_header, '080D'), link, e.__class__.__name__, e]), 'lock')
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
			# delete current line
			sys_write('\x1b[2K')
			
			# cursor up one line
			sys_write('\x1b[1A')

			# delete last line
			sys_write('\x1b[2K')

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
				except (KeyboardInterrupt, EOFError):
					if on_error == LeachICancelError:
						raise LeachICancelError
					else:
						return on_error
				# except LeachICancelError:
				# 	# leach_logger('000||0000F||~||~||~||input exit code L&infin;ping for unknown reason')
				# 	exit(0)
			except (KeyboardInterrupt, EOFError):
				if on_error == LeachICancelError:
					raise LeachICancelError
				else:
					return on_error
		except (KeyboardInterrupt, EOFError):
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
#leach_logger = IOsys.leach_logger
