from os import makedirs, devnull as os_devnull
from subprocess import Popen as subprocess_Popen, DEVNULL as subprocess_DEVNULL, run
from hashlib import sha1 as hashlib_sha1
import webbrowser
from headers_file import header_list        # f_code = 30000 
import Number_sys_conv as Nsys
import requests
from os.path import exists as os_exists, isdir as os_isdir, isfile as os_isfile, basename as os_basename
from platform import system as os_name
from random import choice as random_choice
from rcrypto import encrypt

process_id= 1000

os_name=os_name()

class LeachPermissionError(Exception):
	pass

def header_():    #func_code=00002
	"""returns a random header from header_list for requests lib"""
	return( {'User-Agent':random_choice(header_list)})


def hdr(header, f_code=''):    #func_code=00007
	"""returns the index of a header"""
	try:
		return str(header_list.index(header['User-Agent']))
	except Exception as e:
		print("Some error occured caused, possible cause: DATA CORRUPTION\nError code: 00007x"+f_code)

		leach_logger('00007x-1||'+'||' +f_code+e.__class__.__name__+'||'+ e+'||'+header)
		return str((-1, header))

def loc(x, os_name='Linux'):    #func_code=00005
	"""to fix dir problem based on os

	x: directory

	os_name: Os name *Linux"""
	if os_name == 'Windows':
		return x.replace('/', '\\')
	else:
		return x.replace('\\', '/')

def writer(fname, mode, data, direc=None, f_code='', encoding='utf-8'):    #func_code=00006
	"""Writing on a file

		fname: filename,\n
		mode: write mode (w,wb,a,ab),\n
		data: data to write,\n
		dir: directory of the file, empty for current dir *None,\n
		func_code: (str) code of the running func *empty string,\n
		encoding: if encoding needs to be specified (only str, not binary data) *utf-8"""
	#func_code='00006'
	if any(i in fname for i in ('\\|:*"><?')):
		leach_logger('00006||Invalid Fname||%s||replacing con char'%fname)
		fname=fname.replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
		
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
				leach_logger('00006||Invalid dir||%s||replacing con char'%locs)
				locs=locs.replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')
		
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
				writer(fname, mode, data, locs, f_code)
	except Exception as e:
		if e.__class__.__name__== "PermissionError":
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: 101x'+f_code)
			leach_logger('101||%s||%s||%s||%s'%(f_code, fname, mode, direc))
			raise LeachPermissionError
		else:
			leach_logger('00006x-1||'+e.__class__.__name__+'||%s||%s||%s||%s||%s'%(f_code, fname, mode, direc,e))
			print(e.__class__.__name__,"occured while writing", fname, 'in', 'current directory' if dir==None else dir,'\nPlease inform the author. Error code: 00006x'+f_code)
			raise e

def leach_logger(io, key='lock'):   #func_code=00008
	"""saves encrypted logger data to file\n
	(new in 5.3_class: auto adds dt_() at the begning)
	
	io: the log message\n
	key: salt text"""
	try:
		while True:
			try:
				try:
					_key="Asuna"
					salt = hashlib_sha1(key.encode()).hexdigest()
					writer('userlog.leach', 'ab', encrypt(salt+('||%s||'%Nsys.dt_())+str(process_id)+'||'+io,_key).encode('utf-8')+b'\n','data','00008')
					break
				except EOFError: pass
				except KeyboardInterrupt: pass
			except EOFError: pass
			except KeyboardInterrupt: pass
	
	except EOFError: leach_logger(io, key='lock')
	except KeyboardInterrupt: leach_logger(io, key='lock')

def check_internet(link, f_code):       # f_code= 00020
	"""Check if the connection is available or not

	link: link to check for connection status"""
	current_header=header_()
	try:
		r=requests.head(link, headers=current_header)
		if r:
			return True
		else:
			raise requests.ConnectionError
	except requests.ConnectionError:
		leach_logger('%s||%s'%(link, hdr(current_header, f_code)))
		return False

def run_server(port):
		if check_internet("http://localhost:%i"%port, '10010')==False:
			server_code = subprocess_Popen(['python', '-m','http.server', str(port)],
			stdin=open(os_devnull), start_new_session=True, stdout=subprocess_DEVNULL, stderr=subprocess_DEVNULL)
			server_code.wait()

def make_n_open_server():
	run_server(4444)