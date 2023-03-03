## [continue]
## 반복문 내에서 if문과 함께 사용
## 반복문이 실행되다가 continue를 만나면, 조건 검사하러 위로 올라감

idx = 0

while idx < 10:
    idx = idx + 1

    if idx % 3 == 0:
        continue

    print('idx >>', idx)

print('실행 완료...')