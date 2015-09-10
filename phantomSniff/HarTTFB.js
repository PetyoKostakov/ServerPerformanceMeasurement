/**
 * Created by I312934 on 9/8/2015.
 */
var fs = require('fs'),
    harFile = process.argv[2];

fs.readFile(harFile, 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  } else {
    var sum = 0;
    data = JSON.parse(data);

    data.log.entries.forEach(function (entry) {
      sum += entry.timings.wait;
    });
    console.log("TTFB sum:", sum);
    console.log("TTFB AVG:", sum / data.log.entries.length );
  }
});