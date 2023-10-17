# 문제: 단어 정렬 (실버 5)

# 1) set으로 중복없이 받고, 2) list로 변환하여 정렬
# set은 집합. 파이썬의 기본 데이터 타입 중 하나. 배열과 달리 순서가 없고, 중복된 값을 가지지 않음. 
# sort(key=len)은 길이에 따라 정렬. 하지만 길이가 같을 경우에는 사전 순으로 정렬
# sorted(set)은, set 자료형 인자가 list로 반환됨.
# key는 인자로 함수만 받음. 따라서 익명함수를 정의해주는 것

'''
lambda는 파이썬에서 익명 함수(anonymous function)를 정의하는 문법. lambda를 사용하면 간단한 함수를 한 줄로 작성할 수 있음.
'lambda arguments: expression'
-> 여기서 arguments는 함수의 매개변수이며, expression는 반환되는 값입니다. expression은 단일 표현식만 포함할 수 있음. 

-------------------
lambda x: (len(x), x)
-> 이건 다음과 같음 

def 익명함수(x):
    return len(x), x
--------------------
--------------------
f = lambda x: x + 1
print(f(2))  # 3이 출력
---------------------
'''

import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().rstrip('\n'))

words = list(set(words)) # 중복 삭제
words.sort(key = lambda x: (len(x), x)) # 정렬

for word in words:
    print(word)


