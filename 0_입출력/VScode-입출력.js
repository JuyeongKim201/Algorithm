// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });


// rl.question('숫자 두 개를 입력하세요 (예: 5 10): ', function(input) {
//   const numbers = input.split(' ').map(num => parseInt(num, 10));
//   const sum = numbers[0] + numbers[1];
  
//   console.log(`두 숫자의 합은: ${sum}`);
//   rl.close(); // readline 인터페이스 종료
// });

// rl.on('close', function() {
//   console.log('프로그램 종료');
//   process.exit(0);
// });

let numbers = [10, 2, 15, 1, 120];
numbers.sort();
console.log(numbers); // 출력: [1, 10, 120, 15, 2]
