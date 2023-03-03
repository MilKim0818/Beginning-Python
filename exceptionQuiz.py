
list_value = ['100', 'good', '5', '250', 'hi', '500']
list_number = []

# 예외처리 구문을 이용하여, list_value 요소 중 숫자로된 문자열만 list_number에 저장

# code
for value in list_value:
    try:
        int(value)
        list_number.append(value)
    except:
        pass

print('list_number >>', list_number)
