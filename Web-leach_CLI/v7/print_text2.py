from time import sleep
import re
import sys
from shutil import get_terminal_size
from math import ceil

wait_time = 0
def null(*a):
	return a[0]
class XprintClass:
	def __init__(self) -> None:
		
		self.text = ""
		
		self.normal_tx="0"
		self.ul_tx="4"
		self.neg_tx="7"
		self.bold_tx="1"
		

		self.ash_c="30"
		self.red_c="31"
		self.green_c="32"
		self.yello_c="33"
		self.blue_c="34"
		self.pink_c="35"
		self.cayan_c="36"
		self.white_c="37"

		self.normal_b="40"
		self.red_b="41"
		self.green_b="42"
		self.yello_b="43"
		self.blue_b="44"
		self.pink_b="45"
		self.cayan_b="46"
		self.white_b="47"
		self.black_b="48"





		self.custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']

		self.re = { #regex for custom type codes
			'markup': re.compile(r'/<(.*)?>/'),
			'/u/': re.compile(r'==(.*?)=='),
			'/hu/': re.compile(r'===(.*?)==='),
		}

		
		self.no_code = False
		self.no_colors = False

	def __getattr__(self, name):
		if name=="default_style":
			return  {
						"color": '',
						"bg": '',
						"style": []
						}
		else:
			return self.__dict__[name]
			
	def make_str(self, *text, sep = " ", end="\n", highlighter=False):
		self.text= str(sep).join(map(str, text)) + str(end)
		self.tnt_helper(highlighter)

	def text_styling_markup(self): #not in use
		''' for custom text stypling like html
		print(tnt_helper('/<style= col: red>/ 69'))'''
		if '/<' not in self.text:
			return 0

		
		while self.re['markup'].search(self.text):
			a = self.re['markup'].search(self.text)
			if a:
				style = a.group(1)

				self.text = self.text.replace(a.group(0), '')



	def tnt_helper(self, highlighter):
		''' i) custom_type_codes are used for custom commands to
		simplify the code
		ii) other text modifications are made here and passes optimized
		text for the typing and speaking engine respectively'''

		if highlighter:
			
			self.text = self.re["/hu/"].sub(r"/hu/\1/=/", self.text)
			
			self.text =  self.re["/u/"].sub(r"/u/\1/=/", self.text)

		self.text_styling_markup()
		


	def slowtype(self, *text, sep= ' ', wait_time=wait_time, end='\n', highlighter=False, auto_resetting=True, run_at_start=null, use_self_text=False):
		"""main typing engine that prints inputted text
			slowly based on waiting time
			
			text: text to be printed
			sep: separator between each text args
			wait_time: time to wait between each character
			end: end of line character
			highlighter: if True, will highlight text using ===.*=== -> /hu/ and ==.*== -> /u/
			auto_resetting: if True, will reset the no_code and no_color after each output
			use_self_text: set True if the *text already used by make_str
			"""
		self.custom_style = self.default_style.copy()
		if not use_self_text:
			self.make_str(*text, sep=sep, end=end, highlighter=highlighter)
		self.text= run_at_start(self.text)
		self.wait_time=float(wait_time)
		#self.end=str(end)


		self.custom_style_temp = self.custom_style.copy()

		#custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']
		i=0
		while  i<len(self.text):
			slept= False
			has_code= False

			### MUST CLOSE THESE NO COLOR AND NO CODE TAGS ###

			if self.text[i:i+3] == '/~`':
				self.no_code = True
				i+=3
				continue

			if self.text[i:i+3] == '`~/':
				self.no_code = False
				i+=3	
				continue

			if self.text[i:i+3] == '/~~':
				self.no_colors = True
				i+=3
				continue

			if self.text[i:i+3] == '~~/':
				self.no_colors = False
				i+=3
				continue

			






			if self.no_code==False:
				if self.text[i]=='/' and '/' in self.text[i+2:i+5]:
					if self.no_colors==False and self.text[i+1] in ('a','r','g','y','b','p','c','w','=','u','i','h','_'):
						x=self.text[i+1]
						if x=='a': self.custom_style_temp["color"]=self.ash_c
						elif x=='r': self.custom_style_temp["color"]=self.red_c
						elif x=='g': self.custom_style_temp["color"]=self.green_c
						elif x=='y': self.custom_style_temp["color"]=self.yello_c
						elif x=='b': self.custom_style_temp["color"]=self.blue_c
						elif x=='p': self.custom_style_temp["color"]=self.pink_c
						elif x=='c': self.custom_style_temp["color"]=self.cayan_c
						elif x=='w': self.custom_style_temp["color"]=self.white_c
						elif x=='=':
							sys.stdout.write('\033[0m')
							sys.stdout.flush()
							self.custom_style_temp = self.default_style.copy()
						elif x=='u': self.custom_style_temp["style"].append(self.ul_tx)
						elif x=='i': self.custom_style_temp["style"].append(self.neg_tx)
						elif x=='h': self.custom_style_temp["style"].append(self.bold_tx)
						
						if self.text[i+2]=='/':
							has_code=True
							i+=2
						elif self.text[i+2] in ('a','r','g','y','b','p','c','w','u','i','h','_'):
							x=self.text[i+2]
							if x=='a': self.custom_style_temp["bg"]= self.normal_b
							elif x=='r': self.custom_style_temp["bg"]=self.red_b
							elif x=='g': self.custom_style_temp["bg"]=self.green_b
							elif x=='y': self.custom_style_temp["bg"]=self.yello_b
							elif x=='b': self.custom_style_temp["bg"]=self.blue_b
							elif x=='p': self.custom_style_temp["bg"]=self.pink_b
							elif x=='c': self.custom_style_temp["bg"]=self.cayan_b
							elif x=='w': self.custom_style_temp["bg"]=self.white_b
							elif x=='u': self.custom_style_temp["style"].append(self.ul_tx)
							elif x=='i': self.custom_style_temp["style"].append(self.neg_tx)
							elif x=='h': self.custom_style_temp["style"].append(self.bold_tx)

							if self.text[i+3]=='/':
								has_code=True
								i+=3
							elif self.text[i+3] in ('u','i','h'):
								x=self.text[i+3]
								if x=='u': self.custom_style_temp["style"].append(self.ul_tx)
								elif x=='i': self.custom_style_temp["style"].append(self.neg_tx)
								elif x=='h': self.custom_style_temp["style"].append(self.bold_tx)

								if self.text[i+4]=='/':
									has_code = True
									i+=4


					elif self.text[i+1]=='s':
						
						sys.stdout.flush()
						if self.text[i+3]=='/':
							try:
								sleep(float(self.text[i+2]))
								i+=3
								slept = True
							except: pass
						elif self.text[i+4]=='/':
							try:
								sleep(float(self.text[i+2:i+4]))
								i+=4
								slept = True
							except: pass
						elif self.text[i+5]=='/':
							try:
								sleep(float(self.text[i+2:i+5]))
								i+=5
								slept = True
							except: pass
			if has_code==True:
				self.custom_style = self.custom_style_temp.copy()
				

				#print(self.custom_style)
				
				style = '\033['
				
				for s in ("color", "bg"):
					if self.custom_style[s]:
						style += self.custom_style[s] + ";"
						
				if self.custom_style["style"]:
					style += ";".join(self.custom_style["style"])
				else:
					style = style[:-1]
					
				style += "m"
				sys.stdout.write(style)
				sys.stdout.flush()
			elif slept==True:
				sys.stdout.flush()
			else:
				sys.stdout.write(self.text[i])
				if wait_time!=0:
					sys.stdout.flush()
					sleep(self.wait_time)
			i+=1
			# print(has_code, slept)

		#sys.stdout.write(self.end)
		sys.stdout.flush()

		if auto_resetting:
			self.reset()

	def reset(self):
		self.no_colors = self.no_code = False

	def remove_style(self, text,highlighter=False):
		"""text: must be parsed string (sep, end are parsed)"""
		
		self.text = text
		self.tnt_helper(highlighter)
		self.text = re.sub("/s\d*[.]?\d*/", "", self.text)
		return re.sub("/[argybpcw \=uih_]+/","", self.text)
		
		
