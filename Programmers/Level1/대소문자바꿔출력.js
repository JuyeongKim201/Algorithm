// 문제: 대소문자 바꿔서 출력하기

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let strArray = str.split('');
    let test = strArray.map((i)=>{
        return i === i.toUpperCase() ? i.toLowerCase() : i.toUpperCase();
    })
    console.log(test.join(''));
    
});

