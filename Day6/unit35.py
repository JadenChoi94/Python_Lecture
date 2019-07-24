# 클래스 속성 사용하기
class Person:
    bag = []
    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Person2:
    def __init__(self):
        self.bag = [] #속성 설정
    def put_bag(self, stuff):
        self.bag.append(stuff)

james2 = Person2()
james2.put_bag('책')
maria2 = Person2()
maria2.put_bag('Key')
print(james2.bag)
print(maria2.bag)

# 비공개 클래스 속성 사용하기
class Knight:
    __item_limit = 10  # 비공개 클래스 속성
    def print_item_limit(self):
        print(Knight.__item_limit)  # 클래스 안에서만 접근할 수 있음

x = Knight()
x.print_item_limit()  # 10
print(Knight.__item_limit)  # 클래스 바깥에서는 접근할 수 없음

# 정적 메서드 사용하기
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20)  # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)  # 클래스에서 바로 메서드 호출

import math
math.sqrt(2)
math.pow(22, 10)
