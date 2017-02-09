console.log('Running Custom Shapes Geometry loader.');

AFRAME.registerGeometry('extruded_arrow', {
    schema: {
    depth: {default: 1, min: 0},
    height: {default: 1, min: 0},
    width: {default: 1, min: 0},
    segmentsHeight: {default: 1, min: 1, max: 20, type: 'int'},
    segmentsWidth: {default: 1, min: 1, max: 20, type: 'int'},
    segmentsDepth: {default: 1, min: 1, max: 20, type: 'int'}
    },

    init: function (data) {
        var pts = [];
        pts.push( new THREE.Vector2 ( 0, 0 ) );
        pts.push( new THREE.Vector2 ( (-1 * data.width), (2 * data.height) ) );
        pts.push( new THREE.Vector2 ( (3 * data.width), (1 * data.height)) );
        pts.push( new THREE.Vector2 ( (3 * data.width), (2 * data.height) ) );
        pts.push( new THREE.Vector2 ( (5 * data.width), 0 ) );
        pts.push( new THREE.Vector2 ( (3 * data.width), (-2 * data.height) ) );
        pts.push( new THREE.Vector2 ( (3 * data.width), (-1 * data.height) ) );
        pts.push( new THREE.Vector2 ( (-1 * data.width), (-2 * data.height) ) );
        pts.push( new THREE.Vector2 ( 0, 0 ) );
        var arrowShape = new THREE.Shape( pts );

        var extrudeSettings = {
            steps: 2,
            amount: data.depth,
            bevelEnabled: false
        };

        this.geometry = new THREE.ExtrudeGeometry( arrowShape, extrudeSettings );
    }
});

AFRAME.registerGeometry('extruded_arrow_2', {
    schema: {
    depth: {default: 1, min: 0},
    height: {default: 1, min: 0},
    width: {default: 1, min: 0},
    segmentsHeight: {default: 1, min: 1, max: 20, type: 'int'},
    segmentsWidth: {default: 1, min: 1, max: 20, type: 'int'},
    segmentsDepth: {default: 1, min: 1, max: 20, type: 'int'}
    },

    init: function (data) {
        var pts = [];
        // [571, 0], [312, 259], [250, 233], [250, 164], [-119, 256], [-159, 206], [-56, 0], [-159, -206], [-119, -256], [250, -164], [250, -233], [312, -259]
        pts.push( new THREE.Vector2 ( (5.71  * data.width), 0 ) );
        pts.push( new THREE.Vector2 ( (3.12 * data.width), (2.59 * data.height) ) );
        pts.push( new THREE.Vector2 ( (2.50 * data.width), (2.33 * data.height) ) );
        pts.push( new THREE.Vector2 ( (2.50 * data.width), (1.64 * data.height) ) );
        pts.push( new THREE.Vector2 ( (-1.19 * data.width), (2.56 * data.height) ) );
        pts.push( new THREE.Vector2 ( (-1.59 * data.width), (2.06 * data.height) ) );
        pts.push( new THREE.Vector2 ( (-0.56 * data.width), 0 ) );
        pts.push( new THREE.Vector2 ( (-1.59 * data.width), (-2.06 * data.height) ) );
        pts.push( new THREE.Vector2 ( (-1.19 * data.width), (-2.56 * data.height) ) );
        pts.push( new THREE.Vector2 ( (2.50 * data.width), (-1.64 * data.height) ) );
        pts.push( new THREE.Vector2 ( (2.50 * data.width), (-2.33 * data.height) ) );
        pts.push( new THREE.Vector2 ( (3.12 * data.width), (-2.59 * data.height) ) );
        var arrowShape = new THREE.Shape( pts );

        var extrudeSettings = {
            steps: 2,
            amount: data.depth,
            bevelEnabled: false
        };

        this.geometry = new THREE.ExtrudeGeometry( arrowShape, extrudeSettings );
    }
});


