n1, n2 = eval(input('정수 2개 입력 >>'))

try:
    result1 = n1 / n2
    result2 = n1 % n2
    print('몫 >>', result1)
    print('나머지 >>', result2)
except:
    print('분모 0으로 계산 불능입니다.')

print('<<실행완료>>')

''' 이렇게 써도 상관은 없지만... 문법에 맞게 쓰는 게 좋으니 
위와 같이 작성은 안 하는게 낫다 '''
