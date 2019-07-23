# 함수 안에서 전역 변수 변경하기
x = 10  # 전역 변수
def foo():
    x = 20  # x는 foo의 지역 변수
    print(x)  # foo의 지역 변수 출력
foo()
print(x)  # 전역 변수 출력

# 파이썬에서 변수는 네임스페이스(namespace, 이름공간)에 저장됩니다. 다음과 같이 locals
# 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력할 수 있습니다.
locals()

# 함수 안에서 함수 만들기
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
        print(locals()) # 방금 배운거 응용
    print_message()
print_hello()

# 지역 변수 변경하기
def A():
    x = 10  # A의 지역 변수 x
    def B():
        nonlocal x  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20  # A의 지역 변수 x에 20 할당
    B()
    print(x)  # A의 지역 변수 x 출력
A()

# 33.3 closure 는 넘어감
