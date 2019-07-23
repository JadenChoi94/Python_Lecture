# 언패킹 사용하기
# 리스트나 튜플을 사용할 수도 있습니다.
# 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됩니다.
 def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
x = [10, 20, 30]
print_numbers(*x)

# 리스트 변수 대신 리스트 앞에 바로 *를 붙여도 동작은 같습니다.
print_numbers(*[10, 20, 30])

# 가변 인수 함수 만들기 argument(매개변수)
def print_numbers(*args):
     for arg in args:
         print(arg)

print_numbers(10, 20 ,30, 50)
y=[100, 200, 300 ,400, 500]
print_numbers(*y)
print(*y)

#고정 인수와 가변 인수를 함께 사용하기
def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)
print_numbers(1, 10, 20) # 튜플로찍힘
print_numbers(*y)
# 단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면
# 안 됩니다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동') #똑같이나옴
# 참고로 print 함수에서 사용했던 sep, end도 키워드 인수입니다.

# 키워드 인수와 '딕셔너리' 언패킹 사용하기
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
# 단, 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 합니다.
# 또한, 매개변수 개수와 딕셔너리 키의 개수도 같아야 합니다.

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동')
personal_info(**x)

# 기능추가
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

# 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
def personal_info(name, **kwargs):
     print(name)
     print(kwargs)
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
     print(*args, **kwargs)
custom_print(1, 2, 3, sep=':', end='')

# 매개변수에 초깃값 지정하기
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info(**x)
personal_info('홍길동', 30)

def personal_info(name, address='비공개', age):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)
# 함수를 만들어보면 문법 에러가 발생합니다. 왜냐하면 함수를 이렇게 만들어버리면
# personal_info('홍길동', 30)으로 함수를 호출했을 때 30이 어디로 들어가야 할지 알 수가 없기
# 때문입니다. address에 들어가려니 age 부분이 비어 버리죠. 잘못된 문법이므로
# 이렇게 만들면 안 됩니다.