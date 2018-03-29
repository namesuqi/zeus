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
  'download_flow': function formatter(options) {
    var str = 'topic=download_flow' + sep +
      'public_ip=' + options.meta.publicIP + sep +
      'peer_id=' + options.meta.peer_id + sep +
      'timestamp=' + options.timestamp() + sep +
      'duration=' + options.meta.duration + sep +
      'file_id=' + options.meta.file_id + sep +
      'fsize=' + options.meta.fsize + sep +
      'p2p_download=' + options.meta.p2p_download + sep +
      'cdn_download=' + options.meta.cdn_download + sep;
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
var file_no = input[2];
var seed_start = input[3];
var seed_end = input[4];
var p2p_download = input[5];
var cdn_download = input[6];
var download_flow = Mock_Data.download_flow(file_no, seed_start, seed_end, p2p_download, cdn_download);

download_flow.forEach(function(file) {
  Journey.log('download_flow',file);
});