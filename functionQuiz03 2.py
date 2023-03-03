'''[문제 3] 인수로 정수 2개 입력하여 호출하면, 두 수의 누적합을 출력하는 함수 정의 
호출형태 : accumulator(1, 10) accumulator(10, 1)
실행결과 - 누적 합 : 55

[문제 4] 리스트를 인수로 positive함수 호출하면, 양수 값만 출력하는 함수 정의
호출형태 : positiveValue = positive([1, -2, 3, -4, 5])
print(positiveValue)
실행결과 [1, 3, 5]
'''

## 함수 정의 
def accumulator(n1, n2):

    '''if n1 > n2:
        max, min = n1, n2
    else:
        max, min = n2, n1'''
    
    max, min = (n1, n2) if n1 > n2 else (n2, n1)

    add = sum(range(min, max+1))
    print('누적합 >>', add)

##함수 호출
accumulator(1, 10) 
accumulator(10, 1) 


## [함수 정의]
def positive(arg):
    result = []

    for ar in arg:
        if ar > 0:
            result.append(ar)
    return result 

## [함수 호출]
positiveValue = positive([1, -2, 3, -4, 5])
print(positiveValue)
