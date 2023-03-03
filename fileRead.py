'''
---------------------------------
[읽기 함수]     읽는 단위   자료형
---------------------------------
- readline  : 한 라인       str
- readlines : 전체          list
- read      : 전체          str
---------------------------------
'''


## 1. open 함수
gugudan = open('D:\\python\\workspace\\p221105\\gugudan.txt', 'r')
# print('gugudan >>', gugudan)

## 2. 읽기 함수 : read()
lines = gugudan.read()

#for line in lines: 
print(lines[:15])
print(type(lines))

## 3. close 함수
gugudan.close()

