
from os.path import isdir as os_isdir, isfile as os_isfile, basename as os_basename
from os import makedirs
from random import choice as random_choice
import re


import natsort, requests
from bs4 import BeautifulSoup as bs

header_list = ("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20190101 Firefox/70.0",
"Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
"Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
"Mozilla/5.0 (Windows ME 4.9; rv:35.0) Gecko/20100101 Firefox/35.0",
"Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62")

parser='lxml'
try:
	bs('<br>', parser)
except:
	parser = 'html.parser'

if True:
	def loc(x, _os_name='Linux'):   
		"""to fix dir problem based on os

		x: directory

		os_name: Os name *Linux"""
		if _os_name == 'Windows':
			return x.replace('/', '\\')
		else:
			return x.replace('\\', '/')

	def go_prev_dir(link): 
		"""returns the previous path str of web link or directory\n
		**warning: returns only in linux directory format"""
		link=loc(link,'Linux')
		if link.endswith('/'):
			return '/'.join(link[:-1].split('/')[:-2])+'/'
			
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

	def remove_duplicate(seq, return_type = list):	
		"removes duplicates from a list or a tuple"
		return return_type(dict.fromkeys(seq))

	def trans_str(txt, dicts): 
		"""replaces all the matching charecters of a string for multuple times
		txt: string data
		dicts: dict of { find : replace }"""
		for i in dicts.keys():
			a= dicts[i]
			for j in i:
				txt = txt.replace(j, a)
		return txt


	def writer(fname, mode, data, direc=None, f_code='None', encoding='utf-8'):    
		"""Writing on a file

			fname: filename,\n
			mode: write mode (w,wb,a,ab),\n
			data: data to write,\n
			direc: directory of the file, empty for current dir *None,\n
			func_code: (str) code of the running func *empty string,\n
			encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""
		

		
		if any(i in fname for i in ('\\|:*"><?')):
			
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
							
							del _temp, _temp2, _temp3
							
						raise e
					writer(fname, mode, data, locs, f_code)
		except Exception as e:
			if e.__class__.__name__== "PermissionError":
				
				
				
				pass
			else:
				
				
				raise e

	def get_file_name(directory, mode= 'dir'):      
		"""[takes a file directory and returns the last last part of the dir (can be file or folder)

		directory: the file directory, only absolute path to support multiple os
		mode: url or file directory
		"""
		if mode=='url':
			fragment_removed = directory.split("#")[0]
			query_string_removed = fragment_removed.split("?")[0]
			scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
			if scheme_removed.find("/") == -1:
				return ""
			return os_basename(scheme_removed)
		elif mode=='dir':
			return os_basename(directory)
		else:
			raise ValueError
	def header_():    
		"""returns a random header from header_list for requests lib"""
		return( {'User-Agent':random_choice(header_list)})
	def delete_last_line():      
		"Use this function to delete the last line in the STDOUT"

		
		print('\x1b[1A\x1b[2K', end='')

		
		


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
sp_extension = '.jpg'

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

page_list= remove_duplicate(page_list)
for i in page_list:
	
	temp1 = bs(session.get(i).content, parser)
	ul = temp1.find_all('ul', id= "_listUl")[0].find_all('a')
	for ii in ul:
		sub_links.append(get_link(ii.get('href'), _temp, homepage))
		sub_dirs.append(ii.find('span', class_= 'subj').text)

for i in  sub_links:
	temp1= bs(session.get(i).content, parser)
	img_div = temp1.find('div', id='_imageList')

	for ii in img_div.find_all('img'):
		all_list.append(tuple((sub('\?type\=q\d*.*', '', ii.get('data-url')), sub_links.index(i))))



n=0
a= len(all_list)
for i in all_list:
	current_header=header_()	
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
##########################################################################

main_link = input("Enter the Webtoon link: ")

special_starts ={ 'webtoon_ep':'https\:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/.*?\/viewer\?title_no\=(\d+)\&episode_no\=\d+',
						'webtoon': 'https:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/list\?title_no=(\d+)'}


_t = re.search(special_starts['webtoon'] ,main_link)
if _t:
	datas = _t.groups()
else:
	_t = re.search(special_starts['webtoon_ep'] ,main_link)
	if _t:
		datas = _t.groups()  # category, title, code
	else:
		print("Invalid link\n please recheck the Main link")
		exit()

session= requests.Session()

page_list = []
prev_lists = []
next_lists = []
sub_links = []
sub_dirs = []
all_list = []
homepage= 'https://www.webtoons.com'

input_link = "https://www.webtoons.com/en/%s/%s/list?title_no=%s"%(datas)
if not requests.get(input_link, headers = header_()):
	print('Webtoon Page not found. Recheck the link')
	exit()

input_page = session.get(input_link, headers = header_())
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
	paginate__ = bs(session.get(_temp, headers = header_()).content, parser).find_all("div", class_="paginate")[0]
	paginate_ = paginate__.find_all('a', class_='pg_prev')
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

_temp= input_link
paginate_ = paginate.find_all('a', class_='pg_next')
paginate__ = paginate
page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
while len(paginate_)!=0:
	next_lists.append(get_link(paginate_[0].get('href'), _temp, homepage))
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]
	_temp = next_lists[-1]
	paginate__ = bs(session.get(_temp, headers = header_()).content, parser).find_all("div", class_="paginate")[0]
	paginate_ = paginate__.find_all('a', class_='pg_next')
	page_list+= [get_link(i.get('href'), _temp, homepage) for i in paginate__.find_all("a")]

del paginate__


page_list= remove_duplicate(page_list)

all_chapters = []


for i in page_list:
	temp1 = bs(session.get(i, headers = header_()).content, parser)
	ul = temp1.find_all('ul', id= "_listUl")[0].find_all('li')
	for li in ul:
		all_chapters.append([get_link(li.find('a').get('href'), _temp, homepage),
										li.find('span', class_= 'subj').text,
										li.get('data-episode-no')])
all_chapters = natsort.natsorted(all_chapters, key = lambda x: x[2]) # sub_links, sub_dirs, index



total_all_chapters = len(sub_dirs)

print('Found %i all_chapters'%total_all_chapters)

nn=0

while nn < total_all_chapters:
	all_chapters[nn].append([])
	temp1= bs(session.get(all_chapters[nn][0], headers = header_()).content, parser)
	img_div = temp1.find('div', id='_imageList')

	for ii in img_div.find_all('img'):
		all_chapters[nn][4].append(tuple((re.sub('\?type\=q\d*.*', '', ii.get('data-url')), nn)))
	nn+=1


n=0
a= len(all_list)
for chapter in all_chapters:
	count = 1
	for i in chapter[3]:
		current_header=header_()	
		if sub_links!=[]:
			current_header['referer']= chapter[0]
		download =True
		if sub_dirs[i[1]].endswith('\\') or sub_dirs[i[1]].endswith('/'):
			if os_isfile('Download_Projects/'+Project+'/'+chapter[1] +str(count)+sp_extension): download=False
		else:
			if os_isfile('Download_Projects/'+Project+'/'+chapter[1]+'/'+str(count)+sp_extension): download=False
		writer(str(count)+sp_extension,'wb',b'','Download_projects/'+Project+'/'+chapter[1], '10002')
		_temp = session.get(i[0], headers= current_header, timeout=2).content
		writer(str(count)+sp_extension,'wb', _temp,'Download_projects/'+Project+'/'+chapter[1], '10002')

		delete_last_line()
		n+=1
		print(n,a)
