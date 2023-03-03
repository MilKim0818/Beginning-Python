
even = (2, 4, 6)
print('even의 자료형 >>', type(even))

## 자료형 변경 : tuple -> list 
even = list(even)
print('even의 자료형 변경 후 >>', type(even))

## 마지막 요소를 10으로 변경
print('요소 변경 전 >>', even)
even[-1] = 10
print('요소 변경 후 >>', even)

## 자료형 변경 : list -> tuple 
even = tuple(even)
print('자료형 변경 후 : even의 자료형 >>', type(even))
print('even >>', even)