## [break]
## 반복문 내에서 if문과 함께 사용
## 반복문이 실행되다가 break를 만나면, 반복문을 탈출

idx = 0

while idx < 10:
    idx = idx + 1

    if idx % 3 == 0:
        break

    print('idx >>', idx)

print('실행 완료...')