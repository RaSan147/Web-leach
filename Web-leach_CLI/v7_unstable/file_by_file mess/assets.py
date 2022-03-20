from constants import *  # fc=4000

import gen_uuid as uuid
config = AppConfig_()
	
from os.path import isfile as os_isfile
from os import listdir as os_listdir, remove
from IOsys import IOsys_
from Fsys import Fsys_
from Datasys import  Datasys_
from response_cache import  Cached_Response

class CachedData_:  # fc=0C00
	def __init__(self):  # fc=0C01
		self.data_vars = ("cached_webpages", "cached_link_facts")
		self.cached_webpages = dict()
		self.cached_link_facts = dict()

	def add_webpage(self, url, response):
		""" Add a webpage to the cache
		url: url of the webpage 
		response: response object"""

		__x = Cached_Response(status_code=response.status_code, headers=response.headers, content=response.content,
		                      encoding=response.encoding, url=response.url)
		file_id = str(config.process_id) + '-' + uuid.random()
		with open(AboutApp.cached_webpages_dir + file_id, 'w') as f:
			f.write(repr(__x))
		self.cached_webpages[url] = file_id

	def get_webpage(self, url):
		""" Get a webpage from the cache
		url: url of the webpage """

		if url in self.cached_webpages:
			if os_isfile(AboutApp.cached_webpages_dir + self.cached_webpages[url]):
				with open(AboutApp.cached_webpages_dir + self.cached_webpages[url], 'r') as f:
					__x = eval(f.read())
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

from Netsys import  Netsys_


IOsys = IOsys_(config)
leach_logger = IOsys.leach_logger
Datasys = Datasys_(leach_logger)
Fsys = Fsys_(IOsys, leach_logger)
Fsys.get_file_name("fuc/k", "url")
Netsys = Netsys_(CachedData, leach_logger)


