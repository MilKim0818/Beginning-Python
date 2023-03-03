with open('D:\\python\\workspace\\p221105\\gugudan.txt', 'a') as gugudan:
    for r in range(1,101):
        gugudan.write(f'{r} ')

        if r%10 == 0:
            gugudan.write('\n')

print('<<쓰기 작업 완료>>')

