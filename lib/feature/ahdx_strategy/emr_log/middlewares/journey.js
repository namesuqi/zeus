var fs = require('fs');
var path = require('path');
var Journey = require('./journey/index.js').Journey;

var sep = null;
var formats = null;
var journeyHandle = null;

function reopen(fileTransport) {
  var fullname = path.join(fileTransport.dirname, fileTransport._getFile(false));
  var oldStream = fileTransport._stream;
  var stream = fs.createWriteStream(fullname, fileTransport.options);
  stream.setMaxListeners(Infinity);

  fileTransport.once('flush', function() {
    fileTransport.opening = false;
    fileTransport._size = 0;
    fileTransport._stream = stream;
    fileTransport.emit('open', fullname);
    if (oldStream) {
      oldStream.end();
      oldStream.destroySoon();
    }
  });

  fileTransport.flush();
};

module.exports.init = function(__formats, __sep) {
  formats = __formats;
  sep = __sep || String.fromCharCode(0x1f);
};

function formatter(options) {
  var func = formats[options.meta.logTag];
  if (!func) {
    console.error('no formatter function', options.meta.logTag);
    return;
  }
  options.meta = options.meta.logBody;
  return func(options);
};

module.exports.gengrateJourney = function(config, callback) {
  journeyHandle = new Journey({
    path: config.path,
    file: config.file,
    formatter: formatter
  });
  if (!journeyHandle || !journeyHandle.transports || !journeyHandle.transports.file) {
    return callback(new Error('E_JOURNEY_ERROR'));
  }
  callback(null);
};

module.exports.registerRotateRoute = function(app, route, name) {
  app.get('/logrotate', function(req, res, next) {
    if (journeyHandle) {
      reopen(journeyHandle.transports.file);
    }
    return res.status(200).end();
  });
};

module.exports.registerRotateSignal = function() {
  process.on('SIGUSR2', function() {
    if (journeyHandle) {
      reopen(journeyHandle.transports.file);
    }
  });
};

module.exports.log = function(logTag, logBody) {
  journeyHandle.log('info', {logTag: logTag, logBody: logBody});
};

