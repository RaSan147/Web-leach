from main_ez import Fsys, getsizeof, Datasys
from print_text2 import xprint
import natsort

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


print(All_list_type(99).get_all_list())