import requests
from os.path import isdir as os_isdir, isfile as os_isfile, basename as os_basename
from os import makedirs
from bs4 import BeautifulSoup as bs

from random import choice as random_choice
from headers_file import header_list
from re import sub
parser='lxml'
try:
	bs('<br>', parser)
except:
	parser = 'html.parser'

if True:
	def loc(x, _os_name='Linux'):    #func_code=00007
		"""to fix dir problem based on os

		x: directory

		os_name: Os name *Linux"""
		if _os_name == 'Windows':
			return x.replace('/', '\\')
		else:
			return x.replace('\\', '/')

	def go_prev_dir(link):    #func_code=0000E
		"""returns the previous path str of web link or directory\n
		**warning: returns only in linux directory format"""
		link=loc(link,'Linux')
		if link.endswith('/'):
			return '/'.join(link[:-1].split('/')[:-2])+'/'
		# x=link.split('/')
		else:
			return '/'.join(link.split('/')[:-2])+'/'

	def get_link(i,current_link, homepage):

		if i.startswith('#'): i= current_link
		elif i.startswith('//'): i='https:'+i

		elif i.startswith('../'):
			_temp= current_link
			while i.startswith('../'):
				_temp= go_prev_dir(_temp)
				i= i.replace('../', '', 1)
			i= _temp+i
			del _temp

		elif i.startswith('/'):
			i= homepage+i
		if '//' not in i:
			temp=homepage
			if temp.endswith('/'):
				if i.startswith('/'): i=temp+i[1:]
				else: i=temp+i
			else:
				if i.startswith('/'): i=temp+i
				else: i=temp+'/'+i

		return i

	def get_union(*args):
		final_list = list(set().union(*args))
		return final_list

	def remove_duplicate(seq, return_type = list):	#func_code=00000
		"removes duplicates from a list or a tuple"
		return return_type(dict.fromkeys(seq))

	def trans_str(txt, dicts): #func_code=00019
		"""replaces all the matching charecters of a string for multuple times
		txt: string data
		dicts: dict of { find : replace }"""
		for i in dicts.keys():
			a= dicts[i]
			for j in i:
				txt = txt.replace(j, a)
		return txt


	def writer(fname, mode, data, direc=None, f_code='None', encoding='utf-8'):    #func_code=00008
		"""Writing on a file

			fname: filename,\n
			mode: write mode (w,wb,a,ab),\n
			data: data to write,\n
			direc: directory of the file, empty for current dir *None,\n
			func_code: (str) code of the running func *empty string,\n
			encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""
		#func_code='00008'

		# err_logged = False
		if any(i in fname for i in ('\\|:*"><?')):
			# leach_logger('00008x1||%s'%fname)
			fname= trans_str(fname, {'/\\|:*><?': '-', '"':"'"})
		if direc == None:
			direc='./'
		else:
			direc ='./'+direc
		try:
			if direc == None:
				if 'b' not in mode:
					with open(fname, mode, encoding=encoding) as file:
						file.write(data)
				else:
					with open(fname, mode) as file:
						file.write(data)
			else:
				locs=loc(direc, 'Linux')
				if any(i in locs for i in ('\\|:*"><?')):
					# leach_logger('00008x2||%s'%locs)
					locs= trans_str(locs, {'\\|:*><?': '-', '"':"'"})

				if os_isdir(locs):
					if locs.endswith('/'):
						if 'b' not in mode:
							with open(loc(locs + fname), mode, encoding=encoding) as f:
								f.write(data)
						else:
							with open(loc(locs + fname), mode) as f:
								f.write(data)
					else:
						if 'b' not in mode:
							with open(loc(locs + '/' + fname), mode, encoding=encoding) as f:
								f.write(data)
						else:
							with open(loc(locs + '/' + fname), mode) as f:
								f.write(data)
				else:
					try:
						makedirs(locs)
					except FileExistsError: pass
					except Exception as e:
						if e.__class__.__name__== "PermissionError":
							_temp= ''
							_temp2= locs.split('/')
							_temp3= 0
							while True:
								_temp+= _temp2[_temp3]+'/'
								if not os_isdir(_temp): break
							# leach_logger('00008x101||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc, _temp))
							del _temp, _temp2, _temp3
							# err_logged = True
						raise e
					writer(fname, mode, data, locs, f_code)
		except Exception as e:
			if e.__class__.__name__== "PermissionError":
				# xprint('/r/',e.__class__.__name__,"occurred while writing", fname, 'in', 'current directory' if dir==None else dir,'/y/\nPlease inform the author. Error code: %sx101/=/'%f_code)
				# leach_logger('00008x101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
				# raise LeachPermissionError
				pass
			else:
				# leach_logger('00008x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc,str(e)))
				# xprint('/r/',e.__class__.__name__,"occurred while writing", fname, 'in', 'current directory' if dir==None else dir,'/y/\nPlease inform the author. Error code: 00008x'+f_code, '/=/')
				raise e

	def get_file_name(directory, mode= 'dir'):      #func_code=00011
		"""[takes a file directory and returns the last last part of the dir (can be file or folder)

		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory
		"""
		if mode=='url':
			fragment_removed = directory.split("#")[0]  # keep to left of first #
			query_string_removed = fragment_removed.split("?")[0]
			scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
			if scheme_removed.find("/") == -1:
				return ""
			return os_basename(scheme_removed)
		elif mode=='dir':
			return os_basename(directory)
		else:
			raise ValueError
	def header_():    #func_code=00004
		"""returns a random header from header_list for requests lib"""
		return( {'User-Agent':random_choice(header_list)})
	def delete_last_line():      #func_code=0002
		"Use this function to delete the last line in the STDOUT"

		#cursor up one line
		print('\x1b[1A\x1b[2K', end='')

		#delete last line
		# sys_write()


session= requests.Session()

page_list = []
prev_lists = []
next_lists = []
paginators = []
sub_links =[]
sub_dirs = []
all_list=[]
homepage= 'https://www.webtoons.com'
Project = 'something'
sp_extension = ''

input_link = "https://www.webtoons.com/en/thriller/dearx/list?title_no=2503"
input_page = session.get(input_link)
input_soup = bs(input_page.content, parser)
_temp = input_link

paginate = input_soup.find_all("div", class_="paginate")[0]
paginate__ = paginate
paginate_ = paginate__.find_all('a', class_='pg_prev')
page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
while len(paginate_)!=0:
	prev_lists.append(get_link(paginate_[0].get('href'), _temp, homepage))
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
	_temp = prev_lists[-1]
	paginate__ = bs(session.get(_temp).content, parser).find_all("div", class_="paginate")[0]
	paginate_ = paginate__.find_all('a', class_='pg_prev')
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

print('done')
_temp= input_link
paginate_ = paginate.find_all('a', class_='pg_next')
paginate__ = paginate
page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
while len(paginate_)!=0:
	next_lists.append(get_link(paginate_[0].get('href'), _temp, homepage))
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
	_temp = next_lists[-1]
	paginate__ = bs(session.get(_temp).content, parser).find_all("div", class_="paginate")[0]
	paginate_ = paginate__.find_all('a', class_='pg_next')
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

del paginate__

all_paginates = get_union(next_lists, prev_lists)

# for i in all_paginates:
# 	paginate__ = bs(session.get(i).content, parser)
# 	paginate_ = paginate__.find_all('a', class_='pg_next')
page_list= remove_duplicate(page_list)
for i in page_list:
	# print(i)
	temp1 = bs(session.get(i).content, parser)
	ul = temp1.find_all('ul', id= "_listUl")[0].find_all('a')
	for ii in ul:
		sub_links.append(get_link(ii.get('href'), _temp, homepage))
		sub_dirs.append(ii.find('span', class_= 'subj').text)
# print(sub_links)
for i in  sub_links:
	temp1= bs(session.get(i).content, parser)
	img_div = temp1.find('div', id='_imageList')

	for ii in img_div.find_all('img'):
		all_list.append(tuple((sub('\?type\=q\d*.*', '', ii.get('data-url')), sub_links.index(i))))
# print(all_list)
# exit()

n=0
a= len(all_list)
for i in all_list:
	current_header=header_()	# randomizes header from list on every download to at least try to fool server
	if sub_links!=[]:
		current_header['referer']=sub_links[i[1]]
	download =True
	if sub_dirs[i[1]].endswith('\\') or sub_dirs[i[1]].endswith('/'):
		if os_isfile('Download_Projects/'+Project+'/'+sub_dirs[i[1]]+get_file_name(i[0])+sp_extension): download=False
	else:
		if os_isfile('Download_Projects/'+Project+'/'+sub_dirs[i[1]]+'/'+get_file_name(i[0])+sp_extension): download=False
	writer(get_file_name(i[0])+sp_extension,'wb',b'','Download_projects/'+Project+'/'+sub_dirs[i[1]], '10002')
	_temp = session.get(i[0], headers= current_header, timeout=2).content
	writer(get_file_name(i[0])+sp_extension,'wb', _temp,'Download_projects/'+Project+'/'+sub_dirs[i[1]], '10002')

	delete_last_line()
	n+=1
	print(n,a)


"""
Ray
wt test
https://www.webtoons.com/en/thriller/dearx/list?title_no=2503
y
"""
