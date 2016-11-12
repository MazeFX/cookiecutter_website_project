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


    jQuery('.dropdown').hover(
        function() {
            // jQuery('.dropdown-menu-wrapper').height(jQuery('.dropdown-menu').height() + 3);
            var $dropDownMenuWidth2 = jQuery('.dropdown-menu').width() + 3;
            console.log('Current width of dropDownMenu: ' + $dropDownMenuWidth2);

            jQuery('.dropdown-menu-wrapper').width($dropDownMenuWidth2);
            console.log('setting width on hover in:  0');

        }, function() {
            jQuery('.dropdown-menu-wrapper').width(0);
            console.log('setting width on hover out: 0');
        }
    );

    jQuery('.navbar-toggler').hover(
        function() {
            jQuery('.navbar-toggler').trigger('click');
            jQuery('.dropdown-menu-wrapper').height(jQuery('.dropdown-menu').height() + 6);
        }, function() {
            jQuery('.navbar-toggler').trigger('click');
        }
    );

    jQuery('#exCollapsingNavbar').hover(
        function() {
        }, function() {
            jQuery('.navbar-toggler').trigger('click');
        }
    );
});

