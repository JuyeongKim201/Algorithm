# 문제: N-Queen (골드 4)

# 0번째 행부터 아래로 내려오면서 퀸을 하나씩 놓는다. 
# base case: 마지막 행에서 퀸을 성공적으로 놓았다. 
# general case: 
# - 가정: n번째 행까지 퀸이 안전하게 배치할 수 있다면
# - 증명: 그렇다면, n+1 번째 행에도 퀸을 안전하게 배치한다면 모든 n에 대해서 성립한다. 
# 1. 해당 열에 퀸이 있다면, 놓지 않는다. 
# 2. 양쪽 대각선에 퀸이 있다면, 놓지 않는다. 


# general case의 증명 부분을 수행하는 함수 
def check(n):
   for i in range(n):
      # 1. 해당 열에 퀸이 있다면, 놓지 않는다. 
      if rows[i] == rows[n]:
         return False
      
      # 2. 양쪽 대각선에 퀸이 있다면, 놓지 않는다. 
      if abs(rows[n] - rows[i]) == abs(n - i): # 열의 차이 == 행의 차이라면 대각선
         return False
      
   return True


# 재귀적으로 N-Queen을 수행하는 함수
def n_queen(row):
    global count

   # base case: 마지막 행에서 퀸을 성공적으로 놓았다. 
    if row == N: 
      count += 1 # 해결책 찾음 -> 카운트 +1 
      return 
   
   # general case
    for i in range(N):
        rows[row] = i # [row, i]에 방문 표시
        if check(row):  # 가정: n번째 행까지 퀸이 안전하게 배치할 수 있다면
            n_queen(row+1)  # n+1 번째 행에도 퀸을 안전하게 배치할 수 있다. 
            


# 실행 부분
N = int(input())
rows = [0] * N
count = 0 

n_queen(0)
print(count)
