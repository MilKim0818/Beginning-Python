'''with open() as 변수명:
    명령어
    명령어
'''

with open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r') as gugudan:
    lines = gugudan.read()
    print(lines)

