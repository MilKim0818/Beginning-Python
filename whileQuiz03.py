## [문제 3] 사용자에게 정수를 입력 받은 후, 덧셈 결과를 출력

'''
<실행>
정수 입력 >> 3
정수 입력 >> 5
정수 입력 >> 1
정수 입력 >> 0

합 >> 9

'''

'''num1 = input('정수 첫번째 입력하세요')
num2 = input('정수 두번째 입력하세요')

num = int(num1) + int(num2)
print('덧셈 결과 >>', num)
print('실행 완료')'''

'''num = 0
add = 0

while True:
    num = int(input('정수 입력>>'))
    add = add + num

    if num == 0:
        break

print('합 >>', add)'''

## 1. 반복문
add = 0

while True:
    ## 1.1. 입력 : input
    userValue = int(input('정수 입력 >>'))

    ## 1.2. 입력값 검사 : 0인지 아닌지 검사
    if userValue == 0:
        break 

    ## 1.3. 누적합
    add = add + userValue
## 2. 누적합 출력
print('누적합 : ', add)