# pylint: ignore=unused-wildcard-import

# from basic_shared import *
import rjsmin
from re import compile as re_compile
# from main import *

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
cssmin = css_minify()
css_min = cssmin.css_min


def return_sub_page(all_list, sub_dirs, page_index, title):
	sub_page_template="""<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">
<html>
<head>
	<title></title>

	<style type="text/css">
	""" + css_min("""

		.container {
			margin: 80px auto;
			width: 400px;
			text-align: center;
		}

		#page_title {
			text-align: center;
			color: #00b7ff;
		}


		#paginate_container {
			justify-self: center;
			display: grid;
			grid-template-columns: auto auto;
			width: min(100%, 720px);
		}

		.outlines {
			text-shadow:
				-1px -1px 0 #000,
				1px -1px 0 #000,
				-1px 1px 0 #000,
				1px 1px 0 #000;

		}

		.paginators {
			font: bold 20px Arial;
			text-decoration: none;
			background-color: #8a8b8d6b;
			color: #00b7ff;
			padding: 2px 6px 2px 6px;
			border-top: 1px solid #828d94;
			box-shadow: 4px 4px #5050506b;
			border-left: 1px solid #828D94;
			text-align: center;
		}

		#lastleft {
			font-size: 20px;
			font-weight: 600;
			font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
			text-decoration: none;
			color: #06A5EE;
		}

		body {
			font-family: Arial, Helvetica, sans-serif;
			min-height: 100vh;
			margin: 0;
			display: flex;
			flex-direction: column;
			background-color: #222
		}

		#pageFormats {
			background-color: rgba(117, 117, 119, 0.507);
			height: 35px;
			width: 140px;
			color: #3ab7ff;
			font-size: 17px;
			font-family: sans-serif;
			font-weight: 700;
		}


		#spacer {
			background-color: #222;
			color: #3094BE;
			font-weight: 500;
		}

		.containerR {
			display: block;
			position: relative;
			padding-left: 35px;
			margin-bottom: 12px;
			cursor: pointer;
			font-size: 22px;
			-webkit-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;
		}

		/* Hide the browser's default radio button */
		.containerR input {
			position: absolute;
			opacity: 0;
			cursor: pointer;
		}

		#LARROW:not(.disabled),
		#RARROW:not(.disabled) {
			cursor: pointer;
			color: #C8C3BC;
			background-color: #103c8b;
		}

		.disabled {
			cursor: default;
			color: #C8C3BC;
			background-color: #999;
		}


		#LARROW:not(.disabled):hover,
		#RARROW:not(.disabled):hover {
			background-color: #6495ED;
			color: #EEE;
		}

		/* Create a custom radio button */
		.checkmark {
			position: absolute;
			top: 0;
			left: 0;
			height: 18px;
			width: 18px;
			background-color: #eee;
			border-radius: 60%;
		}

		/* On mouse-over, add a grey background color */
		.containerR:hover input~.checkmark {
			background-color: #ccc;
		}

		/* When the radio button is checked, add a blue background */
		.containerR input:checked~.checkmark {
			background-color: #3ab7ff;
		}

		/* Create the indicator (the dot/circle - hidden when not checked) */
		.checkmark:after {
			content: "";
			position: absolute;
			display: none;
		}

		/* Show the indicator (dot/circle) when checked */
		.containerR input:checked~.checkmark:after {
			display: block;
		}

		/* Style the indicator (dot/circle) */
		.container .checkmark:after {
			top: 9px;
			left: 9px;
			width: 8px;
			height: 8px;
			border-radius: 50%;
			background: white;
		}

		#myImg {
			cursor: pointer;
			transition: 0.3s;
			max-width: 95vw;
		}

		/* #myImg:hover {opacity: 0.7;} */

		/* The Modal (background) */
		.modal {
			display: none;
			/* Hidden by default */
			position: fixed;
			/* Stay in place */
			z-index: 1;
			/* Sit on top */
			padding-top: 100px;
			/* Location of the box */
			left: 0;
			top: 0;
			width: 100%;
			/* Full width */
			height: 100%;
			/* Full height */
			overflow: auto;
			/* Enable scroll if needed */
			background-color: rgba(0, 0, 0, 0.9);
			/* Black w/ opacity */
		}

		/* Modal Content (image) */
		.modal-content {
			margin: auto;
			display: none;
			width: 80%;
		}

		/* Caption of Modal Image */
		#caption {
			margin: auto;
			display: block;
			width: 80%;
			max-width: 700px;
			text-align: center;
			color: #ccc;
			padding: 10px 0;
			height: 150px;
			overflow-wrap: break-word;
		}

		/* Add Animation */
		.modal-content,
		#caption {
			-webkit-animation-name: zoom;
			-webkit-animation-duration: 0.6s;
			animation-name: zoom;
			animation-duration: 0.6s;
		}

		@-webkit-keyframes zoom {
			from {
				-webkit-transform: scale(0)
			}

			to {
				-webkit-transform: scale(1)
			}
		}

		@keyframes zoom {
			from {
				transform: scale(0)
			}

			to {
				transform: scale(1)
			}
		}

		/* The Close Button */
		.close {
			position: absolute;
			top: 40px;
			right: 40px;
			color: #f1f1f1;
			font-size: 40px;
			font-weight: bold;
			transition: 0.3s;
		}

		.close:hover,
		.close:focus {
			color: #bbb;
			text-decoration: none;
			cursor: pointer;
		}

		/* 100% Image Width on Smaller Screens */
		@media only screen and (max-width: 700px) {
			.modal-content {
				width: 100%;
			}
		}

		.popup .overlay {
			position: fixed;
			top: 0px;
			left: 0px;
			width: 100vw;
			height: 100vh;
			background: rgba(0, 0, 0, 0.7);
			z-index: 1;
			display: none;
		}

		.popup .content {
			position: fixed;
			top: 50%;
			left: 50%;
			color: #AAA;
			transform: translate(-50%, -50%) scale(0);
			background: #222;
			width: 500px;
			height: 250px;
			z-index: 2;
			text-align: center;
			padding: 20px;
			box-sizing: border-box;
			font-family: "Open Sans", sans-serif;
		}

		.popup .close-btn {
			cursor: pointer;
			position: absolute;
			right: 20px;
			top: 20px;
			width: 30px;
			height: 30px;
			background: #222;
			color: #fff;
			font-size: 25px;
			font-weight: 600;
			line-height: 30px;
			text-align: center;
			border-radius: 50%;
		}

		.popup.active .overlay {
			display: block;
		}

		.popup.active .content {
			transition: all 300ms ease-in-out;
			transform: translate(-50%, -50%) scale(1);
		}

		#button {
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			padding: 15px;
			font-size: 18px;
			border: 2px solid #222;
			color: #222;
			text-transform: uppercase;
			font-weight: 600;
			background: #fff;
		}

		#go2main {
			font-size: 20px;
			font-weight: 600;
			font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
			text-decoration: none;
			color: #06A5EE;
		}

		#footer {
			margin-top: auto;
			width: 90%;
			margin-left: auto;
			margin-right: auto;
			text-align: center;
		}
	""") + """

	</style>
</head>

<body>
	<div id="contents">

		<div align="center">
			<h2 id="page_title"></h2>
		</div>


		<div id='customize_tools' style="margin: 4%;">
			<a id='go2main'>Go to Page list</a>
			<h4 style="color: #dbdee0d5;">Customize Your Page For Your Desired Manga</h4>
			<br>
			<select id="pageFormats">
				<option value="shortS" id='spacer'>Short space</option>
				<option value="noS" id='spacer'>No space</option>
			</select>
			<br><br><br><br>
			<label class="containerR" style="color: #bbb;">Border Enabled
				<input type="radio" name="borderSelection" value="be">
				<span class="checkmark"></span>
			</label>
			<label class="containerR" style="color: #bbb;">Border Disabled
				<input type="radio" name="borderSelection" value="bd" checked="checked">
				<span class="checkmark"></span>
			</label>
		</div>
		<br>
		<center>
			<button id="submit" onclick="displayValue()" style='width: 140px; height: 40px; font-size:16px;'>Apply
				Style</button>
			<hr width="95%"><br>
			<div class="popup" id="popup-1">
				<div class="overlay"></div>
				<div class="content">
					<div class="close-btn" onclick="togglePopup('1', 0)">&times;</div>
					<h1>Psst..</h1>
					<p id='last'></p>
				</div>
			</div>

			<div id="myModal" class="modal" onkeydown="nav_n_zoom(event)">
				<span class="close">&times;</span>
				<img class="modal-content" id="img01">
				<div id="caption"></div>
			</div>
			<div id="images" style="position: relative"></div>
		</center>
	</div>
	<br>
	<br>
</body>

<footer id='footer' style="align-self: center;">
	<pre>

	</pre>
	<div id='pagination' align= 'center'>
		<div id= 'paginate_container'>
			<div id="pagiP"></div>
            <div id="pagiN"></div>
		</div>
	</div>


	<br><br>
	<center>
		<hr width='95%'>
		<hr width='89%'>
	</center>
	<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>
	<br><br>
</footer>


<script type="text/javascript">
""" + rjsmin.jsmin("""
	
	
	const page_style = ['bd', "shortS"];

	const images_loc = %s;
	const pages_list = %s;
	const current_page_index = %i;
	const proj_name= '%s';
document.title = pages_list[current_page_index];

	document.getElementById("page_title").innerHTML = document.title;


	document.getElementById('go2main').href = '../' + proj_name + '.html';

	var style_ = JSON.parse(localStorage.getItem('style?' + proj_name));

	function stylish(style){
		style_temp = style;

		localStorage.setItem('style?' + proj_name, JSON.stringify(style_temp));
		var ele = document.getElementsByTagName('input');
		for (i = 0; i < ele.length; i++) {
			if (ele[i].type = "radio") {
				if (ele[i].value == style_temp[0]) {
					ele[i].checked = true;
				} else {
					ele[i].checked = false;
				}
			}
		}

		document.getElementById("pageFormats").value = style_temp[1];


	}


	function display_imgs() {
		for (i = 0; i < images_loc.length; i++) {
			var imgx = document.createElement("IMG");
			imgx.src = images_loc[i];
			imgx.className = 'per_img';
			imgx.alt = 'It seems image is not found (' + images_loc[i] + ')';
			imgx.style.display = 'block';
			imgx.style.margin = 'auto';
			imgx.id = 'myImg';


			var images_const = document.getElementById("images");
			images_const.appendChild(imgx);
			if (i < (images_loc.length) - 1) {
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
				images_const.appendChild(document.createElement("BR"));
			}
		}
	}

	display_imgs();

	function getValue() {
		var ele = document.getElementsByTagName('input');
		var arr = [];
		for (i = 0; i < ele.length; i++) {
			if (ele[i].type = "radio") {
				if (ele[i].checked)
					arr.push(ele[i].value);
			}
		}
		arr.push(document.getElementById("pageFormats").value);
		return arr;
	}

	function pagination() {
		if (current_page_index != 0) {
			var prev_a = document.createElement("A");
			prev_a.href = "../" + pages_list[current_page_index - 1] + "/" + pages_list[current_page_index - 1] + ".html";
			prev_a.innerHTML = '<< Previous page  ';
			prev_a.className='paginators';
			prev_a.onclick = function () {
				localStorage.setItem(proj_name, current_page_index - 1);
			};
			document.getElementById('pagiP').appendChild(prev_a);

		}
		
		if (current_page_index != pages_list.length - 1) {
			var next_a = document.createElement('A');
			next_a.href = "../" + pages_list[current_page_index + 1] + "/" + pages_list[current_page_index + 1] + ".html";
			next_a.innerHTML = '  Next page >>';
			next_a.className='paginators';
			next_a.onclick = function () {
				localStorage.setItem(proj_name, current_page_index + 1);
			};
			document.getElementById('pagiN').appendChild(next_a);
		}
	}

	pagination();

	function displayValue(values = false) {

		if (values == false) {
			var values = getValue();
		}

		stylish(values);

		var str = "Page Status: " + values[1] + "<br>Border Status: " + values[0];
		var img_div1 = document.getElementById('images');
		var eleIMG = document.getElementsByClassName('per_img');
		var breaks = img_div1.getElementsByTagName("BR");

		if (values[0] == "be") {
			for (i = 0; i < eleIMG.length; i++) {
				eleIMG[i].border = "4px";
			}
		}
		if (values[0] == "bd") {
			for (i = 0; i < eleIMG.length; i++) {
				eleIMG[i].border = "0px";
			}
		}

		if (values[1] == "noS") {
			for (i = breaks.length - 1; i >= 0; i--) {
				breaks[i].style.display = 'none'
			}
		}


		if (values[1] == "shortS") {
			var y = img_div1.childElementCount;
			for (i = breaks.length - 1; i >= 0; i--) {
				breaks[i].style.display = 'initial';
			}
		}
	}

	if (style_ == null) {
		displayValue(page_style);
	} else {
		displayValue(style_);
	}


	//###  modal (floating image script)    #####

	// create references to the modal...
	var modal = document.getElementById('myModal');
	// to all images -- note I'm using a class!
	var images = document.getElementsByClassName('per_img');
	// the image in the modal
	var modalImg = document.getElementById("img01");
	// and the caption in the modal
	var captionText = document.getElementById("caption");
	var js_img_src = [];
	var no_arrow = true;
	modalImg.width = 100;

	var modal_img_indx = -1;
	// Go through all of the images with our custom class
	for (var i = 0; i < images.length; i++) {
		var img = images[i];
		js_img_src.push(img.src);
		// and attach our click listener for this image.
		img.onclick = function () {
			modal.style.display = "initial";
			modalImg.style.display = "initial";

			modalImg.src = this.src;
			modal_img_indx = js_img_src.indexOf(modalImg.src);

			if (no_arrow) {
				const LAdiv = document.createElement("DIV");
				LAdiv.style.display = 'inline-block';
				var LArrow = document.createElement('SPAN');
				LArrow.id = 'LARROW';
				LAdiv.appendChild(LArrow);
				captionText.appendChild(LAdiv);

				var captionText_ = document.createElement("SPAN");
				captionText_.id = 'capt_name';
				captionText.appendChild(captionText_);

				const RAdiv = document.createElement("DIV");
				RAdiv.style.display = 'inline-block';
				var RArrow = document.createElement('SPAN');
				RArrow.id = 'RARROW';
				RAdiv.appendChild(RArrow);
				captionText.appendChild(RAdiv);


				no_arrow = false;
			}


			var LArrow = document.getElementById('LARROW');

			LArrow.style.padding = '7px';
			if (modal_img_indx == 0) {
				LArrow.classList.add('disabled');
			}

			LArrow.innerText = '\\u00A0\\u00A0\\u00A0< Prev\\u00A0\\u00A0\\u00A0';
			LArrow.onclick = function () {
				if (modal_img_indx != 0) {
					modal_img_indx -= 1;
					modalImg.src = js_img_src[modal_img_indx];
					document.getElementsByClassName('close')[0].scrollIntoView();
					if (modal_img_indx + 1 == js_img_src.length) {
						RArrow.classList.add('disabled');
					} else {
						RArrow.classList.remove('disabled');
					}

					if (modal_img_indx == 0) {
						LArrow.classList.add('disabled');
					} else {
						LArrow.classList.remove('disabled');
					}

				}
				document.getElementById('capt_name').innerText =
					"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0" + modalImg.src.replace(
						/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
			}




			document.getElementById('capt_name').innerText =
				"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0" + modalImg.src.replace(/^.*[\\/]/,
					'') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";





			var RArrow = document.getElementById('RARROW');

			RArrow.style.padding = '7px';

			if (modal_img_indx + 1 == js_img_src.length) {
				RArrow.classList.add('disabled');
			}
			RArrow.innerText = '\\u00A0\\u00A0\\u00A0Next >\\u00A0\\u00A0\\u00A0'
			RArrow.onclick = function () {
				if (modal_img_indx + 1 != js_img_src.length) {
					modal_img_indx += 1;
					modalImg.src = js_img_src[modal_img_indx];
					document.getElementsByClassName('close')[0].scrollIntoView();
					if (modal_img_indx + 1 == js_img_src.length) {
						RArrow.classList.add('disabled');
					} else {
						RArrow.classList.remove('disabled');
					}
					if (modal_img_indx == 0) {
						LArrow.classList.add('disabled');
					} else {
						LArrow.classList.remove('disabled');
					}
				}
				document.getElementById('capt_name').innerHTML =
					"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0" + modalImg.src.replace(
						/^.*[\\/]/, '') + "\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
			}


			modal.onkeydown = document.addEventListener('keydown', key_control);
		}
	}

	var span = document.getElementsByClassName('close')[0];

	span.onclick = function () {
		modal.style.display = "none";
		modalImg.removeEventListener('keydown', key_control);
	}

	function key_control(event) {

		var RArrow = document.getElementById('RARROW');
		var LArrow = document.getElementById('LARROW');

		if (event.keyCode == 40) {
			modalImg.style.transition = 'width .6s, height .6s';
			modalImg.style.width = modalImg.width * 0.9 + 'px';
		}

		if (event.keyCode == 38) {
			modalImg.style.transition = 'width .6s, height .6s';
			modalImg.style.width = modalImg.width * 1.1 + 'px';
		}

		if (event.keyCode == 37) {
			if (modal_img_indx != 0) {
				modal_img_indx -= 1;
				modalImg.src = js_img_src[modal_img_indx];
				document.getElementsByClassName('close')[0].scrollIntoView();
			}
			if (modal_img_indx + 1 == js_img_src.length) {
				RArrow.classList.add('disabled');
			} else {
				RArrow.classList.remove('disabled');
			}
			if (modal_img_indx == 0) {
				LArrow.classList.add('disabled');
			} else {
				LArrow.classList.remove('disabled');
			}
			document.getElementById('capt_name').innerText =
				"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0" + modalImg.src.replace(/^.*[\\/]/, '') +
				"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
		}

		if (event.keyCode == 39) {
			if (modal_img_indx + 1 != js_img_src.length) {
				modal_img_indx += 1;
				modalImg.src = js_img_src[modal_img_indx];
				document.getElementsByClassName('close')[0].scrollIntoView();
			}
			if (modal_img_indx + 1 == js_img_src.length) {
				RArrow.classList.add('disabled');
			} else {
				RArrow.classList.remove('disabled');
			}
			if (modal_img_indx == 0) {
				LArrow.classList.add('disabled');
			} else {
				LArrow.classList.remove('disabled');
			}
			document.getElementById('capt_name').innerHTML =
				"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0" + modalImg.src.replace(/^.*[\\/]/, '') +
				"\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0";
		}

		if (event.keyCode == 27) {
			modal.style.display = "none";
			modalImg.removeEventListener('keydown', key_control);
		}
	}


	//################################################

	//############ Pop up ###########################
	var last_opened = localStorage.getItem(proj_name);

	function togglePopup(indx, on_or_off = null) {
		document.getElementById("popup-").classList.toggle("active");
		if (indx === '1' && on_or_off === 0) {
			localStorage.setItem(proj_name, current_page_index);
		}

	}


	if (last_opened === undefined || last_opened === null) {
		localStorage.setItem(proj_name, current_page_index);
		last_opened = current_page_index;
	}

	if (last_opened != current_page_index) {
		if (last_opened != -1) {
			document.getElementById('last').innerHTML = "You left the page on <a id= 'lastleft' href='../" + pages_list[
					localStorage.getItem(proj_name)] + '/' + pages_list[localStorage.getItem(proj_name)] + ".html'>" +
				pages_list[localStorage.getItem(proj_name)] +
				'</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
			togglePopup('1', 1);
		}
	}
	"""%(all_list, sub_dirs, page_index, title)) +"""
</script>


"""

	return sub_page_template

