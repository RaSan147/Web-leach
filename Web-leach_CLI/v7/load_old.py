from os.path import  basename
def get_file_name(directory):
	if isinstance(directory, bytes): directory = directory.decode()
	return basename(directory)

from prin


class All_list_type:  # fc=0B00
	""" Data structure for all lists """

	def __init__(self, dir_len, all_links=None, all_names=None):  # fc=0B01
		self.dir_len = dir_len
		self.dir_height = [0 for _ in range(dir_len)]
		self.all_names = [[] for _ in range(dir_len)]
		self.link_len = 0

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
		del self.all_links
		del self.all_names
		del self.dir_height


class Check_old_data:
	def __init__(self,proj_file, list_file, VERSION, server_version, user_ip):
		self.proj_file = proj_file
		self.list_file = list_file
		
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
		self.img_to_sort = False  # indicates if the images should be sorted or not
		self.dir_sorted = True  # will sort directories by name
		self.corruptions = []  # list of corruptions in project data if there's any or empty
		self.sub_dirs_count = 0  # number of sub directories named in the project data

		### Project creation data
		self.first_created = '0'  # Nsys.cdt_() of the time when the project was first created
		self.last_update = '0'  # Nsys.cdt_() of the time when the project was last modified
		self.leacher_version = VERSION  # version of the scrapper
		self.server_version = server_version  # version of the server while scrapping
		self.user_ip = user_ip  # user's ip address

		### Need input
		self.main_link = None  # the main link
		self.dimention = 0
		""" number indication how should the program scrap data from the link
		0: default, if 0 will ask for dimention input
		1: scrap from only the main link and won't ask for sublinks
		2: scrap from only the sublinks of the main link
		3: scrap from both main link and and the sublinks"""
		self.link_startswith = ''  # (str) each sublink must start with
		self.file_types = None  # file types to be downloaded
		self.file_starts = ''  # (str) each files must start with (used regex)
		self.file_exts = []  # (str) (set of file extensions) each files must end with
		self.check_links = False  # if True, the list_writer_img checks the <a> for images
		self.file_to_sort = False  # indicates if the files will be sorted or not
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
		
	def check_proj(self):
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
			if 'file_to_sort' in loaded_data_set:
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
			self.file_types = 'img'
			self.file_exts = Constants.all_image_types