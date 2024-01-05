// 문제: 문자열 반복해서 출력하기
/*
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {    
    str = input[0];
    n = Number(input[1]);
    
    res = ''
    for (let i = 0; i < n; i++){
        res += str;
    }
    console.log(res);
});
*/
/* 2번 풀이: repeat 메서드 활용 
repeat: string에 적용 가능
*/
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {    
    str = input[0];
    n = Number(input[1]);
    
    console.log(str.repeat(n));
});

