""" [조건 연산자]
문법 : True일때 if 조건식 else False일때 
"""

from html.entities import name2codepoint


n1 = 1

print('3보다 크다' if n1>3 else '3보다 작거나 같다')

## [문제] n1과 n2를 비교하여, 큰 값을 result에 저장 후 출력
n1, n2 = 100, 15
result = n1 if n1 > n2 else n2  
print('result >>', result)

""" <연산자>
- 대입 연산자
- 산술 연산자
- 복합 대입 연산자
- 관계 연산자
- 논리 연산자
- 조건 연산자
 """