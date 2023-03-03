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
## [형태1]
print('\n** 리스트 내포 **')
[print(en) for en in even]

## [형태2]
## 리스트 내포
even = [r for r in range(2, 11, 2)]
print('even >>', even)
print('even 자료형 >>', type(even))

## 일반 for문
evenTwo = []

for r in range(2, 11, 2):
    evenTwo.append(r)

print('evenTwo >>', evenTwo)

##[형태 3]
## 리스트 내포
three = [r for r in range(1, 100) if r%3 == 0]
print('three >>', three)

## 일반 for
threeTwo = [] ## 빈 리스트

for r in range(1,100):
    if r%3 == 0:
        threeTwo.append(r)

print('threeTwo >>', threeTwo)