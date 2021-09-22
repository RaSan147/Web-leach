var popup_msg_open = false;
var icon_dex = 0;
const icons = ['icon.ico', 'https://cdn.jsdelivr.net/gh/Ratulhasan14789/Web-Leach_pub@main/resources/icon.ico', '?leach_bkp/icon.ico'];


function switch_icon(icon) {
    icon_dex = (icon_dex + 1)%icons.length;
    document.getElementById('icon').href = icons[icon_dex];
}

    
function helped_user(set = 0) {
    if (set != 0) {
        localStorage.setItem('?helped-user', set);
        return;
    }
    var helped = localStorage.getItem('?helped-user');
    if (helped == 'undefined' || helped == null) {
        helped = false;
    } else {
        helped = true;
    }
    return helped;
}


function is_in(item, array) {
    return array.indexOf(item) > -1;
}
var panel2disable = ['S-image-border'];
class Datas {
    constructor() {
        this.page_style = ['bd', "se"];
        this.images_loc = ['a.bmp', 'b.bmp', 'c.bmp'];
        this.pages_list = ['xx', 'aa', 'yy', 'zz', 'zzz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'xx', 'aa', 'yy',
            'zz', 'zzz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'xx', 'aa', 'yy', 'zz', 'zzz', 'aa', 'bb',
            'cc', 'dd', 'ee', 'ff', 'xx', 'aa', 'yy', 'zz', 'zzz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'xx',
            'aa', 'yy', 'zz', 'zzz', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'xx', 'aa', 'yy', 'zz', 'zzz',
            'aa', 'bb', 'cc', 'dd', 'ee', 'ff'
        ];
        this.current_page_index = 0;
        this.current_page_name = this.pages_list[this.current_page_index];
        this.proj_name = 'aaaaaaaaa';

        this.themes = ['Tron'];
        this.current_theme = 0;

        this.is_webkit = navigator.userAgent.indexOf('AppleWebKit') != -1
        this.is_edge = navigator.userAgent.indexOf('Edg') != -1

        this.cssVar = document.querySelector(':root');
    }


    set_data() {
        // sets titles and Headline data and links
        document.title = this.proj_name + ' » ' + this.pages_list[this.current_page_index];
        document.getElementById("proj_name").innerHTML += this.proj_name;
        document.getElementById('page_title').innerHTML+= this.current_page_name;
        document.getElementById('go2main').href = '../' + this.proj_name + '.html';
    }

    get_css(key) {
        var rs = getComputedStyle(this.cssVar);
        return rs.getPropertyValue(key);
    }

    set_css(key, value) {
        this.cssVar.style.setProperty(key, value);
    }
}

let datas = new Datas();
datas.set_data();


class Tools {
    // various tools for the page
    sleep(ms) {
        // sleeps for a given time in milliseconds
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    set_brightness(n = 0) {
        // sets the brightness of the screen
        var val;
        var input_ = document.getElementById('brightness-input');
        var brightness = document.getElementById('brightness');
        if (n == 0) {
            val = sessionStorage.getItem('bright');
            if (val) {
                val = parseInt(val);
                input_.value = val;
            } else {
                n = 1;
            }
        }
        if (n == 1) {
            val = input_.value;
            //   int to string
            sessionStorage.setItem('bright', val);
        }

        brightness.style.opacity = 0.7 - (val * 0.07);
    }

}

let tools = new Tools();

tools.set_brightness();

class Accordion_ {
    constructor() {
        this.acc = document.getElementsByClassName("accordion");

        var that = this;
        for (let i = 0; i < this.acc.length; i++) {
            this.acc[i].addEventListener("click", function () {
                this.classList.toggle("accordion-active");
                var panel = this.nextElementSibling;
                if (panel.classList.contains("accordion-panel")) {
                    if (panel.style.display === "block") {
                        panel.style.display = "none";
                    } else {
                        panel.style.display = "block";
                        slider_control.slider_fix_tick();
                    }
                }
            });
        }

        document.getElementById("add_theme_name").innerHTML += '[' + datas.themes[datas.current_theme] + ']';
    }
}

let accordion = new Accordion_();

class SwitchBtn_ {
    constructor() {
        var that = this;
        this.switch_btn = document.getElementsByClassName("tron-switch");

        for (let i = 0; i < this.switch_btn.length; i++) {
            this.switch_btn[i].onclick = function () {
                that.set_switch_mode(this.id, that.switch_mode(this.id), true);
            };
        }
    }

