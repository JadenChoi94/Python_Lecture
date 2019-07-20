#람다식: 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
#map(): 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와줌
'''
add= lambda x, y: x+y
print(add(1, 2))
'''

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
my_function=lambda a, b: a*b
result=map(my_function, list1, list2) #같은 인덱스 자리에 있는 것끼리 더하고 빼고 할 수 있음
print(list(result))