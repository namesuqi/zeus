"use strict";

var path = require('path');
var Journey = require('../middlewares/journey.js');
var Mock_Data = require('./data.js');

var configure = {
  isp: 'shata',

  journey: {
    path: path.join(__dirname, "../../testlogs"),
    file: 'emulate.log'
  }
};

var sep = String.fromCharCode(0x1f);

var formats = {
  'peer_info': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=peer_info' + sep +
      'peer_id=' + options.meta.peer_id + sep +
      'sdk_version=' + options.meta.version + sep +
      'nat_type=' + options.meta.natType + sep +
      'public_ip=' + options.meta.publicIP + sep +
      'public_port=' + options.meta.publicPort + sep +
      'private_ip=' + options.meta.privateIP + sep +
      'private_port=' + options.meta.privatePort + sep;
    return str;
  }
};


Journey.init(formats, sep);

Journey.gengrateJourney(configure.journey, function(err) {
  if (err) {
    console.error('journey handle init fail.', err.stack);
  }

  Journey.registerRotateSignal();
});

var input = [];
process.argv.forEach(function (val, index, array) {
  input.push(val);
});
var start = input[2];
var end = input[3];
var peer_info = Mock_Data.peer_info(start, end);

peer_info.forEach(function(file) {
  Journey.log('peer_info',file);
});