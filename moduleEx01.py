'''
##모듈 (module)
- 이미 만들어진 파이썬 파일
- 변수, 함수, 클래스를 모아 놓은 파일

## 모듈 가져오기
[형태 1]
import 모듈명

[형태 2]
from 모듈명 import 변수명, 함수명, 클래스명

[형태 3]
import 모듈명 as 별칭
'''

# [형태 1]
## import random
# 위 랜덤은 파일명
# random 함수 호출 (랜덤 파일 안에 랜덤이라는 함수가 있음 / 무작위)
# print('랜덤값 >>', random.random())

# [형태 2]
# from random import random
# random 함수 호출
# print('[형태 2] 랜덤값 >>', random())

# [형태 3]
import random as rd
# random 함수 호출
print('[형태 3] 랜덤값 >>', rd.random())
