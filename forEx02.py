'''
[리스트 내포]

## 문법
[명령어 for 변수 in 여러값]

'''

even = [2, 4, 6, 8]

## 일반 for문
print('** 일반 for문 **')
for en in even:
    print(en)

## 리스트 내포
print('\n** 리스트 내포 **')
[print(en) for en in even]
