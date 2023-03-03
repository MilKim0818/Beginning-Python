'''
[반복문] for

for 변수 in 여러값:
    명령어
    명령어
    명령어

'''

even = [2, 4, 6, 8]

for en in even:
    print(en)

print('=' * 20)
print('range함수 연습')
print('=' * 20)

''' for num in 5:
    print(en)'''

## range : 연속된 정수값
## range(시작값, 종료값)
for r in range(1, 10):
    print(r)

## range(시작값, 종료값, 증분값)
print('\n<< 홀수 출력 >>')
for r in range(1, 11, 2):
    print(r)

## range(종료값)
print('\n<< 0~9 출력 >>')
for r in range(10):
    print(r)

print('\n<< 1~10 출력 >>')
for r in range(1, 11):
    print(r)

## [문제] 10~1 출력
## 출력 예시
## 10 9 8 7 6 5 4 3 2 1
print('\n<< 문제 >>')
for r in range(10, 0, -1):
    print(r, end=' ')
    
