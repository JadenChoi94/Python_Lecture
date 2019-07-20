#문자열 자료형 뒤집기
str="Hello world!"
print(str[::-1])

#len():문자열 길이를 출력
print(len(str))

#isalpha():특정한 문자열이 문자로만 이루어져 있는지 확인
print(str.isalpha()) #공백이 있으면 False라고 나옴

#isdigit():특정한 문자열이 숫자로만 이루어져 있는지 확인
print(str.isdigit())

#isalnum():특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
print(str.isalnum())

#join(리스트 자료형): 여러개의 문자열을 구분자와 함께 합치는 함수
'''
list=['Hello', 'World', '홍길동']
print('_'.join(list)
'''
#sorted(문자열 자료형)
#split(토큰): 문자열을 토큰에 따라서 분리하는 함수
str="I wanna watch a movie."
list=str.split(' ')
print(list)

#upper(): lower(): 문자열을 대문자로 혹은 소문자로 변환해주는 함수
#strip(): 좌우로 특정한 문자열을 제거하는 함수
print(str.rstrip()) #오른쪽에만 있는 공백제거
#eval()= 문자열 수식 계산해주는 함수
exp= "(203+705)*2-4"
print(eval(exp))