    switch_mode(id) {
        let btn = document.getElementById(id + '-mode');
        if (btn.innerText == "ON") {
            return true;
        } else return false;
    }

    set_switch_mode(id, mode, not = false) {
        let btn = document.getElementById(id + '-mode');
        let parent = document.getElementById(id);

        function toggle_panel(disable) {
            let Guncle = parent.parentElement.nextElementSibling;
            if (is_in(id, panel2disable)) {
                if (disable == true) {
                    Guncle.classList.add('disabled')
                    Guncle.disabled = true;
                } else {
                    Guncle.classList.remove('disabled')
                    Guncle.disabled = false;
                }
            }
        }
        if (not) {
            if (mode == "ON" || mode === true) {
                btn.innerText = "OFF";
                parent.classList.remove("active"); {
                    toggle_panel(true);
                }
            } else {
                btn.innerText = "ON";
                parent.classList.add("active");
                toggle_panel(false);

            }
        } else {
            if (mode == "ON" || mode === true) {
                btn.innerText = "ON";
                parent.classList.add("active");
                toggle_panel(false);
            } else {
                btn.innerText = "OFF";
                parent.classList.remove("active");
                toggle_panel(true);
            }
        }
    }
}

let switchBtn = new SwitchBtn_();

class Pagination {

    pagination() {
        var prev_direction = document.getElementById("pagination-prev");
        var next_direction = document.getElementById("pagination-next");

        if (datas.current_page_index != 0) {
            prev_direction.href = "../" + datas.pages_list[datas.current_page_index - 1] + "/" + datas
                .pages_list[
                    datas.current_page_index - 1] + ".html";
            prev_direction.onclick = function () {
                localStorage.setItem(datas.proj_name, datas.current_page_index - 1);
            };
        } else {
            prev_direction.classList.add("hidden");
        }

        if (datas.current_page_index != datas.pages_list.length - 1) {
            next_direction.href = "../" + datas.pages_list[datas.current_page_index + 1] + "/" + datas
                .pages_list[
                    datas.current_page_index + 1] + ".html";
            next_direction.onclick = function () {
                localStorage.setItem(datas.proj_name, datas.current_page_index + 1);
            };
        } else {
            next_direction.classList.add("hidden");
        }
    }
}

let pagination = new Pagination();
pagination.pagination();


class PageStyler {
    constructor() {
        // assigns required elements for theme changing in attributes
        this.border_enabled = false;
        this.border_color = '#bbb';
        this.border_width = '1';

        this.space_enabled = true;
        this.space_height = '3em';



        this.img_div1 = document.getElementById('images');
        this.eleIMG = document.getElementsByClassName('per_img');
        this.breaks = document.getElementsByClassName('Break_in_image');

        // image border switch
        this.S_image_border = document.getElementById('S-image-border');
        this.S_image_space = document.getElementById('S-image-space');



    }

    set_default_style() {
        var style = ["bd", "se", 1, 1];
        //0: border disabled "bd"
        //1: spaceing enabled "se"
        //2: border color 1> black 2> white 3> theme #......> custom
        //3: border width

        this.set_menu_style(style);
        this.set_local_style(style);
        this.display_changes(style);
    }

    get_local_style() {
        return JSON.parse(localStorage.getItem('style?' + datas.proj_name));
    }

    set_local_style(style) {
        localStorage.setItem('style?' + datas.proj_name, JSON.stringify(style));
    }

    get_menu_style() {
        var arr = [];

        if (this.S_image_border.classList.contains("active") == true) {
            arr.push("be");
        } else {
            arr.push("bd");
        }

        if (this.S_image_space.classList.contains("active") == true) {
            arr.push("se");
        } else {
            arr.push("sd");
        }

        var border_color_radios = document.getElementsByName("border-color");
        var border_color = 0;
        for (var i = 0; i < border_color_radios.length; i++) {
            if (border_color_radios[i].checked) {
                border_color = border_color_radios[i].value;
            }
        }
        arr.push(border_color);
        arr.push(document.getElementsByName("border-width")[0].value);
        return arr;
    }

