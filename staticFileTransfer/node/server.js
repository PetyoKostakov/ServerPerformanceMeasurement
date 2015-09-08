var express = require('express'),
    port = process.env.PORT || 3000,
    app = express();

app.use('/', express.static("./static"));

app.listen(port, function () {
  console.log('Listening on port', port);
});

module.exports = app;