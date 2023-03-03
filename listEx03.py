'''
[리스트 연산자]
+ 연산자 : 요소 추가 (이어주세요) 
* 연산자 : 요소 반복 
'''

odd = [1, 3, 5]
even = [2, 4, 6]

print('+ 연산자 >>', odd + even)
print('* 연산자 >>', odd * 3)

## 원본에는 영향이 없다 !
print('odd >>', odd)
print('even >>', even)

## [문제] 리스트 변수 odd에 even의 요소를 추가하시오.
## odd 출력 결과 : [1, 3, 5, 2, 4, 6] / 대입을 기준으로 오른쪽은 식 왼쪽은 변수 / 대입기준 왼쪽 오른쪽 같으면 생략가능 
#odd = odd + even
odd += even
print('odd >>', odd)
