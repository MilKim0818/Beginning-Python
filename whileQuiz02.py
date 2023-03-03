'''[문제 2]
1 ~ 10 합 (누적합)
1+2+...+10 = 55'''

'''iOne = 0
iTwo = 0

iOne = 1
while iOne < 11:
    iTwo = iTwo + iOne
    iOne = iOne + 1

print('1부터 n까지 합 >>', iTwo)'''

## [방법 1]
idx = 1
add = 0

while idx < 11:
    add = add + idx
    idx = idx + 1

print('1~10까지 누적합 >>', add)

## [방법 2]
addTwo = sum(range(1,11))
print('addTwo >>', addTwo)