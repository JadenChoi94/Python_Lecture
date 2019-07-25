# 클래스와 메서드 만들기
# 상속
# 캡슐화
# 다형성(method overriding, method overloading)
class Person:
     def greeting(self): #self, 밖에서 부를때 괄호안에 아무것도 안씀
         print('Hello')

james = Person()
james.greeting()

c = dict(x=10, y=20)
c

# 메서드 안에서 메서드 호출하기
class Person:
    def greeting(self):
        print('Hello')
    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출
james = Person()
james.hello()  # Hello

# 특정 클래스의 인스턴스인지 확인하기
isinstance(james, Person)

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 속성 사용하기
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
    def greeting(self):
        print(self.hello)
james = Person()
james.greeting()
james.hello
james.hello = 'Goodbye world!'
james.hello

# 인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

# 비공개 '속성' 사용하기!
# 비공개 '속성'은 __속성과 같이 이름이 __(밑줄 두 개)로 시작해야 합니다. 단,
# __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아니므로 주의해야 합니다.
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))

    def pay(self, amount):
        if amount > self.__wallet:    # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('돈이 모자라네...')
            return
        self.__wallet -= amount

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
maria.pay(8000)
# 사이트참조

# 비공개 '메서드' 사용하기
class Person:
    def __greeting(self):
        print('Hello')
    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음

james = Person()
james.__greeting()  # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음
