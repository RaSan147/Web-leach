# pylint: disable=unused-wildcard-import
# pylint: disable=unused-import


import rjsmin
from re import compile as re_compile
import json

# from main import AboutApp

class css_minify():
	def __init__(self):
		# remove comments - this will break a lot of hacks :-P
		self.css1 = re_compile( r'\s*/\*\s*\*/') # preserve IE<6 comment hack .sub( r'\s*/\*\s*\*/', "$$HACK1$$", css )
		self.css2 = re_compile( r'/\*[\s\S]*?\*/') # .sub( r'/\*[\s\S]*?\*/', "", css )
		#css = css.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

		# url() doesn't need quotes
		self.css3 = re_compile( r'url\((["\'])([^)]*)\1\)') # .sub( r'url\((["\'])([^)]*)\1\)', r'url(\2)', css )

		# spaces may be safely collapsed as generated content will collapse them anyway
		self.css4 = re_compile( r'\s+') # .sub( r'\s+', ' ', css )

		# shorten collapsable colors: #aabbcc to #abc
		self.css5 = re_compile( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)')
		# .sub( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)', r'#\1\2\3\4', css )
		# fragment values can loose zeros
		self.css6 = re_compile( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;')
		# .sub( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;', r':\1;', css )

		self.css7 = re_compile( r'([^{]+){([^}]*)}')
		self.css8 = re_compile( r'(?<=[\[\(>+=])\s+|\s+(?=[=~^$*|>+\]\)])')
		self.css9 = re_compile( r'(.*?):(.*?)(;|$)')


	def css_min(self, css_txt):
		# remove comments - this will break a lot of hacks :-P
		css = self.css1.sub( "$$HACK1$$", css_txt ) # preserve IE<6 comment hack
		css = self.css2.sub( "", css )
		css = css.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

		# url() doesn't need quotes
		css = self.css3.sub( r'url(\2)', css )

		# spaces may be safely collapsed as generated content will collapse them anyway
		css = self.css4.sub( ' ', css )

		# shorten collapsable colors: #aabbcc to #abc
		css = self.css5.sub( r'#\1\2\3\4', css )

		# fragment values can loose zeros
		css = self.css6.sub( r':\1;', css )
		box = []
		for rule in self.css7.findall( css ):

			# we don't need spaces around operators
			selectors = [self.css8.sub( r'', selector.strip() ) for selector in rule[0].split( ',' )]

			# order is important, but we still want to discard repetitions
			properties = {}
			porder = []
			for prop in self.css9.findall( rule[1] ):
				key = prop[0].strip().lower()
				if key not in porder: porder.append( key )
				properties[ key ] = prop[1].strip()

			# output rule if it contains any declarations
			if properties:
				box.append("%s{%s}" % ( ','.join( selectors ), ''.join(['%s:%s;' % (key, properties[key]) for key in porder])[:-1] ))
		return '\n'.join(box)
CSSmin = css_minify()

class MakeHtml_:   #func_code= 7000
	#def ensure_template(self)
	def return_sub_page(self, all_list, sub_dirs, page_index, proj_name, 
			discuss_id="", description="", tags=[], stars=3.3, poster_loc=""):   #func_code= 7002
		#if not os_isfile(AboutApp.temp_dir+'wl-page.html'):
		#	if UserData.god_mode(2) == 'offline':
		#		return False
		sub_page_template= Fsys.reader('pwa-wl-page.xhtml', encoding='utf8')%(proj_name, "CHAPTER", str(all_list), str(sub_dirs), page_index, "[]", proj_name, "[0,1,1,1]", "", "", 0, "[]", "")
		#print(type(sub_page_template))

		return sub_page_template


	def return_main_page(self, sub_dirs, proj_name, json_dict):   #func_code= 7003
		"""
		Return the main page of the project.
		"""
		#if not os_isfile(AboutApp.temp_dir+'wl-page.html'):
		#	if UserData.god_mode(2) == 'offline':
		#		return False
		main_page_template= Fsys.reader('pwa-wl-page.xhtml', encoding='utf8')%(proj_name, "CHAPTER-LIST", "[]", str(sub_dirs), -1, "[]", proj_name, str(json_dict["default_style"]), json_dict["discuss_id"] , json_dict["description"].replace('"', '\\"') , json_dict["stars"], json_dict["tags"], json_dict["poster_loc"])
		#print("000000", type(main_page_template))
		
		return main_page_template
		
		
	def make_online_page(self, all_li, dir_list, project, project_alias, seq,
			new_sub_dirs =[], ext='', dir_sorted = False,
			discuss_id="", description="", tags=[], stars=3.3, poster_loc=""):   #func_code= 7001
		"""all_li: all_list.all_names
		dir_list: sub_dirs
		project: project_name
		project_alias: project_alias to be Desplayed in the page
		seq: img to sort
		new_sub_dirs: new sub_dirs when update
		ext: extension
		dir_sorted: if dir_sorted is true, then the dir_list is sorted
		discuss_id: discuss_id
		description: project description
		tags: project tags
		stars: project rating stars
		poster_loc: project poster location
		"""
		
		#from main_ez import IOsys

		dir_path = os_dirname(os_realpath(__file__))

		leach_logger(log(['7001xI', project, seq, ext, dir_sorted]))
		first_page=None
		dir_len = len(dir_list)
		dir_bkp = dir_list[:]

		if dir_sorted:
			dir_list = natsort.natsorted(dir_list)
			
		first_page = dir_path+'/Download_projects/'+ project+'/'+'index.html'
		def make_json(type, imgs =[], index = -1, return_dict=False):
			
			
			x = {}
			x["page_type"] = type
			x["proj_name"] = project_alias
			x["pages_list"] = dir_list
			x["default_style"] = [0,1,1,1]
			if type=="CHAPTER-LIST":
				x["new_pages"] = new_sub_dirs
				x["discuss_id"] = discuss_id
				x["description"] = description
				x["tags"] = tags
				x["stars"] = stars
				x["poster_loc"] = poster_loc
			if type =="CHAPTER":
				x["images_loc"] = imgs
				x["current_page_index"] = index
				
				
			if return_dict: return x, json.dumps(x)
			return json.dumps(x)
				

		for i in range(dir_len):
			if '.' == dir_list[i]:
				dir_list.extend(natsort.natsorted(all_li[dir_bkp.index('.')]))
			
			temp= all_li[dir_bkp.index(dir_list[i])]
			
			if seq:
				box= self.return_sub_page(natsort.natsorted(temp), dir_list, i, project)
			else:
				box= self.return_sub_page(temp, dir_list, i, project)
			
			if not box:
				return False

			json_file = make_json("CHAPTER", temp, i)

			Fsys.writer('index.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
			Fsys.writer('index.html.json', 'w', json_file,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
			
		
		
		json_dict, json_file = make_json("CHAPTER-LIST", return_dict=True)

		box = self.return_main_page(dir_list, project, json_dict)
		
		
		Fsys.writer('index.html', 'w', box,'Download_projects/'+ project, f_code= '40001')

		Fsys.writer('index.html.json', 'w', json_file,'Download_projects/'+ project, f_code= '40001')
		return first_page


	

	def make_pages(self, all_li, dir_list, project, project_alias, seq, 
			new_sub_dirs =[], ext='', dir_sorted = False,
			discuss_id="", description="", tags=[], stars=3.3, poster_loc=""):   #func_code= 7001
		"""all_li: all_list.all_names
		dir_list: sub_dirs
		project: project_name
		project_alias: project_alias to be Desplayed in the page
		seq: img to sort
		new_sub_dirs: new sub_dirs when update
		ext: extension
		dir_sorted: if dir_sorted is true, then the dir_list is sorted
		discuss_id: discuss_id
		description: project description
		tags: project tags
		stars: project rating stars
		poster_loc: project poster location
		"""

		dir_path = os.path.dirname(os.path.realpath(__file__))

		leach_logger(log(['7001xI', project, seq, ext, dir_sorted]))

		dir_len = len(dir_list)
		dir_bkp = dir_list[:]

		if dir_sorted:
			dir_list = natsort.natsorted(dir_list)
			
		first_page = dir_path+'/Download_projects/'+ project+'/'+'index.html'
		def make_json(type, imgs =[], index = -1, return_dict=False):
			
			
			x = {}
			x["page_type"] = type
			x["proj_name"] = project_alias
			x["pages_list"] = dir_list
			x["default_style"] = [0,1,1,1]
			if type=="CHAPTER-LIST":
				x["new_pages"] = new_sub_dirs
				x["discuss_id"] = discuss_id
				x["description"] = description
				x["tags"] = tags
				x["stars"] = stars
				x["poster_loc"] = poster_loc
			if type =="CHAPTER":
				x["images_loc"] = imgs
				x["current_page_index"] = index
				
				
				
			if return_dict: return x, json.dumps(x)
			return json.dumps(x)
				
				
				
			
		for i in range(dir_len):
			if '.' == dir_list[i]:
				dir_list.extend(natsort.natsorted(all_li[dir_bkp.index('.')]))
			
			temp= all_li[dir_bkp.index(dir_list[i])]
			
			if seq:
				box= self.return_sub_page(natsort.natsorted(temp), dir_list, i, project)
			else:
				box= self.return_sub_page(temp, dir_list, i, project_alias)
			
			if not box:
				return False

			json_file = make_json("CHAPTER", temp, i)

			Fsys.writer('index.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
			Fsys.writer('index.html.json', 'w', json_file,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
			
		
		json_dict, json_file = make_json("CHAPTER-LIST", return_dict=True)

		box = self.return_main_page(dir_list, project_alias, json_dict)
		
		
		Fsys.writer('index.html', 'w', box,'Download_projects/'+ project, f_code= '40001')

		Fsys.writer('index.html.json', 'w', json_file,'Download_projects/'+ project, f_code= '40001')
		return first_page

MakeHtml = MakeHtml_()
