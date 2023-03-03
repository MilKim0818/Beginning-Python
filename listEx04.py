'''
[리스트 함수]
'''

data = [5, 1, 7, 3, 9]

## 정렬 : 오름차순
## 문법 : 리스트.sort()
## 정렬 : 내림차순
## 문법 : 리스트.sort(reverse=True)
print('정렬 전 >>', data)
#data.sort()
data.sort(reverse=True)
print('정렬 후 >>', data)

## 정렬 : 역순
## 문법 : 리스트.reverse()
print('정렬 전 >>', data)
data.reverse()
print('정렬 후 >>', data)

## 특정 요소의 인덱스 추출
## 문법 : 리스트.index(요소값)
number = ['one', 'two', 'three', 'four']
print('two 요소의 인덱스 >>', number.index('two'))

## 요소 추가 : '하나의 값'을 마지막 위치에 추가
## 문법 : 리스트.append(값) -> 기존에 있는 거에 마지막에 덧붙이는 거 
number.append('five')
print('요소 five 추가 후 number >>', number)

## 요소 추가 : 여러 개의 값을 마지막 위치에 추가
## 문법 : 리스트.extend([값1],[값2])
number.extend(['six', 'seven'])
print('여러 요소 추가 후 >>', number)

## [주의] 리스트를 하나의 요소로 추가 시킴.
## append 함수는 하나의 요소를 마지막 위치에 추가한다.
## 여러 개의 요소를 추가할 때는 extend 함수를 사용하세요.
# number.append([8, 9])
# print('주의 >>', number)

## 요소 추가 : 특정 위치에 요소 추가
## 문법 : 리스트.insert(인덱스, 값)
number.insert(2, 'five')
print('인덱스 2의 자리에 five 값 추가 후 >>', number)

## 요소 개수 : 특정 요소의 개수
## 문법 : 리스트.count(요소)
print('요소 five 개수 >>', number.count('five'))

## 요소 삭제 
## 문법 : 리스트.remove(요소)
## [문제] number 리스트의 길이 (요소 개수)를 확인하시오.
print('number 길이 >>', len(number))

number.remove('two')
print('요소 two 삭제 후 >>', number)
print('요소 two 삭제 후 길이>>', len(number))

## [문제] number 변수의 five 요소 모두 삭제
number.remove('five')
print('요소 five 삭제 후 >>', number)
number.remove('five')
print('요소 five 삭제 후 >>', number)
print('요소 five 삭제 후 길이>>', len(number))

## 요소 삭제 (특정 위치에 있는 요소 삭제)
## 문법 1) : 리스트.pop(인덱스)
## 문법 2) : 리스트.pop() <- 무조건 끝에 있는 것을 지움
number.pop(2)
print('인덱스 2의 요소 삭제 후 >>', number)
print('인덱스 2 삭제 후 길이>>', len(number))

number.pop()
print('마지막 위치의 요소 삭제 후 >>', number)
print('마지막 위치의 요소 삭제 후 길이>>', len(number))
