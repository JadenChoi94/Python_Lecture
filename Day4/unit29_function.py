def hello():
    print('Hello world!')
hello()
# 내용이 없는 빈 함수를 만들 때는 코드 부분에 pass를 넣어줍니다.
# def hello():
#     pass
# 나중에 다른 사람이 만든 파이썬 소스 코드를 보다 보면 pass를 자주
# 접할 수 있습니다. pass는 아무 일을 하지 않아도 함수의 틀을 유지할
# 필요가 있을 때 사용합니다.

# 함수 독스트링 사용하기
# 파이썬에서는 함수의 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개)
# 로 문자열을 입력하면 함수에 대한 설명을 넣을 수 있습니다. 이런 방식
# 의 문자열을 독스트링(문서화 문자열, documentation strings, docstrin
# gs)이라고 합니다.
# 단, 독스트링의 윗줄에 다른 코드가 오면 안 됩니다.
# def add(a, b):
#     """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
#     return a + b
#
#
# x = add(10, 20)  # 함수를 호출해도 독스트링은 출력되지 않음
# print(x)
#
# print(add.__doc__)  # 함수의 __doc__로 독스트링 출력

def not_ten(a):
    if a == 10:
        return
    print('10이 아닙니다.')

not_ten(20)
not_ten(10)

def grade(score):
    if score >= 90:
        gpa="A"
    elif score >= 80:
        gpa='B'
    elif score >= 70:
        gpa='C'
    elif score >= 60:
        gpa ='D'
    else:
        gpa ='F'
    return gpa

def grade2(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

 def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
x
y
# 물론 return에서 리스트를 직접 반환해도 됩니다.
# 이때도 반환값을 변수 여러 개에 저장할 수 있습니다
def one_two():
    return [1, 2]
x, y = one_two()
print(x, y)

#지역변수는 Stack 에 저장
def mysum(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

a = 20
mysum(20)