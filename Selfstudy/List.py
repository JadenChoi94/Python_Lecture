#index(원소): 리스트 내 특정한 원소의 인덱스를 찾기
list=['1', '2', '3', '4', '5']
print(list.index('1'))
#reverse(): 리스트의 원소를 뒤집기
list.reverse()
print(list)
list=list[::-1]
#sum(): 리스트의 모든 원소의 합
print(sum(list)) #리스트가 문자열일 경우 오류발생\

#range(시작, 끝-1): 특정 범위를 지정
#list(특정범위): 특정 범위의 원소를 가지는 리스트를 반환
my_range=range(4,10)
list=list(my_range)
print(list)

#all() / any(): 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별하는 함수
#enumerate(): 리스트에서 인덱스와 원소를 함께 추출
#sort(): 리스트의 원소를 정렬(오름차순)
#count(): 특정한 원소의 개수를 추출
#del: 리스트의 특정원소를 제거
#insert(): 리스트에 특정원소를 삽입, ex) list.insert(1, -1)
#append():리스트의 가장 마지막 원소로서 원소를 삽입



