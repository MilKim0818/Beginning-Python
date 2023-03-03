data = [2, 4, 6, 8]
print('리시트 변수 data의 길이>>', len(data))

## 인덱싱
print('첫번째 요소 추출>>', data[0])
print('마지막 요소 추출>>', data[-1])

## 슬라이싱
print('첫번째~두번째 요소 추출 1>>', data[0:2])
print('첫번째~두번째 요소 추출 2>>', data[:2])

print('세번째~마지막 요소 추출 1>>', data[2:4])
print('세번째~마지막 요소 추출 2>>', data[2:])
print('세번째~마지막 요소 추출 3>>', data[-2:])

number = [1, 3, [11, 13, 15], 5, 7, 9]
print('리스트 변수 number의 길이 >>', len(number))

## 리스트 변수 number의 리스트 요소를 추출
print('리스트 요소 추출 >>', number[2])
print('리스트 요소 추출 후 마지막 요소 추출 >>', number[2][-1])

## 리스트 변수 number의 리스트 요소를 추출 후, 마지막에서 두번째 이후 추출
print('요소 13, 15 추출 >>', number[2][-2:])

# print('요소 13, 15 추출 >>', number[1][0])
