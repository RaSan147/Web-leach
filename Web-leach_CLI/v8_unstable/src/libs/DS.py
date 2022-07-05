import json
import time
import traceback
from collections import Counter
from html import unescape as html_unescape
from math import floor
import os
from os import listdir as os_listdir
from os import makedirs, remove, rename
from os import system as os_system
from os.path import exists as os_exists
from os.path import isdir as os_isdir
from os.path import isfile as os_isfile
from os.path import splitext as os_splitext
from re import compile as re_compile
from re import findall as re_find_all
from re import search as re_search
from re import sub as re_sub
from shutil import get_terminal_size
from shutil import rmtree as rmdir
from sys import getsizeof
from sys import stdout as sys_stdout
sys_write = sys_stdout.write

from threading import Thread as Process
from urllib import parse

from zipfile import BadZipFile, ZipFile
import re


import natsort
from googlesearch import search as g_search

import requests
import urllib3
from bs4 import BeautifulSoup as bs

import Number_sys_conv as Nsys
from config import AboutApp, leach_logger, log, config
from constants import Constants, Ctitle
from filesize import alternative as filesize_alt
from filesize import size as filesize_size
from print_text2 import oneLine, xprint
oneline = oneLine()


from FNDsys import (Fsys, Netsys, Datasys, IOsys, NetErrors, push_config as FND_push_config,
LeachICancelError, LeachKnownError, LeachPermissionError)


config = config
def push_config(config_):
	global config
	config = config_
	FND_push_config(config)

Netsys.init()

from User_Data import UserData