    set_menu_style(style) {
        var style_temp = style;

        this.set_local_style(style);

        if (style_temp[0] == "be") {
            switchBtn.set_switch_mode("S-image-border", "ON");
        } else {
            switchBtn.set_switch_mode("S-image-border", "OFF");
        }



        if (style_temp[1] == "se") {
            switchBtn.set_switch_mode("S-image-border", "ON");
        } else {
            switchBtn.set_switch_mode("S-image-border", "OFF");
        }


        var border_color_radios = document.getElementsByName("border-color");
        for (var i = 0; i < border_color_radios.length; i++) {
            if (border_color_radios[i].value == style_temp[2]) {
                border_color_radios[i].checked = true;
            }
        }
        document.getElementsByName("border-width")[0].value = style_temp[3];

        if (style_temp[1] == "sd") {
            switchBtn.set_switch_mode("S-image-space", "OFF");
        } else {
            switchBtn.set_switch_mode("S-image-space", "ON");
        }
    }

    display_changes(values) {
        var border_color = "#000"
        if (values[0] == "be") {
            if (values[2] == "2") {
                border_color = "#fff";
            } else if (values[2] == "3")
                border_color = "var(--theme-color)";
            // convert string to int
            var border_width = parseInt(values[3]);
            datas.set_css("--border-width", (1 + border_width) * 1.5 + "px");
            datas.set_css("--border-color", border_color);
        }
        if (values[0] == "bd") {
            datas.set_css("--border-width", "0");
            datas.set_css("--border-color", "transparent");
        }

        if (values[1] == "sd") {
            datas.set_css("--space-height", "0");
        }


        if (values[1] == "se") {
            datas.set_css("--space-height", "3em");
        }
    }


    load_style_on_start() {
        const style_ = this.get_local_style();

        if (style_ == null) {
            this.set_default_style();
        } else {
            this.set_menu_style(style_);
            this.display_changes(style_);
        }
    }

    change_style() {
        var style = this.get_menu_style();
        this.set_local_style(style);
        this.display_changes(style);
    }

}

let page_styler = new PageStyler();
document.getElementById("mySidebarR").onclick = function () {
    page_styler.change_style()
}

class Image_loader {
    load_image(dirs) {
        const break_in_image = document.createElement('div')
        break_in_image.className = 'Break_in_image'

        var images_const = document.getElementById("images");

        for (var i = 0; i < datas.images_loc.length; i++) {
            var imgx = document.createElement("IMG");
            imgx.src = datas.images_loc[i];
            imgx.className = 'per_img';
            imgx.alt = 'It seems image is not found (' + datas.images_loc[i] + ')';
            imgx.style.display = 'block';
            imgx.style.margin = 'auto';


            images_const.appendChild(imgx);
            if (i < (datas.images_loc.length - 1)) {
                images_const.appendChild(break_in_image.cloneNode(true));
            }
        }
    }
}

let image_loader = new Image_loader();
image_loader.load_image();

page_styler.load_style_on_start();

class Modal_img {
    //###  modal (floating image script)    #####

    constructor() {
        // create references to the modal...
        this.modal = document.getElementById('myModal');
        // to all images -- note I'm using a class!
        this.images = document.getElementsByClassName('per_img');
        // the image in the modal
        this.modalImg = document.getElementById("img01");
        this.modalContent = document.getElementById("image-modal-content");
        // and the caption in the modal
        this.captionText = document.getElementById("caption");
        this.js_img_src = [];


        this.modal_img_indx = -1;
        // Go through all of the images with our custom class

        this.LArrow = document.getElementById('prev_view');
        this.RArrow = document.getElementById('next_view');

    }


