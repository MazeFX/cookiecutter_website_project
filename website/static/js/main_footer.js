/**
 * File: recruiter_footer.js
 * Creator: MazeFX
 * Date: 27-7-2016
 *
 * JS for recruiter footer
 * Function for rebumping the footer to the bottom of the page
 * while keeping the height variable
 */

// TODO - Rework footer to general site footer

var bumpIt = function() {
      jQuery('#main-wrap').css('margin-bottom', -Math.abs(jQuery('footer').outerHeight()));
      jQuery('#footer-push').css('height', jQuery('footer').outerHeight());
    },
    didResize = false;

bumpIt();

jQuery(window).resize(function() {
  didResize = true;
});
setInterval(function() {
  if(didResize) {
    didResize = false;
    bumpIt();
    jQuery('.dropdown-menu-wrapper').height(jQuery('.dropdown-menu').height() + 6);
  }
}, 250);
