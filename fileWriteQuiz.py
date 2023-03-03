## 1. open 함수
file = open('D:/python/workspace/p221105/number.txt', 'a')

## 2. write 함수
for r in range(1,101):
    file.write(f'{r}\n')

## 3. close 함수
file.close()

print('<< 쓰기 작업 완료 >>')