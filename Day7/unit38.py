# 예외 처리 사용하기 ↓↓↓
def ten_div(x):
     return 10 / x
ten_div(0)
# 하지만 0을 넣으면 실행하는 중에 에러가 발생합니다.
# 이런 상황을 예외라고 하는데 여기서는 어떤 숫자를 0으로 나누어서 "ZeroDivisionError" 예외가 발생했습니다.

# try except로 사용하기 ↓↓↓
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

# 특정 예외만 처리하기 ↓↓↓
y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())# 2 0
    print(y[index] / x)
except ZeroDivisionError:  # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:  # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')

# 예외의 에러 메시지 받아오기 ↓↓↓
# 앞에서 만든 코드의 except에 as e를 넣습니다. 보통 예외( exception)의
# e를 따서 변수 이름을 e로 짓습니다.
y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:  # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e)  # e에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)

#제일 부모 ↓↓↓
except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
    print('예외가 발생했습니다.', e)


#  else와 finally 사용하기 ↓↓↓
try:
    x = int(input('나눌 숫자를 입력하세요: ')) # 2
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)

# 예외와는 상관없이 항상 코드 실행하기 ↓↓↓
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')

# 예외 발생시키기 ↓↓↓
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)

# raise의 처리 과정
def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:  # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴
    print(x)  # 현재 함수 안에는 except가 없으므로
    # 예외를 상위 코드 블록으로 넘김
try:
    three_multiple()
except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('예외가 발생했습니다.', e)

#이하 교재 참조