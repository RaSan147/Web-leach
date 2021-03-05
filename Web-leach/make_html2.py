# from leach5_31_class import *

sub_page_template="""<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">

<head>
  <title></title>
  <script type="text/javascript">
  var images_loc = %s;
  var pages_list = %s;
  var current_page_index = %i;
  var proj_name= '%s';
  document.title = pages_list[current_page_index];
  </script>
  <style type="text/css">
    .container {
      margin: 80px auto;
      width: 400px;
      text-align: center;
    }

    .paginationA {
      font: bold 20px Arial;
      text-decoration: none;
      background-color: #8a8b8d6b;
      color: #00b7ff;
      padding: 2px 6px 2px 6px;
      border-top: 1px solid #828d94;
      box-shadow: 4px 4px #5050506b;
      border-left: 1px solid rgb(130, 141, 148)
    }

#lastleft{
  font: bold Arial;
  text-decoration: none;
  color: #00b7ff;
}

    body {
      font-family: Arial, Helvetica, sans-serif;
      position: relative;
      min-height: 100vh;
      background-color: #222;

    }
    #pageFormats{
      background-color: rgba(117, 117, 119, 0.507);
      height: 35px;
      width: 140px;
      color:  #3ab7ff;
      font-size: 17px;
      font-family: sans-serif;
      font-weight: 700;
    }

    
    #spacer{
      background-color: #222;
      color:rgb(57, 148, 190);
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

/* Create a custom radio button */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 18px;
  width: 18px;
  background-color: #eee;
  border-radius: 60%%;
}

/* On mouse-over, add a grey background color */
.containerR:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the radio button is checked, add a blue background */
.containerR input:checked ~ .checkmark {
  background-color: #3ab7ff;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the indicator (dot/circle) when checked */
.containerR input:checked ~ .checkmark:after {
  display: block;
}

/* Style the indicator (dot/circle) */
.container .checkmark:after {
 	top: 9px;
	left: 9px;
	width: 8px;
	height: 8px;
	border-radius: 50%%;
	background: white;
}

    #myImg {
      cursor: pointer;
      transition: 0.3s;
      max-width: 100%%;
      max-height: 100vh;
    }

    /* #myImg:hover {opacity: 0.7;} */

    /* The Modal (background) */
    .modal {
      display: none; /* Hidden by default */
      position: fixed; /* Stay in place */
      z-index: 1; /* Sit on top */
      padding-top: 100px; /* Location of the box */
      left: 0;
      top: 0;
      width: 100%%; /* Full width */
      height: 100%%; /* Full height */
      overflow: auto; /* Enable scroll if needed */
      background-color: rgb(0,0,0); /* Fallback color */
      background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
    }

    /* Modal Content (image) */
    .modal-content {
      margin: auto;
      display: none;
      width: 80%%;
    }

    /* Caption of Modal Image */
    #caption {
      margin: auto;
      display: block;
      width: 80%%;
      max-width: 700px;
      text-align: center;
      color: #ccc;
      padding: 10px 0;
      height: 150px;
    }

    /* Add Animation */
    .modal-content, #caption {  
      -webkit-animation-name: zoom;
      -webkit-animation-duration: 0.6s;
      animation-name: zoom;
      animation-duration: 0.6s;
    }

    @-webkit-keyframes zoom {
      from {-webkit-transform:scale(0)} 
      to {-webkit-transform:scale(1)}
    }

    @keyframes zoom {
      from {transform:scale(0)} 
      to {transform:scale(1)}
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

    /* 100%% Image Width on Smaller Screens */
    @media only screen and (max-width: 700px){
      .modal-content {
        width: 100%%;
      }
    }

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
  transform:translate(-50%%,-50%%) scale(0);
  background:#fff;
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

#button {
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

#go2main{
  font-size: 20px;
  font-weight: 600;
  font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
  text-decoration: none;
  color: rgb(6, 165, 238);
}

#footer {
  position: absolute;
  bottom: 0;
  width: 100%%;
  height: 2.5rem;            /* Footer height */
}
  </style>
  </head>
  
  <body>
  <div id="contents">
  <div id='customize_tools' style="margin: 4%%;">
  <a id='go2main'>Go to Page list</a>
  <h4 style="color: #dbdee0d5;">Customize Your Page For Your Desired Manga</h4>
  <br>
  <select id="pageFormats">
  <option value="noS" id='spacer'>No space</option>
  <option value="shortS" id ='spacer'>Short space</option>
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
    <button id="submit" onclick="displayValue()">Submit</button> <hr><br>
    <div class="popup" id="popup-1">
      <div class="overlay"></div>
      <div class="content">
        <div class="close-btn" onclick="togglePopup(0)">&times;</div>
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
</body>
<footer id ='footer' style= "align-self: center;">
  <pre>



  <pre>
   <p id="pagination" style="text-align: center;" ></p>
  <pre>




  <pre>
</footer>
<script type="text/javascript">

  document.getElementById('go2main').href= '../'+proj_name+'.html';

  function display_imgs() {
    for (i = 0; i < images_loc.length; i++) {
      var imgx = document.createElement("IMG");
      imgx.src = images_loc[i];
      imgx.className = 'per_img';
      imgx.alt = 'It seems image is not found ('+images_loc[i]+')';
      imgx.style.display= 'block';
      imgx.style.margin= 'auto';
      imgx.id = 'myImg';

      
      var images_const = document.getElementById("images");
      images_const.appendChild(imgx);
      if (i < (images_loc.length)-1) {
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

  function pagination () {
    var page_direction=document.getElementById("pagination");
    
    if (current_page_index != 0) {
      var prev_a= document.createElement("A");
      prev_a.href= "../"+pages_list[current_page_index-1]+"/"+pages_list[current_page_index-1]+".html";
      prev_a.innerHTML= '<< Previous page  ';
      prev_a.className='paginationA';
      prev_a.onclick= function(){
        localStorage.setItem(proj_name, current_page_index-1);
      };
      page_direction.appendChild(prev_a);
      
    }
    
    page_direction.innerHTML+='&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'

    if (current_page_index != pages_list.length-1){
      var next_a= document.createElement('A');
      next_a.href= "../"+pages_list[current_page_index+1]+"/"+pages_list[current_page_index+1]+".html";
      next_a.innerHTML= '  Next page >>';
      next_a.className='paginationA';
      next_a.onclick= function(){
        localStorage.setItem(proj_name, current_page_index+1);
      };
      page_direction.appendChild(next_a);
    } 

    
  }
  
  pagination();
  function displayValue() {
    
    var values = getValue();
    var str = "Page Status: "+values[1]+"<br>Border Status: "+ values[0];
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
      for (i = breaks.length-1; i >= 0; i--) {
        breaks[i].style.display = 'none'
      }
    }
    
    
    if (values[1] == "shortS") {
      var y = img_div1.childElementCount;
      for (i = breaks.length-1; i >= 0; i--) {
        breaks[i].style.display = 'initial';
      }
    }
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
  modalImg.width =100;
  // Go through all of the images with our custom class
  for (var i = 0; i < images.length; i++) {
    var img = images[i];
    js_img_src.push(img.src);
    // and attach our click listener for this image.
    img.onclick = function(evt) {
      modal.style.display = "initial";
      modalImg.style.display = "initial";
      
      modal.onkeydown =document.addEventListener('keydown',function(event) {
        if(event.keyCode==40){modalImg.style.transition='width .6s, height .6s'; modalImg.style.width = modalImg.width*0.9+'px';}
        if(event.keyCode==38){modalImg.style.transition='width .6s, height .6s'; modalImg.style.width = modalImg.width*1.1+'px';}
        if(event.keyCode==37){
          var pos =js_img_src.indexOf(modalImg.src)-1;
          if (pos != -1){
          modalImg.src = js_img_src[pos];}}
        if(event.keyCode==39){
          var pos =js_img_src.indexOf(modalImg.src)+1;
          if (pos != js_img_src.length){
          modalImg.src = js_img_src[pos];}}
        captionText.innerHTML = modalImg.src.replace(/^.*[\\\/]/, '');
  });
      modalImg.src = this.src;
      captionText.innerHTML = this.src.replace(/^.*[\\\/]/, '');
    }
  }

  var span = document.getElementsByClassName("close")[0];

  span.onclick = function() {
    modal.style.display = "none";
  }
  //################################################

  //############ Pop up ###########################
  var last_opened = localStorage.getItem(proj_name);
  function togglePopup(on_or_off){
    document.getElementById("popup-1").classList.toggle("active");
    if(on_or_off==0){
      localStorage.setItem(proj_name, current_page_index);
    }

  }
  

    if(last_opened === undefined || last_opened === null) {
   localStorage.setItem(proj_name, current_page_index);
   last_opened = current_page_index;
}

  if(last_opened!=current_page_index){
        if(last_opened!=-1){
        document.getElementById('last').innerHTML= "You left the page on <a id= 'lastleft' href='../"+ pages_list[localStorage.getItem(proj_name)]+ '/'+pages_list[localStorage.getItem(proj_name)]+".html'>"+ pages_list[localStorage.getItem(proj_name)]+ '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
      togglePopup(1);}
    }





</script>
"""