class SubDirs_Type:  # fc=
	""" SubDirs_Type class """
	def __demo__(self):  # fc=
		self.sub_dirs = [['http..../dir1', 'dir1'],...] #[[link, name]]

		self.all_links = [["http.../file.png", ...] ,...] # [[file links]]
		self.all_names = [["file.png", ...] ,...] # [[file names]]

		self.sub_dir_order = [2,4,3,...] # how the dirs are ordered or sorted
		# self.sub_dir_order won't be used until creating web-pages
		# always use this index when making web-pages

		self.len = 6966 # total number of files

	def __init__(self, sub_dirs_len, sub_dirs=None, all_links=None, all_names=None, dl_links=None):  # fc=
		self.sub_dirs = [[None, None] for _ in range(sub_dirs_len)]
		self.all_links = [[] for _ in range(sub_dirs_len)]
		self.all_names = [[] for _ in range(sub_dirs_len)]
		self.sub_dir_order = [i for i in range(sub_dirs_len)] # keeps same as how they are present in the websites

		self.dl_links = None
		self.len = 0
		
		if sub_dirs and all_links and all_names and dl_links:
			self.sub_dirs = sub_dirs
			self.all_links = all_links
			self.all_names = all_names
			self.dl_links = all_links
			
			self.gen_len()



	
	def __getitem__(self, indx) -> list:  # fc=
		""" Get the link at the given index 
		returns [link, name, dir_name] """
		if self.dl_links == None:
			self.gen_dl_links()
			
		d_i, l_i = self.dl_links[indx] # dir_index, link_index in sub_dir
			
		return [self.all_links[d_i][l_i], self.all_names[d_i][l_i], self.sub_dirs[d_i]]

	def __len__(self):  # fc=
		""" Get the length of the list """
		return len(self.sub_dirs)

	def add_link(self, link, dir_indx, name=None, ext=None):  # fc=
		""" Add a link to the sub_links list
		link: link to add
		dir_indx: index of the directory
		name: name of the file (optional)
		ext: extension of the file (optional) """


		# if name is not False: # False when using mangafreaks?? totally not sure
		if name is None:
			name = self.get_name(link, ext=ext)
		
		self.add_name(name, dir_indx)
		
		self.all_links[dir_indx].append(link)

		self.len += 1

	def gen_len(self): # fc=
		""" Generate the len of the all_links list """
		self.len = sum([len(i) for i in self.all_links])


	def get_name(self, link, ext=None) ->str:  # fc=
		""" Get the name of the link
		link: link to get the name from
		ext: extension of the file (optional) """

		name = Fsys.get_file_name(link, 'url')
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
		
		return name

	def purify_duplicate_name(self, name, dir_indx):  # fc=
		name_, _, ext_ = name.rpartition('.')
		n = 1

		# X = ''.join((name_, '(', str(n), ')', '.', ext_))

		for i in range(len(self.all_names[dir_indx]) - 1, 0, -1):
			dup = self.all_names[dir_indx][i]
			if dup.startswith(name_ + '(') and dup.endswith(
					')' + '.' + ext_):
				if dup[len(name_) + 1:-len(ext_) - 2].isdigit():
					n = int(dup[len(name_) + 1:-len(ext_) - 2]) + 1
				name = ''.join((name_, '(', str(n), ')', '.', ext_))

				if name not in self.all_names[dir_indx]:
					break
			n += 1

		return name



	def add_name(self, name, dir_indx):  # fc=
		"""Add name of the link to all_names

		* performs a check to see if the name is already in the list
			-> if the name is already in the list then add a number at the end
		"""

		if name in self.all_names[dir_indx]:
			name = self.purify_duplicate_name(name, dir_indx)
		
		self.all_names[dir_indx].append(name)

	
	def update_name(self, name, dir_indx, name_indx, ext=None):  # fc=0B0D
		""" Update the name of a link
		name: new name
		dir_indx: index of the directory
		name_indx: index of the name """

		if ext is None: ext = ''
		name = name + ext

		if self.all_names[dir_indx][name_indx] == name:
			return 0

		if name in self.all_names[dir_indx]:
			name = self.purify_duplicate_name(name, dir_indx)
		
		self.all_names[dir_indx][name_indx] = name


	def gen_dl_links(self): # fc
		""" Generate the dl_links list 
		dl_links: list of all links with names and dir
		
		will be accessed by project.downloader
		SO need to init this before downloading
		"""
		self.dl_links = []
		# simplify this code:
		for i in range(len(self.sub_dirs)):
			for j in range(len(self.all_links[i])):
				self.dl_links.append((i, j))


	def sort_by_name(self, reverse=False): # fc
		""" Sort the all_names & all_links lists by name """
		for i in range(len(self.sub_dirs)):
			indx = natsort.index_natsorted(self.all_names[i])
			if reverse: indx = indx[::-1]
			self.all_names[i] = natsort.order_by_index(self.all_names[i], indx)
			self.all_links[i] = natsort.order_by_index(self.all_links[i], indx)

	def auto_sort_dirs(self, reverse=False): # fc
		""" Sort the sub_dirs list by name """
		key = lambda x: x[1]
		indx = natsort.index_natsorted(self.sub_dirs, key = key)
		if reverse: indx = indx[::-1]
		self.sub_dir_order = indx
		
	def import_from_All_list_type(self, all_list, sub_links, sub_dirs): # fc=
		""" Import from the All_list_type class """

		sub_len = len(sub_dirs)

		self.__init__(sub_len)

		self.sub_dirs = []
		for i in range(len(sub_dirs)):
			self.sub_dirs.append([sub_links[i], sub_dirs[i]])

		for i in range(len(all_list.all_links)):
			self.all_links.append(all_list.all_links[i][0])
			self.all_names.append(all_list.get_name(i))


		self.gen_len()
	def json(self):
		if self.dl_links is None:
			self.gen_dl_links()

		sub_dirs = {
		"sub_dirs": self.sub_dirs,
		"all_links": self.all_links,
		"all_names": self.all_names,
		"dir_order": self.sub_dir_order,
		"dl_links": self.dl_links
		}
		
		return json.dumps(sub_dirs, indent=1)

	def from_json(self, sub_dirs):
		"""loads datas from json.parse (dict)
		
		sub_dirs: the dict (made in store_current_state whice also includes the all_list made by self.gen_all_list)
		"""
		
		self.sub_dirs = sub_dirs["sub_dirs"]
		self.all_links = sub_dirs["all_links"]
		self.all_names = sub_dirs["all_names"]
		self.sub_dir_order = sub_dirs["dir_order"]
		self.dl_links = sub_dirs["dl_links"]
		
		self.gen_len()


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



