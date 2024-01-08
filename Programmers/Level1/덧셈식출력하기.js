const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

// input에서 map 함수를 이용해 Number로 바꿔 넣어준다. 
rl.on('line', function (line) {
    input = line.split(' ').map(Number);
}).on('close', function () {
    const [a, b] = input;
    console.log(`${a} + ${b} = ${a+b}`);    
});