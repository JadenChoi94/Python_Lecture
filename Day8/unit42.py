# 지금까지 클래스에서 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙였는데,
# 이렇게 @로 시작하는 것들이 데코레이터입니다. 즉, 함수(메서드)를 장식한다고 해서 이런 이름이 붙었습니다.
def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper  # wrapper 함수 반환

def hello():
    print('hello')
def world():
    print('world')

trace_hello = trace(hello)  # 데코레이터에 호출할 함수를 넣음
trace_hello()  # 반환된 함수를 호출
trace_world = trace(world)  # 데코레이터에 호출할 함수를 넣음
trace_world()  # 반환된 함수를 호출
# hello와 world 함수의 시작과 끝이 출력되었습니다. 먼저 데코레이터 trace는 호출할

# @로 데코레이터 사용하기
def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper  # wrapper 함수 반환

@trace  # @데코레이터
def hello():
    print('hello')
@trace  # @데코레이터
def world():
    print('world')

hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출


# 데코레이터를 여러 개 지정하기
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper


# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
hello()

# 이하 생략

