# 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# 세트는 요소의 순서가 정해져 있지 않습니다(unordered). 따라서 세트를 출력해보면 매번 요소의 순서가 다르게 나옵니다.
fruits #sort 되서 나옴

fruits2 = {'orange', 'orange', 'cherry'}
fruits2 #'orange'를 두 개 넣어도 실제로는 한 개만 들어갑니다.
fruits[0] #이렇게 못씀! Set 에서 값을 못뺴옴

# 세트에 특정 값이 있는지 확인하기
'orange' in fruits

#  set를 사용하여 세트 만들기
a = set('apple') #  중복된 문자는 포함되지 않습니다.
b = set(range(5))

# 빈세트 만들기
c = {}
type(c)
# 한글문자열
set('안녕하세요')

# 세트는 리스트, 딕셔너리와 달리 세트 안에 세트를 넣을 수 없습니다.
a = {{1, 2}, {3, 4}}

# 프로즌 세트, 파이썬은 내용을 변경할 수 없는 세트도 제공합니다.
# 다음과 같이 frozenset의 요소를 변경하려고 하면 에러가 발생합니다.
a = frozenset(range(10))
a |= 10
a.update({10})
a.update({10})

# frozenset는 세트 안에 세트를 넣고 싶을 때 사용합니다. 다음과 같이 frozenset는 frozenset를 중첩해서
# 넣을 수 있습니다. 단, frozenset만 넣을 수 있고, 일반 set는 넣을 수 없습니다.
frozenset({frozenset({1, 2}), frozenset({3, 4})})

# 집합 연산 사용하기
# 합집합(union)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
set.union(a, b)

# 교집합(intersection)
a & b
set.intersection(a, b)

# 차집합(difference)
a - b
set.difference(a, b)

# 대칭차집합(symmetric difference)
a ^ b
set.symmetric_difference(a, b)

# 집합 연산 후 할당 연산자 사용하기
a = {1, 2, 3, 4}
a |= {5}
a = {1, 2, 3, 4}
a.update({5})
# &=은 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장
a &= {0, 1, 2, 3, 4}
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
# -=은 현재 세트에서 다른 세트를 빼며 difference_update 메서드와 같습니다.
# ^=은 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장하며
# symmetric_difference_update 메서드와 같습니다.

# 부분 집합과 상위집합 확인하기
a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}
a.issubset({1, 2, 3, 4, 5})
# 이하 내용 영상참조
# https://dojang.io/mod/page/view.php?id=2315

# 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
a.isdisjoint({5, 6, 7, 8}) # 겹치는 요소가 없음
a.isdisjoint({3, 4, 5, 6}) # a와 3, 4가 겹침

# 세트에 요소 추가하기
a.add(5) # 합집합도 가능
# 세트에 요소 삭제하기
a.remove(3)
# discard(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어갑니다.
# 다음은 세트 a에 2가 있으므로 2를 삭제하고, 3은 없으므로 그냥 넘어갑니다.

# 세트에서 임의의 요소 삭제하기
a.pop()

# 세트의 모든 요소를 삭제하기
a.clear()

# 세트의 요소 개수 구하기
len(a)

# 세트 a와 b를 완전히 두 개로 만들려면 copy 메서드로 모든 요소를 복사해야 합니다.
a = {1, 2, 3, 4}
b = a.copy()

# 세트 표현식 사용하기
a = {i for i in 'pineapple' if i not in 'apl'}
a