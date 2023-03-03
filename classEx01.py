'''[class] 클래스
- 클래스는 '자료형'이다.
    ex) 자료형 : int, float, str, ...
- 사용자 정의 자료형
- 관련 있는 변수와 메서드를 하나의 이름 관리 
- 멤버 : 변수, 메서드(메소드, method)


<< 클래스 정의 >>
class 클래스명:
    멤버 

<< 객체(인스턴스) 생성 >>
변수 = 클래스명()
'''

## 클래스 정의 
class Student: # 타입을 만든 거
    ## 멤버 함수 : 메서드(메소드)
    def greeting(self):
        print('안녕하세요')
        #print('self에 저장된 주소 >>', id(self))

    def setName(self, name):
        self.name = name

    def infoPrint(self):
        print('제 이름은 ' + self.name + '입니다.')


## 객체(인스턴스) 생성 -> 구체화된 대상
hong = Student()
hong.greeting()
# print('참조변수 hong에 저장된 주소 >>', id(hong))
hong.setName('홍길동')
hong.infoPrint()

park = Student()
park.greeting()
park.setName('박보검')
park.infoPrint()
# print('참조변수 hong에 저장된 주소 >>', id(park))
