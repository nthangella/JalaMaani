/**
 * waterLevelStatusServerDemo4.js
 * 
 * Water Level Indicator Web Service
 * 
 * Author : Nagendra Thangella
 * No warranties or guaranties. Use this at your own risk.
 * @version 1.0.0 
 */

var express = require('express');
var app = express();
var htmlFile = '/home/pi/html/index.html';
var staticContentPath = '/home/pi/html';

//Define static HTML files
app.use(express.static(staticContentPath));

//Return the html file for uri /
app.get('/', function(req, res) {
    res.sendFile(htmlFile);
});

//Listen on port 8900
app.listen('8900');
