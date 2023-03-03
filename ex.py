# 전역 변수
value = 5

# 함수 정의


def show():
    print('show()함수 실행됨')

# 클래스 정의


class Increment:
    # 메서드 정의
    def printNum(self, num):
        # 인스턴스 변수
        self.num = num + 1
        print('1증가된 값 :', self.num)
