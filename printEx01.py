## print 함수

# help(함수명) 함수에 대한 정보를 알려줌...
# help(print)

note = open('test.txt', 'w')

'''print('one', 'two', 'three')
print('one', 'two', 'three', sep='')
print('one', 'two', 'three', sep='-', end='\n\n')
print('출력합니다.')'''

print(1, 'one', 'two', 'three')
print(2,'one', 'two', 'three', sep='', file=note)
print(3, 'one', 'two', 'three', sep='-', end='\n\n')
print(4, '출력합니다.')

note.close()