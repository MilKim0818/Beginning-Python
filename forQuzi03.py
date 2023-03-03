## 수학 점수가 60점 이상인 학생의 이름과 점수를 출력
## << 출력 형태 >>
## 일길동 학생은 90점으로 합격입니다. 

math = {'일길동' : 90, '이길동' : 45, '삼길동' : 60, '사길동' : 75, '오길동' : 50}

print(math['일길동'])
## [방법1]
'''for m in math:
    if math[m] >= 60:
        print(f'{m} 학생은 {math[m]}점으로 합격입니다.')'''
        
        # print(f'{i}번 학생은 {m}점으로 합격입니다.')

print(math.items())
## [방법2]
for m in math.items():
    if m[1] >= 60:
        print(f'{m[0]}번 학생은 {m[1]}점으로 합격입니다.')
        
## [방법2-2]
for key, value in math.items():
    if value >= 60:
        print(f'{key}번 학생은 {value}점으로 합격입니다.')