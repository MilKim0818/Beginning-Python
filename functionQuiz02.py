## 덧셈 결과를 출력하는 함수를 정의하시오.
## 함수명 : add, 매개변수 : 2개, 리턴값 : 없음

## [실행 결과]
'''덧셈 결과 : 9
덧셈 결과 : onetwo
자료형이 달라서 덧셈 불가능 '''
## << 함수 정의 >>
'''[방법1]
def add(a, b):
    if type(a) != type(b):
        print('자료형이 달라서 덧셈 불가능')
    else:
        print('덧셈 결과 :', a + b)'''

## [방법 2]
def add(a, b):
    if type(a) != type(b):
        print('자료형이 달라서 덧셈 불가능')
        return

    print('덧셈 결과 :', a + b)

## << 함수 호출 >>
add(5, 4)
add('one', 'two')
add(5, 'five')
