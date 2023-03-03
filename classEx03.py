'''
[클래스 변수]
- (일반적으로) 클래스명 아래에 위치 
- 클래스 변수는 클래스가 메모리에 로드될 때, 메모리 할당 
- 클래스명으로 관리 --> 클래스명으로 접근
- [문법] 클래스명.변수 

[인스턴스(객체) 변수]
- 객체 내에 존재 
- 참조변수를 통해서 접근
- [문법] self.변수
'''

## 클래스 정의 
class Person: 
    # 클래스 변수
    count = 1

    ## 생성자
    def __init__(self):
        print('사람 객체를 1개 생성했습니다.')

    ## 메서드(메소드)
    def info(self):
        #객체 변수(인스턴스 변수)
        '''self.count = 1
        print('현재 생성된 사람 객체는 {self.count} 입니다.')
        self.count = self.count + 1'''
        print(f'현재 생성된 객체는 {Person.count} 입니다.')

print('클래스 변수 count >>', Person.count)

## 객체(인스턴스) 생성 -> 구체화된 대상
'''p1 = Person()
p1.info()

p2 = Person()
p2.info()'''
