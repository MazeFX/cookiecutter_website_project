/**
 * File: recruiter.js
 * Creator: MazeFX
 * Date: 14-7-2016
 *
 * JS for recruiter page.
 * Startup functions for js.
 */

jQuery(document).ready(function(){

    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };

    if ( $( "#parallax" ).length ) {
        jQuery('#parallax .parallax-layer')
            .parallax({
                mouseport: jQuery('#parallax')
            });
    }

    if ($(window).width() < 440) {
        jQuery('.parallax-layer')
        .trigger({ type: 'freeze', x: 0.5, y: 0.5, decay: 0 });
    }

    function menuToggle (toggle) {
        if (toggle) {
            var $dropDownMenuWidth = jQuery('.dropdown-menu').width() + 6;
            jQuery('.dropdown-menu-wrapper').width($dropDownMenuWidth);
        } else {
            jQuery('.dropdown-menu-wrapper').width(0);
        }
    }

    var toggle = false;
    jQuery('.navbar-toggler').click(
        function() {
            if (toggle) {
                toggle = !toggle;
                menuToggle(toggle);
            }
        }
    );

    if(isMobile.any()) {
        var dropDown = jQuery('.dropdown');
        jQuery.each(dropDown, function(index, element) {
            var hammertime = new Hammer(element);
            hammertime.on('tap', function(event) {
                toggle = !toggle;
                menuToggle(toggle);
            });
        });
    } else {
        jQuery('.dropdown').click(
        function() {
            toggle = !toggle;
            menuToggle(toggle);
            }
        );

        jQuery('.dropdown').hover(
            function() {
                menuToggle(true);
            }, function() {
                menuToggle(false);
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

    }
});