    assign_modals_in_img() {
        var that = this;
        for (var i = 0; i < this.images.length; i++) {
            var img = that.images[i];
            that.js_img_src.push(img.src);
            // and attach our click listener for this image.
            img.onclick = function () {
                // get window size and set modal sizeodal when the image was clicked
                if (window.innerWidth < 700) {
                    that.modalImg.style.width = '100vw';
                } else {
                    that.modalImg.style.width = '80vw';
                }

                that.modal.style.display = "initial";
                that.modalImg.style.display = "initial";

                that.modalImg.src = this.src;
                that.modal_img_indx = that.js_img_src.indexOf(this.src);


                that.captionText.innerHTML = datas.images_loc[that.modal_img_indx].split('/').pop().split(
                    '.')[
                    0];

                // disable scroll on body
                document.body.classList.add('overflowHidden');

                if (that.modal_img_indx == 0) {
                    that.LArrow.style.display = 'none';
                } else {
                    that.LArrow.style.display = 'block';
                }

                if (that.modal_img_indx + 1 == that.js_img_src.length) {
                    that.RArrow.style.display = 'none';
                } else {
                    that.RArrow.style.display = 'block';
                }
                that.modal.onkeydown = document.addEventListener('keydown', that.key_control);

            }
        }

        this.create_close_button();
    }


    set_modal_state(is_negative_move) {
        if (is_negative_move) {
            this.modalImg.setAttribute('data-state', 1);
        } else {
            this.modalImg.setAttribute('data-state', 2);
        }
    }

    async change_image(move) {
        const is_negative_move = move < 0;
        const after_move = this.modal_img_indx + move;
        if (after_move >= this.images.length || after_move < 0) {
            return 0;
        }

        this.modal_img_indx += move;


        this.set_modal_state(is_negative_move);


        await tools.sleep(250);
        this.modalImg.style.display = "none";

        this.modalImg.setAttribute('data-state', 0);

        this.modalImg.src = this.js_img_src[this.modal_img_indx];
        this.captionText.innerHTML = datas.images_loc[this.modal_img_indx].split('/').pop().split('.')[0];

        document.getElementsByClassName('close-image-modal')[0].scrollIntoView();

        if (this.modal_img_indx + 1 == this.js_img_src.length) {
            this.RArrow.style.display = 'none';
        } else {
            this.RArrow.style.display = 'block';
        }
        if (this.modal_img_indx == 0) {
            this.LArrow.style.display = 'none';
        } else {
            this.LArrow.style.display = 'block';
        }

        this.modalImg.style.display = 'block';
    }



    create_close_button() {
        var that = this;
        var span = document.getElementsByClassName('close-image-modal')[0];

        span.onclick = function () {
            that.modal.style.display = "none";
            document.removeEventListener('keydown', that.key_control);
            document.body.classList.remove('overflowHidden');
        }
    }

    key_control(event) {
        var that = modal_img;

        if (event.keyCode == 40) {
            that.modalImg.style.width = that.modalImg.width * 0.9 + 'px';

        }

        if (event.keyCode == 38) {
            that.modalImg.style.width = that.modalImg.width * 1.1 + 'px';
        }

        if (event.keyCode == 37) {
            that.change_image(-1);
        }
        if (event.keyCode == 39) {
            that.change_image(1);
        }

        if (event.keyCode == 27) {
            that.modal.style.display = "none";
            document.removeEventListener('keydown', that.key_control);
            document.body.classList.remove('overflowHidden');
        }
    }

}

let modal_img = new Modal_img();
modal_img.assign_modals_in_img();

class Popup_Msg {

    togglePopup(indx, on_or_off = null) {
        document.getElementById("popup-" + indx).classList.toggle("active");
    }

}

let popup_msg = new Popup_Msg();

class Local_Data_Manager {
    constructor() {
        this.last_opened = localStorage.getItem(datas.proj_name);
    }

    show_last_opened() {
        if (this.last_opened != 'undefined' || this.last_opened != null) {
            localStorage.setItem(datas.proj_name, datas.current_page_index);
            this.last_opened = datas.current_page_index;
            return;
        }

        if (this.last_opened == datas.current_page_index) {
            if (this.last_opened != -1) {
                document.getElementById('last').innerHTML =
                    "You left the page on <a id= 'lastleft' href='../" +
                    datas.pages_list[
                        localStorage.getItem(datas.proj_name)] + '/' + datas.pages_list[localStorage.getItem(
                        datas
                        .proj_name)] + ".html'>" +
                    datas.pages_list[localStorage.getItem(datas.proj_name)] +
                    '</a><br> Click on the link to go there<hr>Close this dialog to continue from here';
                popup_msg.togglePopup('1', 1);
            }
        }
    }
}

let local_data_manager = new Local_Data_Manager();
local_data_manager.show_last_opened();




var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("TopBar").style.top = "0";
        document.body.style.top = "50px";
    } else {
        document.getElementById("TopBar").style.top = "-50px";
        document.body.style.top = "0";
    }
    prevScrollpos = currentScrollPos;
}

