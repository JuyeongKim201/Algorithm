// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// let input = [];

// // 풀이 1
// rl.on('line', function (line) {
//     input = [line];
// }).on('close',function(){
//     str = input[0];
//     for(let i = 0; i < str.length; i++){
//         console.log(str[i]);
//     }
// });

// // 풀이 2
// rl.on('line', function (line) {
//     input = [line];
// }).on('close',function(){
//     str = input[0];
//     for (let i of str){
//         console.log(i);
//     }
// });


// // 풀이 3
// rl.on('line', function (line) {
//     input = [line];
// }).on('close',function(){
//     str = input[0];
//     [...str].map((i)=>console.log(i));
// });


// // 풀이 4
// rl.on('line', function (line) {
//     input = [line];
// }).on('close',function(){
//     str = input[0];
//     [...str].forEach((i)=>console.log(i));
// });


function sum(x, y, z) {
    return x + y + z;
}

const chars = ['a', 'b', 'c'];

console.log(sum(...chars));
// Expected output: abc