class oneLine(XprintClass):
	def __init__(self):
		super().__init__()
		self.old_len = None
		pass#print(self.__dir__())
		self.__all__ = ["new", "update"]

	def get_len(self, string):
		# loop to read each line
		lens = []
		for line in string.split("\n"):
			lens.append(len(line))

		return lens

		
	def update(self, *text, sep= ' ', wait_time=wait_time, end='\n', highlighter=False, auto_resetting=True, run_at_start=null):
		
		self.make_str(*text, sep=sep, end=end, highlighter=highlighter)
		
		if self.old_len is not None:
			# print(self.old_len)
			for i in self.old_len:
				sleep(.001)
				size = int(get_terminal_size()[0])
				sys.stdout.write('\x1b[2K\x1b[1A\x1b[2K'*ceil(i/size))
				sys.stdout.flush()


		self.old_len = self.get_len(self.remove_style(self.text))

		
		self.slowtype(use_self_text=True, sep=sep, wait_time=wait_time, end=end, highlighter=highlighter, auto_resetting=auto_resetting, run_at_start=run_at_start)
		
	def new(self):
		self.__init__()
		

XprintEngine = XprintClass()
xprint = XprintEngine.slowtype
remove_style = XprintEngine.remove_style


if __name__ == '__main__':
	xprint("/rhu/hello/=/ q to quit")

	x = ''

	while x != 'q':
		x = input()
		xprint(x, highlighter=True)