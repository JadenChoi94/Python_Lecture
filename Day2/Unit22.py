# 객체
# Attribute(속성값), Method(동작)
a=[12, 24, 35, 75]
a.append(500)
a
a.append([100,200])
a[5]
a.insert(2, 1000)
a
a.extend([100,200])
a
a.pop()
a
del a[1]
a
# Stack(lifo), Queue(fifo) 자료구조!
# 파이썬에서 스택은 리스트를 그대로 활용해도 되지만, 큐는 좀 더 효율적으로 사용할 수 있도록
# 덱(deque, double ended queue)이라는 자료형을 제공합니다. 덱은 양쪽 끝에서 추가/삭제가 가능한 자료 구조입니다.
from collections import deque
b = deque([10, 20, 30])
b.popleft()
b
if 35 in a:
    a.index(35)
a.count(35)
a.reverse()
a
a.sort()
# del a[:] = a.clear() 둘다 같음
a[len(a):] = [500]
a
c = a.copy()
c
del a[1]
min(a)
max(a)
sum(a)

# 리스트 컴프리헨션(list comprehension)이라고 합니다.
doo = [i for i in range(10)]
doo
foo = list(i for i in range(10))
foo
soo = [i * i for i in range(10)]
soo
zoo = [i*i for i in range(10) if i % 2 == 1]
zoo
goo = [i * k for k in range(2, 10)
             for i in range(1, 10)]
goo
# 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를 정수로 변환하려면
p = [1.2, 2.5, 3.7, 4.6]
for i in range(len(p)):
    p[i] = int(p[i])
p
p = list(map(int, p))
p

# range로 0부터 9까지 숫자를 만들고, str을 이용해서 모두 문자열로 변환했습니다.
# 리스트를 출력해보면 각 요소가 ' '(작은따옴표)로 묶인 것을 볼 수 있습니다.
koo = list(map(str, range(10)))
koo
from pprint import pprint
a = [[10, 20], [30, 40], [50, 60]]
pprint(a, indent=4, width=20)
a[1][1]