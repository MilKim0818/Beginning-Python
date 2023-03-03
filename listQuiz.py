'''
[문제] 'hi' 요소를 찾아서 'hello' 변경
단, 'hi' 요소의 위치가 변경되도, 실행되어야 함 
[100, 200, 'hi', 'good', 300]
'''

data = [100, 200, 'hi', 'good', 300]
## [해결방법 1]
## 1. 요소 hi의 위치 (인덱스)
# idx = data.index('hi')
# print('요소 hi의 인덱스 >>', idx)
## 2. 요소 hi를 hello로 변경 
# data[idx] = 'hello'

## [해결방법 2]
data[data.index('hi')] = 'hello'
print(data)
