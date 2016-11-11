/**
 * File: recruiter.js
 * Creator: MazeFX
 * Date: 14-7-2016
 *
 * JS for recruiter page.
 * Startup functions for js.
 */

jQuery(document).ready(function(){

    jQuery('#parallax .parallax-layer')
    .parallax({
      mouseport: jQuery('#parallax')
    });

    if ($(window).width() < 440) {
        jQuery('.parallax-layer')
        .trigger({ type: 'freeze', x: 0.5, y: 0.5, decay: 0 });
    }

    // jQuery('.navbar-toggler').hover(
    //     function() {
    //         jQuery('.navbar-toggler').trigger('click');
    //     }, function() {
    //         jQuery('.navbar-toggler').trigger('click');
    //     }
    // );
    //
    // jQuery('#exCollapsingNavbar').hover(
    //     function() {
    //     }, function() {
    //         jQuery('.navbar-toggler').trigger('click');
    //     }
    // );
});

