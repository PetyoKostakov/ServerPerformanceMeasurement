var express = require('express'),
    port = process.env.PORT || 3000,
    fs = require('fs'),
    app = express();

app.use('/', express.static("./static"));


app.use('/file/', function (req, res) {
  var fileName = req.query.fileName,
      method = req.query.method,
      dataToWrite = req.query.dataToWrite;

  if (method === 'read') {
    fs.readFile("./temp/" + fileName, 'utf8', function (err, data) {
      if (err) return console.log(err);
      res.send(data);
    });
  } else {
    fs.writeFile("./temp/" + fileName, dataToWrite, function (err) {
      if (err) {
        console.log(err);
        return console.log(err);
      }
      res.send(dataToWrite,">", fileName);
    });
  }
});

app.listen(port, function () {
  console.log('Listening on port', port);
});

module.exports = app;