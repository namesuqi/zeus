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
  'push_error': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=push_error' + sep +
      'server=push' + sep +
      'isp=' + configure.isp + sep +
      'level=' + options.meta.level + sep +
      'module=' + options.meta.module + sep +
      'err_info=' + options.meta.err_info + sep;
    return str;
  },

  'push_request': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=push_request' + sep +
      'server=push' + sep +
      'isp=' + configure.isp + sep +
      'request_url=' + options.meta.request_url + sep +
      'response_status_code=' + options.meta.response_status_code + sep;
    return str;
  },

  'push_memory_cache': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=push_memory_cache' + sep +
      'server=push' + sep +
      'isp=' + configure.isp + sep +
      'file_id=' + options.meta.file_id + sep +
      'chunk_id=' + options.meta.chunk_id + sep +
      'behavior=' + options.meta.behavior + sep;
    return str;
  },

  'push_disk_cache': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=push_disk_cache' + sep +
      'server=push' + sep +
      'isp=' + configure.isp + sep +
      'universe=' + options.meta.universe + sep +
      'file_id=' + options.meta.file_id + sep +
      'behavior=' + options.meta.behavior + sep +
      'lsm_free=' + options.meta.lsm_free + sep;
    return str;
  },

  'push_prefetch_task': function formatter(options) {
    var str = 'timestamp=' + options.timestamp() + sep +
      'topic=push_prefetch_task' + sep +
      'server=push' + sep +
      'isp=' + configure.isp + sep +
      'file_id=' + options.meta.file_id + sep +
      'file_size=' + options.meta.file_size + sep +
      'flag=' + options.meta.flag + sep;
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
var lsm_free = input[4];

var diskFiles_interrupt = Mock_Data.disk_cache_interrupt(file_start, file_end, lsm_free);

diskFiles_interrupt.forEach(function(file) {
  Journey.log('push_disk_cache',file);
});

setTimeout(function() {
    var diskFiles_out = Mock_Data.disk_cache_out(file_start, file_end, lsm_free);
    diskFiles_out.forEach(function(file) {
      Journey.log('push_disk_cache',file);
    });
}, 210000);