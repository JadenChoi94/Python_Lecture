# 람다 표현식으로 함수 만들기
def plus_ten(x):
     return x + 10
plus_ten(1)

# lambda 매개변수들: 식
#  이 상태로는 함수를 호출할 수 없습니다. 왜냐하면 람다 표현식은 이름이
#  없는 함수를 만들기 때문입니다. 그래서 람다 표현식을 익명 함수(anonymous function)로
#  부르기도 합니다.
lambda x: x + 10

plus_ten = lambda x: x + 10
plus_ten(1)

# 람다 표현식 자체를 호출하기
(lambda x: x + 10)(1)

# 람다 표현식 안에서는 변수를 만들 수 없다
(lambda x: y = 10; x + y)(1)

# 람다 표현식을 인수로 사용하기
def plus_ten(x):
     return x + 10

list(map(plus_ten, [1, 2, 3]))
list(map(lambda x: x + 10, [1, 2, 3]))

# 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
a=range(1, 10)
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

#  map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))

#  filter 사용하기
def f(x):
     return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))]

# reduce 사용하기
#  reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전
#  결과와 누적해서 반환하는 함수입니다.
from functools import reduce
 def f(x, y):
     return x + y
a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a)

#  map, filter, reduce와 리스트 표현식
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
[i for i in a if i > 5 and i < 10]

a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) - 1):
     x = x + a[i + 1]
x
