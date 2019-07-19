#{} : dict(키:값), set(element 하나)
# 딕셔너리의 중요한 기능 중 하나가 바로 키-값 쌍 추가입니다.
# 다음과 같이 딕셔너리에 키-값 쌍을 추가하는 메서드는 2가지가 있습니다.
# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x
x.setdefault('f', 500)
x
x.update(a=90)
x
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
y
y.update([[2, 'TWO'], [4, 'FOUR']])
y
y.update(zip([1, 2], ['one', 'two']))
y

# etdefault는 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없습니다.
# 하지만 update는 키-값 쌍 추가와 값 수정이 모두 가능합니다. 다음과 같이 setdefault로 이미 들어있는
# 키 'a'를 90으로 저장해도 'a'의 값은 바뀌지 않습니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90)
x

# 딕셔너리에서 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
x.pop('z', 0)
x.pop('b', 0)

# 딕셔너리에서 임의의 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()

# 딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
x

# 딕셔너리에서 키의 값을 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a'); x['a']
x.get('z', 0)

# 딕셔너리에서 키-값 쌍을 모두 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()
x.keys()
x.values()

# 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
x

# ict.fromkeys(키리스트, 값)처럼 키 리스트와 값을 지정하면 해당 값이 키의 값으로 저장됩니다.
y = dict.fromkeys(keys, 100)
y

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
x['z']    # 키 'z'는 없음

from collections import defaultdict   # collections 모듈에서 defaultdict를 가져옴
y = defaultdict(int)   # int로 기본값 생성
y['z']
y['a']
y = defaultdict(int, {'a':0})
y
int()
z = defaultdict(lambda: 'python') # 익명함수:lamba
z['a']
z[0]
z

def return_python():
    return 'python'

return_python()
y=defaultdict(return_python)
y['a']
y[0]
y

# 키만 가져오기!
for key in x.keys():
    print(key, end=' ')

#값만!
for value in x.values():
    print(value, end=' ')

#키와 값을 모두 가져오기!
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

for i in x:
    print(i, x[i])

for i in x:
    print(i, x.get(i))

# 리스트와 마찬가지로 딕셔너리도 for 반복문과 if 조건문을 사용하여 딕셔너리를 생성할 수 있습니다.
# 다음과 같이 딕셔너리 안에 키와 값, for 반복문을 지정하면 됩니다.
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
x

{key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()} # 키만 가져옴
{value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}  # 값을 키로 사용
{value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}  # 키-값 자리를 바꿈

# 딕셔너리 표현식에서 if 조건문 사용하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for key, value in x.items():
    if value == 20:  # 값이 20이면
        del x[key]  # 키-값 쌍 삭제
print(x)

x = {key: value for key, value in x.items() if value != 20}
x

# 25.4 딕셔너리 안에서 딕셔너리 사용하기
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
print(terrestrial_planet['Venus']['mean_radius'])  # 6051.8

# 25.5 딕셔너리의 할당과 복사
# 영상참조

