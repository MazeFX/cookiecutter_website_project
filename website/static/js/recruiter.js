/**
 * File: recruiter.js
 * Creator: MazeFX
 * Date: 14-7-2016
 * 
 * JS for recruiter page.
 * Startup functions for js.
 */
jQuery(function() {

    jQuery('#da-slider').cslider({
        autoplay	: true,
        bgincrement	: 450
    });

});
jQuery(document).ready(function(){
    jQuery('#parallax .parallax-layer')
    .parallax({
      mouseport: jQuery('#parallax')
    });
});
