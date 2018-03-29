var peerid = require('./peerid.js');
var PEER_ID = peerid.PEER_ID;
var FILE_ID = [
    "AAAAA51782F34770873611C851D6A001",
	"AAAAAFFB73D14FCEA2554342C33C7002",
	"AAAAAF3FB91F4C50B222CB3E2226A003",
	"AAAAAF3638DD4507BCA93F86E76F8004",
	"AAAAA5431F0C43DC9940781E20C54005",
	"AAAAACA3E16942E4828A8F7F32723006",
	"AAAAA27CA9974C6596D39CF76BA67007",
	"AAAAA9855DDF45CA85945C92FC222008",
	"AAAAA63D1F6C4470BF5F93923E874009",
	"AAAAA27E9A5E4386A50A496E47C9B010",
	"AAAAA86A32B745C894B9E95FFAB77011",
	"AAAAA799E2264C6E85C5B4AB75EDB012",
	"AAAAA4A329594F43A1FFC06C01C9D013",
	"AAAAA21C47054723BF27B21804CA3014",
	"AAAAAAA384194AC9AEFE1C26E8F40015",
	"AAAAA6807ED24F9CB2FF9EF5BBE1A016",
	"AAAAACD7BFA04DF2996414A9908AA017",
	"AAAAA240CBA142B1B3923A3DC2264018",
	"AAAAA58CBE1D47B4A7A5D89D11CE2019",
	"AAAAA13B2C13461F9FD75E09E75C7020"
];

var FILE_SIZE = [
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200,
	51200
]


exports.disk_cache_in = function(start, end, disk_free) {
	var diskFiles_in = [];
	for(var i = start; i < end; i++) {
		disk_free = parseInt(disk_free) - parseInt(FILE_SIZE[i]);
		var str = {file_id:FILE_ID[i],behavior:"in",lsm_free:parseInt(disk_free),universe:true,timestamp:Date.now()};
		diskFiles_in.push(str);
	};
	return diskFiles_in;
};

exports.disk_cache_interrupt = function(start, end, disk_free) {
	var diskFiles_interrupt = [];
	for(var i = start; i < end; i++) {
		var str = {file_id:FILE_ID[i],behavior:"interrupt",lsm_free:parseInt(disk_free),universe:true,timestamp:Date.now()};
		diskFiles_interrupt.push(str);
	};
	return diskFiles_interrupt;
};

exports.disk_cache_out = function(start, end, disk_free) {
	var diskFiles_out = [];
	for(var i = start; i < end; i++) {
		disk_free = parseInt(disk_free) + parseInt(FILE_SIZE[i]);
		var str = {file_id:FILE_ID[i],behavior:"out",lsm_free:parseInt(disk_free),universe:true,timestamp:Date.now()};
		diskFiles_out.push(str);
	};
	return diskFiles_out;
};

exports.push_prefetch_task_start = function(start, end){
	var prefetchFiles_start = [];
	for(var i = start; i < end; i++) {
		var str = {file_id:FILE_ID[i],flag:"start",file_size:parseInt(FILE_SIZE[i]),timestamp:Date.now()};
		prefetchFiles_start.push(str);
	};
	return prefetchFiles_start;
};

exports.push_prefetch_task_downloading = function(start, end){
	var prefetchFiles_downloading = [];
	for(var i = start; i < end; i++) {
		var str = {file_id:FILE_ID[i],flag:"downloading",file_size:parseInt(FILE_SIZE[i]),timestamp:Date.now()};
		prefetchFiles_downloading.push(str);
	};
	return prefetchFiles_downloading;
};

exports.push_prefetch_task_end = function (start, end){
	var prefetchFiles_end = [];
	for(var i = start; i < end; i++) {
		var str = {file_id:FILE_ID[i],flag:"end",file_size:parseInt(FILE_SIZE[i]),timestamp:Date.now()};
		prefetchFiles_end.push(str);
	};
	return prefetchFiles_end;
};

exports.peer_info = function (start, end){
	var peer_info = [];
	for(var i = start; i < end; i++) {
		var str = {peer_id:PEER_ID[i],version:"2.4.1",natType:0,publicIP:"192.168.1.1",publicPort:32717,privateIP:"192.168.1.1",privatePort:32717,timestamp:Date.now()};
		peer_info.push(str);
	};
	return peer_info;
};

exports.heartbeat = function (start, end){
	var heartbeat = [];
	for(var i = start; i < end; i++) {
		var str = {peer_id:PEER_ID[i],version:"2.4.1",natType:0,publicIP:"192.168.1.1",publicPort:32717,privateIP:"192.168.1.1",privatePort:32717,timestamp:Date.now()};
		heartbeat.push(str);
	};
	return heartbeat;
};

exports.fod_report = function (file_start, file_end, peer_num){
	var fod = [];
	var peer_start = 0
    var peer_end = peer_start + parseInt(peer_num)

    for(var i = file_start; i < file_end; i++ ) {
        for(var j = peer_start; j < peer_end; j++) {
            var str = {id:"F88A0D1BD86A4044BE6EF2669D206F32",timestamp:Date.now(),peer_id:PEER_ID[j],url:"http://testvideo.cloutropy.com/twice.ts",file_id:FILE_ID[i],type:"vod",publicIP:"192.168.1.1",fsize:FILE_SIZE[i]};
			fod.push(str);           
        }
        peer_start = peer_end
        peer_end = peer_start + parseInt(peer_num)
    }
	return fod;
};

exports.distribute = function (file_start, file_end, seed_start, seed_end){
	var distribute = [];

    for(var i = file_start; i < file_end; i++ ) {
        for(var j = seed_start; j < seed_end; j++) {
            var str = {peer_id:PEER_ID[j],file_id:FILE_ID[i],operation:"update",slice_map:"FFFFFFFFFFFFFFFF",cppc:12,timestamp:Date.now()};
			distribute.push(str);           
        }
    }
	return distribute;
};

exports.delDistribute = function (file_start, file_end, seed_start, seed_end){
	var delDistribute = [];

    for(var i = file_start; i < file_end; i++ ) {
        for(var j = seed_start; j < seed_end; j++) {
            var str = {peer_id:PEER_ID[j],file_id:FILE_ID[i],operation:"delete",slice_map:"0000000000000000",cppc:0,timestamp:Date.now()};
			delDistribute.push(str);           
        }
    }
	return delDistribute;
};

 exports.download_flow = function (file_no, seed_start, seed_end, p2p_download, cdn_download){
	var download_flow = [];

    for(var i = seed_start; i < seed_end; i++ ) {    
        var str = {peer_id:PEER_ID[i],file_id:FILE_ID[file_no],duration:60,publicIP:"192.168.1.1",fsize:FILE_SIZE[file_no],p2p_download:p2p_download,cdn_download:cdn_download,timestamp:Date.now()};
		download_flow.push(str);           
    }
	return download_flow;
};