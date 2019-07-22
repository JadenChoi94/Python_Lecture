s = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i] = 0
    dic[i] +=1
print(dic)

s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
d= {}
for k in s:
d.setdefault(k,0)
d[k]+=1
print(list(d.itemes()))

import collections
s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
    print(d)
print(dict(d))

# copy() - 사전을 복제해 리턴
# update() - 기존 데이터에 전달 받은 데이터를 더하여 사전을 갱신
# setdefault(키, 디폴트값) - 키가 있는 경우 그냥 값을 리턴, 키가 없으면 디폴트값으로 새로운 요소를 추가
# (디폴트값을  전달하지 않는 경우 None 값으로 설정한다.)
# fromkeys() - 순환가능한(iterable) 키 값을 전달받아 사전을 생성
# (디폴트 값이 있으면 그 값으로 없으면 None으로 값을 설정)
# (fromkeys는 dict 클래스로 바로 호출하는 클래스 메소드 함수다.)