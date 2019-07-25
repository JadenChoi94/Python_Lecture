# 다음과 같은 딕셔너리 vegetables가 주어졌을 때 아래 그림과 같이
# 가격이 높은 것부터 내림차순으로 출력하는 프로그램을 작성하되,
# 가격은 길이를 7로 만들고 1000단위 ,를 찍은 뒤 우측정렬 하시오.
vegetables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}

import operator
sv = sorted(vegetables.items(), key=operator.itemgetter(1), reverse=True)
for veg, price in sv:
    print('%s:%7s' % (veg, format(price, ',')))
