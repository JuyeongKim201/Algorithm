var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var a = parseInt(input[0]);

for (var i = 1; i <= input[0]; i++) {
    input[i].split("");
    console.log("Case #" + i + ": " + parseInt(input[i][0]) + " + " + parseInt(input[i][2]) + " = " + (parseInt(input[i][0])+parseInt(input[i][2])));
}