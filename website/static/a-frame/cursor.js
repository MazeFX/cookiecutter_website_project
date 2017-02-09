/**
 * Created by nickgeense on 03/02/17.
 */

AFRAME.registerComponent('cursor-listener', {
  init: function () {
    this.el.addEventListener('click', function (evt) {
        startArrowAnimation()
    });
  }
});
