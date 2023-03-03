'''
[문자열 함수]
모두 복사본으로 작업함'''

st = "  Hello  "

## 문자열의 길이
print('문자열 길이 >>', len(st))

## 특정 문자의 개수
## 문법 : 문자열.count(문자)
print('l의 개수 >> ', st.count('l'))


## 공백 제거 (문자열 사이에 있는 공백을 지우지는 못함)
## 1) 왼쪽 공백 제거  : 문자열.lstrip() <- left
## 2) 오른쪽 공백 제거 : 문자열.rstrip() <- right
## 3) 양쪽 공백 제거 : 문자열.strip()
print('|' + st + '|')
print('|' + st.lstrip() + '|')
print('|' + st.rstrip() + '|')
print('|' + st.strip() + '|')

## 대소문자 변경
## [문법]
## 대문자로 변경 : 문자열.upper()
## 소문자로 변경 : 문자열.lower()

print('모두 대문자로 변경 >>', st.upper())
print('모두 소문자로 변경 >>', st.lower())

## 특정 문자의 위치(인덱스)
## 1) find : 문법 - 문자열.find('찾고자 하는 문자')
##         : 찾고자 하는 문자열 없을 경우 -1
## 2) index : 문법 - 문자열.index('찾고자 하는 문자')
##         : 찾고자 하는 문자열 없을 경우 Error 발생

print('e의 위치를 찾아라 1 >>', st.find('e'))
print('e의 위치를 찾아라 2 >>', st.index('e'))

print('p의 위치를 찾아라 1 >>', st.find('p')) # 없으면 -1로 나옴 (에러처리 안할 때, find를 씀)
# print('p의 위치를 찾아라 2 >>', st.index('p')) # 인덱스 함수는 error가 나옴 

## 특정 문자 변경 
## 문법 : 문자열.replace('old', 'new')
print('ello를 찾아서 i로 변경 후1 >>', st.replace('ello', 'i'))

stCopy = st.replace('ello', 'i')
print('ello를 찾아서 i로 변경 후2 >>', stCopy)
print('st >>', st) #원본은 그대로 !!

## 특정 문자를 기준으로 문자열 나누기 (왼쪽, 오른쪽 쪼개기 / 기준으로 사용된 문자는 결과에 없음)
## 문법 : 문자열.split('기준') / 결과값 타입은 리스트임 
print('e를 기준으로 문자열 나누기 >>', st.split('e'))
print('e를 기준으로 문자열 나누고 첫번째 리스트 추출 >>', st.split('e')[0])

## 특정 문자를 추가 (삽입)
## 문법 : '추가하는 문자'.join(문자열)
print('~ 추가 >>', '~'.join(st)) # 요소 사이사이에 해당 문자가 추가됨
