/* 
[모듈 가져오기]
여기서 readline 모듈을 불러오고 있습니다. 이 모듈은 Node.js에서 사용자의 입력을 읽는 데 사용됩니다
*/
const readline = require('readline');

/*
[readline 인터페이스 생성]
readline.createInterface 메소드는 input과 output 스트림을 설정하여 readline 인터페이스를 생성합니다. 
process.stdin은 표준 입력 스트림(보통 키보드 입력)을, process.stdout은 표준 출력 스트림(보통 콘솔 출력)을 나타냅니다.
*/
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/*
[변수 선언]
input이라는 이름의 빈 배열을 선언합니다. 이 배열은 나중에 사용자의 입력을 저장하는 데 사용됩니다.
*/
let input = [];

/*
['line' 이벤트 리스너]
rl.on('line', ...)은 사용자가 새로운 줄을 입력할 때마다 트리거됩니다. 이 함수는 입력된 줄(line)을 받아 input 배열에 저장합니다. 여기서 배열은 새로운 입력마다 덮어쓰기 됩니다.

['close' 이벤트 리스너]
rl.on('close', ...)는 인터페이스가 닫힐 때 트리거됩니다. 이 예제에서는 input 배열의 첫 번째 요소를 str 변수에 할당하고, 이를 콘솔에 출력합니다.
*/
rl.on('line', function (line) {
    input = [line];
}).on('close',function(){    
    str = input[0];
    console.log(str);
});