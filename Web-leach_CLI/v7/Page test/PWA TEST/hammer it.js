// source: https://stackoverflow.com/questions/18011099/pinch-to-zoom-using-hammer-js

function hammerIt(elm) {
    hammertime = new Hammer(elm, {touchAction: "none"});
    hammertime.get('pan').set({direction: Hammer.DIRECTION_ALL, threshold: 0 });
//hammertime.get('pan').set({enable: false})
    hammertime.get('pinch').set({
        enable: true
    });
    
    
    var posX = 0,
        posY = 0,
        scale = 1,
        last_scale = 1,
        last_posX = 0,
        last_posY = 0,
        max_pos_x = 0,
        max_pos_y = 0,
        transform = "",
        el = elm,
        width__ = 0,
        height__ = 0,
        
        xtra =0,
        top_gap = 0;
        
      function init(){
        posX = 0,
        posY = 0,
        scale = 1,
        last_scale = 1,
        last_posX = 0,
        last_posY = 0,
        max_pos_x = 0,
        max_pos_y = 0,
        transform = "",
        el = elm,
        width__ = 0,
        height__ = 0,
        
        xtra =0,
        top_gap = 100;
      }
      var display_height = isNaN(window.innerHeight) ? window.clientHeight : window.innerHeight;
        
    

      
    hammertime.on('doubletap pan pinch panend pinchend', function(ev) {
 
      top_gap = 100 // el.parentElement.getBoundingClientRect()["y"] // 10
      try {
        if (window.getComputedStyle(el, null).getPropertyValue('-webkit-transform').toString() == "matrix(1, 0, 0, 1, 0, 0)")
        init()}
      catch (err) {}
      
        if (ev.type == "doubletap") {
            transform =
                "translate3d(0, 0, 0) " +
                "scale3d(2, 2, 1) ";
            scale = 2;
            last_scale = 2;
            try {
                if (window.getComputedStyle(el, null).getPropertyValue('-webkit-transform').toString() != "matrix(1, 0, 0, 1, 0, 0)") {
                    transform =
                        "translate3d(0, 0, 0) " +
                        "scale3d(1, 1, 1) ";
                    scale = 1;
                    last_scale = 1;
                }
            } catch (err) {}
            el.style.webkitTransform = transform;
            transform = "";
        }
        
        width__= el.clientWidth; //get_style_val(el, "width");
        height__= el.clientHeight;
        
        xtra = (height__+ top_gap - display_height)*scale +50;
        // TODO: CONTAINS SOME ALGORITHM ISSUE
        
        
        //pan    
        if (scale != 0) {

          //console.log("X:"+posX+" Y:"+posY+"\nl X:"+last_posX+"l Y:"+last_posY+"\nm X:"+max_pos_x+"m Y:"+max_pos_y);
          //ev.preventDefault()
           //get_style_val(el, "height");
          
          //console.log(height__);
          //console.log(width__);
          // console.log(width__)
            posX = last_posX + ev.deltaX*1.5;
            posY = last_posY + ev.deltaY*2;
            max_pos_x = Math.ceil((scale - 1) * width__ / 2);
            max_pos_y = Math.ceil((scale - 1) * height__ / 2);
            
            
            if(xtra>0){
            max_pos_yD = Math.ceil(((scale - 1) * (display_height-top_gap-50) / 2) +xtra)*(-1);
            // TODO: CONTAINS SOME ALGORITHM ISSUE for loger images on zoom
              
              
            }
            else{
              max_pos_yD = -max_pos_y
            }
            //max_pos_yD = -max_pos_y
           
            //console.log(height__+ " "+top_gap+" "+ display_height+" "+ scale + " "+ " extra" + xtra+ " "+ max_pos_yD)
            if (posX > max_pos_x) {
                posX = max_pos_x;
            }
            if (posX < -max_pos_x) {
                posX = -max_pos_x;
            }
            if (posY > max_pos_y) {
                posY = max_pos_y;
            }
            if (posY < max_pos_yD) {
                posY = max_pos_yD;
            }
        }


        //pinch
        if (ev.type == "pinch") {
            scale = Math.max(1, Math.min(last_scale * (ev.scale), 3));
        }
        if(ev.type == "pinchend"){last_scale = scale;}

        //panend
        if(ev.type == "panend"){
            
            last_posX = posX;
            last_posY = posY;
            if (posX > max_pos_x) {
                last_posX = max_pos_x;
            }
            if (posX < -max_pos_x) {
                last_posX = -max_pos_x;
            }
            if (posY > max_pos_y) {
                last_posY = max_pos_y;
            }
            if (posY < max_pos_yD) {
                last_posY = max_pos_yD;
            }
            
            
            
        }

        if (scale != 0) {
            transform =
                "translate3d(" + posX + "px," + posY + "px, 0) " +
                "scale3d(" + scale + ", " + scale + ", 1)";
        }

        if (transform) {
          
          el.clientHeight
            el.style.transform = transform;
          
        }
    });
}
