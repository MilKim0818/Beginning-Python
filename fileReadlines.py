## 1. open 함수
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r')
# print('gugudan >>', gugudan)

## 2. 읽기 함수 : readlines()
lines = gugudan.readlines()

for line in lines: 
    print(line, end='')

## 3. close 함수
gugudan.close()