function fuck(x = '') {
    alert("fuck" + x);
}

class Sidebar_control {
    constructor() {
        this.left_bar = document.getElementById('mySidebarL')
        this.right_bar = document.getElementById('mySidebarR')
        this.app_name = document.getElementById('app_name')
    }

    is_open(side) {
        return 'mySidebar-active' in document.getElementById("mySidebar" + side).classList
    }

    toggle_left() {
        if (this.is_open('L')) {
            this.closeNavL();
        } else {
            this.closeNavR();
            if (document.body.clientWidth < 340) {
                this.left_bar.classList.toggle('mySidebar-active-full');
                document.body.classList.add('overflowHidden');
            } else if (document.body.clientWidth < 450) {
                // document.getElementById('app_name').innerText = ' WL '
                this.left_bar.classList.toggle('mySidebar-active-mid');
            } else {
                this.left_bar.classList.toggle('mySidebar-active');
                document.getElementById("app_header").classList.toggle('top-titleR-active');
            }
        }
    }

    toggle_right() {
        // document.getElementById("page_title").classList.add('x')
        if (this.is_open('R')) {
            this.closeNavR();
        } else {
            this.closeNavL();
            if (document.body.clientWidth < 340) {
                this.right_bar.classList.toggle('mySidebar-active-full');
                document.body.classList.add('overflowHidden');
            } else if (document.body.clientWidth < 450) {
                // document.getElementById('app_name').innerText = ' WL '
                this.right_bar.classList.toggle('mySidebar-active-mid');
            } else {
                this.right_bar.classList.toggle('mySidebar-active');
                document.getElementById("app_header").classList.toggle('top-titleR-active');
            }
        }
    }

    closeNavL() {
        this.left_bar.classList.remove('mySidebar-active', 'mySidebar-active-full', 'mySidebar-active-mid');
        document.body.classList.remove('overflowHidden');
        document.getElementById("app_header").classList.remove('top-titleL-active');
        tools.sleep(3000);
    }

    closeNavR() {
        this.right_bar.classList.remove('mySidebar-active', 'mySidebar-active-full', 'mySidebar-active-mid');
        // document.getElementById("app_header").classList.remove('top-titleR-active');
        document.body.classList.remove('overflowHidden');
        tools.sleep(3000);
    }
}

let sidebar_control = new Sidebar_control();


class Slider_control_ {
    constructor() {
        var self = this;
        self.slider = document.getElementsByClassName('ranger');
        for (let i = 0; i < self.slider.length; i++) {
            self.slider[i].style.setProperty('--value', self.slider[i].value * 10);
            self.slider[i].addEventListener('input', function () {
                // alert(this.value);
                this.style.setProperty('--value', this.value * 10);
            });
        }
        self.slider_ticks = document.getElementsByClassName('slider-tick');
    }
    border_slider_width(i) {
        return this.slider[i].clientWidth;
    }

    slider_fix_tick(e = '') {
        for (let i = 0; i < this.slider_ticks.length; i++) {
            // alert(this.border_slider_width(i));
            this.slider_ticks[i].parentElement.style.setProperty('--tick-spacing', (this.border_slider_width(
                i) - 42) / 10 + 'px');
        }
    }
}

let slider_control = new Slider_control_();
slider_control.slider_fix_tick();
window.addEventListener('resize', slider_control.slider_fix_tick.bind(slider_control));



class Project_Panel_ {
    constructor() {
        this.rside_project = document.getElementById('proj-panel-body');
        this.input_ = document.getElementById('proj_search_input');
        this.button_ = document.getElementById('proj_search_icn')
    }

