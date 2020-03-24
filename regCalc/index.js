const data = require('./data');
const reg = require('./regression');

let buckets = data.data.map(row => row[0]);
let max = data.data.map(row => row[1]);
let min = data.data.map(row => row[2]);
let avg = data.data.map(row => row[3]);



let minRes = reg.findLineByLeastSquares(buckets, min);
console.log("Results min: y = "+minRes.m +" * x + "+minRes.b);
let maxRes = reg.findLineByLeastSquares(buckets, max);
console.log("Results max: y = "+maxRes.m +" * x + "+maxRes.b);
let avgRes = reg.findLineByLeastSquares(buckets, avg);
console.log("Results avh: y = "+avgRes.m +" * x + "+avgRes.b);