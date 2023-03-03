## 리턴값
## 여러 개(2개 이상)의 리턴값 --> 튜플

## [함수 정의]
def div(n1, n2):
    result1 = n1 // n2
    result2 = n1 % n2
    return result1, result2

## [함수 호출]
divResult = div(5, 3)
print('div(5, 3) 호출 결과 >>', divResult)
