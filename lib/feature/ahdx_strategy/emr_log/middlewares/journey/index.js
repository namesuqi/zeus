var winston = require('winston');
var path = require('path');

var Journey = function(options) {
  options = options || {};

  this.__path = options.path;
  this.__file = options.file;
  this.formatter = options.formatter;
  this.__logger = null;
  this.__init();

  return this.__logger;
};

Journey.prototype.__init = function() {
  var self = this;
  var transport = new(winston.transports.File)({
    filename: path.join(self.__path , self.__file),
    timestamp: function() { return Date.now();},
    formatter: self.formatter,
    json: false
  });

  self.__logger = new (winston.Logger)({
    transports: [
      transport
    ]
  });
};

exports.Journey = Journey;
