## 1. open 함수
file = open('D://python//workspace//p221105//numberTwo.txt', 'w')

## 2. write 함수
for r in range(1,101):
    file.write(f'{r} ')

    if r%10 == 0:
        file.write('\n')

## 3. close 함수
file.close()

print('<< 쓰기 작업 완료 >>')
