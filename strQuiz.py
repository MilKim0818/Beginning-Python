## [문제 1] 문자열 사이에 존재하는 공백 제거 
quizOne = 'He  ll o'
quiztwo = quizOne.replace(' ','')
print('공백제거 후 >>', quiztwo)
## [문제 2] 가운데 숫자를 추출
numbering = 'a23-456-bc321'
numberingmid = numbering.split('-')
print('-기준으로 쪼개기 >>', numberingmid[1])