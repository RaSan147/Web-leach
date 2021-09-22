# pylint: disable=unused-wildcard-import
# pylint: disable=unused-import

if __file__ == 'make_html2.py':
	from main import *
	pass
import rjsmin
from re import compile as re_compile

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

class MakeHtml_:
	def return_sub_page(self, all_list, sub_dirs, page_index, title):
		sub_page_template= open('wl-page-2.html').read()%(all_list, sub_dirs, page_index, title)

		return sub_page_template


	def return_main_page(self, sub_dirs, proj_name):
		"""
		Return the main page of the project.
		"""
		main_page_template="""
<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">

<head>
	<title></title>
	<style>""" + CSSmin.css_min("""
		.popup .overlay {
			position:fixed;
			top:0px;
			left:0px;
			width:100vw;
			height:100vh;
			background:rgba(0,0,0,0.7);
			z-index:1;
			display:none;
		}

		.popup .content {
			position:fixed;
			top:50%;
			left:50%;
			color: #AAA;
			transform:translate(-50%,-50%) scale(0);
			background:#222;
			width:500px;
			height:250px;
			z-index:2;
			text-align:center;
			padding:20px;
			box-sizing:border-box;
			font-family:"Open Sans",sans-serif;
		}

		.popup .close-btn {
			cursor:pointer;
			position:absolute;
			right:20px;
			top:20px;
			width:30px;
			height:30px;
			background:#222;
			color:#fff;
			font-size:25px;
			font-weight:600;
			line-height:30px;
			text-align:center;
			border-radius:50%;
		}

		.popup.active .overlay {
			display:block;
		}

		.popup.active .content {
			transition:all 300ms ease-in-out;
			transform:translate(-50%,-50%) scale(1);
		}

		button {
			position:absolute;
			top:50%;
			left:50%;
			transform:translate(-50%,-50%);
			padding:15px;
			font-size:18px;
			border:2px solid #222;
			color:#222;
			text-transform:uppercase;
			font-weight:600;
			background:#fff;
		}
		
		
		body{
			min-height:100vh; 
			margin:0; 
			display: flex;
			flex-direction: column;
		}

		html, body, input, textarea, select, button {
			border-color: #736b5e;
			color: #e8e6e3;
			background-color: #131516;
		}
		* {
			scrollbar-color: #0f0f0f #454a4d;
		}
		#allA{
		text-align: center;
		margin-left: 5%;
		margin-right: 5%;
		width: 85%;
		}

		#lastleft{
		font-size: 20px;
		font-weight: 600;
		font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
		text-decoration: none;
		color: #06A5EE;
		}

		#proj_title{
		font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
		}
		.list_class{
		font-size: 20px;
		font-weight: 600;
		font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
		text-decoration: none;
		color: #06A5EE;
		overflow-wrap: break-word;
		padding-left: 5%;
		padding-right: 5%;
		}

		
		#footer {
		margin-top: auto;
		width: 100%;
		text-align: center;
		}

""") + """

	</style>

</head>

<body>
	<div class="popup" id="popup-1">
	<div class="overlay"></div>
	<div class="content">
		<div class="close-btn" onclick="togglePopup(0)">&times;</div>
		<h1>Psst.. </h1>
		<p id="last"></p>
	</div>
	</div>
	<h2 style="text-align: center;" id="proj_title"></h2>
	<hr style="width: 80%;">
	<center>
	<div id='allA'></div>
	</center>
	<br><br>

</body>

<footer id='footer'>
	<br><br><center><hr width='95%'><hr width='89%'></center>
	<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>
	<br><br>
</footer>


<script type="text/javascript">
""" + rjsmin.jsmin("""
const pages_list = %s;
const current_page_index = -1;
const proj_name= "%s";
document.title = proj_name;

document.getElementById('proj_title').innerText=proj_name;

var all_li= document.getElementById('allA');
for (var i = 0; i < pages_list.length; i++){
	var linkX =document.createElement('A');
	var linkContainer = document.createElement('DIV');
	linkContainer.className = 'sub_li_divs';
	linkX.href = pages_list[i]+ '/'+pages_list[i]+".html";

	linkX.innerHTML = pages_list[i];
	if(i%%2==0){
	linkContainer.style.backgroundColor = '#35393b' ;
	}
	else{
	linkContainer.style.backgroundColor = '#222426' ;
	}

	linkX.className = 'list_class';
	linkContainer.appendChild(linkX);
	linkContainer.appendChild(document.createElement('BR'));
	var hr_ = document.createElement('HR');
	linkContainer.appendChild(hr_);
	all_li.appendChild(linkContainer);
}
	function togglePopup(on_or_off){
	document.getElementById("popup-1").classList.toggle("active");
	if(on_or_off==0){
	localStorage.setItem(proj_name, current_page_index);
	}

}
	if(localStorage.getItem(proj_name)!=null){
	if(localStorage.getItem(proj_name)!=current_page_index){
	document.getElementById('last').innerHTML= "You left the page on <a id='lastleft' href='"+ pages_list[localStorage.getItem(proj_name)]+ '/'+pages_list[localStorage.getItem(proj_name)]+".html'>"+ pages_list[localStorage.getItem(proj_name)]+ '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
	togglePopup(1);
	}}

	else{
		localStorage.setItem(proj_name, current_page_index);
	}"""%(str(sub_dirs),proj_name)) + """
</script>"""

		return main_page_template


	dir_path = os_dirname(os_realpath(__file__))

	def make_pages(self, all_li, dir_list, project, seq, ext='', dir_sorted = False):   #func_code= 7001
		"""all_li: all_list.all_names
		dir_list: sub_dirs
		project: project_name
		seq: img to sort
		ext: extension
		dir_sorted: if dir_sorted is true, then the dir_list is sorted
		"""

		leach_logger(log(['7001xI', project, seq, ext, dir_sorted]))
		first_page=None
		dir_len = len(dir_list)
		dir_bkp = dir_list[:]


		first_page = self.dir_path+'/Download_projects/'+ project+'/'+project+'.html'
		for i in range(dir_len):
			temp= all_li[dir_bkp.index(dir_list[i])]
			
			if seq:
				box= self.return_sub_page(str(natsort.natsorted(temp)), str(dir_list), i, project)
			else:
				box= self.return_sub_page(str(temp), str(dir_list), i, project)
			
			Fsys.writer(dir_list[i]+'.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
		Fsys.writer(project+'.html', 'w', self.return_main_page(str((dir_list)), project),'Download_projects/'+ project, f_code= '40001')
		return first_page

MakeHtml = MakeHtml_()