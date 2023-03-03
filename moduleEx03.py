# [형태 2]
# from 패키지명 import 모듈명 변수명, 함수명, 클래스명

from pack.ex import value, show, Increment

print('value >>', value)

# show함수 호출
show()

# Increment class로 객체 생성
ic = Increment()

# printNum() 메서드 호출
ic.printNum(15)
