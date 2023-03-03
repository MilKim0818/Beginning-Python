'''
[문자열]
- 여러 값(데이터)들을 묶어서 하나의 이름으로 관리
- 자료형(type) : str

- 인덱스를 이용하여 특정 값(데이터) 접근
:인덱스는 0부터 시작

- 하나의 값을 추출 : 인덱싱
- 연속된 여러 값을 추출 : 슬라이싱
'''

st = "Hello"

print('문자열 변수 st의 자료형 >>', type(st))

## 인덱싱
print('첫문자 추출 >>', st[0])
print('마지막 문자 추출 >>', st[-1])

## 슬라이싱
print('ell 추출 >>', st[1:4])
print('ell 추출2 >>', st[1:-1])

## index1과 3에 해당하는 문자 추출
print('el 추출 >>', st[1:4:2]) #시작, 끝, 증감 크기
print('Hlo 추출 1 >>', st[0:5:2]) #시작, 끝, 증감 크기 / 이런 형태는 잘 쓰지 않음
print('Hlo 추출 2 >>', st[::2]) #시작, 끝, 증감 크기 / 시작부터 끝 나타날 때는 이렇게 씀 

## olleH 형태로 추출
print('문자열 역순으로 추출 >>', st[ : :-1]) 

fruit = '하나둘셋넷'
print('나셋 >>', fruit[1:4:2]) #시작, 끝, 증감 크기
