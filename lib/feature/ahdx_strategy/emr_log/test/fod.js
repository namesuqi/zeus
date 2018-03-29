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
  'fod_report': function formatter(options) {
    var str = 'topic=fod_report' + sep +
      'public_ip=' + options.meta.publicIP + sep +
      'timestamp=' + options.timestamp() + sep +
      'id=' + options.meta.id + sep +
      'peer_id=' + options.meta.peer_id + sep +
      'url=' + options.meta.url + sep +
      'file_id=' + options.meta.file_id + sep +
      'play_type=' + options.meta.type + sep +
      'fsize=' + options.meta.fsize + sep;
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
var peer_num = input[4];
var fod = Mock_Data.fod_report(start, end, peer_num);

fod.forEach(function(file) {
  Journey.log('fod_report',file);
});