# backwards compatibility 0.5 -> 0.8
class ProjectType_ :  # fc=0P00
	def __init__(self, project_name):  # fc=0P01
		"""initialize variables on every start of a project"""
		self.Project = project_name  # project name (case insensitive *need to work on it)
		self.project_alias = project_name # case sensitive
		self.__default__()

	def __default__(self):  # fc=0P02
		"""set default values on every start of a project"""
		self.project_alias = ''  # project alias (case sensitive)
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
		self.sub_dir_done = False # same as above
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


		self.online_page = False  # indicates if the page is online or not

		self.discuss_id = ""
		self.description = ""
		self.tags = []
		self.stars = 3.3
		self.poster_loc = ""



	def set_directories(self):  # fc=0P03
		"""Set important directories for the project
		self.download_dir: Download directory
		self.data_dir: *.wlproj directory
		self.threads_dir: directory where downloaded threads data are stored
		"""

		self.download_dir = AboutApp.download_dir + self.Project + '/'
		self.data_dir = AboutApp.leach_projects + self.Project + '.wlproj'
		self.threads_dir = AboutApp.thread_data_dir + self.Project + '/'
		
	# V8
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
			"project_alias": self.project_alias,
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
			"sub_dir_done": self.sub_dir_done,
			
			
			'sub_links': None, # for backward comp #None
			'sub_dirs': None, # for backward comp #None
			'all_names': None, # for backward comp #None

			'online_page': self.online_page,

			'discuss_id': self.discuss_id,
			'description': self.description,
			'tags': self.tags,
			'stars': self.stars,
			'poster_loc': self.poster_loc,
		}

		json_proj = json.dumps(dataset, cls=SetEncoder, indent=4)
		# clean the files if exist
		Fsys.writer(self.Project + '.wllist', 'w', '', AboutApp.leach_projects, '0M05')
		Fsys.writer(self.Project + '.wlproj', 'w', '', AboutApp.leach_projects, '0M05')

		# write new data
		Fsys.writer(self.Project + '.wlproj', 'w', json_proj, AboutApp.leach_projects, '0M05')

		if self.sub_dir_done:
			
			json_list = self.sub_dirs.json()
			Fsys.writer(self.Project + '.wllist', 'w', json_list, AboutApp.leach_projects, '0M05')
			del json_proj
		

		
	def store_current_data_v7(self): #fc=????
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
			'all_names': self.all_list.all_names,

			'online_page': self.online_page,

			'discuss_id': self.discuss_id,
			'description': self.description,
			'tags': self.tags,
			'stars': self.stars,
			'poster_loc': self.poster_loc,
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
					
					
	def _load_data(self, file_dir):
		new = True
		file_dir = file_dir.replace('"', '')
		if file_dir.endswith("'") and file_dir.startswith("'"):
			file_dir = file_dir[1:-1]

		if file_dir.endswith('.proj'):
			new=False
			
		print(1)

		
		if file_dir.endswith(('.proj', '.wlproj')) and os_isfile(file_dir):
			self.from_file = file_dir
			proj_path = file_dir

			if file_dir.endswith('.proj'):
				self.proj_ext = ('.proj', '.list')	
		

		if new and not self.from_file:
			if os_isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				proj_path = AboutApp.leach_projects + self.Project + self.proj_ext[0]
				
			elif os_isfile(AboutApp.leach_projects + self.Project + '.proj'):
				new = False

			else:
				self.__default__()
				return False

		print(new)
		if not new:
			return self.load_old_data(file_dir)
			
		

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
			print(self.leacher_version)
			
			if self.leacher_version > "8":
				out = self.load_data_v8(proj_path, list_path)
				print(out)
				return out
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
			if config.logger: traceback.print_exc()
			
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
			if config.logger: traceback.print_exc()
			
			return False
			
	def load_data(self, file_dir):
		"""
		return values:
			0: not found
			1: only proj found
			2: both list and proj found
		"""
		out = self._load_data(file_dir)
		if out:
			if self.leacher_version < '8':
				# nh patch for <=7.0001 save files
				if 'nh' in self.sp_flags:
					if len(self.sub_links)==0:
						self.sub_links = self.main_link
						
				sub_dirs = SubDirs_Type(len(self.sub_dirs))
				sub_dirs.import_from_All_list_type(self.all_list, self.sub_links, self.sub_dirs)
				self.sub_dirs = sub_dirs
				self.sub_links = None
				self.all_list = None
				
				self.store_current_data_v8()
				
		
		return out

	def load_data_v8(self, proj_path, list_path):  # fc=
		""" loadkng data for v8.001"""
		
		if self.sub_dir_done and os_isfile(list_path):
			self.list_file = Fsys.reader(list_path, 'rb', True, 'str')
			_list_json = json.loads(self.list_file)
			self.sub_dirs = SubDirs_Type(0)
			
			self.sub_dirs.from_json(_list_json["sub_dirs"])
			return 2
			
		else: self.sub_dir_done = False
		return 1
			

	def load_old_data(self, file_dir):  # fc=0P04
		"""loads the data from the project file
			returns: None if failed to load file
					False if there is no project file"""

		file_dir = file_dir.replace('"', '')
		if file_dir.endswith("'") and file_dir.startswith("'"):
			file_dir = file_dir[1:-1]

		if file_dir.endswith(('.proj', '.wlproj')) and os_isfile(file_dir):
			self.from_file = file_dir
			proj_path = file_dir

			if file_dir.endswith('.proj'):
				self.proj_ext = ('.proj', '.list')
				

		if not self.from_file:
			if os_isfile(AboutApp.leach_projects + self.Project + '.wlproj'):
				pass
			elif os_isfile(AboutApp.leach_projects + self.Project + '.proj'):
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
						self.leacher_version = '6.0001'
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
				self.leacher_version = loaded_data_set['leacher_version']
			

			if 'magic_number' in loaded_data_set:
				self.last_user_ip = Nsys.dec_ip(loaded_data_set['magic_number'])

			if 'get_html_title' in loaded_data_set:
				self.get_html_title = loaded_data_set['get_html_title']

			proj_good = True

		except:
			if config.LOGGER: traceback.print_exc()

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
				if config.logger: traceback.print_exc()
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
			soup = bs(Netsys.remove_noscript(page.content), Netsys.PARSER)

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
							soup = bs(Netsys.remove_noscript(page.content), Netsys.PARSER)
							self.update_sub_dirs(html_unescape(soup.title.text).strip(), j)
							__x = 1

					if __x == 0:
						name = Fsys.get_dir(i, 'url')
						self.update_sub_dirs(name, j)
		
					self.sub_dirs_count += 1
					if self.break_all: return 0
					oneline.update("Getting pages [%i/%i]" % (self.sub_dirs_count, len(self.sub_links)))

		except (KeyboardInterrupt, EOFError):
			self.break_all = True
			raise LeachICancelError

	def gen_sub_dirs(self):  # fc=0P08
		"""Generates sub-directories|`self.sub_dirs`"""
		oneline.new()
		oneline.update("Getting pages [0/%i]"%len(self.sub_links))

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

		except (KeyboardInterrupt, EOFError):
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
		from math import ceil
		last_chunks = 0
		last_done = 0
		percent =0
		old_len = len("".join(map(str, ['Downloaded [', ('━'*percent), '╺' if percent<30 else '━', '━'*(30-percent), '][', last_done, '/', self.total, ']', self.current_speed , '/s'])))
		while (not (self.dl_done or self.break_all)) or self.total == 0:
			_temp = self.dl_chunks
			self.current_speed = filesize_size((_temp - last_chunks) * config.sp_arg_flag['chunk_size'] * 2, filesize_alt)

			if self.break_all or self.total == 0: return 0
			percent = floor((self.done / self.total) * 30)
			#IOsys.delete_last_line()
			size = int(get_terminal_size()[0])
			IOsys.delete_last_line(int(ceil(old_len/size)))
			#print("\n"*2,int(ceil(old_len/size)),"\n"*2)
			last_done = self.done

			sys_write(''.join(['Downloaded [', '\u001b[32;1m', ('━'*percent), '\u001b[30;1m╺' if percent<30 else '━', '━'*(30-percent), '\u001b[0m][', str(last_done), '/', str(self.total), ']', self.current_speed , '/s\n']))
			
			
			old_len = len("".join(map(str, ['Downloaded [', ('━'*percent), '╺' if percent<30 else '━', '━'*(30-percent), '][', last_done, '/', self.total, ']', self.current_speed , '/s'])))
			time.sleep(.5)
			last_chunks = _temp

	def downloader(self, part, is_error=False, partitions=None):  # fc=0P0B
		if partitions is None:
			partitions = self.dl_threads

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

								xprint('\n\n/y/Something Went wrong, Returning to main Menu/=/\n\n')
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
										zf.extractall(path=self.download_dir + fdir + '/' + os_splitext(fname)[0])
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
							self.errors += 1

						else:
							self.re_error += 1
							if self.re_error == 1: IOsys.delete_last_line()
							IOsys.delete_last_line()
							if self.re_error < 4:
								print("\n\nFailed to download from '%s'\n\n" % i[0])
							else:
								if self.re_error != 4: IOsys.delete_last_line()
								print("Failed %i others links" % (self.re_error - 3))
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
			

					self.errors += 1


				else:
					self.re_error += 1
					if self.re_error < 4:
						print("Failed to download from '%s'\n\n" % i[0])
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
		oneline.update('Indexed [' + str(self.indx_count) + '/' + str(len(self.sub_links)) + '] /~`' + link + '`~/')

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
					soup = bs(Netsys.remove_noscript(page.text), Netsys.PARSER)

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
		code = re_search('https://nhentai.[^/]*?/g/((\d)*)', link)

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
			soup = bs(Netsys.remove_noscript(page.text), Netsys.PARSER)

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
				net_search = re_compile("https://i\d*.nhentai.net/galleries/\d*/")
				for imgs in soup.find_all('img'):
					img_link = imgs.get('data-src')
					if img_link is None:
						img_link = imgs.get('src')

					if '/thumb.' in img_link:
						continue

					if 'cover' not in img_link:
						img_link = img_link.replace('s://t', 's://i')[::-1].replace('t', '', 1)[::-1]
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
				temp1 = bs(Netsys.remove_noscript(session.get(i).text), Netsys.PARSER)
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

			input_soup = bs(Netsys.remove_noscript(input_page.text), Netsys.PARSER)
			_temp = input_link

			paginate = input_soup.find_all("div", class_="paginate")[0]
			paginate__ = paginate
			paginate_ = paginate__.find_all('a', class_='pg_prev')
			page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
			while len(paginate_) != 0:
				prev_lists.append(Netsys.get_link(paginate_[0].get('href'), _temp, homepage))
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
				_temp = prev_lists[-1]
				paginate__ = bs(Netsys.remove_noscript(session.get(_temp).text), Netsys.PARSER).find_all("div", class_="paginate")[0]
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
				paginate__ = bs(Netsys.remove_noscript(session.get(_temp).text), Netsys.PARSER).find_all("div", class_="paginate")[0]
				paginate_ = paginate__.find_all('a', class_='pg_next')
				page_list += [Netsys.get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

			del paginate__

			page_list = natsort.natsorted(Datasys.remove_duplicate(page_list))

			for i in page_list:
				temp1 = bs(Netsys.remove_noscript(session.get(i).text), Netsys.PARSER)
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

		except (KeyboardInterrupt, EOFError):
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

	
	def import_make(self, f_code="????"):  # fc=0704 v
		""" reads and exec() necessary files to create different formats of
		output [ie: html, cbz]
		args:
			f_code: caller function id
		"""
		cd = os.path.dirname(os.path.realpath(__file__))

		try:
			exec(Fsys.reader(os.path.join(cd,'make_html4.py')), globals())
		except Exception as e:
			traceback.print_exc()
			xprint("\n\nSome error occurred while loading make_html file. \n/hui/Error code: 0704x0/=/\nReport to the author\nExiting in 5 seconds")
			leach_logger(log(['0704x0', f_code, 'make_html4.py', e.__class__.__name__, e]))

			time.sleep(5)
			exit()

		try:
			exec(Fsys.reader(os.path.join(cd,'make_cbz2.py')), globals())
		except Exception as e:
			xprint("\n\nSome error occurred while loading make_html file. \n/hui/Error code: 0704x0/=/\nReport to the author\nExiting in 5 seconds")
			leach_logger(log(['0704x0', f_code, 'make_cbz2.py', e.__class__.__name__, e]))
			time.sleep(5)
			exit()


	def make_html(self):  # fc=0P0O
		"""Make the html file"""
		self.import_make()
		self.manga_freak_patch()

		self.online_page = False
		self.store_current_data()

		return MakeHtml.make_pages(self.all_list.all_names, self.sub_dirs, self.Project, self.file_to_sort, [],
									self.sp_extension, self.dir_sorted, 
									self.discuss_id, self.description, self.tags, self.stars, self.poster_loc)
								   
	def make_online_html(self):  # fc=0P0O
		"""Make the html file"""
		self.import_make()
		#self.manga_freak_patch()
		self.online_page = True
		self.store_current_data()

		return MakeHtml.make_online_page(self.all_list.get_all_list(), self.sub_dirs, self.Project, self.file_to_sort, [],
								   self.sp_extension, self.dir_sorted, 
								   self.discuss_id, self.description, self.tags, self.stars, self.poster_loc)





	def make_cbz(self):  # fc=0P0P
		"""Make the cbz file"""
		self.import_make()
		self.manga_freak_patch()

		return MakeCbz.make_cbz(self.all_list, self.sub_dirs, self.Project, self.file_to_sort, self.sp_extension)

	def post_online(self):
		"""Sends project images to online 
		adds source links and online file links in """

		pass

	def edit_page(self):  # fc=????
		"""Edit the html file Datas"""

		discuss_id = IOsys.safe_input('Enter the discuss id: ')
		self.discuss_id = self.discuss_id if discuss_id=="?" else discuss_id

		description = IOsys.safe_input("\n/hui/Description:/=/ ")
		self.description = self.description if description=="?" else description

		tags = IOsys.safe_input("\n/hui/Tags ( sep by comma ):/=/ ")
		self.tags = self.tags if tags=="?" else [i.strip() for i in tags.split(",") if i.strip()!=""]

		stars = IOsys.safe_input("\n/hui/Stars:/=/ ")
		self.stars = self.stars if stars=="?" else float(stars)

		poster_loc = IOsys.safe_input("\n/hui/Poster location:/=/ ")
		self.poster_loc = self.poster_loc if poster_loc=="?" else poster_loc


		xprint("/hui/DONE!!!/=/\n")

		self.store_current_data()
		if self.online_page:
			self.make_online_html()
		
		else:
			self.make_html()
