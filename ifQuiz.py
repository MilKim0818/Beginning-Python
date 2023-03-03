## [문제]
## 큰 값을 출력하시오.
## << 출력형태 >>
## 큰 값 >> 5

n1, n2 = 5, 5
## [방법 1] 조건문
''' if n1 > n2: #콜론 넣어야 씬텍스 에러가 안 나고, 변수 바로 뒤에 붙여서 씀
    print('큰 값 >>', n1)
else: #이프와 엘스 사이에는 빈라인(화이트라인)을 넣지 않음
    print('큰 값 >>', n2)'''

if n1 > n2: #콜론 넣어야 씬텍스 에러가 안 나고, 변수 바로 뒤에 붙여서 씀
    print('큰 값 >>', n1)
elif n1 < n2: #같은 값을 출력하지 않을 조건을 걸 때
    print('큰 값 >>', n2)

## [방법 2] 조건 연산자 
## True일때 if 조건식 else False일때
maxValue = n1 if n1 > n2 else n2
print('result >>', maxValue)