main_page_template="""
<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">

<head>
  <title></title>
  <script type="text/javascript">
  var pages_list = %s;
  var current_page_index = -1;
  var proj_name= "%s";
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
  transform:translate(-50%%,-50%%) scale(0);
  background:#fff;
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
  
  position: relative;
  min-height: 100vh;
}
html, body, input, textarea, select, button {
    border-color: #736b5e;
    color: #e8e6e3;
    background-color: rgb(19, 21, 22);
}
* {
    scrollbar-color: #0f0f0f #454a4d;
}
#allA{
  text-align: center;
  margin-left: 12%%;
  margin-right: 12%%;
}

#proj_title{
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.list_class{
  font-size: 20px;
  font-weight: 600;
  font-family: 'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif';
  text-decoration: none;
  color: rgb(6, 165, 238);
}

#footer {
  position: absolute;
  bottom: 0;
  width: 100%%;
  height: 2.5rem;            /* Footer height */
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
  <div id='allA'></div>
</body>

<footer id='footer'><br><br><br><br><hr><hr>
<p style="color: darkgray;">Made by Ratul Hasan with Web leach</p>
<br><br>
</footer>

<script type="text/javascript">

document.getElementById('proj_title').innerText=proj_name;

var all_li= document.getElementById('allA');
all_li.style.alignContent ='center';
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
    document.getElementById('last').innerHTML= "You left the page on <a href='"+ pages_list[localStorage.getItem(proj_name)]+ '/'+pages_list[localStorage.getItem(proj_name)]+".html'>"+ pages_list[localStorage.getItem(proj_name)]+ '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
    togglePopup(1);
  }}

  else{
      localStorage.setItem(proj_name, current_page_index);
    }
</script>"""


dir_path = os_dirname(os_realpath(__file__))

def make_pages(all_li, dir_list, project, seq):
	first_page=None
	dir_len = len(dir_list)

	# print(all_li)
	for i in range(dir_len):
		temp=[]
		for j in range(len(all_li)):
			if all_li[j][1] == i:
				temp.append(html_escape(html_unescape(get_file_name(all_li[j][0])).replace('/','-').replace('\\','-').replace('|','-').replace(':','-').replace('*','-').replace('"',"'").replace('>','-').replace('<','-').replace('?','-')))

		temp=remove_duplicate(temp)

		if i==0:
			first_page = dir_path+'/Download_projects/'+ project+'/'+project+'.html'
		if seq:
			box= sub_page_template%(str(natsort.natsorted(temp)), str((dir_list)), i, project)
		else:
			box= sub_page_template%(str(temp), str((dir_list)), i, project)
		
		writer(dir_list[i]+'.html', 'w', box,'Download_projects/'+ project+'/'+dir_list[i])
	writer(project+'.html', 'w', main_page_template%(str((dir_list)), project),'Download_projects/'+ project)
	return first_page
