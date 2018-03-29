var Mock_Data = require('./data.js');
var input = [];
process.argv.forEach(function (val, index, array) {
  input.push(val);
});

var file_start = input[2];
var file_end = input[3];
var interrupt_start = input [4];
var interrupt_end = input [5];
var free = input[6];

    var diskFiles_out = Mock_Data.disk_cache_out(file_start, file_end, free);

    var out_free = diskFiles_out[diskFiles_out.length - 1].lsm_free
    var interrupt_out = Mock_Data.disk_cache_out(interrupt_start, interrupt_end, out_free);
console.log(diskFiles_out);
console.log(interrupt_out);