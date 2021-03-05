import hashlib
file_name=input('enter file name')
with open(file_name+'.exe', 'rb') as file_to_check:
			# read contents of the file
			data = file_to_check.read()    
			# pipe contents of the file through
			md5_returned = hashlib.md5(data).hexdigest()
			print("_latest_hash='"+md5_returned+"'")
input()

"""
if _VERSION!=_latest:
	print("An update available (v4.1), Do you want to update? ")
	if True:
		from zipfile import ZipFile
		from os import remove
		update_filename='Web Leach v4.1'
		with ZipFile(update_filename+'.zip') as zf:
			zf.extractall(pwd=b'lock')
		# Import hashlib library (md5 method is part of it)
		import hashlib

		# File to check
		file_name = update_filename+'.exe'

		# Correct original md5 goes here
		original_md5 = '5f6e2f07fde96468e3aa8be2a9680211'  

		# Open,close, read file and calculate MD5 on its contents 
		with open(file_name, 'rb') as file_to_check:
			# read contents of the file
			data = file_to_check.read()    
			# pipe contents of the file through
			md5_returned = hashlib.md5(data).hexdigest()
		print(md5_returned)
		# Finally compare original MD5 with freshly calculated
		if original_md5 == md5_returned:
			print ("MD5 verified. Please open the latest file '"+update_filename+".exe'\n this program will break in 5 seconds\n\n")
			remove(update_filename+'.zip')
			time.sleep(5)
			raise ValueError
		else:
			print ("MD5 verification failed!. \nPlease inform the coder- wwwqweasd147[at]gmail[dot]com")
"""