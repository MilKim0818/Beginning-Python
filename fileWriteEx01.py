'''
[파일 쓰기]
1. open 함수 : mode - w, a
2. write 함수
3. close 함수
'''

## 1. open 함수
## 문법 : 변수 = open('파일명 또는 경로', '모드')
# file = open('ex.txt', 'w')
file = open('D:\python\workspace\p221105\ex.txt', 'a')

## 2. write 함수
file.write('\nNew Line!!')

## 3. close 함수
file.close()

print('<< 실행 완료 >>')
