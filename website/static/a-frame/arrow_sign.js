/**
 * Created by nickgeense on 01/02/17.
 */
var animation_running = false;

function isIterable(obj) {
  // checks for null and undefined
  if (obj == null) {
    return false;
  }
  return typeof obj[Symbol.iterator] === 'function';
}


function iterElements (elements, f, s) {
    if( isIterable(elements) == true ) {
        for (var i = 0; i < elements.length; i++) {
            elements[i][f](s);
        }
    } else {
        elements[f](s);
    }
}

function moveLights (lit_rows) {
    for (var i=0; i < lit_rows.length; i++) {
        if (lit_rows[i] !== 0) {
            if (i == 0 && lit_rows[i] == 11) {
                continue
            } else if (i == 1 && lit_rows[i] == 10) {
                continue
            } else if (i == 2 && lit_rows[i] == 9) {
                continue
            } else if (i == 3 && lit_rows[i] == 8) {
                continue
            } else {
                var cssSelector1 = '.bulb-row-' + lit_rows[i] + ' .lightbulb';
                lit_rows[i] = lit_rows[i] + 1;
                var cssSelector2 = '.bulb-row-' + lit_rows[i] + ' .lightbulb';
                iterElements(document.querySelectorAll(cssSelector1), 'emit', 'light-off');
                iterElements(document.querySelectorAll(cssSelector2), 'emit', 'light-on');
            }
        }
    }
}

function startBlinkLights (light_cycle){
    var bulbs_row_1 = document.querySelectorAll('.bulb-row-1 .lightbulb');
    setInterval(function() {
        var lit_rows = [0, 0, 0, 0];

        setInterval(function(){
            moveLights(lit_rows);

            if (lit_rows[0] == 0) {
                lit_rows[0] = 1;
                iterElements(bulbs_row_1, 'emit', 'light-on');
            } else if (lit_rows[0] == 4) {
                lit_rows[1] = 1;
                iterElements(bulbs_row_1, 'emit', 'light-on');
            } else if (lit_rows[0] == 7) {
                lit_rows[2] = 1;
                iterElements(bulbs_row_1, 'emit', 'light-on');
            } else if (lit_rows[0] == 10) {
                lit_rows[3] = 1;
                iterElements(bulbs_row_1, 'emit', 'light-on');
            }
        }, (light_cycle / 15));
    }, light_cycle);
}

function startArrowLight () {
    iterElements(document.querySelectorAll('.arrow-light'), 'emit', 'light-on');
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-light'), 'emit', 'light-off');
    }, 200);
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-light'), 'emit', 'light-on');
    }, 300);
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-light'), 'emit', 'light-off');
    }, 700);
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-light'), 'emit', 'light-on');
    }, 1000);
}

function startArrowAnimation () {
    if (animation_running) {
        return
    }
    console.log('Starting Developer animation..');
    animation_running = true;
    startBlinkLights(4500);
    iterElements(document.querySelectorAll('.arrow-black-hole'), 'emit', 'open');
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-container'), 'emit', 'fade-in');
        iterElements(document.querySelectorAll('.arrow-container'), 'emit', 'grow');
    }, 500);
    setTimeout(function () {
        iterElements(document.querySelectorAll('.arrow-black-hole'), 'emit', 'close');
    }, 750);
    setTimeout(function () {
        startArrowLight();
        startNeonAnimation();
    }, 1500);
}

function setFlickerLoop (neon_part) {
    var neon_prt = neon_part;
    var end_time = Math.round(Math.random() * (1500 - 1000)) + 1000;
    var timer = 0;

    (function loop() {
        var rand = Math.round(Math.random() * (400 - 100)) + 100;
        timer = timer + rand;
        if (timer > end_time) {
            if (neon_prt[1] == false) {
                iterElements(neon_prt[0], 'emit', 'light-on');
                neon_prt[1] = true;
            }
        } else {
            setTimeout(function () {
                //alert('A');
                if (neon_prt[1] == true) {
                    iterElements(neon_prt[0], 'emit', 'light-off');
                    neon_prt[1] = false;
                } else {
                    iterElements(neon_prt[0], 'emit', 'light-on');
                    neon_prt[1] = true;
                }
                loop();
            }, rand);
        }
    }());
}

function startNeonAnimation () {
    iterElements(document.querySelectorAll('.neon-black-hole'), 'emit', 'open');
    setTimeout(function () {
        iterElements(document.querySelectorAll('.neon-logo-container'), 'emit', 'fade-in');
        iterElements(document.querySelectorAll('.neon-logo-container'), 'emit', 'grow');
    }, 500);
    setTimeout(function () {
        iterElements(document.querySelectorAll('.neon-black-hole'), 'emit', 'close');
    }, 750);
    setTimeout(function () {
        startNeonLogo()
    }, 1500);
}

function startNeonLogo() {
    var neon_parts = document.querySelectorAll('.neon-logo');

    for (var i=0; i < neon_parts.length; i++) {
        var neon_part = [neon_parts[i], false];
        setFlickerLoop(neon_part);
    }

}

function startNeonLight() {
    var neon_parts = document.querySelectorAll('.neon-part');

    for (var i=0; i < neon_parts.length; i++) {
        var neon_part = [neon_parts[i], false];
        setFlickerLoop(neon_part);
    }
}

jQuery(document).ready(function(){
    setTimeout(function () {
        startNeonLight()
    }, 1000);
});




