/*
이스케이프 시퀀스(escape sequence) 사용 -> ' 와 " 앞에 \ (백슬래시) 붙이기
*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('close', function () {
    // !@#$%^&*(\ '"   <>?:;
    // !@#$%^&*(\ \'\" <>?:;
    console.log("!@#$%^&*(\\'\"<>?:;");
});