import shutil, math, time, sys


from print_text2 import xprint, XprintEngine

print(shutil.get_terminal_size()[0])


for i in range(100):
	size = int(shutil.get_terminal_size()[0])
	x = "ab/r/c/=/ xyz"
	xprint(x*i)
	#time.sleep(1)
	print('\x1b[1A'*int(math.ceil(len(XprintEngine.remove_style(x*i))/size)), end ="")
	#time.sleep(.1)
#print(len())