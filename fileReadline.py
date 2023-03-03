## 1. open 함수
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r')
print('gugudan >>', gugudan)

## 2. 읽기 함수 : readline()
while True:
    line = gugudan.readline()

    if not line:
        break

    print('line >>', line, end='')

## 3. close 함수
gugudan.close()
