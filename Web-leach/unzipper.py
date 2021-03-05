from zipfile import ZipFile
from os import remove
		
with ZipFile('Data/.temp/'+'Web Leach v4.22.zip') as zf:
	zf.extractall(pwd=b'lock')
