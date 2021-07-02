from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename, dirname as os_dirname, realpath as os_realpath

def get_file_name(directory, mode= 'dir'):      #func_code=00011  v
	"""takes a file directory and returns the last last part of the dir (can be file or folder)

	args:
	-----
		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory
	"""

	if isinstance(directory, bytes): directory = directory.decode()
	if mode == 'url':
		fragment_removed = directory.split("#")[0]  # keep to left of first #
		query_string_removed = fragment_removed.split("?")[0]
		scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
		if scheme_removed.find("/") == -1:
			return ""
		return os_basename(scheme_removed)
	elif mode == 'dir':
		return os_basename(directory)
	else:
		raise ValueError

def remove_duplicate(seq, return_type = list):	#func_code= 00000  vx
	"""removes duplicates from a list or a tuple
	also keeps the array in the same order

	args:
	-----
		seq: `tuple`|`list` to remove dups
		return_type: type of array to return"""

	return return_type(dict.fromkeys(seq))

class x():
	def __init__(self):
		self.all_list = [('https://cdn.nhentai.xxx/g/1584515/1.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/2.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/3.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/4.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/5.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/6.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/7.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/8.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/9.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/10.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/11.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/12.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/13.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/14.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/15.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/16.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/17.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/18.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/19.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/20.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/21.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/22.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/23.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/24.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/25.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/26.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/27.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/28.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/29.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/30.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/31.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/32.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/33.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/34.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/35.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/36.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/37.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/38.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/39.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/40.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/41.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/42.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/43.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/44.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/45.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/46.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/47.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/48.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/49.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/50.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/51.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/52.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/53.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/54.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/55.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/56.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/57.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/58.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/59.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/60.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/61.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/62.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/63.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/64.jpg', 0), ('https://cdn.nhentai.xxx/g/1584515/65.jpg', 0)]

		self.FName_allIndx_dirIndx = None

		self.sub_dirs = ['[Nishizawa Mizuki] Akarui Kazoku Seikatsu [English] [Otokonoko Scans]']
		print(self.sub_dirs)

	def gen_FName_allIndx_dirIndx(self):
		if not isinstance(self.all_list[0], tuple):
			return
		if self.FName_allIndx_dirIndx is not None:
			return

		uniq_all_list = remove_duplicate([a[0] for a in self.all_list])
		self.FName_allIndx_dirIndx = [[]*len(self.sub_dirs)]
		length = len(self.all_list)
		n= 0
		while n<length:
			# print(n)
			i = self.all_list[n]
			indx = uniq_all_list.index(i[0])
			f_name_ = get_file_name(i[0])

			if f_name_ not in self.FName_allIndx_dirIndx[i[1]]:
				self.FName_allIndx_dirIndx[i[1]].append([f_name_, indx, i[1]])
				# self.all_list[n] = i[0]
			else:
				count = 0
				while True:
					if f_name_ + f"({count})" in self.FName_allIndx_dirIndx[i[1]]:
						count += 1
					self.FName_allIndx_dirIndx[i[1]].append([f_name_ + f"({count})", indx, i[1]])
					# self.all_list[n] = i[0]
					break
			n += 1

		self.all_list = uniq_all_list



y = x()
y.gen_FName_allIndx_dirIndx()
print(y.FName_allIndx_dirIndx)
