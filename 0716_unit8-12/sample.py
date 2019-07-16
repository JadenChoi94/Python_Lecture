# 리스트는 여러가지 타입이 올수있음[]
'''
a = []
b = list()
b = list(range(5, 12))
b
c = list(range(-4, 10, 2))
c
d = list(range(10, 0, -1))
d
==========================================
Tuple, read-only!!() 이것도 역시 여러자료형이 올수있다.
하나짜리 튜플은 ,를 붙이자
튜플에서 리스트로, 리스트에서 튜플로
hello = '안녕하세요'
len(hello.encode('utf-8'))
hello=('Hello World!')
len(hello.encode('euc-kr'))

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']    # 키가 중복되면 가장 뒤에 있는 값만 사용함
lux
'''
# 딕셔너리의 키는 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있으며 자료형을 섞어서 사용해도 됩니다.
# 그리고 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있습니다.
# 단, 키에는 리스트와 딕셔너리를 사용할 수 없습니다.

# dict는 다음과 같이 키와 값을 연결하거나, 리스트, 튜플, 딕셔너리로 딕셔너리를 만들 때 사용합니다.
# 딕셔너리 = dict(키1=값1, 키2=값2)
# 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
# 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
# 딕셔너리 = dict({키1: 값1, 키2: 값2})
# 먼저 다음과 같이 dict에서 키=값 형식으로 딕셔너리를 만들 수 있습니다. 이때는 키에 ' '(작은따옴표)나 " "(큰따옴표)를
# 사용하지 않아야 합니다. 키는 딕셔너리를 만들고 나면 문자열로 바뀝니다.
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux1
lux2=dict(zip(['health','mana','melee','armor'], [290, 334, 550, 18.72]))
lux2
lux3=dict([('health', 490),('mana',334), ('melee', 550), ('armor', 18.72)])
lux3
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
lux4
lux['armor']

lux['mana_regen']=3.28
lux['attack_speed']=10.2
lux