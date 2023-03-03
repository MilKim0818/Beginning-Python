## [변수 종류]
## 전역 변수
## 지역 변수

num = 5 ## 전역변수 

## 함수 정의 
def increment():
    # num = 100 ## 지역변수
    global num 
    num = num + 1
    print('함수 내 num 출력 >>', num)

## 함수 호출
increment()

print('num :', num)
