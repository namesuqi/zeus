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
  'file_seed_change': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=file_seed_change' + sep +
      'peer_id=' + options.meta.peer_id + sep +
      'file_id=' + options.meta.file_id + sep +
      'operation=' + options.meta.operation + sep +
      'slice_map=' + options.meta.slice_map + sep +
      'cppc=' + options.meta.cppc + sep;
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

var file_start = input[2];
var file_end = input[3];
var seed_start = input[4];
var seed_end = input[5];
var delDistribute = Mock_Data.delDistribute(file_start, file_end, seed_start, seed_end);

delDistribute.forEach(function(file) {
  Journey.log('file_seed_change',file);
});