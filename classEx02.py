'''
[생성자] Costructor
- 객체가 생성될 때, 멤버 변수에 값 초기화
- 객체가 생성될 때, 특정 기능(메서드) 실행

- 객체가 생성될 때, 무조건 하나의 생성자 호출
- 생성자는 '메서드'다.
? 생성자는 메서드가 아니다? (관점의 차이라서 우선은 메서드라고 보기...)
- 생성자명 : __init__(self)
- 생성자는 하나만 정의 가능 

[객체 생성 순서] 객체는 선언이 아니다?
1. 메모리 할당
2. 생성자 실행

<< 클래스 정의 >>
class 클래스명:
    멤버 

<< 객체(인스턴스) 생성 >>
변수 = 클래스명()
'''

## 클래스 정의 
class Student: # 타입을 만든 거
    ## 멤버 함수 : 메서드(메소드)
    def __init__(self,name):
        self.name = name
        self.age = age
        print('<< 생성자 실행 완료!!!>>>')

    ## 메서드(메소드)
    def greeting(self):
        print('안녕하세요')
        #print('self에 저장된 주소 >>', id(self))

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def infoPrint(self):
        print('제 이름은 ' + self.name + '이고, ')
        print(f'제 나이는 {self.age}세 입니다.')


## 객체(인스턴스) 생성 -> 구체화된 대상
hong = Student('홍길동', 25)
hong.greeting()
# print('참조변수 hong에 저장된 주소 >>', id(hong))
# hong.setName('홍길동')
hong.infoPrint()

park = Student('박보검', 24)
park.greeting()
# park.setName('박보검')
park.infoPrint()
# print('참조변수 hong에 저장된 주소 >>', id(park))
