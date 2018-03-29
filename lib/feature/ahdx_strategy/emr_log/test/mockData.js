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
  },

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
  },

  'heartbeat': function formatter(options) {
  	var str = 'timestamp=' + options.timestamp() + sep +
      'topic=heartbeat' + sep +
      'peer_id=' + options.meta.peer_id + sep +
  	  'sdk_version=' + options.meta.version + sep +
  	  'nat_type=' + options.meta.natType + sep +
  	  'public_ip=' + options.meta.publicIP + sep +
  	  'public_port=' + options.meta.publicPort + sep +
  	  'private_ip=' + options.meta.privateIP + sep +
  	  'private_port=' + options.meta.privatePort + sep;
  	 return str;
  },

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
  },

  'file_seed_change': function formatter(options) {
  	var str = 'timestamp=' + options.timestamp() + sep +
      'topic=file_seed_change' + sep +
      'peer_id=' + options.meta.peer_id + sep +
  	  'file_id=' + options.meta.file_id + sep +
  	  'operation=' + options.meta.operation + sep +
  	  'slice_map=' + options.meta.slice_map + sep +
  	  'cppc=' + options.meta.cppc + sep;
  	 return str;
  },

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



var diskFiles = [
  {file_id:"0000000000000001",behavior:"out",lsm_free:10000,universe:true,timestamp:Date.now()},
  {file_id:"0000000000000002",behavior:"in",lsm_free:10000,universe:true,timestamp:Date.now()}
];

var prefetchFiles = [
  {file_id:"0000000000000001",flag:"end",file_size:10000,timestamp:Date.now()},
  {file_id:"0000000000000002",flag:"downloading",file_size:10000,timestamp:Date.now()},
  {file_id:"0000000000000003",flag:"downloading",file_size:10000,timestamp:Date.now()}
];

diskFiles.forEach(function(file) {
  Journey.log('push_disk_cache',file);
})

prefetchFiles.forEach(function(file) {
  Journey.log('push_prefetch_task',file);
})

var peer_info = Mock_Data.peer_info(0, 3);

peer_info.forEach(function(file) {
  Journey.log('peer_info',file);
})