# print(return_sub_page('aaa','sss', 6, 'ttt'))
main_page_template="""
<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">

<head>
	<title></title>
	<script type="text/javascript">
		const pages_list = %s;
		const current_page_index = -1;
		const proj_name= "%s";
		document.title = proj_name;
	</script>

	<style>
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
			top:50%%;
			left:50%%;
			color: #AAA;
			transform:translate(-50%%,-50%%) scale(0);
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
			border-radius:50%%;
		}

		.popup.active .overlay {
			display:block;
		}

		.popup.active .content {
			transition:all 300ms ease-in-out;
			transform:translate(-50%%,-50%%) scale(1);
		}

		button {
			position:absolute;
			top:50%%;
			left:50%%;
			transform:translate(-50%%,-50%%);
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
		margin-left: 5%%;
		margin-right: 5%%;
		width: 85%%;
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
		padding-left: 5%%;
		padding-right: 5%%;
		}

		
		#footer {
		margin-top: auto;
		width: 100%%;
		text-align: center;
		}


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
	<hr style="width: 80%%;">
	<center>
	<div id='allA'></div>
	</center>
	<br><br>

</body>

<footer id='footer'>
	<br><br><center><hr width='95%%'><hr width='89%%'></center>
	<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>
	<br><br>
</footer>


<script type="text/javascript">

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
	}
</script>"""


dir_path = os_dirname(os_realpath(__file__))

# del make_pages
def make_pages(all_li, dir_list, project, seq, ext='', dir_sorted = False):  #func_code= 40001

	first_page = None
	dir_len = len(dir_list)

	if not dir_sorted:
		dir_list = natsort.natsorted(dir_list)
	
	for i in range(dir_len):
		temp = all_li.all_names[i].copy()
		
		if seq:
			box= return_sub_page(str(natsort.natsorted(temp)), str(dir_list), i, project)
		else:
			box= return_sub_page(str(temp), str(dir_list), i, project)
		Fsys.writer(dir_list[i]+'.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i], f_code= '40001')
	Fsys.writer(project+'.html', 'w', main_page_template%(str((dir_list)), project),'Download_projects/'+ project, f_code= '40001')
	print('html done')
	return first_page



