"""Will return (also save output as out.txt) line by line encrypted or decrypted data"""


##########################################################################
#                                                                        #
#                             C Based                                    #
#                                                                        #
##########################################################################

from os import environ, remove
from sys import platform as _sys_platform
from time import time


def _get_platform():
	# On Android sys.platform returns 'linux2', so prefer to check the
	# presence of python-for-android environment variables (ANDROID_ARGUMENT
	# or ANDROID_PRIVATE).
	if 'ANDROID_ARGUMENT' in environ:
		return 'android'
	elif environ.get('KIVY_BUILD', '') == 'ios':
		return 'ios'
	elif _sys_platform in ('win32', 'cygwin'):
		return 'win'
	elif _sys_platform == 'darwin':
		return 'macosx'
	elif _sys_platform.startswith('linux'):
		return 'linux'
	elif _sys_platform.startswith('freebsd'):
		return 'linux'
	return 'unknown'


platform = _get_platform()

from os import system as os_sys
if platform == "win":
	compiled_c = 'main.exe'
elif platform== "android" or platform=='linux':
	compiled_c = './main'
else: pass#print(platform)

def Cencrypt(text, key):
    with open('i.txt','w') as f:
        f.write(text)
    with open('k.txt','w') as f:
        f.write(key)
        
    try:remove('out.txt')
    except:pass
    os_sys(" ".join([compiled_c, "en"]))
    remove('i.txt')
    remove('k.txt')
    with open('out.txt') as f:
        returner= f.read()
    remove('out.txt')
    return returner
        
def Cdecrypt(text, key):
    with open('i.txt','w') as f:
        f.write(text)
    with open('k.txt','w') as f:
        f.write(key)
    try:remove('out.txt')
    except:pass
    os_sys(" ".join([compiled_c, "de"]))
    remove('i.txt')
    remove('k.txt')
    with open('out.txt') as f:
        returner= f.read()
    remove('out.txt')
    return returner




##########################################################################
#                                                                        #
#                             Py Based                                   #
#                                                                        #
##########################################################################


from hashlib import sha1 as hashlib_sha1


seq={
"a": [5, 8, 1, 7, 2, 4, 3, 6],
"b": [7, 2, 1, 6, 3, 8, 4, 5],
"c": [3, 6, 2, 4, 7, 5, 1, 8],
"d": [1, 8, 3, 6, 5, 7, 4, 2],
"e": [2, 7, 8, 5, 4, 1, 3, 6],
"f": [3, 4, 6, 8, 1, 2, 5, 7],
"g": [2, 7, 4, 8, 3, 5, 6, 1],
"h": [8, 6, 1, 5, 4, 2, 7, 3],
"i": [4, 8, 1, 6, 3, 2, 5, 7],
"j": [1, 7, 8, 2, 3, 4, 6, 5],
"k": [1, 8, 3, 6, 2, 4, 7, 5],
"l": [1, 4, 2, 8, 5, 3, 6, 7],
"m": [5, 4, 7, 8, 3, 2, 1, 6],
"n": [8, 2, 1, 4, 5, 6, 3, 7],
"o": [6, 5, 4, 7, 1, 8, 3, 2],
"p": [5, 8, 7, 1, 4, 2, 6, 3],
"q": [2, 6, 4, 8, 1, 7, 3, 5],
"r": [6, 3, 7, 5, 4, 1, 2, 8],
"s": [4, 5, 7, 2, 6, 1, 3, 8],
"t": [7, 3, 6, 5, 2, 1, 8, 4],
"u": [3, 6, 4, 5, 1, 8, 2, 7],
"v": [5, 1, 2, 8, 4, 7, 6, 3],
"w": [6, 4, 2, 1, 7, 3, 5, 8],
"x": [5, 7, 4, 2, 6, 3, 1, 8],
"y": [7, 1, 2, 5, 6, 3, 8, 4],
"z": [4, 8, 2, 1, 5, 7, 3, 6],
"A": [3, 5, 8, 7, 1, 2, 6, 4],
"B": [7, 5, 6, 8, 4, 2, 3, 1],
"C": [7, 2, 1, 6, 5, 3, 8, 4],
"D": [6, 3, 1, 8, 7, 5, 4, 2],
"E": [3, 1, 5, 8, 7, 6, 4, 2],
"F": [8, 3, 1, 5, 7, 4, 2, 6],
"G": [7, 5, 8, 1, 3, 6, 2, 4],
"H": [7, 5, 1, 8, 4, 3, 6, 2],
"I": [7, 2, 3, 1, 6, 5, 4, 8],
"J": [1, 2, 6, 4, 8, 7, 3, 5],
"K": [7, 6, 2, 5, 4, 3, 8, 1],
"L": [2, 8, 5, 3, 7, 6, 1, 4],
"M": [4, 3, 5, 6, 2, 8, 7, 1],
"N": [8, 1, 6, 2, 7, 5, 3, 4],
"O": [4, 8, 3, 6, 1, 5, 2, 7],
"P": [3, 4, 7, 6, 2, 8, 5, 1],
"Q": [4, 5, 8, 3, 6, 1, 2, 7],
"R": [5, 4, 6, 2, 3, 7, 8, 1],
"S": [7, 4, 3, 5, 1, 6, 8, 2],
"T": [7, 4, 1, 5, 3, 8, 2, 6],
"U": [5, 2, 8, 3, 7, 1, 4, 6],
"V": [8, 2, 5, 6, 1, 7, 4, 3],
"W": [7, 5, 1, 4, 3, 6, 8, 2],
"X": [8, 5, 4, 6, 1, 3, 2, 7],
"Y": [6, 5, 7, 4, 8, 2, 1, 3],
"Z": [8, 3, 1, 7, 5, 4, 6, 2],
"1": [2, 6, 7, 8, 4, 3, 1, 5],
"2": [5, 2, 7, 8, 4, 3, 6, 1],
"3": [4, 6, 8, 3, 1, 5, 7, 2],
"4": [5, 1, 6, 3, 8, 7, 4, 2],
"5": [7, 6, 3, 5, 1, 4, 2, 8],
"6": [6, 8, 2, 7, 3, 4, 5, 1],
"7": [7, 3, 5, 4, 6, 8, 1, 2],
"8": [5, 8, 3, 7, 2, 4, 1, 6],
"9": [7, 8, 6, 2, 1, 4, 5, 3],
"0": [4, 8, 1, 3, 5, 2, 6, 7],
"+": [8, 6, 7, 2, 5, 4, 3, 1],
"-": [5, 8, 4, 2, 6, 3, 7, 1],
"*": [4, 8, 7, 5, 2, 1, 3, 6],
"/": [7, 1, 4, 2, 5, 8, 3, 6],
".": [2, 5, 1, 3, 7, 4, 6, 8],
",": [3, 7, 1, 4, 8, 2, 6, 5],
"\\": [7, 5, 6, 4, 8, 2, 3, 1],
"<": [3, 8, 4, 7, 6, 2, 5, 1],
">": [4, 6, 3, 5, 8, 1, 2, 7],
"?": [7, 2, 8, 4, 1, 3, 5, 6],
";": [4, 6, 7, 2, 1, 3, 8, 5],
"'": [8, 2, 1, 5, 6, 4, 7, 3],
":": [6, 8, 5, 2, 4, 7, 3, 1],
'\"': [3, 7, 6, 8, 1, 5, 4, 2],
"[": [3, 8, 1, 7, 5, 2, 6, 4],
"]": [7, 2, 5, 6, 4, 3, 1, 8],
"{": [3, 4, 1, 8, 2, 7, 5, 6],
"}": [4, 7, 6, 2, 5, 1, 3, 8],
"|": [6, 1, 3, 2, 5, 4, 7, 8],
"_": [8, 4, 3, 5, 7, 2, 6, 1],
"=": [3, 5, 6, 7, 1, 2, 8, 4],
"`": [1, 3, 8, 6, 2, 7, 5, 4],
"~": [5, 4, 1, 7, 6, 3, 8, 2],
"!": [6, 3, 2, 1, 4, 5, 7, 8],
"@": [3, 4, 5, 8, 7, 1, 2, 6],
"#": [5, 6, 3, 8, 4, 2, 7, 1],
"$": [7, 3, 4, 2, 5, 6, 8, 1],
"%": [4, 6, 1, 3, 7, 2, 8, 5],
"^": [1, 3, 6, 2, 8, 5, 7, 4],
"&": [7, 1, 8, 5, 6, 4, 3, 2],
"(": [3, 1, 5, 2, 8, 4, 6, 7],
")": [8, 5, 2, 4, 3, 1, 6, 7],
" ": [2, 8, 7, 1, 4, 5, 3, 6],
"’": [6, 5, 7, 3, 4, 8, 1, 2],
"—": [3, 2, 8, 4, 6, 5, 7, 1],
}

