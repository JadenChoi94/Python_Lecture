# 두 개의 정수를 입력받아 작은 수에서부터 큰 수까지(큰 수 포함) 홀수의 합을
# 구해서 출력하는 프로그램을 for loop을 사용하여 작성하시오.
small, large = map(int, input('두개의 정수> ').split())
if small > large:
    small, large = large, small
sum = 0
for i in range(small, large+1):
    if i % 2 == 1:
        sum += i
print('홀수의 합 =', sum)