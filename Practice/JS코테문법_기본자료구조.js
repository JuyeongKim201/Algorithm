/*
[반복문]
- for, while: 이건 알지?
- for of: 파이썬에서 for i in arr 과 같은 용도임
*/
let arr_loop = ['a','b','c','d','e'];

for (let i in arr_loop) { // i에는 index가 저장됨
    console.log(arr_loop[i]); // 'a' ~ 'e' 까지 출력
}

/*
[순회]
- map
- forEach
*/

let arr_map = [1,2,3,4];
let arr_map_2 = arr_map.map(num => {
    if (num % 2 == 0){
        return 0;        
    } else {
        return 1;
    }
})
console.log(arr_map); // [1, 2, 3, 4]
console.log(arr_map_2); // [1, 0, 1, 0]

let arr_forEach = [1,2,3,4];
arr_forEach.forEach(num => {
    if (num == 3){
        return;
    }     
    console.log(arr_forEach); // 1, 2, 4 출력
})

//
let arr_forEach2 = [1, 2, 3, 4];

arr_forEach2.forEach(num => {
  num += 1;
  console.log(num); // 2, 3, 4, 5 출력
});

console.log(arr_forEach2); // [1, 2, 3, 4]


//
let numbers_1 = [1,2,3];
let numbers_2 = [0];
numbers_1.forEach(num => {
    numbers_2.push(num);
})
console.log(numbers_2); [0, 1, 2, 3]

//////////////////// 자료구조 ///////////////////////
console.log("------------자료구조------------");
/*
[객체]

- 키 값 쌍으로 이루어진 형식없는 데이터 집합 (JSON)
*/
let obj = {
    name: "홍길동",
    age: 30,
}

let customer = obj.name;
console.log(customer); // '홍길동'


/*
[해시맵]
- 선언: let map = new Map();
- 삽입: map.set();
- 조회: map.get();
- 삭제: map.delete();
- 크기 확인: map.size;

순회할 경우, forEach 활용
*/
let map = new Map();

map.set("name", "하이");
map.set("age", 30);
map.set("age", 40); // 덮어씌워짐
console.log(map); // Map(2) { 'name' => '하이', 'age' => 40 }

map.forEach(i => {
    console.log(i); // "하이", 40 출력
})

let map_size = map.size;
console.log(map_size); // 2

let map_name = map.get("name"); // 해당 키에 해당하는 value 조회
map.delete("name"); // 해당 키에 해당하는 키값쌍 삭제
console.log(map_name); // "하이"
console.log(map); // Map(1) { 'age' => 40 }


map.set("name", "김덕배");
map.set("age", 30);
map.set("country", "korea");

map.forEach(i => 
    console.log(i) // 30, 김덕배, korea
)

/*
[Set (집합)]


*/
let setTest = new Set();
console.log(setTest);



// 기존 맵을 순회하며 각 요소를 변환하여 새로운 맵을 생성
let newMap = new Map();
map.forEach((value, key) => {
    if (value === 30) {
        newMap.set(key, 40);
    } else {
        newMap.set(key, value);
    }
});

// 변환된 맵 출력
console.log(newMap); // Map(3) { 'age' => 40, 'name' => '김덕배', 'country' => 'korea' }
console.log(newMap.get("age"));

/*
[스택, 큐]

1. 배열에서 shift를 이용한 큐 구현은 뒤 요소들의 index를 당기는 연산이 들어가므로 O(n)의 시간복잡도를 지니게 됨
*/

let a = [1,2,3,4,5]

a.push(6);
console.log(a); // [1, 2, 3, 4, 5, 6]

a.pop();
console.log(a); // [1, 2, 3, 4, 5]

a.shift();
console.log(a); // [2, 3, 4, 5]
