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

    jQuery('.navbar-toggler').hover(
        function() {
            console.log('Hovering into menu..');
            jQuery('.navbar-toggler').trigger('click');
        }, function() {
            console.log('Hovering out of menu..');
            jQuery('.navbar-toggler').trigger('click');
        }
    );

    jQuery('#exCollapsingNavbar').hover(
        function() {
            console.log('Hovering into inner nav..');
        }, function() {
            console.log('Hovering out of inner nav..');
            jQuery('.navbar-toggler').trigger('click');
        }
    );
});

