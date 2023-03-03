''' [문제 1]
구구단 2단 출력
2 * 1 = 2
...
2 * 9 = 18
'''

'''num = 1

while num < 10:
    print('2단 출력 >>', 2 * num)
    num = num + 1'''
    
i = 1

while i < 10:
    print(f'2 * {i} = {2 * i}')
    # print('2 * ' + str(i) + " = " + str(2 * i))
    i = i + 1

print('반복문 실행 후 i >>', i)
print('실행 완료...')