    show_search_results() {
        var self = this;
        var to_search = this.input_.value.toLowerCase();
        this.rside_project.innerHTML = '';
        if (to_search.length > 0) {
            this.input_.setAttribute('data-state', '1')
            this.button_.innerHTML = "&#x2716;";
            this.button_.onclick = function () {
                self.input_.value = '';
                self.input_.setAttribute('data-state', '0');
                this.innerHTML = "&#x1F50E;&#xFE0E;";
                return false;
            }
        } else {
            this.input_.setAttribute('data-state', '0')
            this.button_.innerHTML = "&#x1F50E;&#xFE0E;";
        }
        for (let i = 0; i < datas.pages_list.length; i++) {
            if (datas.pages_list[i].toLowerCase().indexOf(to_search) !== -1) {
                var loc = document.createElement('div')
                loc.classList.add('proj-panel-item');
                if (i == datas.current_page_index) {
                    loc.classList.add('proj-panel-item-active');
                } else {
                    loc.onclick = function () {
                        const link = "../" + datas.pages_list[i] + "/" + datas.pages_list[i] + ".html";
                        window.location.href = link;
                    }
                }
                loc.innerHTML = datas.pages_list[i];
                this.rside_project.appendChild(loc);
            }
        }
    }
}

let project_panel = new Project_Panel_();
project_panel.show_search_results();

project_panel.input_.addEventListener('input', project_panel.show_search_results.bind(project_panel));


function show_credits() {
    if (sidebar_control.is_open('R')) {
        sidebar_control.toggle_right();
    }
    if (popup_msg_open) {
        popup_msg.togglePopup('2', 0);
        document.body.classList.remove('overflowHidden');
        popup_msg_open = false;
    } else {
        document.getElementById("Popup-header").innerHTML = "Credits";
        document.getElementById("Popup-content").innerHTML =
            "<h3>Created by Ratul Hasan</h3><h2>Special Thanks to:<hr width='80%'></h2><h3>Inul Haque</h3><h3>Sanjida Sirat</h3>";
        popup_msg.togglePopup('2', 1);
        document.body.classList.add('overflowHidden');


        document.getElementById("popup-2").getElementsByClassName('close-btn')[0].onclick = show_credits;

        popup_msg_open = true;
    }
}

function show_about() {
    if (sidebar_control.is_open('R')) {
        sidebar_control.toggle_right();
    }
    if (popup_msg_open) {
        popup_msg.togglePopup('2', 0);
        document.body.classList.remove('overflowHidden');
        popup_msg_open = false;
    } else {
        document.getElementById("Popup-header").innerHTML = "About";
        document.getElementById("Popup-content").innerHTML = "<b>App version:</b> " + datas.app_version +
            "<br><b>Page Version:</b> " + datas.page_version;
        popup_msg.togglePopup('2', 1);
        document.body.classList.add('overflowHidden');


        document.getElementById("popup-2").getElementsByClassName('close-btn')[0].onclick = show_credits;

        popup_msg_open = true;
    }
}

function show_help() {
    if (sidebar_control.is_open('R')) {
        sidebar_control.toggle_right();
    }
    if (popup_msg_open) {
        popup_msg.togglePopup('2', 0);
        document.body.classList.remove('overflowHidden');
        popup_msg_open = false;
        helped_user(1);

    } else {
        document.getElementById("Popup-header").innerHTML = "Help";
        let help = `1. Open focus mode by clicking on image <br>
        2. Use <b>Sidebar</b> to quick access other pages <br>
        3. From settings you can change or customize theme style <br>
        4. You can also change brightness level of the page <br>
        5. On focus mode you can use keyboard to resize and move to next or previous image <br>
        <hr>
        <b>Note:</b> Theme style is reused all over the Project <br>
        *EXCEPT Brightness level, it only stays until the session ends`;
        document.getElementById("Popup-content").innerHTML = help;
        popup_msg.togglePopup('2', 1);
        document.body.classList.add('overflowHidden');


        document.getElementById("popup-2").getElementsByClassName('close-btn')[0].onclick = show_help;

        popup_msg_open = true;
    }
}

if(helped_user()==false){
    show_help()
}