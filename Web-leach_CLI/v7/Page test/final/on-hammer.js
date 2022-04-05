function disable_on_hammer(){
  let styleEl = document.getElementById("to_disable_on_hammer")
  // toggle enabled/disabled
  styleEl.setAttribute('media', "not all")
}

function enable_on_hammer(){
  let styleEl = document.getElementById("to_disable_on_hammer")
  
  styleEl.removeAttribute('media')
}


class hammer_load{
  constructor(id){
    this.MIN_SCALE = 1; // 1=scaling when first loaded
    this.MAX_SCALE = 64;
  }
       
      // HammerJS fires "pinch" and "pan" events that are cumulative in nature and not
      // deltas. Therefore, we need to store the "last" values of scale, x and y so that we can
      // adjust the UI accordingly. It isn't until the "pinchend" and "panend" events are received
      // that we can set the "last" values.

      // Our "raw" coordinates are not scaled. This allows us to only have to modify our stored
      // coordinates when the UI is updated. It also simplifies our calculations as these
      // coordinates are without respect to the current scale.

      this.imgWidth = null;
      this.imgHeight = null;
      this.viewportWidth = null;
      this.viewportHeight = null;
      this.scale = null;
      this.lastScale = null;
      this.container = null;
      this.img = null;
      this.x = 0;
      this.lastX = 0;
      this.y = 0;
      this.lastY = 0;
      this.pinchCenter = null;
      this.curWidth = null;
      this.curheight = null;

      // We need to disable the following event handlers so that the browser doesn't try to
      // automatically handle our image drag gestures.
   disableImgEventHandlers () {
     const events = ['onclick', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover',
                      'onmouseup', 'ondblclick', 'onfocus', 'onblur'];

        events.forEach(function (event) {
          img[event] = function () {
            return false;
          };
        });
      };

      // Traverse the DOM to calculate the absolute position of an element
    absolutePosition(el) {
        var x = 0,
          y = 0;

        while (el !== null) {
          x += el.offsetLeft;
          y += el.offsetTop;
          el = el.offsetParent;
        }

        return { x: x, y: y };
      };

    restrictScale(scale) {
        if (scale < this.MIN_SCALE) {
          scale = this.MIN_SCALE;
        } else if (scale > this.MAX_SCALE) {
          scale = this.MAX_SCALE;
        }
        return scale;
      };

    restrictRawPos(pos, viewportDim, imgDim) {
        if (pos < viewportDim/this.scale - imgDim) { // too far left/up?
          pos = viewportDim/this.scale - imgDim;
        } else if (pos > 0) { // too far right/down?
          pos = 0;
        }
        return pos;
      };

     updateLastPos(deltaX, deltaY) {
        this.lastX = this.x;
        this.lastY = this.y;
      };

