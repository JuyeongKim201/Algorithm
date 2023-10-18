# 문제: 색종이 만들기 (실버 2)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)] 

result = []

def solution(x, y, N):
  color = paper[x][y] # 첫번째 요소로 컬러 추출
  # 컬러 통일되는지 검사
  for i in range(x, x+N): 
    for j in range(y, y+N):
      # 만일 컬러가 통일되지 않으면
      if color != paper[i][j]: 
        # 분할 정복
        solution(x, y, N//2) 
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  
  # 만일 모든 컬러가 통일되면 카운트
  if color == 0 : 
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))
