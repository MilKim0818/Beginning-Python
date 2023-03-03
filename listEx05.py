'''
리스트의 요소 값 변경
'''

data = ['one', 'two', 'three']

## 두번째 요소의 값을 2로 변경
print('요소 변경 전 >>', data)
data[1] = 2
print('요소 변경 후 1 >>', data)

## 여러 값을 의미하는 데이터 타입에서 여러 값을 추가하겠다
data[0:1] = [5, 7]
print('요소 변경 후 2 >>', data)

data[-2:] = [9]
print('요소 2와 three를 9로 변경 후 >>', data)