   translate(deltaX, deltaY) {
        // We restrict to the min of the viewport width/height or current width/height as the
        // current width/height may be smaller than the viewport width/height

        var newX = this.restrictRawPos(this.lastX + deltaX/this.scale,
                                  Math.min(this.viewportWidth, this.curWidth), this.imgWidth);
        this.x = newX;
        this.img.style.marginLeft = Math.ceil(newX*this.scale) + 'px';

        var newY = this.restrictRawPos(this.lastY + deltaY/this.scale,
                                  Mathis.viewportHeight), this.imgHeight);
        this.y = newY;
        this.img.style.marginTop = Math.ceil(newY*this.scale) + 'px';
      };

      zoom(scaleBy){
        this.scale = this.restrictScale(this.lastScale*scaleBy);

        this.curWidth = this.imgWidth*this.scale;
        this.curHeight = this.imgHeight*this.scale;

        this.img.style.width = Math.ceil(this.curWidth) + 'px';
        this.img.style.height = Math.ceil(this.curHeight) + 'px';

        // Adjust margins to make sure that we aren't out of bounds
        this.translate(0, 0);
      };

    rawCenter(e) {
        var pos = this.absolutePosition(container);

        // We need to account for the scroll position
        var scrollLeft = window.pageXOffset ? window.pageXOffset : document.body.scrollLeft;
        var scrollTop = window.pageYOffset ? window.pageYOffset : document.body.scrollTop;

        var zoomX = -this.x + (e.center.x - pos.x + scrollLeft)/this.scale;
        var zoomY = -this.y + (e.center.y - pos.y + scrollTop)/this.scale;

        return { x: zoomX, y: zoomY };
      };

      updateLastScale() {
        this.lastScale = this.scale;
      };

      zoomAround(scaleBy, rawZoomX, rawZoomY, doNotUpdateLast) {
        // Zoom
        this.zoom(scaleBy);

        // New raw center of viewport
        var rawCenterX = -this.x + Math.min(this.viewportWidth, this.curWidth)/2/this.scale;
        var rawCenterY = -this.y + Math.min(this.viewportHeight, this.curHeight)/2/this.scale;

        // Delta
        var deltaX = (rawCenterX - rawZoomX)*this.scale;
        var deltaY = (rawCenterY - rawZoomY)*this.scale;

        // Translate back to zoom center
        translate(deltaX, deltaY);

        if (!doNotUpdateLast) {
          this.updateLastScale();
          this.updateLastPos();
        }
      };

    zoomCenter(scaleBy) {
        // Center of viewport
        var zoomX = -this.x + Math.min(this.viewportWidth, this.curWidth)/2/this.scale;
        var zoomY = -this.y + Math.min(this.viewportHeight, this.curHeight)/2/this.scale;

    this.zoomAround(scaleBy, zoomX, zoomY);
      };

   zoomIn () {
        this.zoomCenter(2);
      };

    zoomOut () {
        this.zoomCenter(1/2);
      };

   Hammer_onLoad = function (id) {
   this.constructor()

        this.img = document.getElementById(id);
        container = img.parentElement;

        disableImgEventHandlers();

        this.imgWidth = img.width;
        this.imgHeight = img.height;
        this.viewportWidth = this.img.offsetWidth;
        this.scale = this.viewportWidth/this.imgWidth;
        this.lastScale = this.scale;
        this.viewportHeight = this.img.parentElement.offsetHeight;
        this.curWidth = this.imgWidth*this.scale;
        this.curHeight = this.imgHeight*this.scale;

        var hammer = new Hammer(container, {
          domEvents: true
        });

        hammer.get('pinch').set({
          enable: true
        });

        hammer.on('pan', function (e) {
          disable_on_hammer()

          translate(e.deltaX, e.deltaY);
        });

        hammer.on('panend', function (e) {
          updateLastPos();
          enable_on_hammer()

        });

        hammer.on('pinch', function (e) {
          
          disable_on_hammer()

          // We only calculate the pinch center on the first pinch event as we want the center to
          // stay consistent during the entire pinch
          if (pinchCenter === null) {
            pinchCenter = rawCenter(e);
            var offsetX = pinchCenter.x*scale - (-x*scale + Math.min(viewportWidth, curWidth)/2);
            var offsetY = pinchCenter.y*scale - (-y*scale + Math.min(viewportHeight, curHeight)/2);
            pinchCenterOffset = { x: offsetX, y: offsetY };
          }

          // When the user pinch zooms, she/he expects the pinch center to remain in the same
          // relative location of the screen. To achieve this, the raw zoom center is calculated by
          // first storing the pinch center and the scaled offset to the current center of the
          // image. The new scale is then used to calculate the zoom center. This has the effect of
          // actually translating the zoom center on each pinch zoom event.
          var newScale = restrictScale(scale*e.scale);
          var zoomX = pinchCenter.x*newScale - pinchCenterOffset.x;
          var zoomY = pinchCenter.y*newScale - pinchCenterOffset.y;
          var zoomCenter = { x: zoomX/newScale, y: zoomY/newScale };

          zoomAround(e.scale, zoomCenter.x, zoomCenter.y, true);
        });

        hammer.on('pinchend', function (e) {
          updateLastScale();
          updateLastPos();
          pinchCenter = null;
          enable_on_hammer()
        });

        hammer.on('doubletap', function (e) {
          disable_on_hammer()
          var c = rawCenter(e);
          zoomAround(2, c.x, c.y);
          enable_on_hammer()
        });

      };

}
