# 연 복리 이자율을 입력받아(단위 %) 원금이 2배가 되는데 최소 몇 년이 걸리는지
# 알아보는 프로그램을 while loop을 사용하여 작성하시오.
rate = float(input('이율(%)> '))
rate /= 100
year = 1
money = 1
while True:
    money *= (1 + rate)
    if money > 2:
        break
    year += 1
print('이율 =', rate*100, '%, 기간 =', year, '년')