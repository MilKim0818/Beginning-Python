# 클래스 정의
class Person:
    # 클래스 변수
    count = 1

    # 생성자
    def __init__(self):
        print("현재 생성된 사람 수 >> ", Person.count)
        Person.count += 1


# 클래스 변수 값 출력
print('객체 생성 전 : 클래스 변수 출력 >> ', Person.count)

# 객체(인스턴스) 생성
p1 = Person()
p2 = Person()
p3 = Person()

print('클래스 변수 출력 >> ', Person.count)

print('p1에 저장된 주소 >>', id(p1))
print('p2에 저장된 주소 >>', id(p2))
print('p3에 저장된 주소 >>', id(p3))
