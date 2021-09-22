#: *****************************************************************************
#:               The code in this file was created by Ratul Hasan              *
#:                     So comlpete credit goes to him(me)                      *
#: *****************************************************************************
#:         Sharing this code without my permission is not allowed              *
#: *****************************************************************************
#: This code was created based on IDLE, Pydroid(Android), qPython(Android) etc.*
#: So most online/web site based idle(i.e: Sololearn) can't run this code	   *
#: properly.                                                                   *
#: *****************************************************************************
#: If there is any bug or you want to help please let me know.                 *
#: e-mail: wwwqweasd147[at]gmail[dot]com                                       *
#: *****************************************************************************


from random import randint
from functools import partial

base_li0= {'0':0,

	'1':1,

	'2':2 ,

	'3':3 ,

	'4':4 ,

	'5':5 ,

	'6':6 ,

	'7':7 ,

	'8':8 ,

	'9':9 ,

	'a':10 ,

	'b':11 ,

	'c':12 ,

	'd':13 ,

	'e':14 ,

	'f':15 ,

	'g':16 ,

	'h':17 ,

	'i':18 ,

	'j':19 ,

	'k':20 ,

	'l':21 ,

	'm':22 ,

	'n':23 ,

	'o':24 ,

	'p':25 ,

	'q':26 ,

	'r':27 ,

	's':28 ,

	't':29 ,

	'u':30 ,

	'v':31 ,

	'w':32 ,

	'x':33 ,

	'y':34 ,

	'z':35 ,

	'A':36 ,

	'B':37 ,

	'C':38 ,

	'D':39 ,

	'E':40 ,

	'F':41 ,

	'G':42 ,

	'H':43 ,

	'I':44 ,

	'J':45 ,

	'K':46 ,

	'L':47 ,

	'M':48 ,

	'N':49 ,

	'O':50 ,

	'P':51 ,

	'Q':52 ,

	'R':53 ,

	'S':54 ,

	'T':55 ,

	'U':56 ,

	'V':57 ,

	'W':58 ,

	'X':59 ,

	'Y':60 ,

	'Z':61 ,

	'?':62 ,

	'!':63 

}

base_li= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!"
#import sys

def dec2base(n,base):

	out=''
	if n==0:
		return '0'

	while n!=0:

		out+=base_li[n%base]

		n//=base

	

	return out[::-1]



def base2dec(n, base, _type=int):
	out=0
	n=n[::-1]

	for  i in range(len(n)):

		out+=base_li0[n[i]]*(base**(i))

	return _type(out)

from datetime import datetime, timedelta

def dt_():
	"""returns time in GMT+6 
	"""
	return str(datetime.utcnow()+ timedelta(hours=6))

	# return str(datetime.now())

# print(dt_())
#print(int(str(dt_()).replace('-','').replace(' ','').replace('.','').replace(':','')))

def compressed_dt(_dt= None):

	dt_now= int((dt_() if _dt is None else _dt).replace('-','').replace(' ','').replace('.','').replace(':',''))

	return dec2base(dt_now,63)

def compressed_ip(ip):
	
	ip_now= ip.split('.')
	new_dec2base = partial(dec2base, base=63)

	junk = [randint(0,255) for i in range(4)]
	return '~'.join(map(new_dec2base, map(int, junk[:2]+ip_now+junk[2:])))

def dec_ip(ip):
	ip_now= ip.split('~')[2:-2]
	new_base2dec = partial(base2dec, base=63, _type=str)

	return '.'.join(map(new_base2dec, ip_now))	

def dec_dt(dt):
	ddt = str(base2dec(dt, 63))
	#print(ddt)
	YYYY = ddt[:4]
	MM= ddt[4:6]
	DD= ddt[6:8]
	hh= ddt[8:10]
	mm= ddt[10:12]
	ss= ddt[12:14]+'.'+ddt[14:]

	return (YYYY,MM,DD,hh, mm, ss)

# print(dec_dt(compressed_dt()))
cdt_ = compressed_dt

def get_tz():

	tznow = datetime.now().astimezone()

	return (str(tznow)[-6:])


def flatten_array(out, output_type = list):
	'''Will flatten `list`, `tuple`, `set`'''
	if not isinstance(out, list):
		out= list(out)
	i=0
	l =len(out)
	while i<l:
		if isinstance(out[i], (list, tuple, set)):
			out.extend(flatten_array(out.pop(i)))
			l-=1
		else: i+=1
	if not isinstance(out, output_type):
		out= output_type(out)
	return out

# from time import time
# arr = [1,[],[],[],[],2, 3, [], 4, [], 5, [6], 7, 8, 9, [10,[1,1,3]], []]*500
# print(len(arr))
# x=time()
# oo= flatten_array(arr)
# print(len(oo))
# print(time()-x)
'''def atoi(text):
	return int(text) if text.isdigit() else text


def sorting_algoN(test_string): 


	a= sorting_algoN_re.findall(test_string)

	if a!=[]:

		a=[atoi(x) for x in a]

	else:

		a=[0]

	return a'''

# print(sys.argv)

#print(dec2base(20201123220123445462,63))

# print(compressed_dt())

# datetime object containing current date and time





# dt_now= int(str(dt_()).replace('-','').replace(' ','').replace('.','').replace(':',''))

# for i in range (2,75):

#	 print(i,'\t=\t', dec2base(int(dt_now),int(i)), '\t', base2dec(dec2base(int(dt_now),int(i)),i), '\t',dt_now,'\t', base2dec(dec2base(int(dt_now),int(i)),i)==dt_now)



#	 # point1=0

#	 # dt_now= int(str(dt_now).replace('-','').replace(' ','').replace('.','').replace(':',''))

#	 # for _ in range(10):

#	 #	 if base2dec(dec2base(int(dt_now),int(i)),i)==dt_now:

#	 #		 point1+=1

#	 # point2=0

#	 # for _ in range(100):

#	 #	 dt_now= int(str(dt_now).replace('-','').replace(' ','').replace('.','').replace(':',''))

#	 #	 if base2dec(dec2base(int(dt_now),int(i)),i)==dt_now:

#	 #		 point2+=1

#	 # print(i, '\t>>\t',point1, '\t>>\t',point2)

#	 # # print(i,'\t=\t', dec2base(int(dt_now),int(i)), '\t', base2dec(dec2base(int(dt_now),int(i)),i), '\t',dt_now,'\t', base2dec(dec2base(int(dt_now),int(i)),i)==dt_now)



# print(getSystemInfo())

