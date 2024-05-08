// 이분탐색
const a = [1,2,3,4,5,6,7,8,9,10];
let lo = 0;
let hi = a.length - 1;

const binary_search = (target, array) => {    
    while (lo <= hi) {        
        let mid = Math.floor((lo+hi)/2);
        if (target == array[mid]) {
            console.log('찾았다!');
            return;
        } else if (target < array[mid]) {            
            hi = mid - 1;
        } else {            
            lo = mid + 1;
        }     
    }
    
    console.log('대상이 없습니다');
}

binary_search(4, a);

// DFS: Set, 재귀 활용 | BFS: 큐, while 활용
const graph = {
    1: [2, 3, 4],
    2: [4],
    3: [4, 5],
    4: [],
    5: [],
}

/* 
[Array가 아닌 Set를 이용하는 이유] Set은 해시맵 기반으로 구성되어 있어, 탐색 시간복잡도가 O(1)이다
*/
const dfs = (here, visited = new Set()) => {
    if (visited.has(here)) return;
    visited.add(here);

    console.log(`${here} 방문 - visited: ${Array.from(visited)}`);
    graph[here].forEach(e => dfs(e, visited));
}

dfs(1);


const bfs = (start, visited = new Set(), que = []) => {    
    // 첫 노드 방문
    que.push(start);
    visited.add(start);    

    while (que.length > 0) {        
        let here = que.shift();
        console.log(`${here} 방문 - visited: ${Array.from(visited)}`);

        graph[here].forEach(neighbor => {
            if (!visited.has(neighbor)) {
                que.push(neighbor);
                visited.add(neighbor);             
            }
        })
    }
}

bfs(1);


// DP (피보나치 예시) - 재귀 활용
function fibonacciTopDown(n, memo = {}) {
    if (n in memo) return memo[n];  // 이미 계산된 값이면 반환
    if (n <= 2) return 1;  // 피보나치 수열의 초기값

    // 재귀적으로 이전 두 값을 계산하여 현재 값을 도출
    memo[n] = fibonacciTopDown(n - 1, memo) + fibonacciTopDown(n - 2, memo);
    return memo[n];
}

console.log(fibonacciTopDown(10));  // 55



// DP - 메모이제이션
function fibonacciBottomUp(n) {
    if (n <= 2) return 1;  // 피보나치 수열의 초기값

    const table = Array(n + 1).fill(0);  // 계산 결과를 저장할 테이블
    table[1] = 1;
    table[2] = 1;

    for (let i = 3; i <= n; i++) {
        table[i] = table[i - 1] + table[i - 2];
    }

    return table[n];
}

console.log(fibonacciBottomUp(10));  // 55
