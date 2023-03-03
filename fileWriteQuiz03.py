file = open('D:/python/workspace/p221105/gugudan.txt', 'w')

## 2. write 함수
for i in range(2, 10):
    for j in range(1, 10):
        file.write(f'{i} * {j} = {i*j} \n')
    file.write('\n')
    
## 3. close 함수
file.close()

print('<< 쓰기 작업 완료 >>')

