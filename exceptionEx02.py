n1, n2 = eval(input('정수 2개 입력 >>'))

try:
    result1 = n1 / n2
    result2 = n1 % n2
except:
    print('분모 0으로 계산 불능입니다.')
else:
    print('몫 >>', result1)
    print('나머지 >>', result2)
finally:
    print('++ 예외 처리 구문 종료 ++')

print('<<실행완료>>')
