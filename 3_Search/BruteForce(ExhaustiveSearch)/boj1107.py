# 문제: 리모컨 (백준 1107번, 골드5)
# itertools.product() 활용한 풀이는 일부 예외를 처리하기 어려움.
import sys
input = sys.stdin.readline

start = 100 # 시작 채널
targetChannel = int(input()) # 목표 채널 입력받기

# 고장난 버튼 리스트 받기
NumberOfBroken = int(input())
if NumberOfBroken > 0:
    broken = list(input().split())
else:
    broken = []

##### 최솟값 구하기 #####

# 최댓값은 +, - 만으로 접근했을 때
cnt = abs(targetChannel - start) 

# 999,999 까지 모든 가능성 탐색
for channel in range(999900):
    # 고장난 버튼을 눌렀다면 패스!
    for i in str(channel): 
        if i in broken:
            break
    # 모든 버튼이 정상이었다면 계산하기
    else: # for-else: break일 경우 실행되지 않음
        cnt = min(cnt, abs(channel-targetChannel)+len(str(channel)))            

print(cnt)