def _encrypt(text,C): 
	i=0
	serial= seq[C]
	le=len(text)

	while i<le:
		back=text[i:i+8]
		x=0
		#print('len',le)
		for j in serial:
			#print('i+x',i+x,'\tj',j-1)
			text[i+x]=back[j-1]
			x=(x+1)%8

		i+=8
	return text


def PYencrypt(texts, key):
	returner = []
	for text in texts.replace('\r\n', '\n').split('\n'):
		if text!='':
			text+=" "*((8-len(text)%8)%8)
			text=list(text)
			for c in key:
				text=text[2:]+text[:2]
				text= _encrypt(text, c)

			returner.append(''.join(text))

	return '\n'.join(returner)


def _decrypt(text,C):
	serial=seq[C]
	i=0
	le=len(text)
	while i<le:
		x=0
		back=text[i:i+8]
		for j in serial:
			text[i+ j-1]=back[x]
			x=(x+1)%8
		i+=8
	return text

def PYdecrypt(texts, key):
	returner = []
	key=key[::-1]
	for text in texts.replace('\r\n', '\n').split('\n'):
		if text!='':
			text+=" "*((8-len(text)%8)%8)
			text=list(text)
			for c in key:
				text=_decrypt(text,c)
				text=text[-2:]+text[:-2]

			returner.append(''.join(text))

	return '\n'.join(returner)


def test(msg=False,key=False, mode = 'C'):
	if mode.lower()=='c':
		encrypt = Cencrypt
		decrypt = Cdecrypt
	elif mode.lower() == 'py':
		encrypt = PYencrypt
		decrypt = PYdecrypt


	if msg==False:
		msg=input('Enter your message: ')
	if key==False:
		key=input('Enter your key: ')
	tt=time()
	light=encrypt(msg,key)
	en_tt=(time()-tt)
	print('\n\n     ============\n       encrypted\n     ============')
	
	print('\n"'+light+'"\n\n')
	
	tt=time()
	dark=decrypt(msg,key)
	de_tt=(time()-tt)
	print('\n\n     ============\n       decrypted\n     ============')
	
	print('\n"'+dark+'"\n\n')
	x=len(dark)
	print('\n\nMsg len=', len(msg),'\n key len=', len(key),'\nEncrypted in %fs'%en_tt,'\nDecrypted in %fs'%de_tt,'\n time per key (en): ', en_tt/len(key),'\n time per key (de): ', de_tt/len(key))
	if msg == encrypt(dark, key):
		print("passed")

#print(PYdecrypt(open('data/userlog.leach').read(), 'Asuna'))