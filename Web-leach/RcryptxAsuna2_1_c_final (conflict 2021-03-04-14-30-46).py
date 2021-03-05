"""Will return (also save output as out.txt) line by line encrypted or decrypted data"""

from os import environ
from sys import platform as _sys_platform

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



#from subprocess import call as os_system
from os import system as os_sys, remove
if platform == "win":
	compiled_c = 'main.exe'
elif platform== "android" or platform=='linux':
	compiled_c = './main'
else: print(platform)

def encrypt(text, key):
    with open('i.txt','w') as f:
        f.write(text)
    with open('k.txt','w') as f:
        f.write(key)
    os_sys(" ".join([compiled_c, "en"]))
    remove('i.txt')
    remove('k.txt')
    with open('out.txt') as f:
        returner= f.read()
    remove('out.txt')
    return returner
        
def decrypt(text, key):
    with open('i.txt','w') as f:
        f.write(text)
    with open('k.txt','w') as f:
        f.write(key)
    os_sys(" ".join([compiled_c, "de"]))
    remove('i.txt')
    remove('k.txt')
    with open('out.txt') as f:
        returner= f.read()
    remove('out.txt')
    return returner

from time import time








print('Welcome to Rcryption.una')

def test(msg=False,key=False):
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

	
	# re_msg=decrypt(light, key)
	# re_tt=(time()-tt)
	# if msg+" "*((8-len(msg)%8)%8)==re_msg:
	# 	print("Tested\nPassed!\nTest time taken=%fs"%re_tt)
	# else:
	# 	print("Tested\nFaileded!\nTest time taken=%fs"%re_tt)

# test('1'*200, '2'*64)
#test(open('data/userlog.leach').read(), 'Asuna')
# while True:
# 	test()
'''
Msg len= 5306
 key len= 263
Encrypted in 0.069003s
Decrypted in 0.059997s
 time per key (en):  0.000262367408085232
 time per key (de):  0.00022812487961221557
Entered message!
Entered key!
Tested
Passed!
Test time taken=0.081000s
'''

'''
Msg len= 530600
 key len= 2630
Encrypted in 271.080402s
Decrypted in 278.949799s
 time per key (en):  0.1030723963400257
 time per key (de):  0.10606456228988706
Tested
Passed!
Test time taken=266.160028s
'''

