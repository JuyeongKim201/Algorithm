
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