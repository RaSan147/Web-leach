from re import  compile as re_compile
from html import unescape as html_unescape, escape as html_escape
from random import  choice as random_choice

from  headers_file import  header_list

from print_text import  xprint

from constants import  log

class Netsys_:  # fc=0800
	"""Network system functions"""

	def __init__(self, CacheData, leach_logger):  # fc=0801 v
		""" initializes important variables """
		self.CacheData = CacheData
		self.leach_logger = leach_logger
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

			self.leach_logger(log(['0803x1', f_code, header]))
			return str((-1, header))

		except Exception as e:
			xprint("/y/Some error occurred caused, possible cause: DATA CORRUPTION\nError code: 00009x" + f_code, '/=/')

			self.leach_logger(log(['0803x1', f_code, header, e.__class__.__name__, e]))
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
					self.leach_logger('||'.join(map(str,['0806x2', f_code, link, self.hdr(current_header, '0806'), timeout, r.status_code])))
		except NetErrors as e:
			if not no_log:
				self.leach_logger('||'.join(map(str,['0806x2', f_code, link, self.hdr(current_header, '0806'), timeout, e.__class__.__name__, e])))
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
				r - requests.head('https://www.bing.com', headers = self.header_())

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
			self.leach_logger(log(['0807x1', f_code, port, cd]))
			time.sleep(5)
			os_exit(1)

		if not os_isdir(cd):  # invalid missing directory
			xprint('\n/y/' + cd, "not found!\nPlease inform the author\nError code: 0000Bx3/=/")
			self.leach_logger(log(['0807x2', f_code, port, cd]))
			time.sleep(5)
			os_exit(1)

		try:
			if config.server_status in (False, None):
				if cd != '.':
					return _server001_.run_server(port, cd)
				else:
					return _server001_.run_server(port)
			else:
				return 0
		except EOFError:
			pass
		except KeyboardInterrupt:
			pass
		except OSError: #TODO: add note in files
			traceback.printexec()
			self.leach_logger(log(['0807x-1', f_code, port, cd]))

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
					self.leach_logger(log(['080Ax2', link, f_code, response.status_code, response.text[:20]]))
					return False  # not web-leach server or older server

			else:
				self.leach_logger(log(['080Ax3', link, f_code, response.status_code]))
				return False  # not web-leach server

		except (requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout, requests.exceptions.SSLError,
		        urllib3.exceptions.SSLError) as e:
			self.leach_logger(log(['080Ax1', link, f_code, e.__class__.__name__, e]))
			return 2

		except requests.exceptions.ConnectionError:
			return None  # port is open

		except EOFError:
			return 2
		except KeyboardInterrupt:
			return 2

		except Exception as e:
			self.leach_logger(log(['080Ax0', link, f_code, e.__class__.__name__, e]))
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
				self.leach_logger(log([server_error_code, Netsys.hdr(self.current_header, '080D'), link, file.status_code]), 'lock')
				if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%server_error_code)
				returner = False
		except NetErrors as e:
			if err_print: xprint("/rh/Error code: %s\nNo internet connection!/=/\nRunning offline mode"%internet_error_code)
			self.leach_logger(log([internet_error_code, Netsys.hdr(self.current_header, '080D'), link, e.__class__.__name__, e]), 'lock')
			returner = False

		if not returner and allow_old:
			return os_isfile(file_loc + filename)
